// version 4.0 - updated 2025/6/19

#ifndef INC_SERACC_H_
#define INC_SERACC_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stddef.h>

void seracc_init();

void seracc_transmit(const uint8_t* data, size_t size);

typedef void (*SerAccHandlerType)(uint8_t*, size_t);

void seracc_register_handler(const char*, SerAccHandlerType);

void seracc_idle_handler();

#ifdef __cplusplus
}
#endif

#endif /* INC_SERACC_H_ */
