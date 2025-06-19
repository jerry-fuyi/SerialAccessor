// version 4.0 - updated 2025/6/19

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stddef.h>

void seracc_init_bsp();

void seracc_transmit_bsp(const uint8_t* data, size_t size);

uint16_t seracc_crc_bsp(const uint8_t* data, size_t size);

size_t seracc_dma_remain_bsp();
void seracc_dma_start_bsp(uint8_t* buf, size_t size);
void seracc_dma_stop_bsp();

#ifdef __cplusplus
}
#endif
