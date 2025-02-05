// version 3.2 - updated 2025/2/1

#ifndef INC_SERACC_H_
#define INC_SERACC_H_

#ifdef __cplusplus
extern "C" {
#endif

void seracc_init(UART_HandleTypeDef*, DMA_HandleTypeDef*);

void seracc_transmit(const uint8_t* data, size_t size);

typedef void (*UartHandlerType)(uint8_t*, size_t);

void seracc_register_handler(const char*, UartHandlerType);

void seracc_idle_handler();

#ifdef __cplusplus
}
#endif

#endif /* INC_SERACC_H_ */
