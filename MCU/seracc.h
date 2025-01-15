#ifndef INC_SERACC_H_
#define INC_SERACC_H_

#ifdef __cplusplus
extern "C" {
#endif

void uart_init(UART_HandleTypeDef*, DMA_HandleTypeDef*);

void uart_transmit(const uint8_t* data, size_t size);

typedef void (*UartHandlerType)(uint8_t*, size_t);

void uart_register_handler(const char*, UartHandlerType);

void uart_idle_handler();
void uart_dma_handler();

#ifdef __cplusplus
}
#endif

#endif /* INC_SERACC_H_ */
