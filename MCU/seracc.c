#include "main.h"
#include "seracc.h"

#include "string.h"

UART_HandleTypeDef* huart_reg;
DMA_HandleTypeDef* hdma_rx;
extern CRC_HandleTypeDef hcrc;

static void uart_receive_start();
static void reg_handler(uint8_t* data, size_t size);

static uint8_t rx_buf[520];

void uart_init(UART_HandleTypeDef* huart, DMA_HandleTypeDef* hdma)
{
  huart_reg = huart;
  hdma_rx = hdma;

  uart_register_handler("_SA", reg_handler);

  uart_receive_start();
}

void uart_transmit(const uint8_t* data, size_t size)
{
  uint8_t tx_buf[4] = {0x55, 0xA5,
      (uint8_t)(size & 0xFF), (uint8_t)(size >> 8)};
  HAL_UART_Transmit(huart_reg, tx_buf, 4, 10);
  uint16_t crc = HAL_CRC_Calculate(&hcrc, (uint32_t*)data, size);
  HAL_UART_Transmit(huart_reg, data, size, size+1);
  tx_buf[0] = crc & 0xFF;
  tx_buf[1] = crc >> 8;
  HAL_UART_Transmit(huart_reg, tx_buf, 2, 10);
}

static int handler_count = 0;
static char keys[16][8];
static void (*handlers[16])(uint8_t*, size_t);

void uart_register_handler(const char* cmd, void(*cb)(uint8_t*, size_t))
{
  if (handler_count >= 16)
    return;
  if (strlen(cmd) > 7)
    return;
  strcpy(keys[handler_count], cmd);
  handlers[handler_count] = cb;
  handler_count += 1;
}

static int uart_manager(uint8_t* begin, uint8_t* end)
{
  if (end - begin < 8)
    return -1;

  if (*begin++ != 0x55)
    return -1;
  if (*begin++ != 0xA5)
    return -1;

  int size = *begin++;
  size += *begin++ << 8;

  if (size > end - begin + 2 || size < 2)
    return -1;

  int crc = begin[size] + (begin[size+1] << 8);
  int calc = HAL_CRC_Calculate(&hcrc, (uint32_t*)begin, size);
  if (calc != crc)
    return -1;

  end = begin + size;
  uint8_t* p = begin;
  for (; p != end; ++p)
  {
    if (*p == ':')
      break;
  }

  if (p != end)
  {
    char key[8];
    if (p - begin > 7)
      return -1;

    memcpy(key, begin, p - begin);
    key[p - begin] = '\0';

    for (int i = 0; i != handler_count; ++i)
    {
      if (strcmp(key, keys[i]) == 0)
      {
        ++p;
        handlers[i](p, end-p);
      }
    }
  }

  return size + 6;
}

void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
{
  if (huart != huart_reg)
    return;

  uint8_t* end = rx_buf + Size;
  for (uint8_t* p = rx_buf; p < end; )
  {
    int res = uart_manager(p, end);
    if (res < 0)
      break;
    p += res;
  }

  uart_receive_start();
}

static void uart_receive_start()
{
  HAL_UARTEx_ReceiveToIdle_DMA(huart_reg, rx_buf, sizeof(rx_buf)/sizeof(*rx_buf));
}

static void reg_handler(uint8_t* data, size_t size)
{
  uint_fast8_t id = data[0] & 0b11;
  uint32_t addr = *(uint32_t*)data;
  addr &= ~0b11u;
  uint32_t result = 0;
  uint_fast8_t len = 0;
  switch (size*4+id)
  {
  case 17: // 8-bit read
    result = *(volatile uint8_t*)addr;
    len = 1;
    break;
  case 18: // 16-bit read
    result = *(volatile uint16_t*)addr;
    len = 2;
    break;
  case 16: // 32-bit read
    result = *(volatile uint32_t*)addr;
    len = 4;
    break;
  case 21: // 8-bit write
    *(volatile uint8_t*)addr = *(uint8_t*)(data+4);
    break;
  case 24: // 16-bit write
    *(volatile uint16_t*)addr = *(uint16_t*)(data+4);
    break;
  case 32: // 32-bit write
    *(volatile uint32_t*)addr = *(uint32_t*)(data+4);
    break;
  case 20: // single bit set
    *(volatile uint32_t*)addr |= 1u << data[4];
    break;
  case 22: // single bit clear
    *(volatile uint32_t*)addr &= ~(1u << data[4]);
    break;
  case 33: // |=
    *(volatile uint32_t*)addr |= *(uint32_t*)(data+4);
    break;
  case 34: // &=
    *(volatile uint32_t*)addr &= *(uint32_t*)(data+4);
    break;
  case 48: // modify masked bits
  {
    volatile uint32_t* reg = (volatile uint32_t*)addr;
    uint32_t mask  = *(uint32_t*)(data+4);
    uint32_t value = *(uint32_t*)(data+8);
    *reg = (*reg & ~mask) | value;
    break;
  }
  default:
    return;
  }

  if (len > 0)
    uart_transmit((uint8_t*)&result, len);
}

