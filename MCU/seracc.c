// version 3.1 - updated 2024/12/16

#include "main.h"

#if defined(STM32G4)
  #include <stm32g4xx_ll_usart.h>
  #include <stm32g4xx_ll_dma.h>
#elif defined(STM32H5)
  #include <stm32h5xx_ll_usart.h>
  #include <stm32h5xx_ll_dma.h>
#else
 #error STM32 series not supported yet
#endif

#include "seracc.h"

#include "string.h"

UART_HandleTypeDef* huart_acc;
DMA_HandleTypeDef* hdma_rx;
extern CRC_HandleTypeDef hcrc;

static void uart_receive_start();
static void reg_handler(uint8_t* data, size_t size);

static uint8_t rx_buf[1040];
static uint8_t* rx_ptr = rx_buf;
static int rx_error = 0;
static int tx_synced = 0;

void uart_init(UART_HandleTypeDef* huart, DMA_HandleTypeDef* hdma)
{
  huart_acc = huart;
  hdma_rx = hdma;

  uart_register_handler("_", reg_handler);

  __HAL_UART_CLEAR_IDLEFLAG(huart_acc);
  __HAL_UART_ENABLE_IT(huart_acc, UART_IT_IDLE);
  __HAL_DMA_DISABLE_IT(hdma_rx, DMA_IT_HT);

  uart_receive_start();
}

void uart_transmit(const uint8_t* data, size_t size)
{
  HAL_UART_DMAStop(huart_acc);
  uart_receive_start();
  tx_synced = 1;

  uint8_t tx_buf[2];
  *(uint16_t*)tx_buf = size; // little-endian
  HAL_UART_Transmit(huart_acc, tx_buf, 2, 10);
  uint16_t crc = HAL_CRC_Calculate(&hcrc, (uint32_t*)data, size);
  HAL_UART_Transmit(huart_acc, data, size, size+1);
  *(uint16_t*)tx_buf = crc;
  HAL_UART_Transmit(huart_acc, tx_buf, 2, 10);
}

static void uart_sync()
{
  HAL_UART_DMAStop(huart_acc);
  uart_receive_start();
  uint8_t tx_buf[2] = {'O', 'K'};
  HAL_UART_Transmit(huart_acc, tx_buf, 2, 10);
}

static int handler_count = 0;
static char keys[16][8];
static void (*handlers[16])(uint8_t*, size_t);

void uart_register_handler(const char* cmd, UartHandlerType cb)
{
  if (handler_count >= 16)
    return;
  if (strlen(cmd) > 7)
    return;
  strcpy(keys[handler_count], cmd);
  handlers[handler_count] = cb;
  handler_count += 1;
}

static UartHandlerType find_handler(const char* cmd)
{
  for (int i = 0; i != handler_count; ++i)
  {
    if (strcmp(cmd, keys[i]) == 0)
    {
      return handlers[i];
    }
  }
  return 0;
}

#define UART_SYNC      -1
#define UART_TR_ERROR  -2
#define UART_FMT_ERROR -3
// return value:
// sync                 - -1
// transmission  error  - -2
// format error         - -3
// for incomplete error - -size
// no error             -  size
static int uart_manager(uint8_t* begin, uint8_t* end)
{
  if (end - begin < 2)
    return -6; // not complete

  size_t size = *(uint16_t*)begin; // little-endian

  if (size == 0xAA55)
  {
    uart_sync();
    return UART_SYNC; // sync
  }

  if (size < 2)
    return UART_TR_ERROR; // illegal size

  if (end - begin < size + 4)
    return -size - 4; // not complete

  int crc = begin[size+2] + (begin[size+3] << 8);
  int calc = HAL_CRC_Calculate(&hcrc, (uint32_t*)(begin+2), size);
  if (calc != crc)
    return UART_TR_ERROR; // CRC error

  begin += 2;
  end = begin + size;
  uint8_t* p = begin;
  for (; p != end; ++p)
  {
    if (*p == ':')
      break;
  }
  if (p == end)
    return UART_FMT_ERROR; // no colon, format error

  char key[8];
  if (p - begin > 7)
    return UART_FMT_ERROR; // key too long, format error

  memcpy(key, begin, p - begin);
  key[p - begin] = '\0';

  UartHandlerType handler = find_handler(key);
  if (!handler)
    return UART_FMT_ERROR; // no handler, format error

  ++p;
  handler(p, end-p);

  if (tx_synced)
  {
    tx_synced = 0;
    return UART_SYNC;
  }

  return size + 4;
}

//void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
void uart_idle_handler()
{
  __HAL_UART_CLEAR_IDLEFLAG(huart_acc);

  size_t dma_remain = __HAL_DMA_GET_COUNTER(hdma_rx);
  size_t size = sizeof(rx_buf) - dma_remain;
  uint8_t* end = rx_buf + size;

  if (rx_error)
  {
    if (*(uint32_t*)(end-4) == 0xAA55AA55)
      uart_sync();
    return;
  }

  while (rx_ptr < end)
  {
    int res = uart_manager(rx_ptr, end);
    if (res == UART_SYNC)
    {
      return;
    }
    else if (res == UART_TR_ERROR)
    {
      rx_error = 1;
      break;
    }
    else if (res == UART_FMT_ERROR)
    {
      rx_ptr += res;
    }
    else if (res < 0)
    {
      if (end - rx_buf >= -size)
        rx_error = 1;
      break;
    }
    else
    {
      rx_ptr += res;
    }
  }
}

void uart_dma_handler()
{
  if (
#if defined(STM32H5)
      __HAL_DMA_GET_FLAG(hdma_rx, DMA_FLAG_TC)
#else
      __HAL_DMA_GET_TC_FLAG_INDEX(hdma_rx)
#endif
      )
    rx_error = 1;
}

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
  if (huart != huart_acc)
    return;

  uart_dma_handler();
}

static void uart_receive_start()
{
//  HAL_UARTEx_ReceiveToIdle_DMA(huart_reg, rx_buf, sizeof(rx_buf)/sizeof(*rx_buf));
  rx_ptr = rx_buf;
  rx_error = 0;
  HAL_UART_Receive_DMA(huart_acc, rx_buf, sizeof(rx_buf));
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

