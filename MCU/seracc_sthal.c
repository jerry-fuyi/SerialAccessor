// version 4.1 - updated 2025/10/19

#include "main.h"

#include "seracc_bsp.h"

#ifndef SERACC_HUART
#error "You should #define SERACC_HUART huartX in main.h"
#endif
#ifndef SERACC_HDMA
#error "You should #define SERACC_HDMA hdma_uartX_rx in main.h"
#endif

extern UART_HandleTypeDef SERACC_HUART;
extern DMA_HandleTypeDef SERACC_HDMA;
extern CRC_HandleTypeDef hcrc;

void seracc_init_bsp()
{
    __HAL_DMA_DISABLE_IT(&SERACC_HDMA, DMA_IT_HT);
}

void seracc_transmit_bsp(const uint8_t* data, size_t size)
{
    HAL_UART_Transmit(&SERACC_HUART, data, size, size+1);
}

uint16_t seracc_crc_bsp(const uint8_t* data, size_t size)
{
    return HAL_CRC_Calculate(&hcrc, (uint32_t*)data, size);
}

size_t seracc_dma_remain_bsp()
{
    __HAL_UART_CLEAR_IDLEFLAG(&SERACC_HUART);
    return __HAL_DMA_GET_COUNTER(&SERACC_HDMA);
}

void seracc_dma_start_bsp(uint8_t* buf, size_t size)
{
    __HAL_UART_DISABLE_IT(&SERACC_HUART, UART_IT_IDLE);
    HAL_UART_Receive_DMA(&SERACC_HUART, buf, size);
    __HAL_UART_CLEAR_IDLEFLAG(&SERACC_HUART);
    __HAL_UART_ENABLE_IT(&SERACC_HUART, UART_IT_IDLE);
}

void seracc_dma_stop_bsp()
{
    HAL_UART_DMAStop(&SERACC_HUART);
}

