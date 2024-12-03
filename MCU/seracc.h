#ifndef INC_SERACC_H_
#define INC_SERACC_H_

#ifdef __cplusplus
extern "C" {
#endif

void uart_init(UART_HandleTypeDef*, DMA_HandleTypeDef*);

void uart_transmit(const uint8_t* data, size_t size);

void uart_register_handler(const char*, void(*)(uint8_t*, size_t));

#ifdef __cplusplus
}
#endif

#endif /* INC_SERACC_H_ */
