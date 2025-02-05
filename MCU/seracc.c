// version 3.2 - updated 2025/2/1
// matches PC v3.1

#include "main.h"

#include "seracc.h"

#include "string.h"

UART_HandleTypeDef* huart_acc;
DMA_HandleTypeDef* hdma_rx;
extern CRC_HandleTypeDef hcrc;

static void receive_start();
static void receive_stop();
static void reg_handler(uint8_t* data, size_t size);

static uint8_t rx_buf[1040];
static uint8_t* handle_ptr = rx_buf;
static int rx_error = 0;
static int tx_synced = 0;

void seracc_init(UART_HandleTypeDef* huart, DMA_HandleTypeDef* hdma)
{
  huart_acc = huart;
  hdma_rx = hdma;

  seracc_register_handler("_", reg_handler);

  __HAL_DMA_DISABLE_IT(hdma_rx, DMA_IT_HT);

  receive_start();
}

void seracc_transmit(const uint8_t* data, size_t size)
{
  receive_stop();
  receive_start();
  tx_synced = 1;

  uint8_t tx_buf[2];
  *(uint16_t*)tx_buf = size; // little-endian
  HAL_UART_Transmit(huart_acc, tx_buf, 2, 10);
  uint16_t crc = HAL_CRC_Calculate(&hcrc, (uint32_t*)data, size);
  HAL_UART_Transmit(huart_acc, data, size, size+1);
  *(uint16_t*)tx_buf = crc;
  HAL_UART_Transmit(huart_acc, tx_buf, 2, 10);
}

static void seracc_sync()
{
  receive_stop();
  receive_start();
  uint8_t tx_buf[2] = {'O', 'K'};
  HAL_UART_Transmit(huart_acc, tx_buf, 2, 10);
}

static int handler_count = 0;
static char keys[16][8];
static void (*handlers[16])(uint8_t*, size_t);

void seracc_register_handler(const char* cmd, UartHandlerType cb)
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
static int seracc_manager(uint8_t* begin, uint8_t* end)
{
  if (end - begin < 2)
    return -6; // not complete

  size_t size = *(uint16_t*)begin; // little-endian

  if (size == 0xAA55)
  {
    seracc_sync();
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
void seracc_idle_handler()
{
  __HAL_UART_CLEAR_IDLEFLAG(huart_acc);

  size_t dma_remain = __HAL_DMA_GET_COUNTER(hdma_rx);
  size_t size = sizeof(rx_buf) - dma_remain;
  uint8_t* end = rx_buf + size;

  if (rx_error)
  {
    if (*(uint32_t*)(end-4) == 0xAA55AA55)
      seracc_sync();
    return;
  }

  while (handle_ptr < end)
  {
    int res = seracc_manager(handle_ptr, end);
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
      handle_ptr += res;
    }
    else if (res < 0)
    {
      if (end - rx_buf >= -size)
        rx_error = 1;
      break;
    }
    else
    {
      handle_ptr += res;
    }
  }
}

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
  if (huart != huart_acc)
    return;

  rx_error = 1;
}

static void receive_start()
{
//  HAL_UARTEx_ReceiveToIdle_DMA(huart_reg, rx_buf, sizeof(rx_buf)/sizeof(*rx_buf));
  handle_ptr = rx_buf;
  rx_error = 0;
  __HAL_UART_DISABLE_IT(huart_acc, UART_IT_IDLE);
  HAL_UART_Receive_DMA(huart_acc, rx_buf, sizeof(rx_buf));
  __HAL_UART_CLEAR_IDLEFLAG(huart_acc);
  __HAL_UART_ENABLE_IT(huart_acc, UART_IT_IDLE);
}

static void receive_stop()
{
  HAL_UART_DMAStop(huart_acc);
}

typedef struct
{
  uint32_t value;
} __attribute__((packed)) uint32_unaligned;

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
    uint32_t mask, value;
    if ((uint32_t)data % 4) // not word-aligned, prevent LDRD instruction
    {
      mask = ((uint32_unaligned*)(data+4))->value;
      value = ((uint32_unaligned*)(data+8))->value;
    }
    else
    {
      mask = *(uint32_t*)(data+4);
      value = *(uint32_t*)(data+8);
    }
    *reg = (*reg & ~mask) | value;
    break;
  }
  default:
    return;
  }

  if (len > 0)
    seracc_transmit((uint8_t*)&result, len);
}

