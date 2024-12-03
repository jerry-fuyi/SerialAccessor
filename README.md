# Serial Accessor

A framework for interactive MCU register access through UART.

## Introduction

This is a framework for interactive register access. It consists of C code for MCU side and Python code for PC side.

The Python code include a parser and a base library. The parser can parse the register and bit field definitions from an [SVD file](https://arm-software.github.io/CMSIS_5/SVD/html/svd_Format_pg.html) and generate Python definitions for them, resulting in a device-dependent module. Once the module is generated, you can access the registers in MCU in simple semantics, e.g.,

``` Python
GPIOA.ODR.ODR15 = 1
TIM1.PSC = 100 - 1
TIM1.CNT = TIM1.ARR.read() - 1
```

These statements further invokes low-level functions in the base library, sending commands to MCU through UART. The C code handles the protocol in MCU, executing commands, and returning the results, if any.

Python programming on PC is flexible and can be interactive in Jupyter Notebook/Lab. This means you no longer need to code, build, run (these are really time-consuming) each time you make changes to MCU control logic. Instead, you can implement minimal logic, i.e., an adapter, in MCU, for once, then put all control logic on PC. For register accesses, this adapter in already contained in this framework. Register accesses can even be translated back to C for deployment.

Currently this framework is only supported on STM32 with HAL library, but in principle it can work with all MCUs with UART.

## MCU Usage

1. Enable a U(S)ART with 115200 bps, 8 data bits, 1 stop bit and no parity.

2. Enable the interrupt for this UART.

3. Configure a DMA channel for UART RX.

4. Disable the interuupt for this DMA channel. You should first uncheck "Force DMA channels interrupts".

5. Enable CRC:
    - Default Polynomial State: Disable
    - CRC Length: 16-bit
    - CRC Generating Polynomial: X12+X5+X0
    - Default Init Value State: Disable
    - Init Value for CRC Computation: 0

6. Save and generate code.

7. Add `seracc.h` and `seracc.c` to your project (either link or copy).

8. Call `uart_init()` to start the framework. The parameters are pointers to the UART instance and the DMA instance respectively.

## PC Usage

1. Install the dependencies:
    ``` shell
    pip install pyserial
    pip install crc
    ```

2. Run `parse.ipynb` to generate the device-dependent module. Follow the instructions in the notebook. I have generated the modules for some parts. If you find the one for your part, you can skip this step.

3. Import the generated module. Here take STM32G474 as an example.
    ``` Python
    from g474 import *
    ```
    This may take several seconds.

4. During importing, the framework will ask you which COM port to use. Look up the COM number in device manager and tell it. If you are using the UART bridge from ST-LINK/V2-1 and have the driver installed, the framework can automatically detect it.
    - If you accidentally disconnected the UART bridge, you can restart the kernel to reestablish the connection. If you don't want to restart, call `serial_init` in `seracc` to reestablish.
    - Enter `0` to enter evaluation mode. In this mode, all writes are omitted and all reads return 0's. You can test the functionalities and syntaxes without connecting to the MCU.

5. You can evaluate a peripheral, a register or a bit field by typing it in Jupyter Notebook/Lab:
    ```
    In[1] : TIM1
    Out[1]:
    ```
    <table style="width:800px">
        <tr>
            <th style="width:100px">Offset</th>
            <th style="width:100px">Register</th>
            <th>Content</th>
        </tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x00</td>
            <td align="center">CR1</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x04</td>
            <td align="center">CR2</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x0C</td>
            <td align="center">DIER</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x10</td>
            <td align="center">SR</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x14</td>
            <td align="center">EGR</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x24</td>
            <td align="center">CNT</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x28</td>
            <td align="center">PSC</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
        <tr>
            <td align="center" style='font-family:"Courier New"'>0x2C</td>
            <td align="center">ARR</td>
            <td align="right" style='font-family:"Courier New"'>DEC: 0, HEX: 0x00000000</td>
    	</tr>
    </table>

    ```
    In[2] : TIM1.CR1
    Out[2]:
    ```
    <table style="width:1000px">
        <tr>
            <th>31</th>
            <th>30</th>
            <th>29</th>
            <th>28</th>
            <th>27</th>
            <th>26</th>
            <th>25</th>
            <th>24</th>
            <th>23</th>
            <th>22</th>
            <th>21</th>
            <th>20</th>
            <th>19</th>
            <th>18</th>
            <th>17</th>
            <th>16</th>
        </tr>
        <tr>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        <tr>
            <th>15</th>
            <th>14</th>
            <th>13</th>
            <th>12</th>
            <th>11</th>
            <th>10</th>
            <th>9</th>
            <th>8</th>
            <th>7</th>
            <th>6</th>
            <th>5</th>
            <th>4</th>
            <th>3</th>
            <th>2</th>
            <th>1</th>
            <th>0</th>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td>DITHEN</td>
            <td>UIFREMAP</td>
            <td></td>
            <td></td>
            <td></td>
            <td>ARPE</td>
            <td></td>
            <td></td>
            <td></td>
            <td>OPM</td>
            <td>URS</td>
            <td>UDIS</td>
            <td>CEN</td>
        </tr>
        <tr>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
    </table>

    ```
    In[3] : TIM6.CR2.MMS
    Out[3]: 0b000
    ```
    Essentially, the environment calls the object's `__repr__` method, which shows a table in HTML and returns a string. Note that, however, do not write `TIM1.CNT = TIM1.ARR - 1`; if you want to directly make use of the value of a register, use `.read()`: `TIM1.CNT = TIM1.ARR.read() - 1`.
    Hovering the mouse on a register or bit field name shows its description. In this readme I cannot make it work. You can open the `example.ipynb` to experience this feature.

6. You can write to a register or a bit field by making an assignment:
    ``` Python
    TIM6.PSC = 15
    TIM6.ARR = 99
    ```
    The assignment and `__repr__` method access the register in 32-bit width. If you want to read/write in 8- or 16-bit, use `read8()`/`read16()`/`write8()`/`write16()`. This makes sense for data registers of USART and SPI.

7. For more functionalities, refer to `example.ipynb`.

## Recording

The framework can record your operations and generate C code so that you can deploy your code into MCU. Note that this feature does not record branch or loop statements within the block, nor the expressions on right hand side; only the EXACT accesses with the EXACT masks and values are recorded.

Operations inside the `with logging():` block are recorded. The `logging()` function can take one parameter, which is the filename to dump the records. If left empty, it prints on the console.

If you intend to fully configure a register, it's recommended to call `.reset()` before writing bit fields. This also generates more compact code.

If you intend to wait for some flag in the register, it's recommended to use the `wait_until_equal` function. Wihout recording, this is equivalent to a explicit `while` loop, but regarding C code generation, the latter will be converted to several reads while the former to a `while` loop in C.

The generation engine automatically combines contiguous write accesses to the same register into one access. If you intend to seperate them, you can use `barrier()` between accesses.

Example:

``` Python
with logging() as log:
    SPI1.CR1.SPE = 1
    SPI1.DR.write8(0x80)
    wait_until_equal(SPI1.SR.BSY, 0)
    TIM1.CR1.CEN = 0
    log.barrier()
    TIM1.CR1.DIR = 1
    TIM1.CR2.reset()
    TIM1.CR2.MMS = 0b0001
    TIM1.CR2.OIS1 = 1
```

Output:

``` C
*(volatile uint32_t*)0x40013000 |= 1u << 6;    // SPI1.CR1.SPE = 0b1
*(volatile uint8_t*)0x4001300C = 128;          // SPI1.DR = 128
volatile uint32_t* _reg = (volatile uint32_t*)0x40013008;
while ((*_reg & 0x00000080) != 0x00000000);    // SPI1.SR.BSY != 0b0
*(volatile uint32_t*)0x40012C00 &= ~(1u << 0); // TIM1.CR1.CEN = 0b0
*(volatile uint32_t*)0x40012C00 |= 1u << 4;    // TIM1.CR1.DIR = 0b1
*(volatile uint32_t*)0x40012C04 = 272;         // TIM1.CR2 = 0
                                               // TIM1.CR2.MMS = 0b0001
                                               // TIM1.CR2.OIS1 = 0b1
```

## Custom Handler

You can implement your own handler in addition to the register accessor based on the UART communication infrastructure provided by the framework.

Some limitations:
- The number of handlers, including the built-in register access protocol handler, is limit to 16.
- The keys of handlers (explained below) should not exceed 7 characters. It is recommended that the key contains letters and numbers only. The key must not contain colon `:`, nor start with underline `_`, which are reserved characters.
- The length between UART idle states, i.e., the maximum length of a single UART command, is limited to 512.
These limitations may be changed or removed in future releases.

Let's consider a Jupyter-to-I2C bridge: you can construct the data packet in Jupyter and send it to an I2C slave by the MCU.

1. Write wrapper functions in Python.
    - Let `I2C` be the **key** for the handler.
    - Following the colon is the **content** of your protocol. The first byte of the content is either `W` for write or `R` for read. For writing, `W` is followed by the slave address (left-aligned), then the packet. You don't need to explicitly encode the length. For reading, `R` is followed by the slave address, then the size (no larger than 255).
    - In either cases, MCU will return one byte indicating if the I2C operation is successful (e.g., if the slave sends ACK). 0 indicates success.
    - Here is just an example. You are free to change the implementation details.
    ``` Python
    from seracc import serial_transmit, serial_receive

    def i2c_write(addr, val):
        if not isinstance(val, list):
            val = [val]
        cmd = "I2C:W".encode()
        cmd += bytes([addr])
        cmd += bytes(val)
        serial_transmit(cmd)
        rec = serial_receive(1)
        if rec[0] != 0:
            print("I2C error")

    def i2c_read(addr, size):
        cmd = "I2C:R".encode()
        cmd += bytes([addr])
        cmd += bytes([size])
        serial_transmit(cmd)
        rec = serial_receive(size+1)
        if rec[0] != 0:
            print("I2C error")
        return rec[1:]
    ```

2. Configure related peripherals in CubeMX.
    - In this case, configure the I2C and GPIO.

3. Write handler functions in C.
    - The handler function must have signature `void(uint8_t*, size_t)`. The first parameter is a pointer to the content, the second being its size.
    - According to the protocol defined above, the function should first judge if the first byte is `W` or `R`.
    - Then it sends the data with length implied by the content size, or receives data with specified length, with HAL functions.
    - Finally, it sends back the result to PC, including a byte indicating success and, in the `R` case, the received data.
    ``` C
    void i2c_handler(uint8_t* data, size_t size)
    {
      if (data[0] == 'W')
      {
        uint8_t addr = data[1];
        uint8_t len = size - 2;
        uint8_t ret = 0;
        if (HAL_I2C_Master_Transmit(&hi2c1, addr, data+2, len, len+1) != HAL_OK)
          ret = -1;
        uart_transmit(&ret, 1);
      }
      else if (data[0] == 'R')
      {
        uint8_t addr = data[1];
        uint8_t len = data[2];
        uint8_t ret[len+1];
        ret[0] = 0;
        if (HAL_I2C_Master_Receive(&hi2c1, addr, ret+1, len, len+1) != HAL_OK)
          ret[0] = -1;
        uart_transmit(ret, len+1);
      }
    }
    ```

4. Register the handlers.
    - Register the handler with a call to `uart_register_handler`. The first parameter should match the key specified in Python wrapper function.
    ``` C
    uart_register_handler("I2C", i2c_handler);
    ```

## Todo

Access to global variables: Global variables have fixed address in RAM. This can be found in `.map` files. In the near future this library will support parsing `.map` files and provide access to the global variables. This eliminate the need to implement custom protocols to access the variable, making parameter tuning easier, e.g., PID.

A more robust framework regarding UART and DMA is required. The mapping from string to handler can be optimized in complexity.

UI improvement: descriptions that are too long cannot be completely displayed. (Need help, I can't do front-end.)

More tests on other platforms, including other series in STM32 and MCUs from other manufacturers, are needed.

**Contributions are welcome!**

## Changelog

### Version 3.0 - Uploaded to Github
This library is made open-source. It is renamed to "Serial Accessor" to reflect its main functionality.

### Version 2.4 - Waiting for Flag
Added `wait_until_equal`. This can be archived by a while statement at runtime, but not for code generation. `wait_until_equal` provides a method to wait for some flag in generated C code.

### Version 2.3 - Code Generation Optimization
Contiguous write accesses to the same register is now combined into one access in generated code. If you intend to seperate them, call `barrier()` between accesses.

### Version 2.2 - Code Generation
Transactions made in Python can be translated to C simply by enclosing the statements with a `with logging():` block. Note that this feature does not record branch or loop statements within the block; only the EXACT masks and values are recorded.
The `reset()` method resets a bitfield or a register. For peripheral reset, please use RCC reset registers.

### Version 2.1 - Protocol Optimization
Previously all write commands were 12-byte long, including a 32-bit address, a 32-bit value and a 32-bit mask. However, some accesses, e.g., setting or clearing a single bit, are common and should be optimized. Now the protocol is remastered and the average length of commands in typical use cases is reduced to, say, 8 bytes.

### Version 2.0 - SVD Parsing
Parsing source is switched to the SVD file. This makes the register map more complete and accurate.
Registers and bit fields can now be accessed with subsripts, e.g., `TIM1.CCR[1]` is equivalent to `TIM1.CCR1`. This enables a simpler syntax for multi-instance/channel treatment.
Taking the `repr` of a peripheral now shows all registers in it. Similar for those subscriptable names including `TIM1.CCR`.
In all tables, hovering the mouse on a name shows the description of that register or bit field.

### Version 1.5 - Register Details
Evaluating a register now shows a table consisting its bit fields and the corresponding values.

### Version 1.0 - Initial Release
This project is started for teaching purposes. The registers and data fields are parsed from C headers, e.g., "[stm32g474xx.h](https://github.com/STMicroelectronics/cmsis-device-g4/blob/master/Include/stm32g474xx.h)". This may be inaccurate or even fails with some advanced peripherals, but still okay for teaching purpose.

