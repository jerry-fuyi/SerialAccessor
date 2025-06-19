// version 4.0 - updated 2025/6/19

#include "ti_msp_dl_config.h"

#include "seracc.h"
#include "seracc_bsp.h"

#ifndef UART_SERACC_INST
#error "You should name the UART instance UART_SERACC or manually #define UART_SERACC_INST in ti_msp_dl_config.h"
#endif
#ifndef DMA_UART_RX_CHAN_ID
#error "You should name the DMA channel DMA_UART_RX or manually #define DMA_UART_RX_CHAN_ID in ti_msp_dl_config.h"
#endif

extern CRC_Regs* const CRC;
extern DMA_Regs* const DMA;

void seracc_init_bsp()
{
    ;
}

void seracc_transmit_bsp(const uint8_t* data, size_t size)
{
    for (int i = 0; i != size; ++i)
        DL_UART_Main_transmitDataBlocking(UART_SERACC_INST, data[i]);
}

uint16_t seracc_crc_bsp(const uint8_t* data, size_t size)
{
    uint32_t i;

    DL_CRC_setSeed16(CRC, 0x0000);

    for (i = 0; i < size; i++) {
        DL_CRC_feedData8(CRC, data[i]);
    }

    return (DL_CRC_getResult16(CRC));
}

size_t seracc_dma_remain_bsp()
{
    return DL_DMA_getTransferSize(DMA, DMA_UART_RX_CHAN_ID);
}

void seracc_dma_start_bsp(uint8_t* buf, size_t size)
{
    NVIC_DisableIRQ(UART_SERACC_INST_INT_IRQN);
    DL_DMA_setSrcAddr(DMA, DMA_UART_RX_CHAN_ID, (uint32_t)&(UART_SERACC_INST->RXDATA));
    DL_DMA_setDestAddr(DMA, DMA_UART_RX_CHAN_ID, (uint32_t)&buf[0]);
    DL_DMA_setTransferSize(DMA, DMA_UART_RX_CHAN_ID, size);
    DL_DMA_enableChannel(DMA, DMA_UART_RX_CHAN_ID);
    NVIC_EnableIRQ(UART_SERACC_INST_INT_IRQN);
}

void seracc_dma_stop_bsp()
{
    DL_DMA_disableChannel(DMA, DMA_UART_RX_CHAN_ID);
}

void UART_SERACC_INST_IRQHandler(void)
{
    switch (DL_UART_Main_getPendingInterrupt(UART_SERACC_INST))
    {
        case DL_UART_MAIN_IIDX_RX_TIMEOUT_ERROR:
            // trigger RX DMA
            UART_SERACC_INST->DMA_TRIG_RX.ISET = UART_DMA_TRIG_RX_ISET_RXINT_SET;
            // wait for RX FIFO empty
            while (!DL_UART_Main_isRXFIFOEmpty(UART_SERACC_INST))
                ;
            // no break

        case DL_UART_MAIN_IIDX_RX:
            seracc_idle_handler();
            break;

        default:
            break;
    }
}

