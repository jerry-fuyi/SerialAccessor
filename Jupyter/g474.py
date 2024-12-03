from seracc import BitField, RegisterBase, PeripheralBase, Subscriptor
from seracc import logging, wait_until_equal

class SA_CRC_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "DR", "Data register")
        self.DR = BitField(self, 0xFFFFFFFF, "DR", "Data register bits")

class SA_CRC_IDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IDR", "Independent data register")
        self.IDR = BitField(self, 0xFFFFFFFF, "IDR", "General-purpose 8-bit data register bits")

class SA_CRC_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "Control register")
        self.REV_OUT = BitField(self, 0x00000080, "REV_OUT", "Reverse output data")
        self.REV_IN = BitField(self, 0x00000060, "REV_IN", "Reverse input data")
        self.POLYSIZE = BitField(self, 0x00000018, "POLYSIZE", "Polynomial size")
        self.RESET = BitField(self, 0x00000001, "RESET", "RESET bit")

class SA_CRC_INIT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "INIT", "Initial CRC value")
        self.CRC_INIT = BitField(self, 0xFFFFFFFF, "CRC_INIT", "Programmable initial CRC value")

class SA_CRC_POL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x4C11DB7, "POL", "polynomial")
        self.POL = BitField(self, 0xFFFFFFFF, "POL", "Programmable polynomial")

class SA_CRC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Cyclic redundancy check calculation unit")
        self.DR = SA_CRC_DR(self, 0x0)
        self.IDR = SA_CRC_IDR(self, 0x4)
        self.CR = SA_CRC_CR(self, 0x8)
        self.INIT = SA_CRC_INIT(self, 0x10)
        self.POL = SA_CRC_POL(self, 0x14)

CRC = SA_CRC(0x40023000, "CRC")

class SA_IWDG_KR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "KR", "Key register")
        self.KEY = BitField(self, 0x0000FFFF, "KEY", "Key value (write only, read 0x0000)")

class SA_IWDG_PR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PR", "Prescaler register")
        self.PR = BitField(self, 0x00000007, "PR", "Prescaler divider")

class SA_IWDG_RLR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFF, "RLR", "Reload register")
        self.RL = BitField(self, 0x00000FFF, "RL", "Watchdog counter reload value")

class SA_IWDG_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "Status register")
        self.WVU = BitField(self, 0x00000004, "WVU", "Watchdog counter window value update")
        self.RVU = BitField(self, 0x00000002, "RVU", "Watchdog counter reload value update")
        self.PVU = BitField(self, 0x00000001, "PVU", "Watchdog prescaler value update")

class SA_IWDG_WINR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFF, "WINR", "Window register")
        self.WIN = BitField(self, 0x00000FFF, "WIN", "Watchdog counter window value")

class SA_IWDG(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "WinWATCHDOG")
        self.KR = SA_IWDG_KR(self, 0x0)
        self.PR = SA_IWDG_PR(self, 0x4)
        self.RLR = SA_IWDG_RLR(self, 0x8)
        self.SR = SA_IWDG_SR(self, 0xC)
        self.WINR = SA_IWDG_WINR(self, 0x10)

IWDG = SA_IWDG(0x40003000, "IWDG")

class SA_WWDG_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7F, "CR", "Control register")
        self.WDGA = BitField(self, 0x00000080, "WDGA", "Activation bit")
        self.T = BitField(self, 0x0000007F, "T", "7-bit counter (MSB to LSB)")

class SA_WWDG_CFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7F, "CFR", "Configuration register")
        self.WDGTB = BitField(self, 0x00003800, "WDGTB", "Timer base")
        self.EWI = BitField(self, 0x00000200, "EWI", "Early wakeup interrupt")
        self.W = BitField(self, 0x0000007F, "W", "7-bit window value")

class SA_WWDG_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "Status register")
        self.EWIF = BitField(self, 0x00000001, "EWIF", "Early wakeup interrupt flag")

class SA_WWDG(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "System window watchdog")
        self.CR = SA_WWDG_CR(self, 0x0)
        self.CFR = SA_WWDG_CFR(self, 0x4)
        self.SR = SA_WWDG_SR(self, 0x8)

WWDG = SA_WWDG(0x40002C00, "WWDG")

class SA_I2C1_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "Control register 1")
        self.PE = BitField(self, 0x00000001, "PE", "Peripheral enable")
        self.TXIE = BitField(self, 0x00000002, "TXIE", "TX Interrupt enable")
        self.RXIE = BitField(self, 0x00000004, "RXIE", "RX Interrupt enable")
        self.ADDRIE = BitField(self, 0x00000008, "ADDRIE", "Address match interrupt enable (slave only)")
        self.NACKIE = BitField(self, 0x00000010, "NACKIE", "Not acknowledge received interrupt enable")
        self.STOPIE = BitField(self, 0x00000020, "STOPIE", "STOP detection Interrupt enable")
        self.TCIE = BitField(self, 0x00000040, "TCIE", "Transfer Complete interrupt enable")
        self.ERRIE = BitField(self, 0x00000080, "ERRIE", "Error interrupts enable")
        self.DNF = BitField(self, 0x00000F00, "DNF", "Digital noise filter")
        self.ANFOFF = BitField(self, 0x00001000, "ANFOFF", "Analog noise filter OFF")
        self.TXDMAEN = BitField(self, 0x00004000, "TXDMAEN", "DMA transmission requests enable")
        self.RXDMAEN = BitField(self, 0x00008000, "RXDMAEN", "DMA reception requests enable")
        self.SBC = BitField(self, 0x00010000, "SBC", "Slave byte control")
        self.NOSTRETCH = BitField(self, 0x00020000, "NOSTRETCH", "Clock stretching disable")
        self.WUPEN = BitField(self, 0x00040000, "WUPEN", "Wakeup from STOP enable")
        self.GCEN = BitField(self, 0x00080000, "GCEN", "General call enable")
        self.SMBHEN = BitField(self, 0x00100000, "SMBHEN", "SMBus Host address enable")
        self.SMBDEN = BitField(self, 0x00200000, "SMBDEN", "SMBus Device Default address enable")
        self.ALERTEN = BitField(self, 0x00400000, "ALERTEN", "SMBUS alert enable")
        self.PECEN = BitField(self, 0x00800000, "PECEN", "PEC enable")

class SA_I2C1_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "Control register 2")
        self.PECBYTE = BitField(self, 0x04000000, "PECBYTE", "Packet error checking byte")
        self.AUTOEND = BitField(self, 0x02000000, "AUTOEND", "Automatic end mode (master mode)")
        self.RELOAD = BitField(self, 0x01000000, "RELOAD", "NBYTES reload mode")
        self.NBYTES = BitField(self, 0x00FF0000, "NBYTES", "Number of bytes")
        self.NACK = BitField(self, 0x00008000, "NACK", "NACK generation (slave mode)")
        self.STOP = BitField(self, 0x00004000, "STOP", "Stop generation (master mode)")
        self.START = BitField(self, 0x00002000, "START", "Start generation")
        self.HEAD10R = BitField(self, 0x00001000, "HEAD10R", "10-bit address header only read direction (master receiver mode)")
        self.ADD10 = BitField(self, 0x00000800, "ADD10", "10-bit addressing mode (master mode)")
        self.RD_WRN = BitField(self, 0x00000400, "RD_WRN", "Transfer direction (master mode)")
        self.SADD = BitField(self, 0x000003FF, "SADD", "Slave address bit (master mode)")

class SA_I2C1_OAR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OAR1", "Own address register 1")
        self.OA1 = BitField(self, 0x000003FF, "OA1", "Interface address")
        self.OA1MODE = BitField(self, 0x00000400, "OA1MODE", "Own Address 1 10-bit mode")
        self.OA1EN = BitField(self, 0x00008000, "OA1EN", "Own Address 1 enable")

class SA_I2C1_OAR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OAR2", "Own address register 2")
        self.OA2 = BitField(self, 0x000000FE, "OA2", "Interface address")
        self.OA2MSK = BitField(self, 0x00000700, "OA2MSK", "Own Address 2 masks")
        self.OA2EN = BitField(self, 0x00008000, "OA2EN", "Own Address 2 enable")

class SA_I2C1_TIMINGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMINGR", "Timing register")
        self.SCLL = BitField(self, 0x000000FF, "SCLL", "SCL low period (master mode)")
        self.SCLH = BitField(self, 0x0000FF00, "SCLH", "SCL high period (master mode)")
        self.SDADEL = BitField(self, 0x000F0000, "SDADEL", "Data hold time")
        self.SCLDEL = BitField(self, 0x00F00000, "SCLDEL", "Data setup time")
        self.PRESC = BitField(self, 0xF0000000, "PRESC", "Timing prescaler")

class SA_I2C1_TIMEOUTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMEOUTR", "Status register 1")
        self.TIMEOUTA = BitField(self, 0x00000FFF, "TIMEOUTA", "Bus timeout A")
        self.TIDLE = BitField(self, 0x00001000, "TIDLE", "Idle clock timeout detection")
        self.TIMOUTEN = BitField(self, 0x00008000, "TIMOUTEN", "Clock timeout enable")
        self.TIMEOUTB = BitField(self, 0x0FFF0000, "TIMEOUTB", "Bus timeout B")
        self.TEXTEN = BitField(self, 0x80000000, "TEXTEN", "Extended clock timeout enable")

class SA_I2C1_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x1, "ISR", "Interrupt and Status register")
        self.ADDCODE = BitField(self, 0x00FE0000, "ADDCODE", "Address match code (Slave mode)")
        self.DIR = BitField(self, 0x00010000, "DIR", "Transfer direction (Slave mode)")
        self.BUSY = BitField(self, 0x00008000, "BUSY", "Bus busy")
        self.ALERT = BitField(self, 0x00002000, "ALERT", "SMBus alert")
        self.TIMEOUT = BitField(self, 0x00001000, "TIMEOUT", "Timeout or t_low detection flag")
        self.PECERR = BitField(self, 0x00000800, "PECERR", "PEC Error in reception")
        self.OVR = BitField(self, 0x00000400, "OVR", "Overrun/Underrun (slave mode)")
        self.ARLO = BitField(self, 0x00000200, "ARLO", "Arbitration lost")
        self.BERR = BitField(self, 0x00000100, "BERR", "Bus error")
        self.TCR = BitField(self, 0x00000080, "TCR", "Transfer Complete Reload")
        self.TC = BitField(self, 0x00000040, "TC", "Transfer Complete (master mode)")
        self.STOPF = BitField(self, 0x00000020, "STOPF", "Stop detection flag")
        self.NACKF = BitField(self, 0x00000010, "NACKF", "Not acknowledge received flag")
        self.ADDR = BitField(self, 0x00000008, "ADDR", "Address matched (slave mode)")
        self.RXNE = BitField(self, 0x00000004, "RXNE", "Receive data register not empty (receivers)")
        self.TXIS = BitField(self, 0x00000002, "TXIS", "Transmit interrupt status (transmitters)")
        self.TXE = BitField(self, 0x00000001, "TXE", "Transmit data register empty (transmitters)")

class SA_I2C1_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "Interrupt clear register")
        self.ALERTCF = BitField(self, 0x00002000, "ALERTCF", "Alert flag clear")
        self.TIMOUTCF = BitField(self, 0x00001000, "TIMOUTCF", "Timeout detection flag clear")
        self.PECCF = BitField(self, 0x00000800, "PECCF", "PEC Error flag clear")
        self.OVRCF = BitField(self, 0x00000400, "OVRCF", "Overrun/Underrun flag clear")
        self.ARLOCF = BitField(self, 0x00000200, "ARLOCF", "Arbitration lost flag clear")
        self.BERRCF = BitField(self, 0x00000100, "BERRCF", "Bus error flag clear")
        self.STOPCF = BitField(self, 0x00000020, "STOPCF", "Stop detection flag clear")
        self.NACKCF = BitField(self, 0x00000010, "NACKCF", "Not Acknowledge flag clear")
        self.ADDRCF = BitField(self, 0x00000008, "ADDRCF", "Address Matched flag clear")

class SA_I2C1_PECR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PECR", "PEC register")
        self.PEC = BitField(self, 0x000000FF, "PEC", "Packet error checking register")

class SA_I2C1_RXDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXDR", "Receive data register")
        self.RXDATA = BitField(self, 0x000000FF, "RXDATA", "8-bit receive data")

class SA_I2C1_TXDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXDR", "Transmit data register")
        self.TXDATA = BitField(self, 0x000000FF, "TXDATA", "8-bit transmit data")

class SA_I2C1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Inter-integrated circuit")
        self.CR1 = SA_I2C1_CR1(self, 0x0)
        self.CR2 = SA_I2C1_CR2(self, 0x4)
        self.OAR1 = SA_I2C1_OAR1(self, 0x8)
        self.OAR2 = SA_I2C1_OAR2(self, 0xC)
        self.TIMINGR = SA_I2C1_TIMINGR(self, 0x10)
        self.TIMEOUTR = SA_I2C1_TIMEOUTR(self, 0x14)
        self.ISR = SA_I2C1_ISR(self, 0x18)
        self.ICR = SA_I2C1_ICR(self, 0x1C)
        self.PECR = SA_I2C1_PECR(self, 0x20)
        self.RXDR = SA_I2C1_RXDR(self, 0x24)
        self.TXDR = SA_I2C1_TXDR(self, 0x28)
        self.OAR = Subscriptor(self, "OAR{}")

I2C1 = SA_I2C1(0x40005400, "I2C1")
I2C2 = SA_I2C1(0x40005800, "I2C2")
I2C3 = SA_I2C1(0x40007800, "I2C3")
I2C4 = SA_I2C1(0x40008400, "I2C4")

class SA_FLASH_ACR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x600, "ACR", "Access control register")
        self.LATENCY = BitField(self, 0x0000000F, "LATENCY", "Latency")
        self.PRFTEN = BitField(self, 0x00000100, "PRFTEN", "Prefetch enable")
        self.ICEN = BitField(self, 0x00000200, "ICEN", "Instruction cache enable")
        self.DCEN = BitField(self, 0x00000400, "DCEN", "Data cache enable")
        self.ICRST = BitField(self, 0x00000800, "ICRST", "Instruction cache reset")
        self.DCRST = BitField(self, 0x00001000, "DCRST", "Data cache reset")
        self.RUN_PD = BitField(self, 0x00002000, "RUN_PD", "Flash Power-down mode during Low-power run mode")
        self.SLEEP_PD = BitField(self, 0x00004000, "SLEEP_PD", "Flash Power-down mode during Low-power sleep mode")
        self.DBG_SWEN = BitField(self, 0x00040000, "DBG_SWEN", "Debug software enable")

class SA_FLASH_PDKEYR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDKEYR", "Power down key register")
        self.PDKEYR = BitField(self, 0xFFFFFFFF, "PDKEYR", "RUN_PD in FLASH_ACR key")

class SA_FLASH_KEYR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "KEYR", "Flash key register")
        self.KEYR = BitField(self, 0xFFFFFFFF, "KEYR", "KEYR")

class SA_FLASH_OPTKEYR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPTKEYR", "Option byte key register")
        self.OPTKEYR = BitField(self, 0xFFFFFFFF, "OPTKEYR", "Option byte key")

class SA_FLASH_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "Status register")
        self.EOP = BitField(self, 0x00000001, "EOP", "End of operation")
        self.OPERR = BitField(self, 0x00000002, "OPERR", "Operation error")
        self.PROGERR = BitField(self, 0x00000008, "PROGERR", "Programming error")
        self.WRPERR = BitField(self, 0x00000010, "WRPERR", "Write protected error")
        self.PGAERR = BitField(self, 0x00000020, "PGAERR", "Programming alignment error")
        self.SIZERR = BitField(self, 0x00000040, "SIZERR", "Size error")
        self.PGSERR = BitField(self, 0x00000080, "PGSERR", "Programming sequence error")
        self.MISERR = BitField(self, 0x00000100, "MISERR", "Fast programming data miss error")
        self.FASTERR = BitField(self, 0x00000200, "FASTERR", "Fast programming error")
        self.RDERR = BitField(self, 0x00004000, "RDERR", "PCROP read error")
        self.OPTVERR = BitField(self, 0x00008000, "OPTVERR", "Option validity error")
        self.BSY = BitField(self, 0x00010000, "BSY", "Busy")

class SA_FLASH_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xC0000000, "CR", "Flash control register")
        self.PG = BitField(self, 0x00000001, "PG", "Programming")
        self.PER = BitField(self, 0x00000002, "PER", "Page erase")
        self.MER1 = BitField(self, 0x00000004, "MER1", "Bank 1 Mass erase")
        self.PNB = BitField(self, 0x000003F8, "PNB", "Page number")
        self.STRT = BitField(self, 0x00010000, "STRT", "Start")
        self.OPTSTRT = BitField(self, 0x00020000, "OPTSTRT", "Options modification start")
        self.FSTPG = BitField(self, 0x00040000, "FSTPG", "Fast programming")
        self.EOPIE = BitField(self, 0x01000000, "EOPIE", "End of operation interrupt enable")
        self.ERRIE = BitField(self, 0x02000000, "ERRIE", "Error interrupt enable")
        self.RDERRIE = BitField(self, 0x04000000, "RDERRIE", "PCROP read error interrupt enable")
        self.OBL_LAUNCH = BitField(self, 0x08000000, "OBL_LAUNCH", "Force the option byte loading")
        self.SEC_PROT1 = BitField(self, 0x10000000, "SEC_PROT1", "SEC_PROT1")
        self.OPTLOCK = BitField(self, 0x40000000, "OPTLOCK", "Options Lock")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "FLASH_CR Lock")

class SA_FLASH_ECCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ECCR", "Flash ECC register")
        self.ADDR_ECC = BitField(self, 0x0007FFFF, "ADDR_ECC", "ECC fail address")
        self.BK_ECC = BitField(self, 0x00200000, "BK_ECC", "BK_ECC")
        self.SYSF_ECC = BitField(self, 0x00400000, "SYSF_ECC", "SYSF_ECC")
        self.ECCIE = BitField(self, 0x01000000, "ECCIE", "ECCIE")
        self.ECCC2 = BitField(self, 0x10000000, "ECCC2", "ECC correction")
        self.ECCD2 = BitField(self, 0x20000000, "ECCD2", "ECC2 detection")
        self.ECCC = BitField(self, 0x40000000, "ECCC", "ECC correction")
        self.ECCD = BitField(self, 0x80000000, "ECCD", "ECC detection")

class SA_FLASH_OPTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xF0000000, "OPTR", "Flash option register")
        self.RDP = BitField(self, 0x000000FF, "RDP", "Read protection level")
        self.BOR_LEV = BitField(self, 0x00000700, "BOR_LEV", "BOR reset Level")
        self.nRST_STOP = BitField(self, 0x00001000, "nRST_STOP", "nRST_STOP")
        self.nRST_STDBY = BitField(self, 0x00002000, "nRST_STDBY", "nRST_STDBY")
        self.nRST_SHDW = BitField(self, 0x00004000, "nRST_SHDW", "nRST_SHDW")
        self.IDWG_SW = BitField(self, 0x00010000, "IDWG_SW", "Independent watchdog selection")
        self.IWDG_STOP = BitField(self, 0x00020000, "IWDG_STOP", "Independent watchdog counter freeze in Stop mode")
        self.IWDG_STDBY = BitField(self, 0x00040000, "IWDG_STDBY", "Independent watchdog counter freeze in Standby mode")
        self.WWDG_SW = BitField(self, 0x00080000, "WWDG_SW", "Window watchdog selection")
        self.nBOOT1 = BitField(self, 0x00800000, "nBOOT1", "Boot configuration")
        self.SRAM2_PE = BitField(self, 0x01000000, "SRAM2_PE", "SRAM2 parity check enable")
        self.SRAM2_RST = BitField(self, 0x02000000, "SRAM2_RST", "SRAM2 Erase when system reset")
        self.nSWBOOT0 = BitField(self, 0x04000000, "nSWBOOT0", "nSWBOOT0")
        self.nBOOT0 = BitField(self, 0x08000000, "nBOOT0", "nBOOT0")
        self.NRST_MODE = BitField(self, 0x30000000, "NRST_MODE", "NRST_MODE")
        self.IRHEN = BitField(self, 0x40000000, "IRHEN", "IRHEN")
        self.nBOOT = Subscriptor(self, "nBOOT{}")

class SA_FLASH_PCROP1SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF0000, "PCROP1SR", "Flash Bank 1 PCROP Start address register")
        self.PCROP1_STRT = BitField(self, 0x00007FFF, "PCROP1_STRT", "Bank 1 PCROP area start offset")

class SA_FLASH_PCROP1ER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFF0000, "PCROP1ER", "Flash Bank 1 PCROP End address register")
        self.PCROP1_END = BitField(self, 0x00007FFF, "PCROP1_END", "Bank 1 PCROP area end offset")
        self.PCROP_RDP = BitField(self, 0x80000000, "PCROP_RDP", "PCROP area preserved when RDP level decreased")

class SA_FLASH_WRP1AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "WRP1AR", "Flash Bank 1 WRP area A address register")
        self.WRP1A_STRT = BitField(self, 0x0000007F, "WRP1A_STRT", "Bank 1 WRP first area start offset")
        self.WRP1A_END = BitField(self, 0x007F0000, "WRP1A_END", "Bank 1 WRP first area A end offset")

class SA_FLASH_WRP1BR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "WRP1BR", "Flash Bank 1 WRP area B address register")
        self.WRP1B_STRT = BitField(self, 0x0000007F, "WRP1B_STRT", "Bank 1 WRP second area B end offset")
        self.WRP1B_END = BitField(self, 0x007F0000, "WRP1B_END", "Bank 1 WRP second area B start offset")

class SA_FLASH_SEC1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFF00FF00, "SEC1R", "securable area bank1 register")
        self.BOOT_LOCK = BitField(self, 0x00010000, "BOOT_LOCK", "BOOT_LOCK")
        self.SEC_SIZE1 = BitField(self, 0x0000007F, "SEC_SIZE1", "SEC_SIZE1")

class SA_FLASH(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Flash")
        self.ACR = SA_FLASH_ACR(self, 0x0)
        self.PDKEYR = SA_FLASH_PDKEYR(self, 0x4)
        self.KEYR = SA_FLASH_KEYR(self, 0x8)
        self.OPTKEYR = SA_FLASH_OPTKEYR(self, 0xC)
        self.SR = SA_FLASH_SR(self, 0x10)
        self.CR = SA_FLASH_CR(self, 0x14)
        self.ECCR = SA_FLASH_ECCR(self, 0x18)
        self.OPTR = SA_FLASH_OPTR(self, 0x20)
        self.PCROP1SR = SA_FLASH_PCROP1SR(self, 0x24)
        self.PCROP1ER = SA_FLASH_PCROP1ER(self, 0x28)
        self.WRP1AR = SA_FLASH_WRP1AR(self, 0x2C)
        self.WRP1BR = SA_FLASH_WRP1BR(self, 0x30)
        self.SEC1R = SA_FLASH_SEC1R(self, 0x70)

FLASH = SA_FLASH(0x40022000, "FLASH")

class SA_DBGMCU_IDCODE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IDCODE", "MCU Device ID Code Register")
        self.DEV_ID = BitField(self, 0x0000FFFF, "DEV_ID", "Device Identifier")
        self.REV_ID = BitField(self, 0xFFFF0000, "REV_ID", "Revision Identifier")

class SA_DBGMCU_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "Debug MCU Configuration Register")
        self.DBG_SLEEP = BitField(self, 0x00000001, "DBG_SLEEP", "Debug Sleep Mode")
        self.DBG_STOP = BitField(self, 0x00000002, "DBG_STOP", "Debug Stop Mode")
        self.DBG_STANDBY = BitField(self, 0x00000004, "DBG_STANDBY", "Debug Standby Mode")
        self.TRACE_IOEN = BitField(self, 0x00000020, "TRACE_IOEN", "Trace pin assignment control")
        self.TRACE_MODE = BitField(self, 0x000000C0, "TRACE_MODE", "Trace pin assignment control")

class SA_DBGMCU_APB1L_FZ(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB1L_FZ", "APB Low Freeze Register 1")
        self.DBG_TIMER2_STOP = BitField(self, 0x00000001, "DBG_TIMER2_STOP", "Debug Timer 2 stopped when Core is halted")
        self.DBG_TIM3_STOP = BitField(self, 0x00000002, "DBG_TIM3_STOP", "TIM3 counter stopped when core is halted")
        self.DBG_TIM4_STOP = BitField(self, 0x00000004, "DBG_TIM4_STOP", "TIM4 counter stopped when core is halted")
        self.DBG_TIM5_STOP = BitField(self, 0x00000008, "DBG_TIM5_STOP", "TIM5 counter stopped when core is halted")
        self.DBG_TIMER6_STOP = BitField(self, 0x00000010, "DBG_TIMER6_STOP", "Debug Timer 6 stopped when Core is halted")
        self.DBG_TIM7_STOP = BitField(self, 0x00000020, "DBG_TIM7_STOP", "TIM7 counter stopped when core is halted")
        self.DBG_RTC_STOP = BitField(self, 0x00000400, "DBG_RTC_STOP", "Debug RTC stopped when Core is halted")
        self.DBG_WWDG_STOP = BitField(self, 0x00000800, "DBG_WWDG_STOP", "Debug Window Wachdog stopped when Core is halted")
        self.DBG_IWDG_STOP = BitField(self, 0x00001000, "DBG_IWDG_STOP", "Debug Independent Wachdog stopped when Core is halted")
        self.DBG_I2C1_STOP = BitField(self, 0x00200000, "DBG_I2C1_STOP", "I2C1 SMBUS timeout mode stopped when core is halted")
        self.DBG_I2C2_STOP = BitField(self, 0x00400000, "DBG_I2C2_STOP", "I2C2 SMBUS timeout mode stopped when core is halted")
        self.DBG_I2C3_STOP = BitField(self, 0x40000000, "DBG_I2C3_STOP", "I2C3 SMBUS timeout mode stopped when core is halted")
        self.DBG_LPTIMER_STOP = BitField(self, 0x80000000, "DBG_LPTIMER_STOP", "LPTIM1 counter stopped when core is halted")
        self.DBG_I2C_STOP = Subscriptor(self, "DBG_I2C{}_STOP")
        self.DBG_TIM_STOP = Subscriptor(self, "DBG_TIM{}_STOP")

class SA_DBGMCU_APB1H_FZ(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB1H_FZ", "APB Low Freeze Register 2")
        self.DBG_I2C4_STOP = BitField(self, 0x00000002, "DBG_I2C4_STOP", "DBG_I2C4_STOP")

class SA_DBGMCU_APB2_FZ(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB2_FZ", "APB High Freeze Register")
        self.DBG_TIM1_STOP = BitField(self, 0x00000800, "DBG_TIM1_STOP", "TIM1 counter stopped when core is halted")
        self.DBG_TIM8_STOP = BitField(self, 0x00002000, "DBG_TIM8_STOP", "TIM8 counter stopped when core is halted")
        self.DBG_TIM15_STOP = BitField(self, 0x00010000, "DBG_TIM15_STOP", "TIM15 counter stopped when core is halted")
        self.DBG_TIM16_STOP = BitField(self, 0x00020000, "DBG_TIM16_STOP", "TIM16 counter stopped when core is halted")
        self.DBG_TIM17_STOP = BitField(self, 0x00040000, "DBG_TIM17_STOP", "TIM17 counter stopped when core is halted")
        self.DBG_TIM20_STOP = BitField(self, 0x00100000, "DBG_TIM20_STOP", "TIM20counter stopped when core is halted")
        self.DBG_HRTIM0_STOP = BitField(self, 0x04000000, "DBG_HRTIM0_STOP", "DBG_HRTIM0_STOP")
        self.DBG_HRTIM1_STOP = BitField(self, 0x08000000, "DBG_HRTIM1_STOP", "DBG_HRTIM0_STOP")
        self.DBG_HRTIM2_STOP = BitField(self, 0x10000000, "DBG_HRTIM2_STOP", "DBG_HRTIM0_STOP")
        self.DBG_HRTIM3_STOP = BitField(self, 0x20000000, "DBG_HRTIM3_STOP", "DBG_HRTIM0_STOP")
        self.DBG_TIM_STOP = Subscriptor(self, "DBG_TIM{}_STOP")
        self.DBG_HRTIM_STOP = Subscriptor(self, "DBG_HRTIM{}_STOP")

class SA_DBGMCU(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Debug support")
        self.IDCODE = SA_DBGMCU_IDCODE(self, 0x0)
        self.CR = SA_DBGMCU_CR(self, 0x4)
        self.APB1L_FZ = SA_DBGMCU_APB1L_FZ(self, 0x8)
        self.APB1H_FZ = SA_DBGMCU_APB1H_FZ(self, 0xC)
        self.APB2_FZ = SA_DBGMCU_APB2_FZ(self, 0x10)

DBGMCU = SA_DBGMCU(0xE0042000, "DBGMCU")

class SA_RCC_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x63, "CR", "Clock control register")
        self.HSION = BitField(self, 0x00000100, "HSION", "HSI16 clock enable. Set and cleared by software. Cleared by hardware to stop the HSI16 oscillator when entering Stop, Standby or Shutdown mode. Set by hardware to force the HSI16 oscillator ON when STOPWUCK=1 or HSIASFS = 1 when leaving Stop modes, or in case of failure of the HSE crystal oscillator. This bit is set by hardware if the HSI16 is used directly or indirectly as system clock.")
        self.HSIKERON = BitField(self, 0x00000200, "HSIKERON", "HSI16 always enable for peripheral kernels.. Set and cleared by software to force HSI16 ON even in Stop modes. The HSI16 can only feed USARTs and I<sup>2</sup>Cs peripherals configured with HSI16 as kernel clock. Keeping the HSI16 ON in Stop mode allows to avoid slowing down the communication speed because of the HSI16 startup time. This bit has no effect on HSION value.")
        self.HSIRDY = BitField(self, 0x00000400, "HSIRDY", "HSI16 clock ready flag. Set by hardware to indicate that HSI16 oscillator is stable. This bit is set only when HSI16 is enabled by software by setting HSION. Note: Once the HSION bit is cleared, HSIRDY goes low after 6 HSI16 clock cycles.")
        self.HSEON = BitField(self, 0x00010000, "HSEON", "HSE clock enable. Set and cleared by software. Cleared by hardware to stop the HSE oscillator when entering Stop, Standby or Shutdown mode. This bit cannot be reset if the HSE oscillator is used directly or indirectly as the system clock.")
        self.HSERDY = BitField(self, 0x00020000, "HSERDY", "HSE clock ready flag. Set by hardware to indicate that the HSE oscillator is stable. Note: Once the HSEON bit is cleared, HSERDY goes low after 6 HSE clock cycles.")
        self.HSEBYP = BitField(self, 0x00040000, "HSEBYP", "HSE crystal oscillator bypass. Set and cleared by software to bypass the oscillator with an external clock. The external clock must be enabled with the HSEON bit set, to be used by the device. The HSEBYP bit can be written only if the HSE oscillator is disabled.")
        self.CSSON = BitField(self, 0x00080000, "CSSON", "Clock security system enable. Set by software to enable the clock security system. When CSSON is set, the clock detector is enabled by hardware when the HSE oscillator is ready, and disabled by hardware if a HSE clock failure is detected. This bit is set only and is cleared by reset.")
        self.PLLON = BitField(self, 0x01000000, "PLLON", "Main PLL enable. Set and cleared by software to enable the main PLL. Cleared by hardware when entering Stop, Standby or Shutdown mode. This bit cannot be reset if the PLL clock is used as the system clock.")
        self.PLLRDY = BitField(self, 0x02000000, "PLLRDY", "Main PLL clock ready flag. Set by hardware to indicate that the main PLL is locked.")

class SA_RCC_ICSCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x40000000, "ICSCR", "Internal clock sources calibration register")
        self.HSICAL = BitField(self, 0x00FF0000, "HSICAL", "HSI16 clock calibration. These bits are initialized at startup with the factory-programmed HSI16 calibration trim value. When HSITRIM is written, HSICAL is updated with the sum of HSITRIM and the factory trim value.")
        self.HSITRIM = BitField(self, 0x7F000000, "HSITRIM", "HSI16 clock trimming. These bits provide an additional user-programmable trimming value that is added to the HSICAL[7:0] bits. It can be programmed to adjust to variations in voltage and temperature that influence the frequency of the HSI16. The default value is 16, which, when added to the HSICAL value, should trim the HSI16 to 16 MHz 1 %.")

class SA_RCC_CFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x5, "CFGR", "Clock configuration register")
        self.SW = BitField(self, 0x00000003, "SW", "System clock switch. Set and cleared by software to select system clock source (SYSCLK). Configured by hardware to force HSI16 oscillator selection when exiting stop and standby modes or in case of failure of the HSE oscillator.")
        self.SWS = BitField(self, 0x0000000C, "SWS", "System clock switch status. Set and cleared by hardware to indicate which clock source is used as system clock.")
        self.HPRE = BitField(self, 0x000000F0, "HPRE", "AHB prescaler. Set and cleared by software to control the division factor of the AHB clock. Note: Depending on the device voltage range, the software has to set correctly these bits to ensure that the system frequency does not exceed the maximum allowed frequency (for more details please refer to Section 6.1.5: Dynamic voltage scaling management). After a write operation to these bits and before decreasing the voltage range, this register must be read to be sure that the new value has been taken into account. 0xxx: SYSCLK not divided")
        self.PPRE1 = BitField(self, 0x00000700, "PPRE1", "APB1 prescaler. Set and cleared by software to control the division factor of the APB1 clock (PCLK1). 0xx: HCLK not divided")
        self.PPRE2 = BitField(self, 0x00003800, "PPRE2", "APB2 prescaler. Set and cleared by software to control the division factor of the APB2 clock (PCLK2). 0xx: HCLK not divided")
        self.MCOSEL = BitField(self, 0x0F000000, "MCOSEL", "Microcontroller clock output . Set and cleared by software. Others: Reserved Note: This clock output may have some truncated cycles at startup or during MCO clock source switching.")
        self.MCOPRE = BitField(self, 0x70000000, "MCOPRE", "Microcontroller clock output prescaler. These bits are set and cleared by software. It is highly recommended to change this prescaler before MCO output is enabled. Others: not allowed")
        self.PPRE = Subscriptor(self, "PPRE{}")

class SA_RCC_PLLCFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x1000, "PLLCFGR", "PLL configuration register")
        self.PLLSRC = BitField(self, 0x00000003, "PLLSRC", "Main PLL entry clock source. Set and cleared by software to select PLL clock source. These bits can be written only when PLL is disabled. In order to save power, when no PLL is used, the value of PLLSRC should be 00.")
        self.PLLM = BitField(self, 0x000000F0, "PLLM", "Division factor for the main PLL input clock. Set and cleared by software to divide the PLL input clock before the VCO. These bits can be written only when all PLLs are disabled. VCO input frequency = PLL input clock frequency / PLLM with 1 <= PLLM <= 16 ... Note: The software has to set these bits correctly to ensure that the VCO input frequency is within the range defined in the device datasheet.")
        self.PLLN = BitField(self, 0x00007F00, "PLLN", "Main PLL multiplication factor for VCO. Set and cleared by software to control the multiplication factor of the VCO. These bits can be written only when the PLL is disabled. VCO output frequency = VCO input frequency x PLLN with 8 =< PLLN =< 127 ... ... Note: The software has to set correctly these bits to assure that the VCO output frequency is within the range defined in the device datasheet.")
        self.PLLPEN = BitField(self, 0x00010000, "PLLPEN", "Main PLL PLL P clock output enable. Set and reset by software to enable the PLL P clock output of the PLL. In order to save power, when the PLL P clock output of the PLL is not used, the value of PLLPEN should be 0.")
        self.PLLP = BitField(self, 0x00020000, "PLLP", "Main PLL division factor for PLL P clock.. Set and cleared by software to control the frequency of the main PLL output clock PLL P clock. These bits can be written only if PLL is disabled. When the PLLPDIV[4:0] is set to 00000PLL P output clock frequency = VCO frequency / PLLP with PLLP =7, or 17 Note: The software has to set these bits correctly not to exceed 170 MHz on this domain.")
        self.PLLQEN = BitField(self, 0x00100000, "PLLQEN", "Main PLL Q clock output enable. Set and reset by software to enable the PLL Q clock output of the PLL. In order to save power, when the PLL Q clock output of the PLL is not used, the value of PLLQEN should be 0.")
        self.PLLQ = BitField(self, 0x00600000, "PLLQ", "Main PLL division factor for PLL Q clock.. Set and cleared by software to control the frequency of the main PLL output clock PLL Q clock. This output can be selected for USB, RNG, SAI (48 MHz clock). These bits can be written only if PLL is disabled. PLL Q output clock frequency = VCO frequency / PLLQ with PLLQ = 2, 4, 6, or 8 Note: The software has to set these bits correctly not to exceed 170 MHz on this domain.")
        self.PLLREN = BitField(self, 0x01000000, "PLLREN", "PLL R clock output enable. Set and reset by software to enable the PLL R clock output of the PLL (used as system clock). This bit cannot be written when PLL R clock output of the PLL is used as System Clock. In order to save power, when the PLL R clock output of the PLL is not used, the value of PLLREN should be 0.")
        self.PLLR = BitField(self, 0x06000000, "PLLR", "Main PLL division factor for PLL R clock (system clock). Set and cleared by software to control the frequency of the main PLL output clock PLLCLK. This output can be selected as system clock. These bits can be written only if PLL is disabled. PLL R output clock frequency = VCO frequency / PLLR with PLLR = 2, 4, 6, or 8 Note: The software has to set these bits correctly not to exceed 170 MHz on this domain.")
        self.PLLPDIV = BitField(self, 0xF8000000, "PLLPDIV", "Main PLLP division factor. Set and cleared by software to control the PLL P frequency. PLL P output clock frequency = VCO frequency / PLLPDIV. ....")

class SA_RCC_CIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CIER", "Clock interrupt enable register")
        self.LSIRDYIE = BitField(self, 0x00000001, "LSIRDYIE", "LSI ready interrupt enable. Set and cleared by software to enable/disable interrupt caused by the LSI oscillator stabilization.")
        self.LSERDYIE = BitField(self, 0x00000002, "LSERDYIE", "LSE ready interrupt enable. Set and cleared by software to enable/disable interrupt caused by the LSE oscillator stabilization.")
        self.HSIRDYIE = BitField(self, 0x00000008, "HSIRDYIE", "HSI16 ready interrupt enable. Set and cleared by software to enable/disable interrupt caused by the HSI16 oscillator stabilization.")
        self.HSERDYIE = BitField(self, 0x00000010, "HSERDYIE", "HSE ready interrupt enable. Set and cleared by software to enable/disable interrupt caused by the HSE oscillator stabilization.")
        self.PLLRDYIE = BitField(self, 0x00000020, "PLLRDYIE", "PLL ready interrupt enable. Set and cleared by software to enable/disable interrupt caused by PLL lock.")
        self.LSECSSIE = BitField(self, 0x00000200, "LSECSSIE", "LSE clock security system interrupt enable. Set and cleared by software to enable/disable interrupt caused by the clock security system on LSE.")
        self.HSI48RDYIE = BitField(self, 0x00000400, "HSI48RDYIE", "HSI48 ready interrupt enable . Set and cleared by software to enable/disable interrupt caused by the internal HSI48 oscillator.")

class SA_RCC_CIFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CIFR", "Clock interrupt flag register")
        self.LSIRDYF = BitField(self, 0x00000001, "LSIRDYF", "LSI ready interrupt flag. Set by hardware when the LSI clock becomes stable and LSIRDYDIE is set. Cleared by software setting the LSIRDYC bit.")
        self.LSERDYF = BitField(self, 0x00000002, "LSERDYF", "LSE ready interrupt flag. Set by hardware when the LSE clock becomes stable and LSERDYDIE is set. Cleared by software setting the LSERDYC bit.")
        self.HSIRDYF = BitField(self, 0x00000008, "HSIRDYF", "HSI16 ready interrupt flag. Set by hardware when the HSI16 clock becomes stable and HSIRDYDIE is set in a response to setting the HSION (refer to Clock control register (RCC_CR)). When HSION is not set but the HSI16 oscillator is enabled by the peripheral through a clock request, this bit is not set and no interrupt is generated. Cleared by software setting the HSIRDYC bit.")
        self.HSERDYF = BitField(self, 0x00000010, "HSERDYF", "HSE ready interrupt flag. Set by hardware when the HSE clock becomes stable and HSERDYDIE is set. Cleared by software setting the HSERDYC bit.")
        self.PLLRDYF = BitField(self, 0x00000020, "PLLRDYF", "PLL ready interrupt flag. Set by hardware when the PLL locks and PLLRDYDIE is set. Cleared by software setting the PLLRDYC bit.")
        self.CSSF = BitField(self, 0x00000100, "CSSF", "Clock security system interrupt flag. Set by hardware when a failure is detected in the HSE oscillator. Cleared by software setting the CSSC bit.")
        self.LSECSSF = BitField(self, 0x00000200, "LSECSSF", "LSE Clock security system interrupt flag. Set by hardware when a failure is detected in the LSE oscillator. Cleared by software setting the LSECSSC bit.")
        self.HSI48RDYF = BitField(self, 0x00000400, "HSI48RDYF", "HSI48 ready interrupt flag . Set by hardware when the HSI48 clock becomes stable and HSI48RDYIE is set in a response to setting the HSI48ON (refer to Clock recovery RC register (RCC_CRRCR)). Cleared by software setting the HSI48RDYC bit.")

class SA_RCC_CICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CICR", "Clock interrupt clear register")
        self.LSIRDYC = BitField(self, 0x00000001, "LSIRDYC", "LSI ready interrupt clear. This bit is set by software to clear the LSIRDYF flag.")
        self.LSERDYC = BitField(self, 0x00000002, "LSERDYC", "LSE ready interrupt clear. This bit is set by software to clear the LSERDYF flag.")
        self.HSIRDYC = BitField(self, 0x00000008, "HSIRDYC", "HSI16 ready interrupt clear. This bit is set software to clear the HSIRDYF flag.")
        self.HSERDYC = BitField(self, 0x00000010, "HSERDYC", "HSE ready interrupt clear. This bit is set by software to clear the HSERDYF flag.")
        self.PLLRDYC = BitField(self, 0x00000020, "PLLRDYC", "PLL ready interrupt clear. This bit is set by software to clear the PLLRDYF flag.")
        self.CSSC = BitField(self, 0x00000100, "CSSC", "Clock security system interrupt clear. This bit is set by software to clear the CSSF flag.")
        self.LSECSSC = BitField(self, 0x00000200, "LSECSSC", "LSE Clock security system interrupt clear. This bit is set by software to clear the LSECSSF flag.")
        self.HSI48RDYC = BitField(self, 0x00000400, "HSI48RDYC", "HSI48 oscillator ready interrupt clear . This bit is set by software to clear the HSI48RDYF flag.")

class SA_RCC_AHB1RSTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AHB1RSTR", "AHB1 peripheral reset register")
        self.DMA1RST = BitField(self, 0x00000001, "DMA1RST", "DMA1 reset. Set and cleared by software.")
        self.DMA2RST = BitField(self, 0x00000002, "DMA2RST", "DMA2 reset. Set and cleared by software.")
        self.DMAMUX1RST = BitField(self, 0x00000004, "DMAMUX1RST", "Set and cleared by software.")
        self.CORDICRST = BitField(self, 0x00000008, "CORDICRST", "Set and cleared by software")
        self.FMACRST = BitField(self, 0x00000010, "FMACRST", "Set and cleared by software")
        self.FLASHRST = BitField(self, 0x00000100, "FLASHRST", "Flash memory interface reset. Set and cleared by software. This bit can be activated only when the Flash memory is in power down mode.")
        self.CRCRST = BitField(self, 0x00001000, "CRCRST", "CRC reset. Set and cleared by software.")
        self.DMARST = Subscriptor(self, "DMA{}RST")

class SA_RCC_AHB2RSTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AHB2RSTR", "AHB2 peripheral reset register")
        self.GPIOARST = BitField(self, 0x00000001, "GPIOARST", "IO port A reset. Set and cleared by software.")
        self.GPIOBRST = BitField(self, 0x00000002, "GPIOBRST", "IO port B reset. Set and cleared by software.")
        self.GPIOCRST = BitField(self, 0x00000004, "GPIOCRST", "IO port C reset. Set and cleared by software.")
        self.GPIODRST = BitField(self, 0x00000008, "GPIODRST", "IO port D reset. Set and cleared by software.")
        self.GPIOERST = BitField(self, 0x00000010, "GPIOERST", "IO port E reset. Set and cleared by software.")
        self.GPIOFRST = BitField(self, 0x00000020, "GPIOFRST", "IO port F reset. Set and cleared by software.")
        self.GPIOGRST = BitField(self, 0x00000040, "GPIOGRST", "IO port G reset. Set and cleared by software.")
        self.ADC12RST = BitField(self, 0x00002000, "ADC12RST", "ADC12 reset. Set and cleared by software.")
        self.ADC345RST = BitField(self, 0x00004000, "ADC345RST", "ADC345 reset. Set and cleared by software.")
        self.DAC1RST = BitField(self, 0x00010000, "DAC1RST", "DAC1 reset. Set and cleared by software.")
        self.DAC2RST = BitField(self, 0x00020000, "DAC2RST", "DAC2 reset. Set and cleared by software.")
        self.DAC3RST = BitField(self, 0x00040000, "DAC3RST", "DAC3 reset. Set and cleared by software.")
        self.DAC4RST = BitField(self, 0x00080000, "DAC4RST", "DAC4 reset. Set and cleared by software.")
        self.AESRST = BitField(self, 0x01000000, "AESRST", "AESRST reset . Set and cleared by software.")
        self.RNGRST = BitField(self, 0x04000000, "RNGRST", "RNG reset. Set and cleared by software.")
        self.DACRST = Subscriptor(self, "DAC{}RST")

class SA_RCC_AHB3RSTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AHB3RSTR", "AHB3 peripheral reset register")
        self.FMCRST = BitField(self, 0x00000001, "FMCRST", "Flexible static memory controller reset. Set and cleared by software.")
        self.QSPIRST = BitField(self, 0x00000100, "QSPIRST", "QUADSPI reset. Set and cleared by software.")

class SA_RCC_APB1RSTR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB1RSTR1", "APB1 peripheral reset register 1")
        self.TIM2RST = BitField(self, 0x00000001, "TIM2RST", "TIM2 timer reset. Set and cleared by software.")
        self.TIM3RST = BitField(self, 0x00000002, "TIM3RST", "TIM3 timer reset. Set and cleared by software.")
        self.TIM4RST = BitField(self, 0x00000004, "TIM4RST", "TIM3 timer reset. Set and cleared by software.")
        self.TIM5RST = BitField(self, 0x00000008, "TIM5RST", "TIM5 timer reset. Set and cleared by software.")
        self.TIM6RST = BitField(self, 0x00000010, "TIM6RST", "TIM6 timer reset. Set and cleared by software.")
        self.TIM7RST = BitField(self, 0x00000020, "TIM7RST", "TIM7 timer reset. Set and cleared by software.")
        self.CRSRST = BitField(self, 0x00000100, "CRSRST", "CRS reset. Set and cleared by software.")
        self.SPI2RST = BitField(self, 0x00004000, "SPI2RST", "SPI2 reset. Set and cleared by software.")
        self.SPI3RST = BitField(self, 0x00008000, "SPI3RST", "SPI3 reset. Set and cleared by software.")
        self.USART2RST = BitField(self, 0x00020000, "USART2RST", "USART2 reset. Set and cleared by software.")
        self.USART3RST = BitField(self, 0x00040000, "USART3RST", "USART3 reset. Set and cleared by software.")
        self.UART4RST = BitField(self, 0x00080000, "UART4RST", "UART4 reset. Set and cleared by software.")
        self.UART5RST = BitField(self, 0x00100000, "UART5RST", "UART5 reset. Set and cleared by software.")
        self.I2C1RST = BitField(self, 0x00200000, "I2C1RST", "I2C1 reset. Set and cleared by software.")
        self.I2C2RST = BitField(self, 0x00400000, "I2C2RST", "I2C2 reset. Set and cleared by software.")
        self.USBRST = BitField(self, 0x00800000, "USBRST", "USB device reset. Set and reset by software.")
        self.FDCANRST = BitField(self, 0x02000000, "FDCANRST", "FDCAN reset. Set and reset by software.")
        self.PWRRST = BitField(self, 0x10000000, "PWRRST", "Power interface reset. Set and cleared by software.")
        self.I2C3RST = BitField(self, 0x40000000, "I2C3RST", "I2C3 reset. Set and cleared by software.")
        self.LPTIM1RST = BitField(self, 0x80000000, "LPTIM1RST", "Low Power Timer 1 reset. Set and cleared by software.")
        self.USARTRST = Subscriptor(self, "USART{}RST")
        self.SPIRST = Subscriptor(self, "SPI{}RST")
        self.UARTRST = Subscriptor(self, "UART{}RST")
        self.I2CRST = Subscriptor(self, "I2C{}RST")
        self.TIMRST = Subscriptor(self, "TIM{}RST")

class SA_RCC_APB1RSTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB1RSTR2", "APB1 peripheral reset register 2")
        self.LPUART1RST = BitField(self, 0x00000001, "LPUART1RST", "Low-power UART 1 reset. Set and cleared by software.")
        self.I2C4RST = BitField(self, 0x00000002, "I2C4RST", "I2C4 reset. Set and cleared by software")
        self.UCPD1RST = BitField(self, 0x00000100, "UCPD1RST", "UCPD1 reset. Set and cleared by software.")

class SA_RCC_APB2RSTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB2RSTR", "APB2 peripheral reset register")
        self.SYSCFGRST = BitField(self, 0x00000001, "SYSCFGRST", "SYSCFG + COMP + OPAMP + VREFBUF reset")
        self.TIM1RST = BitField(self, 0x00000800, "TIM1RST", "TIM1 timer reset. Set and cleared by software.")
        self.SPI1RST = BitField(self, 0x00001000, "SPI1RST", "SPI1 reset. Set and cleared by software.")
        self.TIM8RST = BitField(self, 0x00002000, "TIM8RST", "TIM8 timer reset. Set and cleared by software.")
        self.USART1RST = BitField(self, 0x00004000, "USART1RST", "USART1 reset. Set and cleared by software.")
        self.SPI4RST = BitField(self, 0x00008000, "SPI4RST", "SPI4 reset. Set and cleared by software.")
        self.TIM15RST = BitField(self, 0x00010000, "TIM15RST", "TIM15 timer reset. Set and cleared by software.")
        self.TIM16RST = BitField(self, 0x00020000, "TIM16RST", "TIM16 timer reset. Set and cleared by software.")
        self.TIM17RST = BitField(self, 0x00040000, "TIM17RST", "TIM17 timer reset. Set and cleared by software.")
        self.TIM20RST = BitField(self, 0x00100000, "TIM20RST", "TIM20 reset. Set and cleared by software.")
        self.SAI1RST = BitField(self, 0x00200000, "SAI1RST", "Serial audio interface 1 (SAI1) reset. Set and cleared by software.")
        self.HRTIM1RST = BitField(self, 0x04000000, "HRTIM1RST", "HRTIM1 reset. Set and cleared by software.")
        self.TIMRST = Subscriptor(self, "TIM{}RST")

class SA_RCC_AHB1ENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x100, "AHB1ENR", "AHB1 peripheral clock enable register")
        self.DMA1EN = BitField(self, 0x00000001, "DMA1EN", "DMA1 clock enable. Set and cleared by software.")
        self.DMA2EN = BitField(self, 0x00000002, "DMA2EN", "DMA2 clock enable. Set and cleared by software.")
        self.DMAMUX1EN = BitField(self, 0x00000004, "DMAMUX1EN", "DMAMUX1 clock enable. Set and reset by software.")
        self.CORDICEN = BitField(self, 0x00000008, "CORDICEN", "CORDIC clock enable. Set and reset by software.")
        self.FMACEN = BitField(self, 0x00000010, "FMACEN", "FMAC enable. Set and reset by software.")
        self.FLASHEN = BitField(self, 0x00000100, "FLASHEN", "Flash memory interface clock enable. Set and cleared by software. This bit can be disabled only when the Flash is in power down mode.")
        self.CRCEN = BitField(self, 0x00001000, "CRCEN", "CRC clock enable. Set and cleared by software.")
        self.DMAEN = Subscriptor(self, "DMA{}EN")

class SA_RCC_AHB2ENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AHB2ENR", "AHB2 peripheral clock enable register")
        self.GPIOAEN = BitField(self, 0x00000001, "GPIOAEN", "IO port A clock enable. Set and cleared by software.")
        self.GPIOBEN = BitField(self, 0x00000002, "GPIOBEN", "IO port B clock enable. Set and cleared by software.")
        self.GPIOCEN = BitField(self, 0x00000004, "GPIOCEN", "IO port C clock enable. Set and cleared by software.")
        self.GPIODEN = BitField(self, 0x00000008, "GPIODEN", "IO port D clock enable. Set and cleared by software.")
        self.GPIOEEN = BitField(self, 0x00000010, "GPIOEEN", "IO port E clock enable. Set and cleared by software.")
        self.GPIOFEN = BitField(self, 0x00000020, "GPIOFEN", "IO port F clock enable. Set and cleared by software.")
        self.GPIOGEN = BitField(self, 0x00000040, "GPIOGEN", "IO port G clock enable. Set and cleared by software.")
        self.ADC12EN = BitField(self, 0x00002000, "ADC12EN", "ADC12 clock enable. Set and cleared by software.")
        self.ADC345EN = BitField(self, 0x00004000, "ADC345EN", "ADC345 clock enable . Set and cleared by software")
        self.DAC1EN = BitField(self, 0x00010000, "DAC1EN", "DAC1 clock enable. Set and cleared by software.")
        self.DAC2EN = BitField(self, 0x00020000, "DAC2EN", "DAC2 clock enable. Set and cleared by software.")
        self.DAC3EN = BitField(self, 0x00040000, "DAC3EN", "DAC3 clock enable. Set and cleared by software.")
        self.DAC4EN = BitField(self, 0x00080000, "DAC4EN", "DAC4 clock enable. Set and cleared by software.")
        self.AESEN = BitField(self, 0x01000000, "AESEN", "AES clock enable. Set and cleared by software.")
        self.RNGEN = BitField(self, 0x04000000, "RNGEN", "RNG enable. Set and cleared by software.")
        self.DACEN = Subscriptor(self, "DAC{}EN")

class SA_RCC_AHB3ENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AHB3ENR", "AHB3 peripheral clock enable register")
        self.FMCEN = BitField(self, 0x00000001, "FMCEN", "Flexible static memory controller clock enable. Set and cleared by software.")
        self.QSPIEN = BitField(self, 0x00000100, "QSPIEN", "QUADSPI memory interface clock enable. Set and cleared by software.")

class SA_RCC_APB1ENR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x400, "APB1ENR1", "APB1 peripheral clock enable register 1")
        self.TIM2EN = BitField(self, 0x00000001, "TIM2EN", "TIM2 timer clock enable. Set and cleared by software.")
        self.TIM3EN = BitField(self, 0x00000002, "TIM3EN", "TIM3 timer clock enable. Set and cleared by software.")
        self.TIM4EN = BitField(self, 0x00000004, "TIM4EN", "TIM4 timer clock enable. Set and cleared by software.")
        self.TIM5EN = BitField(self, 0x00000008, "TIM5EN", "TIM5 timer clock enable. Set and cleared by software.")
        self.TIM6EN = BitField(self, 0x00000010, "TIM6EN", "TIM6 timer clock enable. Set and cleared by software.")
        self.TIM7EN = BitField(self, 0x00000020, "TIM7EN", "TIM7 timer clock enable. Set and cleared by software.")
        self.CRSEN = BitField(self, 0x00000100, "CRSEN", "CRS Recovery System clock enable. Set and cleared by software.")
        self.RTCAPBEN = BitField(self, 0x00000400, "RTCAPBEN", "RTC APB clock enable . Set and cleared by software")
        self.WWDGEN = BitField(self, 0x00000800, "WWDGEN", "Window watchdog clock enable. Set by software to enable the window watchdog clock. Reset by hardware system reset. This bit can also be set by hardware if the WWDG_SW option bit is reset.")
        self.SPI2EN = BitField(self, 0x00004000, "SPI2EN", "SPI2 clock enable. Set and cleared by software.")
        self.SPI3EN = BitField(self, 0x00008000, "SPI3EN", "SPI3 clock enable. Set and cleared by software.")
        self.USART2EN = BitField(self, 0x00020000, "USART2EN", "USART2 clock enable. Set and cleared by software.")
        self.USART3EN = BitField(self, 0x00040000, "USART3EN", "USART3 clock enable. Set and cleared by software.")
        self.UART4EN = BitField(self, 0x00080000, "UART4EN", "UART4 clock enable. Set and cleared by software.")
        self.UART5EN = BitField(self, 0x00100000, "UART5EN", "UART5 clock enable. Set and cleared by software.")
        self.I2C1EN = BitField(self, 0x00200000, "I2C1EN", "I2C1 clock enable. Set and cleared by software.")
        self.I2C2EN = BitField(self, 0x00400000, "I2C2EN", "I2C2 clock enable. Set and cleared by software.")
        self.USBEN = BitField(self, 0x00800000, "USBEN", "USB device clock enable. Set and cleared by software.")
        self.FDCANEN = BitField(self, 0x02000000, "FDCANEN", "FDCAN clock enable. Set and cleared by software.")
        self.PWREN = BitField(self, 0x10000000, "PWREN", "Power interface clock enable. Set and cleared by software.")
        self.I2C3EN = BitField(self, 0x40000000, "I2C3EN", "I2C3 clock enable. Set and cleared by software.")
        self.LPTIM1EN = BitField(self, 0x80000000, "LPTIM1EN", "Low power timer 1 clock enable. Set and cleared by software.")
        self.SPIEN = Subscriptor(self, "SPI{}EN")
        self.TIMEN = Subscriptor(self, "TIM{}EN")
        self.UARTEN = Subscriptor(self, "UART{}EN")
        self.I2CEN = Subscriptor(self, "I2C{}EN")
        self.USARTEN = Subscriptor(self, "USART{}EN")

class SA_RCC_APB1ENR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB1ENR2", "APB1 peripheral clock enable register 2")
        self.LPUART1EN = BitField(self, 0x00000001, "LPUART1EN", "Low power UART 1 clock enable. Set and cleared by software.")
        self.I2C4EN = BitField(self, 0x00000002, "I2C4EN", "I2C4 clock enable . Set and cleared by software")
        self.UCPD1EN = BitField(self, 0x00000100, "UCPD1EN", "UCPD1 clock enable. Set and cleared by software.")

class SA_RCC_APB2ENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "APB2ENR", "APB2 peripheral clock enable register")
        self.SYSCFGEN = BitField(self, 0x00000001, "SYSCFGEN", "SYSCFG + COMP + VREFBUF + OPAMP clock enable. Set and cleared by software.")
        self.TIM1EN = BitField(self, 0x00000800, "TIM1EN", "TIM1 timer clock enable. Set and cleared by software.")
        self.SPI1EN = BitField(self, 0x00001000, "SPI1EN", "SPI1 clock enable. Set and cleared by software.")
        self.TIM8EN = BitField(self, 0x00002000, "TIM8EN", "TIM8 timer clock enable. Set and cleared by software.")
        self.USART1EN = BitField(self, 0x00004000, "USART1EN", "USART1clock enable. Set and cleared by software.")
        self.SPI4EN = BitField(self, 0x00008000, "SPI4EN", "SPI4 clock enable. Set and cleared by software.")
        self.TIM15EN = BitField(self, 0x00010000, "TIM15EN", "TIM15 timer clock enable. Set and cleared by software.")
        self.TIM16EN = BitField(self, 0x00020000, "TIM16EN", "TIM16 timer clock enable. Set and cleared by software.")
        self.TIM17EN = BitField(self, 0x00040000, "TIM17EN", "TIM17 timer clock enable. Set and cleared by software.")
        self.TIM20EN = BitField(self, 0x00100000, "TIM20EN", "TIM20 timer clock enable. Set and cleared by software.")
        self.SAI1EN = BitField(self, 0x00200000, "SAI1EN", "SAI1 clock enable. Set and cleared by software.")
        self.HRTIM1EN = BitField(self, 0x04000000, "HRTIM1EN", "HRTIM1 clock enable. Set and cleared by software.")
        self.TIMEN = Subscriptor(self, "TIM{}EN")

class SA_RCC_AHB1SMENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x130F, "AHB1SMENR", "AHB1 peripheral clocks enable in Sleep and Stop modes register")
        self.DMA1SMEN = BitField(self, 0x00000001, "DMA1SMEN", "DMA1 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.DMA2SMEN = BitField(self, 0x00000002, "DMA2SMEN", "DMA2 clocks enable during Sleep and Stop modes. Set and cleared by software during Sleep mode.")
        self.DMAMUX1SMEN = BitField(self, 0x00000004, "DMAMUX1SMEN", "DMAMUX1 clock enable during Sleep and Stop modes.. Set and cleared by software.")
        self.CORDICSMEN = BitField(self, 0x00000008, "CORDICSMEN", "CORDICSM clock enable.. Set and cleared by software.")
        self.FMACSMEN = BitField(self, 0x00000010, "FMACSMEN", "FMACSM clock enable.. Set and cleared by software.")
        self.FLASHSMEN = BitField(self, 0x00000100, "FLASHSMEN", "Flash memory interface clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.SRAM1SMEN = BitField(self, 0x00000200, "SRAM1SMEN", "SRAM1 interface clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.CRCSMEN = BitField(self, 0x00001000, "CRCSMEN", "CRC clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.DMASMEN = Subscriptor(self, "DMA{}SMEN")

class SA_RCC_AHB2SMENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x50F667F, "AHB2SMENR", "AHB2 peripheral clocks enable in Sleep and Stop modes register")
        self.GPIOASMEN = BitField(self, 0x00000001, "GPIOASMEN", "IO port A clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.GPIOBSMEN = BitField(self, 0x00000002, "GPIOBSMEN", "IO port B clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.GPIOCSMEN = BitField(self, 0x00000004, "GPIOCSMEN", "IO port C clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.GPIODSMEN = BitField(self, 0x00000008, "GPIODSMEN", "IO port D clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.GPIOESMEN = BitField(self, 0x00000010, "GPIOESMEN", "IO port E clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.GPIOFSMEN = BitField(self, 0x00000020, "GPIOFSMEN", "IO port F clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.GPIOGSMEN = BitField(self, 0x00000040, "GPIOGSMEN", "IO port G clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.CCMSRAMSMEN = BitField(self, 0x00000200, "CCMSRAMSMEN", "CCM SRAM interface clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.SRAM2SMEN = BitField(self, 0x00000400, "SRAM2SMEN", "SRAM2 interface clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.ADC12SMEN = BitField(self, 0x00002000, "ADC12SMEN", "ADC12 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.ADC345SMEN = BitField(self, 0x00004000, "ADC345SMEN", "ADC345 clock enable. Set and cleared by software.")
        self.DAC1SMEN = BitField(self, 0x00010000, "DAC1SMEN", "DAC1 clock enable. Set and cleared by software.")
        self.DAC2SMEN = BitField(self, 0x00020000, "DAC2SMEN", "DAC2 clock enable. Set and cleared by software.")
        self.DAC3SMEN = BitField(self, 0x00040000, "DAC3SMEN", "DAC3 clock enable. Set and cleared by software.")
        self.DAC4SMEN = BitField(self, 0x00080000, "DAC4SMEN", "DAC4 clock enable. Set and cleared by software.")
        self.AESSMEN = BitField(self, 0x01000000, "AESSMEN", "AESM clocks enable. Set and cleared by software.")
        self.RNGEN = BitField(self, 0x04000000, "RNGEN", "RNG enable. Set and cleared by software.")
        self.DACSMEN = Subscriptor(self, "DAC{}SMEN")

class SA_RCC_AHB3SMENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x101, "AHB3SMENR", "AHB3 peripheral clocks enable in Sleep and Stop modes register")
        self.FMCSMEN = BitField(self, 0x00000001, "FMCSMEN", "Flexible static memory controller clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.QSPISMEN = BitField(self, 0x00000100, "QSPISMEN", "QUADSPI memory interface clock enable during Sleep and Stop modes. Set and cleared by software.")

class SA_RCC_APB1SMENR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xD2FECD3F, "APB1SMENR1", "APB1 peripheral clocks enable in Sleep and Stop modes register 1")
        self.TIM2SMEN = BitField(self, 0x00000001, "TIM2SMEN", "TIM2 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM3SMEN = BitField(self, 0x00000002, "TIM3SMEN", "TIM3 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM4SMEN = BitField(self, 0x00000004, "TIM4SMEN", "TIM4 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM5SMEN = BitField(self, 0x00000008, "TIM5SMEN", "TIM5 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM6SMEN = BitField(self, 0x00000010, "TIM6SMEN", "TIM6 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM7SMEN = BitField(self, 0x00000020, "TIM7SMEN", "TIM7 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.CRSSMEN = BitField(self, 0x00000100, "CRSSMEN", "CRS timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.RTCAPBSMEN = BitField(self, 0x00000400, "RTCAPBSMEN", "RTC APB clock enable during Sleep and Stop modes. Set and cleared by software")
        self.WWDGSMEN = BitField(self, 0x00000800, "WWDGSMEN", "Window watchdog clocks enable during Sleep and Stop modes. Set and cleared by software. This bit is forced to 1 by hardware when the hardware WWDG option is activated.")
        self.SPI2SMEN = BitField(self, 0x00004000, "SPI2SMEN", "SPI2 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.SPI3SMEN = BitField(self, 0x00008000, "SPI3SMEN", "SPI3 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.USART2SMEN = BitField(self, 0x00020000, "USART2SMEN", "USART2 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.USART3SMEN = BitField(self, 0x00040000, "USART3SMEN", "USART3 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.UART4SMEN = BitField(self, 0x00080000, "UART4SMEN", "UART4 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.UART5SMEN = BitField(self, 0x00100000, "UART5SMEN", "UART5 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.I2C1SMEN = BitField(self, 0x00200000, "I2C1SMEN", "I2C1 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.I2C2SMEN = BitField(self, 0x00400000, "I2C2SMEN", "I2C2 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.USBSMEN = BitField(self, 0x00800000, "USBSMEN", "USB device clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.FDCANSMEN = BitField(self, 0x02000000, "FDCANSMEN", "FDCAN clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.PWRSMEN = BitField(self, 0x10000000, "PWRSMEN", "Power interface clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.I2C3SMEN = BitField(self, 0x40000000, "I2C3SMEN", "I2C3 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.LPTIM1SMEN = BitField(self, 0x80000000, "LPTIM1SMEN", "Low power timer 1 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.USARTSMEN = Subscriptor(self, "USART{}SMEN")
        self.SPISMEN = Subscriptor(self, "SPI{}SMEN")
        self.UARTSMEN = Subscriptor(self, "UART{}SMEN")
        self.I2CSMEN = Subscriptor(self, "I2C{}SMEN")
        self.TIMSMEN = Subscriptor(self, "TIM{}SMEN")

class SA_RCC_APB1SMENR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x103, "APB1SMENR2", "APB1 peripheral clocks enable in Sleep and Stop modes register 2")
        self.LPUART1SMEN = BitField(self, 0x00000001, "LPUART1SMEN", "Low power UART 1 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.I2C4SMEN = BitField(self, 0x00000002, "I2C4SMEN", "I2C4 clocks enable during Sleep and Stop modes . Set and cleared by software")
        self.UCPD1SMEN = BitField(self, 0x00000100, "UCPD1SMEN", "UCPD1 clocks enable during Sleep and Stop modes. Set and cleared by software.")

class SA_RCC_APB2SMENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x437F801, "APB2SMENR", "APB2 peripheral clocks enable in Sleep and Stop modes register")
        self.SYSCFGSMEN = BitField(self, 0x00000001, "SYSCFGSMEN", "SYSCFG + COMP + VREFBUF + OPAMP clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM1SMEN = BitField(self, 0x00000800, "TIM1SMEN", "TIM1 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.SPI1SMEN = BitField(self, 0x00001000, "SPI1SMEN", "SPI1 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM8SMEN = BitField(self, 0x00002000, "TIM8SMEN", "TIM8 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.USART1SMEN = BitField(self, 0x00004000, "USART1SMEN", "USART1clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.SPI4SMEN = BitField(self, 0x00008000, "SPI4SMEN", "SPI4 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM15SMEN = BitField(self, 0x00010000, "TIM15SMEN", "TIM15 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM16SMEN = BitField(self, 0x00020000, "TIM16SMEN", "TIM16 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM17SMEN = BitField(self, 0x00040000, "TIM17SMEN", "TIM17 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIM20SMEN = BitField(self, 0x00100000, "TIM20SMEN", "TIM20 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.SAI1SMEN = BitField(self, 0x00200000, "SAI1SMEN", "SAI1 clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.HRTIM1SMEN = BitField(self, 0x04000000, "HRTIM1SMEN", "HRTIM1 timer clocks enable during Sleep and Stop modes. Set and cleared by software.")
        self.TIMSMEN = Subscriptor(self, "TIM{}SMEN")

class SA_RCC_CCIPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCIPR", "Peripherals independent clock configuration register")
        self.USART1SEL = BitField(self, 0x00000003, "USART1SEL", "USART1 clock source selection. This bit is set and cleared by software to select the USART1 clock source.")
        self.USART2SEL = BitField(self, 0x0000000C, "USART2SEL", "USART2 clock source selection. This bit is set and cleared by software to select the USART2 clock source.")
        self.USART3SEL = BitField(self, 0x00000030, "USART3SEL", "USART3 clock source selection. This bit is set and cleared by software to select the USART3 clock source.")
        self.UART4SEL = BitField(self, 0x000000C0, "UART4SEL", "UART4 clock source selection. This bit is set and cleared by software to select the UART4 clock source.")
        self.UART5SEL = BitField(self, 0x00000300, "UART5SEL", "UART5 clock source selection. These bits are set and cleared by software to select the UART5 clock source.")
        self.LPUART1SEL = BitField(self, 0x00000C00, "LPUART1SEL", "LPUART1 clock source selection. These bits are set and cleared by software to select the LPUART1 clock source.")
        self.I2C1SEL = BitField(self, 0x00003000, "I2C1SEL", "I2C1 clock source selection. These bits are set and cleared by software to select the I2C1 clock source.")
        self.I2C2SEL = BitField(self, 0x0000C000, "I2C2SEL", "I2C2 clock source selection. These bits are set and cleared by software to select the I2C2 clock source.")
        self.I2C3SEL = BitField(self, 0x00030000, "I2C3SEL", "I2C3 clock source selection. These bits are set and cleared by software to select the I2C3 clock source.")
        self.LPTIM1SEL = BitField(self, 0x000C0000, "LPTIM1SEL", "Low power timer 1 clock source selection. These bits are set and cleared by software to select the LPTIM1 clock source.")
        self.SAI1SEL = BitField(self, 0x00300000, "SAI1SEL", "clock source selection. These bits are set and cleared by software to select the SAI clock source.")
        self.I2S23SEL = BitField(self, 0x00C00000, "I2S23SEL", "clock source selection. These bits are set and cleared by software to select the I2S23 clock source.")
        self.FDCANSEL = BitField(self, 0x03000000, "FDCANSEL", "None")
        self.CLK48SEL = BitField(self, 0x0C000000, "CLK48SEL", "48 MHz clock source selection. These bits are set and cleared by software to select the 48 MHz clock source used by USB device FS and RNG.")
        self.ADC12SEL = BitField(self, 0x30000000, "ADC12SEL", "ADC1/2 clock source selection. These bits are set and cleared by software to select the clock source used by the ADC interface.")
        self.ADC345SEL = BitField(self, 0xC0000000, "ADC345SEL", "ADC3/4/5 clock source selection. These bits are set and cleared by software to select the clock source used by the ADC345 interface.")
        self.I2CSEL = Subscriptor(self, "I2C{}SEL")
        self.UARTSEL = Subscriptor(self, "UART{}SEL")
        self.USARTSEL = Subscriptor(self, "USART{}SEL")

class SA_RCC_BDCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDCR", "RTC domain control register")
        self.LSEON = BitField(self, 0x00000001, "LSEON", "LSE oscillator enable. Set and cleared by software.")
        self.LSERDY = BitField(self, 0x00000002, "LSERDY", "LSE oscillator ready. Set and cleared by hardware to indicate when the external 32 kHz oscillator is stable. After the LSEON bit is cleared, LSERDY goes low after 6 external low-speed oscillator clock cycles.")
        self.LSEBYP = BitField(self, 0x00000004, "LSEBYP", "LSE oscillator bypass. Set and cleared by software to bypass oscillator in debug mode. This bit can be written only when the external 32 kHz oscillator is disabled (LSEON=0 and LSERDY=0).")
        self.LSEDRV = BitField(self, 0x00000018, "LSEDRV", "LSE oscillator drive capability. Set by software to modulate the LSE oscillators drive capability. The oscillator is in Xtal mode when it is not in bypass mode.")
        self.LSECSSON = BitField(self, 0x00000020, "LSECSSON", "CSS on LSE enable. Set by software to enable the Clock Security System on LSE (32 kHz oscillator). LSECSSON must be enabled after the LSE oscillator is enabled (LSEON bit enabled) and ready (LSERDY flag set by hardware), and after the RTCSEL bit is selected. Once enabled this bit cannot be disabled, except after a LSE failure detection (LSECSSD =1). In that case the software MUST disable the LSECSSON bit.")
        self.LSECSSD = BitField(self, 0x00000040, "LSECSSD", "CSS on LSE failure Detection. Set by hardware to indicate when a failure has been detected by the Clock Security System on the external 32 kHz oscillator (LSE).")
        self.RTCSEL = BitField(self, 0x00000300, "RTCSEL", "RTC clock source selection. Set by software to select the clock source for the RTC. Once the RTC clock source has been selected, it cannot be changed anymore unless the RTC domain is reset, or unless a failure is detected on LSE (LSECSSD is set). The BDRST bit can be used to reset them.")
        self.RTCEN = BitField(self, 0x00008000, "RTCEN", "RTC clock enable. Set and cleared by software.")
        self.BDRST = BitField(self, 0x00010000, "BDRST", "RTC domain software reset. Set and cleared by software.")
        self.LSCOEN = BitField(self, 0x01000000, "LSCOEN", "Low speed clock output enable. Set and cleared by software.")
        self.LSCOSEL = BitField(self, 0x02000000, "LSCOSEL", "Low speed clock output selection. Set and cleared by software.")

class SA_RCC_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xC000000, "CSR", "Control/status register")
        self.LSION = BitField(self, 0x00000001, "LSION", "LSI oscillator enable. Set and cleared by software.")
        self.LSIRDY = BitField(self, 0x00000002, "LSIRDY", "LSI oscillator ready. Set and cleared by hardware to indicate when the LSI oscillator is stable. After the LSION bit is cleared, LSIRDY goes low after 3 LSI oscillator clock cycles. This bit can be set even if LSION = 0 if the LSI is requested by the Clock Security System on LSE, by the Independent Watchdog or by the RTC.")
        self.RMVF = BitField(self, 0x00800000, "RMVF", "Remove reset flag. Set by software to clear the reset flags.")
        self.OBLRSTF = BitField(self, 0x02000000, "OBLRSTF", "Option byte loader reset flag. Set by hardware when a reset from the Option Byte loading occurs. Cleared by writing to the RMVF bit.")
        self.PINRSTF = BitField(self, 0x04000000, "PINRSTF", "Pin reset flag. Set by hardware when a reset from the NRST pin occurs. Cleared by writing to the RMVF bit.")
        self.BORRSTF = BitField(self, 0x08000000, "BORRSTF", "BOR flag. Set by hardware when a BOR occurs. Cleared by writing to the RMVF bit.")
        self.SFTRSTF = BitField(self, 0x10000000, "SFTRSTF", "Software reset flag. Set by hardware when a software reset occurs. Cleared by writing to the RMVF bit.")
        self.IWDGRSTF = BitField(self, 0x20000000, "IWDGRSTF", "Independent window watchdog reset flag. Set by hardware when an independent watchdog reset domain occurs. Cleared by writing to the RMVF bit.")
        self.WWDGRSTF = BitField(self, 0x40000000, "WWDGRSTF", "Window watchdog reset flag. Set by hardware when a window watchdog reset occurs. Cleared by writing to the RMVF bit.")
        self.LPWRRSTF = BitField(self, 0x80000000, "LPWRRSTF", "Low-power reset flag. Set by hardware when a reset occurs due to illegal Stop, Standby or Shutdown mode entry. Cleared by writing to the RMVF bit.")

class SA_RCC_CRRCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CRRCR", "Clock recovery RC register")
        self.HSI48ON = BitField(self, 0x00000001, "HSI48ON", "HSI48 clock enable. Set and cleared by software. Cleared by hardware to stop the HSI48 when entering in Stop, Standby or Shutdown modes.")
        self.HSI48RDY = BitField(self, 0x00000002, "HSI48RDY", "HSI48 clock ready flag. Set by hardware to indicate that HSI48 oscillator is stable. This bit is set only when HSI48 is enabled by software by setting HSI48ON.")
        self.HSI48CAL = BitField(self, 0x0000FF80, "HSI48CAL", "HSI48 clock calibration. These bits are initialized at startup with the factory-programmed HSI48 calibration trim value. They are ready only.")

class SA_RCC_CCIPR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCIPR2", "Peripherals independent clock configuration register")
        self.I2C4SEL = BitField(self, 0x00000003, "I2C4SEL", "I2C4 clock source selection. These bits are set and cleared by software to select the I2C4 clock source.")
        self.QSPISEL = BitField(self, 0x00300000, "QSPISEL", "QUADSPI clock source selection. Set and reset by software.")

class SA_RCC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Reset and clock control")
        self.CR = SA_RCC_CR(self, 0x0)
        self.ICSCR = SA_RCC_ICSCR(self, 0x4)
        self.CFGR = SA_RCC_CFGR(self, 0x8)
        self.PLLCFGR = SA_RCC_PLLCFGR(self, 0xC)
        self.CIER = SA_RCC_CIER(self, 0x18)
        self.CIFR = SA_RCC_CIFR(self, 0x1C)
        self.CICR = SA_RCC_CICR(self, 0x20)
        self.AHB1RSTR = SA_RCC_AHB1RSTR(self, 0x28)
        self.AHB2RSTR = SA_RCC_AHB2RSTR(self, 0x2C)
        self.AHB3RSTR = SA_RCC_AHB3RSTR(self, 0x30)
        self.APB1RSTR1 = SA_RCC_APB1RSTR1(self, 0x38)
        self.APB1RSTR2 = SA_RCC_APB1RSTR2(self, 0x3C)
        self.APB2RSTR = SA_RCC_APB2RSTR(self, 0x40)
        self.AHB1ENR = SA_RCC_AHB1ENR(self, 0x48)
        self.AHB2ENR = SA_RCC_AHB2ENR(self, 0x4C)
        self.AHB3ENR = SA_RCC_AHB3ENR(self, 0x50)
        self.APB1ENR1 = SA_RCC_APB1ENR1(self, 0x58)
        self.APB1ENR2 = SA_RCC_APB1ENR2(self, 0x5C)
        self.APB2ENR = SA_RCC_APB2ENR(self, 0x60)
        self.AHB1SMENR = SA_RCC_AHB1SMENR(self, 0x68)
        self.AHB2SMENR = SA_RCC_AHB2SMENR(self, 0x6C)
        self.AHB3SMENR = SA_RCC_AHB3SMENR(self, 0x70)
        self.APB1SMENR1 = SA_RCC_APB1SMENR1(self, 0x78)
        self.APB1SMENR2 = SA_RCC_APB1SMENR2(self, 0x7C)
        self.APB2SMENR = SA_RCC_APB2SMENR(self, 0x80)
        self.CCIPR = SA_RCC_CCIPR(self, 0x88)
        self.BDCR = SA_RCC_BDCR(self, 0x90)
        self.CSR = SA_RCC_CSR(self, 0x94)
        self.CRRCR = SA_RCC_CRRCR(self, 0x98)
        self.CCIPR2 = SA_RCC_CCIPR2(self, 0x9C)
        self.APB1SMENR = Subscriptor(self, "APB1SMENR{}")
        self.APB1ENR = Subscriptor(self, "APB1ENR{}")
        self.APB1RSTR = Subscriptor(self, "APB1RSTR{}")
        self.AHBRSTR = Subscriptor(self, "AHB{}RSTR")
        self.AHBENR = Subscriptor(self, "AHB{}ENR")
        self.AHBSMENR = Subscriptor(self, "AHB{}SMENR")

RCC = SA_RCC(0x40021000, "RCC")

class SA_PWR_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x200, "CR1", "Power control register 1")
        self.LPMS = BitField(self, 0x00000007, "LPMS", "Low-power mode selection. These bits select the low-power mode entered when CPU enters the deepsleep mode. 1xx: Shutdown mode Note: In Standby mode, SRAM2 can be preserved or not, depending on RRS bit configuration in PWR_CR3.")
        self.FPD_STOP = BitField(self, 0x00000008, "FPD_STOP", "FPD_STOP")
        self.DBP = BitField(self, 0x00000100, "DBP", "Disable backup domain write protection. In reset state, the RTC and backup registers are protected against parasitic write access. This bit must be set to enable write access to these registers.")
        self.VOS = BitField(self, 0x00000600, "VOS", "Voltage scaling range selection")
        self.LPR = BitField(self, 0x00004000, "LPR", "Low-power run. When this bit is set, the regulator is switched from main mode (MR) to low-power mode (LPR).")

class SA_PWR_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "Power control register 2")
        self.PVDE = BitField(self, 0x00000001, "PVDE", "Programmable voltage detector enable. Note: This bit is write-protected when the PVDL bit is set in the SYSCFG_CFGR2 register. The protection can be reset only by a system reset.")
        self.PVDLS = BitField(self, 0x0000000E, "PVDLS", "Programmable voltage detector level selection.. These bits select the PVD falling threshold: Note: These bits are write-protected when the PVDL bit is set in the SYSCFG_CFGR2 register. The protection can be reset only by a system reset.")
        self.PVMEN1 = BitField(self, 0x00000040, "PVMEN1", "Peripheral voltage monitoring 3 enable: V<sub>DDA</sub> vs. ADC/COMP min voltage 1.62V")
        self.PVMEN2 = BitField(self, 0x00000080, "PVMEN2", "Peripheral voltage monitoring 4 enable: V<sub>DDA</sub> vs. DAC 1MSPS /DAC 15MSPS min voltage.")
        self.PVMEN = Subscriptor(self, "PVMEN{}")

class SA_PWR_CR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x8000, "CR3", "Power control register 3")
        self.EWUP1 = BitField(self, 0x00000001, "EWUP1", "Enable Wakeup pin WKUP1. When this bit is set, the external wakeup pin WKUP1 is enabled and triggers a wakeup from Standby or Shutdown event when a rising or a falling edge occurs. The active edge is configured via the WP1 bit in the PWR_CR4 register.")
        self.EWUP2 = BitField(self, 0x00000002, "EWUP2", "Enable Wakeup pin WKUP2. When this bit is set, the external wakeup pin WKUP2 is enabled and triggers a wakeup from Standby or Shutdown event when a rising or a falling edge occurs. The active edge is configured via the WP2 bit in the PWR_CR4 register.")
        self.EWUP3 = BitField(self, 0x00000004, "EWUP3", "Enable Wakeup pin WKUP3. When this bit is set, the external wakeup pin WKUP3 is enabled and triggers a wakeup from Standby or Shutdown event when a rising or a falling edge occurs. The active edge is configured via the WP3 bit in the PWR_CR4 register.")
        self.EWUP4 = BitField(self, 0x00000008, "EWUP4", "Enable Wakeup pin WKUP4. When this bit is set, the external wakeup pin WKUP4 is enabled and triggers a wakeup from Standby or Shutdown event when a rising or a falling edge occurs. The active edge is configured via the WP4 bit in the PWR_CR4 register.")
        self.EWUP5 = BitField(self, 0x00000010, "EWUP5", "Enable Wakeup pin WKUP5. When this bit is set, the external wakeup pin WKUP5 is enabled and triggers a wakeup from Standby or Shutdown event when a rising or a falling edge occurs.The active edge is configured via the WP5 bit in the PWR_CR4 register.")
        self.RRS = BitField(self, 0x00000100, "RRS", "SRAM2 retention in Standby mode")
        self.APC = BitField(self, 0x00000400, "APC", "Apply pull-up and pull-down configuration. When this bit is set, the I/O pull-up and pull-down configurations defined in the PWR_PUCRx and PWR_PDCRx registers are applied. When this bit is cleared, the PWR_PUCRx and PWR_PDCRx registers are not applied to the I/Os.")
        self.UCPD1_STDBY = BitField(self, 0x00002000, "UCPD1_STDBY", "UCPD1_STDBY USB Type-C and Power Delivery standby mode.")
        self.UCPD1_DBDIS = BitField(self, 0x00004000, "UCPD1_DBDIS", "USB Type-C and Power Delivery Dead Battery disable.. After exiting reset, the USB Type-C dead battery behavior is enabled, which may have a pull-down effect on CC1 and CC2 pins. It is recommended to disable it in all cases, either to stop this pull-down or to hand over control to the UCPD1 (which should therefore be initialized before doing the disable).")
        self.EIWUL = BitField(self, 0x00008000, "EIWUL", "Enable internal wakeup line")
        self.EWUP = Subscriptor(self, "EWUP{}")

class SA_PWR_CR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR4", "Power control register 4")
        self.WP1 = BitField(self, 0x00000001, "WP1", "Wakeup pin WKUP1 polarity. This bit defines the polarity used for an event detection on external wake-up pin, WKUP1")
        self.WP2 = BitField(self, 0x00000002, "WP2", "Wakeup pin WKUP2 polarity. This bit defines the polarity used for an event detection on external wake-up pin, WKUP2")
        self.WP3 = BitField(self, 0x00000004, "WP3", "Wakeup pin WKUP3 polarity. This bit defines the polarity used for an event detection on external wake-up pin, WKUP3")
        self.WP4 = BitField(self, 0x00000008, "WP4", "Wakeup pin WKUP4 polarity. This bit defines the polarity used for an event detection on external wake-up pin, WKUP4")
        self.WP5 = BitField(self, 0x00000010, "WP5", "Wakeup pin WKUP5 polarity. This bit defines the polarity used for an event detection on external wake-up pin, WKUP5")
        self.VBE = BitField(self, 0x00000100, "VBE", "V<sub>BAT</sub> battery charging enable")
        self.VBRS = BitField(self, 0x00000200, "VBRS", "V<sub>BAT</sub> battery charging resistor selection")
        self.WP = Subscriptor(self, "WP{}")

class SA_PWR_SR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR1", "Power status register 1")
        self.WUF1 = BitField(self, 0x00000001, "WUF1", "Wakeup flag 1. This bit is set when a wakeup event is detected on wakeup pin, WKUP1. It is cleared by writing 1 in the CWUF1 bit of the PWR_SCR register.")
        self.WUF2 = BitField(self, 0x00000002, "WUF2", "Wakeup flag 2. This bit is set when a wakeup event is detected on wakeup pin, WKUP2. It is cleared by writing 1 in the CWUF2 bit of the PWR_SCR register.")
        self.WUF3 = BitField(self, 0x00000004, "WUF3", "Wakeup flag 3. This bit is set when a wakeup event is detected on wakeup pin, WKUP3. It is cleared by writing 1 in the CWUF3 bit of the PWR_SCR register.")
        self.WUF4 = BitField(self, 0x00000008, "WUF4", "Wakeup flag 4. This bit is set when a wakeup event is detected on wakeup pin,WKUP4. It is cleared by writing 1 in the CWUF4 bit of the PWR_SCR register.")
        self.WUF5 = BitField(self, 0x00000010, "WUF5", "Wakeup flag 5. This bit is set when a wakeup event is detected on wakeup pin, WKUP5. It is cleared by writing 1 in the CWUF5 bit of the PWR_SCR register.")
        self.SBF = BitField(self, 0x00000100, "SBF", "Standby flag. This bit is set by hardware when the device enters the Standby mode and is cleared by setting the CSBF bit in the PWR_SCR register, or by a power-on reset. It is not cleared by the system reset.")
        self.WUFI = BitField(self, 0x00008000, "WUFI", "Wakeup flag internal. This bit is set when a wakeup is detected on the internal wakeup line. It is cleared when all internal wakeup sources are cleared.")
        self.WUF = Subscriptor(self, "WUF{}")

class SA_PWR_SR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR2", "Power status register 2")
        self.REGLPS = BitField(self, 0x00000100, "REGLPS", "Low-power regulator started. This bit provides the information whether the low-power regulator is ready after a power-on reset or a Standby/Shutdown. If the Standby mode is entered while REGLPS bit is still cleared, the wakeup from Standby mode time may be increased.")
        self.REGLPF = BitField(self, 0x00000200, "REGLPF", "Low-power regulator flag. This bit is set by hardware when the MCU is in Low-power run mode. When the MCU exits the Low-power run mode, this bit remains at 1 until the regulator is ready in main mode. A polling on this bit must be done before increasing the product frequency. This bit is cleared by hardware when the regulator is ready.")
        self.VOSF = BitField(self, 0x00000400, "VOSF", "Voltage scaling flag. A delay is required for the internal regulator to be ready after the voltage scaling has been changed. VOSF indicates that the regulator reached the voltage level defined with VOS bits of the PWR_CR1 register.")
        self.PVDO = BitField(self, 0x00000800, "PVDO", "Programmable voltage detector output")
        self.PVMO1 = BitField(self, 0x00004000, "PVMO1", "Peripheral voltage monitoring output: V<sub>DDA</sub> vs. 1.62 V. Note: PVMO1 is cleared when PVM1 is disabled (PVME = 0). After enabling PVM1, the PVM1 output is valid after the PVM1 wakeup time.")
        self.PVMO2 = BitField(self, 0x00008000, "PVMO2", "Peripheral voltage monitoring output: V<sub>DDA</sub> vs. 1.8 V. Note: PVMO2 is cleared when PVM2 is disabled (PVME = 0). After enabling PVM2, the PVM2 output is valid after the PVM2 wakeup time.")
        self.PVMO = Subscriptor(self, "PVMO{}")

class SA_PWR_SCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SCR", "Power status clear register")
        self.CWUF1 = BitField(self, 0x00000001, "CWUF1", "Clear wakeup flag 1. Setting this bit clears the WUF1 flag in the PWR_SR1 register.")
        self.CWUF2 = BitField(self, 0x00000002, "CWUF2", "Clear wakeup flag 2. Setting this bit clears the WUF2 flag in the PWR_SR1 register.")
        self.CWUF3 = BitField(self, 0x00000004, "CWUF3", "Clear wakeup flag 3. Setting this bit clears the WUF3 flag in the PWR_SR1 register.")
        self.CWUF4 = BitField(self, 0x00000008, "CWUF4", "Clear wakeup flag 4. Setting this bit clears the WUF4 flag in the PWR_SR1 register.")
        self.CWUF5 = BitField(self, 0x00000010, "CWUF5", "Clear wakeup flag 5. Setting this bit clears the WUF5 flag in the PWR_SR1 register.")
        self.CSBF = BitField(self, 0x00000100, "CSBF", "Clear standby flag. Setting this bit clears the SBF flag in the PWR_SR1 register.")
        self.CWUF = Subscriptor(self, "CWUF{}")

class SA_PWR_PUCRA(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUCRA", "Power Port A pull-up control register")
        self.PU0 = BitField(self, 0x00000001, "PU0", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU1 = BitField(self, 0x00000002, "PU1", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU2 = BitField(self, 0x00000004, "PU2", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU3 = BitField(self, 0x00000008, "PU3", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU4 = BitField(self, 0x00000010, "PU4", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU5 = BitField(self, 0x00000020, "PU5", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU6 = BitField(self, 0x00000040, "PU6", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU7 = BitField(self, 0x00000080, "PU7", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU8 = BitField(self, 0x00000100, "PU8", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU9 = BitField(self, 0x00000200, "PU9", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU10 = BitField(self, 0x00000400, "PU10", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU11 = BitField(self, 0x00000800, "PU11", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU12 = BitField(self, 0x00001000, "PU12", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU13 = BitField(self, 0x00002000, "PU13", "Port A pull-up bit y (y=0..13). When set, this bit activates the pull-up on PA[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU15 = BitField(self, 0x00008000, "PU15", "Port A pull-up bit 15. When set, this bit activates the pull-up on PA[15] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PD15 bit is also set.")
        self.PU = Subscriptor(self, "PU{}")

class SA_PWR_PDCRA(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDCRA", "Power Port A pull-down control register")
        self.PD0 = BitField(self, 0x00000001, "PD0", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD1 = BitField(self, 0x00000002, "PD1", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD2 = BitField(self, 0x00000004, "PD2", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD3 = BitField(self, 0x00000008, "PD3", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD4 = BitField(self, 0x00000010, "PD4", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD5 = BitField(self, 0x00000020, "PD5", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD6 = BitField(self, 0x00000040, "PD6", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD7 = BitField(self, 0x00000080, "PD7", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD8 = BitField(self, 0x00000100, "PD8", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD9 = BitField(self, 0x00000200, "PD9", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD10 = BitField(self, 0x00000400, "PD10", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD11 = BitField(self, 0x00000800, "PD11", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD12 = BitField(self, 0x00001000, "PD12", "Port A pull-down bit y (y=0..12). When set, this bit activates the pull-down on PA[y] when APC bit is set in PWR_CR3 register.")
        self.PD14 = BitField(self, 0x00004000, "PD14", "Port A pull-down bit 14. When set, this bit activates the pull-down on PA[14] when APC bit is set in PWR_CR3 register.")
        self.PD = Subscriptor(self, "PD{}")

class SA_PWR_PUCRB(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUCRB", "Power Port B pull-up control register")
        self.PU0 = BitField(self, 0x00000001, "PU0", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU1 = BitField(self, 0x00000002, "PU1", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU2 = BitField(self, 0x00000004, "PU2", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU3 = BitField(self, 0x00000008, "PU3", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU4 = BitField(self, 0x00000010, "PU4", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU5 = BitField(self, 0x00000020, "PU5", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU6 = BitField(self, 0x00000040, "PU6", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU7 = BitField(self, 0x00000080, "PU7", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU8 = BitField(self, 0x00000100, "PU8", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU9 = BitField(self, 0x00000200, "PU9", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU10 = BitField(self, 0x00000400, "PU10", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU11 = BitField(self, 0x00000800, "PU11", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU12 = BitField(self, 0x00001000, "PU12", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU13 = BitField(self, 0x00002000, "PU13", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU14 = BitField(self, 0x00004000, "PU14", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU15 = BitField(self, 0x00008000, "PU15", "Port B pull-up bit y (y=0..15). When set, this bit activates the pull-up on PB[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU = Subscriptor(self, "PU{}")

class SA_PWR_PDCRB(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDCRB", "Power Port B pull-down control register")
        self.PD0 = BitField(self, 0x00000001, "PD0", "Port B pull-down bit y (y=0..3). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD1 = BitField(self, 0x00000002, "PD1", "Port B pull-down bit y (y=0..3). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD2 = BitField(self, 0x00000004, "PD2", "Port B pull-down bit y (y=0..3). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD3 = BitField(self, 0x00000008, "PD3", "Port B pull-down bit y (y=0..3). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD5 = BitField(self, 0x00000020, "PD5", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD6 = BitField(self, 0x00000040, "PD6", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD7 = BitField(self, 0x00000080, "PD7", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD8 = BitField(self, 0x00000100, "PD8", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD9 = BitField(self, 0x00000200, "PD9", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD10 = BitField(self, 0x00000400, "PD10", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD11 = BitField(self, 0x00000800, "PD11", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD12 = BitField(self, 0x00001000, "PD12", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD13 = BitField(self, 0x00002000, "PD13", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD14 = BitField(self, 0x00004000, "PD14", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD15 = BitField(self, 0x00008000, "PD15", "Port B pull-down bit y (y=5..15). When set, this bit activates the pull-down on PB[y] when APC bit is set in PWR_CR3 register.")
        self.PD = Subscriptor(self, "PD{}")

class SA_PWR_PUCRC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUCRC", "Power Port C pull-up control register")
        self.PU0 = BitField(self, 0x00000001, "PU0", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU1 = BitField(self, 0x00000002, "PU1", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU2 = BitField(self, 0x00000004, "PU2", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU3 = BitField(self, 0x00000008, "PU3", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU4 = BitField(self, 0x00000010, "PU4", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU5 = BitField(self, 0x00000020, "PU5", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU6 = BitField(self, 0x00000040, "PU6", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU7 = BitField(self, 0x00000080, "PU7", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU8 = BitField(self, 0x00000100, "PU8", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU9 = BitField(self, 0x00000200, "PU9", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU10 = BitField(self, 0x00000400, "PU10", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU11 = BitField(self, 0x00000800, "PU11", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU12 = BitField(self, 0x00001000, "PU12", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU13 = BitField(self, 0x00002000, "PU13", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU14 = BitField(self, 0x00004000, "PU14", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU15 = BitField(self, 0x00008000, "PU15", "Port C pull-up bit y (y=0..15). When set, this bit activates the pull-up on PC[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU = Subscriptor(self, "PU{}")

class SA_PWR_PDCRC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDCRC", "Power Port C pull-down control register")
        self.PD0 = BitField(self, 0x00000001, "PD0", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD1 = BitField(self, 0x00000002, "PD1", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD2 = BitField(self, 0x00000004, "PD2", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD3 = BitField(self, 0x00000008, "PD3", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD4 = BitField(self, 0x00000010, "PD4", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD5 = BitField(self, 0x00000020, "PD5", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD6 = BitField(self, 0x00000040, "PD6", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD7 = BitField(self, 0x00000080, "PD7", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD8 = BitField(self, 0x00000100, "PD8", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD9 = BitField(self, 0x00000200, "PD9", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD10 = BitField(self, 0x00000400, "PD10", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD11 = BitField(self, 0x00000800, "PD11", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD12 = BitField(self, 0x00001000, "PD12", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD13 = BitField(self, 0x00002000, "PD13", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD14 = BitField(self, 0x00004000, "PD14", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD15 = BitField(self, 0x00008000, "PD15", "Port C pull-down bit y (y=0..15). When set, this bit activates the pull-down on PC[y] when APC bit is set in PWR_CR3 register.")
        self.PD = Subscriptor(self, "PD{}")

class SA_PWR_PUCRD(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUCRD", "Power Port D pull-up control register")
        self.PU0 = BitField(self, 0x00000001, "PU0", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU1 = BitField(self, 0x00000002, "PU1", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU2 = BitField(self, 0x00000004, "PU2", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU3 = BitField(self, 0x00000008, "PU3", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU4 = BitField(self, 0x00000010, "PU4", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU5 = BitField(self, 0x00000020, "PU5", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU6 = BitField(self, 0x00000040, "PU6", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU7 = BitField(self, 0x00000080, "PU7", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU8 = BitField(self, 0x00000100, "PU8", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU9 = BitField(self, 0x00000200, "PU9", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU10 = BitField(self, 0x00000400, "PU10", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU11 = BitField(self, 0x00000800, "PU11", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU12 = BitField(self, 0x00001000, "PU12", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU13 = BitField(self, 0x00002000, "PU13", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU14 = BitField(self, 0x00004000, "PU14", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU15 = BitField(self, 0x00008000, "PU15", "Port D pull-up bit y (y=0..15). When set, this bit activates the pull-up on PD[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU = Subscriptor(self, "PU{}")

class SA_PWR_PDCRD(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDCRD", "Power Port D pull-down control register")
        self.PD0 = BitField(self, 0x00000001, "PD0", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD1 = BitField(self, 0x00000002, "PD1", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD2 = BitField(self, 0x00000004, "PD2", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD3 = BitField(self, 0x00000008, "PD3", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD4 = BitField(self, 0x00000010, "PD4", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD5 = BitField(self, 0x00000020, "PD5", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD6 = BitField(self, 0x00000040, "PD6", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD7 = BitField(self, 0x00000080, "PD7", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD8 = BitField(self, 0x00000100, "PD8", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD9 = BitField(self, 0x00000200, "PD9", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD10 = BitField(self, 0x00000400, "PD10", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD11 = BitField(self, 0x00000800, "PD11", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD12 = BitField(self, 0x00001000, "PD12", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD13 = BitField(self, 0x00002000, "PD13", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD14 = BitField(self, 0x00004000, "PD14", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD15 = BitField(self, 0x00008000, "PD15", "Port D pull-down bit y (y=0..15). When set, this bit activates the pull-down on PD[y] when APC bit is set in PWR_CR3 register.")
        self.PD = Subscriptor(self, "PD{}")

class SA_PWR_PUCRE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUCRE", "Power Port E pull-up control register")
        self.PU0 = BitField(self, 0x00000001, "PU0", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU1 = BitField(self, 0x00000002, "PU1", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU2 = BitField(self, 0x00000004, "PU2", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU3 = BitField(self, 0x00000008, "PU3", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU4 = BitField(self, 0x00000010, "PU4", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU5 = BitField(self, 0x00000020, "PU5", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU6 = BitField(self, 0x00000040, "PU6", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU7 = BitField(self, 0x00000080, "PU7", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU8 = BitField(self, 0x00000100, "PU8", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU9 = BitField(self, 0x00000200, "PU9", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU10 = BitField(self, 0x00000400, "PU10", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU11 = BitField(self, 0x00000800, "PU11", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU12 = BitField(self, 0x00001000, "PU12", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU13 = BitField(self, 0x00002000, "PU13", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU14 = BitField(self, 0x00004000, "PU14", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU15 = BitField(self, 0x00008000, "PU15", "Port E pull-up bit y (y=0..15). When set, this bit activates the pull-up on PE[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU = Subscriptor(self, "PU{}")

class SA_PWR_PDCRE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDCRE", "Power Port E pull-down control register")
        self.PD0 = BitField(self, 0x00000001, "PD0", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD1 = BitField(self, 0x00000002, "PD1", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD2 = BitField(self, 0x00000004, "PD2", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD3 = BitField(self, 0x00000008, "PD3", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD4 = BitField(self, 0x00000010, "PD4", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD5 = BitField(self, 0x00000020, "PD5", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD6 = BitField(self, 0x00000040, "PD6", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD7 = BitField(self, 0x00000080, "PD7", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD8 = BitField(self, 0x00000100, "PD8", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD9 = BitField(self, 0x00000200, "PD9", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD10 = BitField(self, 0x00000400, "PD10", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD11 = BitField(self, 0x00000800, "PD11", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD12 = BitField(self, 0x00001000, "PD12", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD13 = BitField(self, 0x00002000, "PD13", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD14 = BitField(self, 0x00004000, "PD14", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD15 = BitField(self, 0x00008000, "PD15", "Port E pull-down bit y (y=0..15). When set, this bit activates the pull-down on PE[y] when APC bit is set in PWR_CR3 register.")
        self.PD = Subscriptor(self, "PD{}")

class SA_PWR_PUCRF(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUCRF", "Power Port F pull-up control register")
        self.PU0 = BitField(self, 0x00000001, "PU0", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU1 = BitField(self, 0x00000002, "PU1", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU2 = BitField(self, 0x00000004, "PU2", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU3 = BitField(self, 0x00000008, "PU3", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU4 = BitField(self, 0x00000010, "PU4", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU5 = BitField(self, 0x00000020, "PU5", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU6 = BitField(self, 0x00000040, "PU6", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU7 = BitField(self, 0x00000080, "PU7", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU8 = BitField(self, 0x00000100, "PU8", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU9 = BitField(self, 0x00000200, "PU9", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU10 = BitField(self, 0x00000400, "PU10", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU11 = BitField(self, 0x00000800, "PU11", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU12 = BitField(self, 0x00001000, "PU12", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU13 = BitField(self, 0x00002000, "PU13", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU14 = BitField(self, 0x00004000, "PU14", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU15 = BitField(self, 0x00008000, "PU15", "Port F pull-up bit y (y=0..15). When set, this bit activates the pull-up on PF[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU = Subscriptor(self, "PU{}")

class SA_PWR_PDCRF(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDCRF", "Power Port F pull-down control register")
        self.PD0 = BitField(self, 0x00000001, "PD0", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD1 = BitField(self, 0x00000002, "PD1", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD2 = BitField(self, 0x00000004, "PD2", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD3 = BitField(self, 0x00000008, "PD3", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD4 = BitField(self, 0x00000010, "PD4", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD5 = BitField(self, 0x00000020, "PD5", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD6 = BitField(self, 0x00000040, "PD6", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD7 = BitField(self, 0x00000080, "PD7", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD8 = BitField(self, 0x00000100, "PD8", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD9 = BitField(self, 0x00000200, "PD9", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD10 = BitField(self, 0x00000400, "PD10", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD11 = BitField(self, 0x00000800, "PD11", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD12 = BitField(self, 0x00001000, "PD12", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD13 = BitField(self, 0x00002000, "PD13", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD14 = BitField(self, 0x00004000, "PD14", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD15 = BitField(self, 0x00008000, "PD15", "Port F pull-down bit y (y=0..15). When set, this bit activates the pull-down on PF[y] when APC bit is set in PWR_CR3 register.")
        self.PD = Subscriptor(self, "PD{}")

class SA_PWR_PUCRG(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUCRG", "Power Port G pull-up control register")
        self.PU0 = BitField(self, 0x00000001, "PU0", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU1 = BitField(self, 0x00000002, "PU1", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU2 = BitField(self, 0x00000004, "PU2", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU3 = BitField(self, 0x00000008, "PU3", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU4 = BitField(self, 0x00000010, "PU4", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU5 = BitField(self, 0x00000020, "PU5", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU6 = BitField(self, 0x00000040, "PU6", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU7 = BitField(self, 0x00000080, "PU7", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU8 = BitField(self, 0x00000100, "PU8", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU9 = BitField(self, 0x00000200, "PU9", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU10 = BitField(self, 0x00000400, "PU10", "Port G pull-up bit y (y=0..10). When set, this bit activates the pull-up on PG[y] when APC bit is set in PWR_CR3 register. The pull-up is not activated if the corresponding PDy bit is also set.")
        self.PU = Subscriptor(self, "PU{}")

class SA_PWR_PDCRG(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDCRG", "Power Port G pull-down control register")
        self.PD0 = BitField(self, 0x00000001, "PD0", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD1 = BitField(self, 0x00000002, "PD1", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD2 = BitField(self, 0x00000004, "PD2", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD3 = BitField(self, 0x00000008, "PD3", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD4 = BitField(self, 0x00000010, "PD4", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD5 = BitField(self, 0x00000020, "PD5", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD6 = BitField(self, 0x00000040, "PD6", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD7 = BitField(self, 0x00000080, "PD7", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD8 = BitField(self, 0x00000100, "PD8", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD9 = BitField(self, 0x00000200, "PD9", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD10 = BitField(self, 0x00000400, "PD10", "Port G pull-down bit y (y=0..10). When set, this bit activates the pull-down on PG[y] when APC bit is set in PWR_CR3 register.")
        self.PD = Subscriptor(self, "PD{}")

class SA_PWR_CR5(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x100, "CR5", "Power control register")
        self.R1MODE = BitField(self, 0x00000100, "R1MODE", "Main regular range 1 mode. This bit is only valid for the main regulator in range 1 and has no effect on range 2. It is recommended to reset this bit when the system frequency is greater than 150 MHz. Refer to")

class SA_PWR(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Power control")
        self.CR1 = SA_PWR_CR1(self, 0x0)
        self.CR2 = SA_PWR_CR2(self, 0x4)
        self.CR3 = SA_PWR_CR3(self, 0x8)
        self.CR4 = SA_PWR_CR4(self, 0xC)
        self.SR1 = SA_PWR_SR1(self, 0x10)
        self.SR2 = SA_PWR_SR2(self, 0x14)
        self.SCR = SA_PWR_SCR(self, 0x18)
        self.PUCRA = SA_PWR_PUCRA(self, 0x20)
        self.PDCRA = SA_PWR_PDCRA(self, 0x24)
        self.PUCRB = SA_PWR_PUCRB(self, 0x28)
        self.PDCRB = SA_PWR_PDCRB(self, 0x2C)
        self.PUCRC = SA_PWR_PUCRC(self, 0x30)
        self.PDCRC = SA_PWR_PDCRC(self, 0x34)
        self.PUCRD = SA_PWR_PUCRD(self, 0x38)
        self.PDCRD = SA_PWR_PDCRD(self, 0x3C)
        self.PUCRE = SA_PWR_PUCRE(self, 0x40)
        self.PDCRE = SA_PWR_PDCRE(self, 0x44)
        self.PUCRF = SA_PWR_PUCRF(self, 0x48)
        self.PDCRF = SA_PWR_PDCRF(self, 0x4C)
        self.PUCRG = SA_PWR_PUCRG(self, 0x50)
        self.PDCRG = SA_PWR_PDCRG(self, 0x54)
        self.CR5 = SA_PWR_CR5(self, 0x80)
        self.SR = Subscriptor(self, "SR{}")

PWR = SA_PWR(0x40007000, "PWR")

class SA_RNG_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "control register")
        self.CED = BitField(self, 0x00000020, "CED", "Clock error detection")
        self.IE = BitField(self, 0x00000008, "IE", "Interrupt enable")
        self.RNGEN = BitField(self, 0x00000004, "RNGEN", "Random number generator enable")

class SA_RNG_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.SEIS = BitField(self, 0x00000040, "SEIS", "Seed error interrupt status")
        self.CEIS = BitField(self, 0x00000020, "CEIS", "Clock error interrupt status")
        self.SECS = BitField(self, 0x00000004, "SECS", "Seed error current status")
        self.CECS = BitField(self, 0x00000002, "CECS", "Clock error current status")
        self.DRDY = BitField(self, 0x00000001, "DRDY", "Data ready")

class SA_RNG_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DR", "data register")
        self.RNDATA = BitField(self, 0xFFFFFFFF, "RNDATA", "Random data")

class SA_RNG(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Random number generator")
        self.CR = SA_RNG_CR(self, 0x0)
        self.SR = SA_RNG_SR(self, 0x4)
        self.DR = SA_RNG_DR(self, 0x8)

RNG = SA_RNG(0x50060800, "RNG")

class SA_GPIOA_MODER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xABFFFFFF, "MODER", "GPIO port mode register")
        self.MODER15 = BitField(self, 0xC0000000, "MODER15", "Port x configuration bits (y = 0..15)")
        self.MODER14 = BitField(self, 0x30000000, "MODER14", "Port x configuration bits (y = 0..15)")
        self.MODER13 = BitField(self, 0x0C000000, "MODER13", "Port x configuration bits (y = 0..15)")
        self.MODER12 = BitField(self, 0x03000000, "MODER12", "Port x configuration bits (y = 0..15)")
        self.MODER11 = BitField(self, 0x00C00000, "MODER11", "Port x configuration bits (y = 0..15)")
        self.MODER10 = BitField(self, 0x00300000, "MODER10", "Port x configuration bits (y = 0..15)")
        self.MODER9 = BitField(self, 0x000C0000, "MODER9", "Port x configuration bits (y = 0..15)")
        self.MODER8 = BitField(self, 0x00030000, "MODER8", "Port x configuration bits (y = 0..15)")
        self.MODER7 = BitField(self, 0x0000C000, "MODER7", "Port x configuration bits (y = 0..15)")
        self.MODER6 = BitField(self, 0x00003000, "MODER6", "Port x configuration bits (y = 0..15)")
        self.MODER5 = BitField(self, 0x00000C00, "MODER5", "Port x configuration bits (y = 0..15)")
        self.MODER4 = BitField(self, 0x00000300, "MODER4", "Port x configuration bits (y = 0..15)")
        self.MODER3 = BitField(self, 0x000000C0, "MODER3", "Port x configuration bits (y = 0..15)")
        self.MODER2 = BitField(self, 0x00000030, "MODER2", "Port x configuration bits (y = 0..15)")
        self.MODER1 = BitField(self, 0x0000000C, "MODER1", "Port x configuration bits (y = 0..15)")
        self.MODER0 = BitField(self, 0x00000003, "MODER0", "Port x configuration bits (y = 0..15)")
        self.MODER = Subscriptor(self, "MODER{}")

class SA_GPIOA_OTYPER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OTYPER", "GPIO port output type register")
        self.OT15 = BitField(self, 0x00008000, "OT15", "Port x configuration bits (y = 0..15)")
        self.OT14 = BitField(self, 0x00004000, "OT14", "Port x configuration bits (y = 0..15)")
        self.OT13 = BitField(self, 0x00002000, "OT13", "Port x configuration bits (y = 0..15)")
        self.OT12 = BitField(self, 0x00001000, "OT12", "Port x configuration bits (y = 0..15)")
        self.OT11 = BitField(self, 0x00000800, "OT11", "Port x configuration bits (y = 0..15)")
        self.OT10 = BitField(self, 0x00000400, "OT10", "Port x configuration bits (y = 0..15)")
        self.OT9 = BitField(self, 0x00000200, "OT9", "Port x configuration bits (y = 0..15)")
        self.OT8 = BitField(self, 0x00000100, "OT8", "Port x configuration bits (y = 0..15)")
        self.OT7 = BitField(self, 0x00000080, "OT7", "Port x configuration bits (y = 0..15)")
        self.OT6 = BitField(self, 0x00000040, "OT6", "Port x configuration bits (y = 0..15)")
        self.OT5 = BitField(self, 0x00000020, "OT5", "Port x configuration bits (y = 0..15)")
        self.OT4 = BitField(self, 0x00000010, "OT4", "Port x configuration bits (y = 0..15)")
        self.OT3 = BitField(self, 0x00000008, "OT3", "Port x configuration bits (y = 0..15)")
        self.OT2 = BitField(self, 0x00000004, "OT2", "Port x configuration bits (y = 0..15)")
        self.OT1 = BitField(self, 0x00000002, "OT1", "Port x configuration bits (y = 0..15)")
        self.OT0 = BitField(self, 0x00000001, "OT0", "Port x configuration bits (y = 0..15)")
        self.OT = Subscriptor(self, "OT{}")

class SA_GPIOA_OSPEEDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xC000000, "OSPEEDR", "GPIO port output speed register")
        self.OSPEEDR15 = BitField(self, 0xC0000000, "OSPEEDR15", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR14 = BitField(self, 0x30000000, "OSPEEDR14", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR13 = BitField(self, 0x0C000000, "OSPEEDR13", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR12 = BitField(self, 0x03000000, "OSPEEDR12", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR11 = BitField(self, 0x00C00000, "OSPEEDR11", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR10 = BitField(self, 0x00300000, "OSPEEDR10", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR9 = BitField(self, 0x000C0000, "OSPEEDR9", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR8 = BitField(self, 0x00030000, "OSPEEDR8", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR7 = BitField(self, 0x0000C000, "OSPEEDR7", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR6 = BitField(self, 0x00003000, "OSPEEDR6", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR5 = BitField(self, 0x00000C00, "OSPEEDR5", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR4 = BitField(self, 0x00000300, "OSPEEDR4", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR3 = BitField(self, 0x000000C0, "OSPEEDR3", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR2 = BitField(self, 0x00000030, "OSPEEDR2", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR1 = BitField(self, 0x0000000C, "OSPEEDR1", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR0 = BitField(self, 0x00000003, "OSPEEDR0", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR = Subscriptor(self, "OSPEEDR{}")

class SA_GPIOA_PUPDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x64000000, "PUPDR", "GPIO port pull-up/pull-down register")
        self.PUPDR15 = BitField(self, 0xC0000000, "PUPDR15", "Port x configuration bits (y = 0..15)")
        self.PUPDR14 = BitField(self, 0x30000000, "PUPDR14", "Port x configuration bits (y = 0..15)")
        self.PUPDR13 = BitField(self, 0x0C000000, "PUPDR13", "Port x configuration bits (y = 0..15)")
        self.PUPDR12 = BitField(self, 0x03000000, "PUPDR12", "Port x configuration bits (y = 0..15)")
        self.PUPDR11 = BitField(self, 0x00C00000, "PUPDR11", "Port x configuration bits (y = 0..15)")
        self.PUPDR10 = BitField(self, 0x00300000, "PUPDR10", "Port x configuration bits (y = 0..15)")
        self.PUPDR9 = BitField(self, 0x000C0000, "PUPDR9", "Port x configuration bits (y = 0..15)")
        self.PUPDR8 = BitField(self, 0x00030000, "PUPDR8", "Port x configuration bits (y = 0..15)")
        self.PUPDR7 = BitField(self, 0x0000C000, "PUPDR7", "Port x configuration bits (y = 0..15)")
        self.PUPDR6 = BitField(self, 0x00003000, "PUPDR6", "Port x configuration bits (y = 0..15)")
        self.PUPDR5 = BitField(self, 0x00000C00, "PUPDR5", "Port x configuration bits (y = 0..15)")
        self.PUPDR4 = BitField(self, 0x00000300, "PUPDR4", "Port x configuration bits (y = 0..15)")
        self.PUPDR3 = BitField(self, 0x000000C0, "PUPDR3", "Port x configuration bits (y = 0..15)")
        self.PUPDR2 = BitField(self, 0x00000030, "PUPDR2", "Port x configuration bits (y = 0..15)")
        self.PUPDR1 = BitField(self, 0x0000000C, "PUPDR1", "Port x configuration bits (y = 0..15)")
        self.PUPDR0 = BitField(self, 0x00000003, "PUPDR0", "Port x configuration bits (y = 0..15)")
        self.PUPDR = Subscriptor(self, "PUPDR{}")

class SA_GPIOA_IDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IDR", "GPIO port input data register")
        self.IDR15 = BitField(self, 0x00008000, "IDR15", "Port input data (y = 0..15)")
        self.IDR14 = BitField(self, 0x00004000, "IDR14", "Port input data (y = 0..15)")
        self.IDR13 = BitField(self, 0x00002000, "IDR13", "Port input data (y = 0..15)")
        self.IDR12 = BitField(self, 0x00001000, "IDR12", "Port input data (y = 0..15)")
        self.IDR11 = BitField(self, 0x00000800, "IDR11", "Port input data (y = 0..15)")
        self.IDR10 = BitField(self, 0x00000400, "IDR10", "Port input data (y = 0..15)")
        self.IDR9 = BitField(self, 0x00000200, "IDR9", "Port input data (y = 0..15)")
        self.IDR8 = BitField(self, 0x00000100, "IDR8", "Port input data (y = 0..15)")
        self.IDR7 = BitField(self, 0x00000080, "IDR7", "Port input data (y = 0..15)")
        self.IDR6 = BitField(self, 0x00000040, "IDR6", "Port input data (y = 0..15)")
        self.IDR5 = BitField(self, 0x00000020, "IDR5", "Port input data (y = 0..15)")
        self.IDR4 = BitField(self, 0x00000010, "IDR4", "Port input data (y = 0..15)")
        self.IDR3 = BitField(self, 0x00000008, "IDR3", "Port input data (y = 0..15)")
        self.IDR2 = BitField(self, 0x00000004, "IDR2", "Port input data (y = 0..15)")
        self.IDR1 = BitField(self, 0x00000002, "IDR1", "Port input data (y = 0..15)")
        self.IDR0 = BitField(self, 0x00000001, "IDR0", "Port input data (y = 0..15)")
        self.IDR = Subscriptor(self, "IDR{}")

class SA_GPIOA_ODR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ODR", "GPIO port output data register")
        self.ODR15 = BitField(self, 0x00008000, "ODR15", "Port output data (y = 0..15)")
        self.ODR14 = BitField(self, 0x00004000, "ODR14", "Port output data (y = 0..15)")
        self.ODR13 = BitField(self, 0x00002000, "ODR13", "Port output data (y = 0..15)")
        self.ODR12 = BitField(self, 0x00001000, "ODR12", "Port output data (y = 0..15)")
        self.ODR11 = BitField(self, 0x00000800, "ODR11", "Port output data (y = 0..15)")
        self.ODR10 = BitField(self, 0x00000400, "ODR10", "Port output data (y = 0..15)")
        self.ODR9 = BitField(self, 0x00000200, "ODR9", "Port output data (y = 0..15)")
        self.ODR8 = BitField(self, 0x00000100, "ODR8", "Port output data (y = 0..15)")
        self.ODR7 = BitField(self, 0x00000080, "ODR7", "Port output data (y = 0..15)")
        self.ODR6 = BitField(self, 0x00000040, "ODR6", "Port output data (y = 0..15)")
        self.ODR5 = BitField(self, 0x00000020, "ODR5", "Port output data (y = 0..15)")
        self.ODR4 = BitField(self, 0x00000010, "ODR4", "Port output data (y = 0..15)")
        self.ODR3 = BitField(self, 0x00000008, "ODR3", "Port output data (y = 0..15)")
        self.ODR2 = BitField(self, 0x00000004, "ODR2", "Port output data (y = 0..15)")
        self.ODR1 = BitField(self, 0x00000002, "ODR1", "Port output data (y = 0..15)")
        self.ODR0 = BitField(self, 0x00000001, "ODR0", "Port output data (y = 0..15)")
        self.ODR = Subscriptor(self, "ODR{}")

class SA_GPIOA_BSRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BSRR", "GPIO port bit set/reset register")
        self.BR15 = BitField(self, 0x80000000, "BR15", "Port x reset bit y (y = 0..15)")
        self.BR14 = BitField(self, 0x40000000, "BR14", "Port x reset bit y (y = 0..15)")
        self.BR13 = BitField(self, 0x20000000, "BR13", "Port x reset bit y (y = 0..15)")
        self.BR12 = BitField(self, 0x10000000, "BR12", "Port x reset bit y (y = 0..15)")
        self.BR11 = BitField(self, 0x08000000, "BR11", "Port x reset bit y (y = 0..15)")
        self.BR10 = BitField(self, 0x04000000, "BR10", "Port x reset bit y (y = 0..15)")
        self.BR9 = BitField(self, 0x02000000, "BR9", "Port x reset bit y (y = 0..15)")
        self.BR8 = BitField(self, 0x01000000, "BR8", "Port x reset bit y (y = 0..15)")
        self.BR7 = BitField(self, 0x00800000, "BR7", "Port x reset bit y (y = 0..15)")
        self.BR6 = BitField(self, 0x00400000, "BR6", "Port x reset bit y (y = 0..15)")
        self.BR5 = BitField(self, 0x00200000, "BR5", "Port x reset bit y (y = 0..15)")
        self.BR4 = BitField(self, 0x00100000, "BR4", "Port x reset bit y (y = 0..15)")
        self.BR3 = BitField(self, 0x00080000, "BR3", "Port x reset bit y (y = 0..15)")
        self.BR2 = BitField(self, 0x00040000, "BR2", "Port x reset bit y (y = 0..15)")
        self.BR1 = BitField(self, 0x00020000, "BR1", "Port x reset bit y (y = 0..15)")
        self.BR0 = BitField(self, 0x00010000, "BR0", "Port x set bit y (y= 0..15)")
        self.BS15 = BitField(self, 0x00008000, "BS15", "Port x set bit y (y= 0..15)")
        self.BS14 = BitField(self, 0x00004000, "BS14", "Port x set bit y (y= 0..15)")
        self.BS13 = BitField(self, 0x00002000, "BS13", "Port x set bit y (y= 0..15)")
        self.BS12 = BitField(self, 0x00001000, "BS12", "Port x set bit y (y= 0..15)")
        self.BS11 = BitField(self, 0x00000800, "BS11", "Port x set bit y (y= 0..15)")
        self.BS10 = BitField(self, 0x00000400, "BS10", "Port x set bit y (y= 0..15)")
        self.BS9 = BitField(self, 0x00000200, "BS9", "Port x set bit y (y= 0..15)")
        self.BS8 = BitField(self, 0x00000100, "BS8", "Port x set bit y (y= 0..15)")
        self.BS7 = BitField(self, 0x00000080, "BS7", "Port x set bit y (y= 0..15)")
        self.BS6 = BitField(self, 0x00000040, "BS6", "Port x set bit y (y= 0..15)")
        self.BS5 = BitField(self, 0x00000020, "BS5", "Port x set bit y (y= 0..15)")
        self.BS4 = BitField(self, 0x00000010, "BS4", "Port x set bit y (y= 0..15)")
        self.BS3 = BitField(self, 0x00000008, "BS3", "Port x set bit y (y= 0..15)")
        self.BS2 = BitField(self, 0x00000004, "BS2", "Port x set bit y (y= 0..15)")
        self.BS1 = BitField(self, 0x00000002, "BS1", "Port x set bit y (y= 0..15)")
        self.BS0 = BitField(self, 0x00000001, "BS0", "Port x set bit y (y= 0..15)")
        self.BR = Subscriptor(self, "BR{}")
        self.BS = Subscriptor(self, "BS{}")

class SA_GPIOA_LCKR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "LCKR", "GPIO port configuration lock register")
        self.LCKK = BitField(self, 0x00010000, "LCKK", "Port x lock bit y (y= 0..15)")
        self.LCK15 = BitField(self, 0x00008000, "LCK15", "Port x lock bit y (y= 0..15)")
        self.LCK14 = BitField(self, 0x00004000, "LCK14", "Port x lock bit y (y= 0..15)")
        self.LCK13 = BitField(self, 0x00002000, "LCK13", "Port x lock bit y (y= 0..15)")
        self.LCK12 = BitField(self, 0x00001000, "LCK12", "Port x lock bit y (y= 0..15)")
        self.LCK11 = BitField(self, 0x00000800, "LCK11", "Port x lock bit y (y= 0..15)")
        self.LCK10 = BitField(self, 0x00000400, "LCK10", "Port x lock bit y (y= 0..15)")
        self.LCK9 = BitField(self, 0x00000200, "LCK9", "Port x lock bit y (y= 0..15)")
        self.LCK8 = BitField(self, 0x00000100, "LCK8", "Port x lock bit y (y= 0..15)")
        self.LCK7 = BitField(self, 0x00000080, "LCK7", "Port x lock bit y (y= 0..15)")
        self.LCK6 = BitField(self, 0x00000040, "LCK6", "Port x lock bit y (y= 0..15)")
        self.LCK5 = BitField(self, 0x00000020, "LCK5", "Port x lock bit y (y= 0..15)")
        self.LCK4 = BitField(self, 0x00000010, "LCK4", "Port x lock bit y (y= 0..15)")
        self.LCK3 = BitField(self, 0x00000008, "LCK3", "Port x lock bit y (y= 0..15)")
        self.LCK2 = BitField(self, 0x00000004, "LCK2", "Port x lock bit y (y= 0..15)")
        self.LCK1 = BitField(self, 0x00000002, "LCK1", "Port x lock bit y (y= 0..15)")
        self.LCK0 = BitField(self, 0x00000001, "LCK0", "Port x lock bit y (y= 0..15)")
        self.LCK = Subscriptor(self, "LCK{}")

class SA_GPIOA_AFRL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AFRL", "GPIO alternate function low register")
        self.AFRL7 = BitField(self, 0xF0000000, "AFRL7", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL6 = BitField(self, 0x0F000000, "AFRL6", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL5 = BitField(self, 0x00F00000, "AFRL5", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL4 = BitField(self, 0x000F0000, "AFRL4", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL3 = BitField(self, 0x0000F000, "AFRL3", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL2 = BitField(self, 0x00000F00, "AFRL2", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL1 = BitField(self, 0x000000F0, "AFRL1", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL0 = BitField(self, 0x0000000F, "AFRL0", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL = Subscriptor(self, "AFRL{}")

class SA_GPIOA_AFRH(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AFRH", "GPIO alternate function high register")
        self.AFRH15 = BitField(self, 0xF0000000, "AFRH15", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH14 = BitField(self, 0x0F000000, "AFRH14", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH13 = BitField(self, 0x00F00000, "AFRH13", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH12 = BitField(self, 0x000F0000, "AFRH12", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH11 = BitField(self, 0x0000F000, "AFRH11", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH10 = BitField(self, 0x00000F00, "AFRH10", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH9 = BitField(self, 0x000000F0, "AFRH9", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH8 = BitField(self, 0x0000000F, "AFRH8", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH = Subscriptor(self, "AFRH{}")

class SA_GPIOA_BRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BRR", "GPIO port bit reset register")
        self.BR0 = BitField(self, 0x00000001, "BR0", "Port Reset bit")
        self.BR1 = BitField(self, 0x00000002, "BR1", "Port Reset bit")
        self.BR2 = BitField(self, 0x00000004, "BR2", "Port Reset bit")
        self.BR3 = BitField(self, 0x00000008, "BR3", "Port Reset bit")
        self.BR4 = BitField(self, 0x00000010, "BR4", "Port Reset bit")
        self.BR5 = BitField(self, 0x00000020, "BR5", "Port Reset bit")
        self.BR6 = BitField(self, 0x00000040, "BR6", "Port Reset bit")
        self.BR7 = BitField(self, 0x00000080, "BR7", "Port Reset bit")
        self.BR8 = BitField(self, 0x00000100, "BR8", "Port Reset bit")
        self.BR9 = BitField(self, 0x00000200, "BR9", "Port Reset bit")
        self.BR10 = BitField(self, 0x00000400, "BR10", "Port Reset bit")
        self.BR11 = BitField(self, 0x00000800, "BR11", "Port Reset bit")
        self.BR12 = BitField(self, 0x00001000, "BR12", "Port Reset bit")
        self.BR13 = BitField(self, 0x00002000, "BR13", "Port Reset bit")
        self.BR14 = BitField(self, 0x00004000, "BR14", "Port Reset bit")
        self.BR15 = BitField(self, 0x00008000, "BR15", "Port Reset bit")
        self.BR = Subscriptor(self, "BR{}")

class SA_GPIOA(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "General-purpose I/Os")
        self.MODER = SA_GPIOA_MODER(self, 0x0)
        self.OTYPER = SA_GPIOA_OTYPER(self, 0x4)
        self.OSPEEDR = SA_GPIOA_OSPEEDR(self, 0x8)
        self.PUPDR = SA_GPIOA_PUPDR(self, 0xC)
        self.IDR = SA_GPIOA_IDR(self, 0x10)
        self.ODR = SA_GPIOA_ODR(self, 0x14)
        self.BSRR = SA_GPIOA_BSRR(self, 0x18)
        self.LCKR = SA_GPIOA_LCKR(self, 0x1C)
        self.AFRL = SA_GPIOA_AFRL(self, 0x20)
        self.AFRH = SA_GPIOA_AFRH(self, 0x24)
        self.BRR = SA_GPIOA_BRR(self, 0x28)

GPIOA = SA_GPIOA(0x48000000, "GPIOA")

class SA_GPIOB_MODER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFEBF, "MODER", "GPIO port mode register")
        self.MODER15 = BitField(self, 0xC0000000, "MODER15", "Port x configuration bits (y = 0..15)")
        self.MODER14 = BitField(self, 0x30000000, "MODER14", "Port x configuration bits (y = 0..15)")
        self.MODER13 = BitField(self, 0x0C000000, "MODER13", "Port x configuration bits (y = 0..15)")
        self.MODER12 = BitField(self, 0x03000000, "MODER12", "Port x configuration bits (y = 0..15)")
        self.MODER11 = BitField(self, 0x00C00000, "MODER11", "Port x configuration bits (y = 0..15)")
        self.MODER10 = BitField(self, 0x00300000, "MODER10", "Port x configuration bits (y = 0..15)")
        self.MODER9 = BitField(self, 0x000C0000, "MODER9", "Port x configuration bits (y = 0..15)")
        self.MODER8 = BitField(self, 0x00030000, "MODER8", "Port x configuration bits (y = 0..15)")
        self.MODER7 = BitField(self, 0x0000C000, "MODER7", "Port x configuration bits (y = 0..15)")
        self.MODER6 = BitField(self, 0x00003000, "MODER6", "Port x configuration bits (y = 0..15)")
        self.MODER5 = BitField(self, 0x00000C00, "MODER5", "Port x configuration bits (y = 0..15)")
        self.MODER4 = BitField(self, 0x00000300, "MODER4", "Port x configuration bits (y = 0..15)")
        self.MODER3 = BitField(self, 0x000000C0, "MODER3", "Port x configuration bits (y = 0..15)")
        self.MODER2 = BitField(self, 0x00000030, "MODER2", "Port x configuration bits (y = 0..15)")
        self.MODER1 = BitField(self, 0x0000000C, "MODER1", "Port x configuration bits (y = 0..15)")
        self.MODER0 = BitField(self, 0x00000003, "MODER0", "Port x configuration bits (y = 0..15)")
        self.MODER = Subscriptor(self, "MODER{}")

class SA_GPIOB_OTYPER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OTYPER", "GPIO port output type register")
        self.OT15 = BitField(self, 0x00008000, "OT15", "Port x configuration bits (y = 0..15)")
        self.OT14 = BitField(self, 0x00004000, "OT14", "Port x configuration bits (y = 0..15)")
        self.OT13 = BitField(self, 0x00002000, "OT13", "Port x configuration bits (y = 0..15)")
        self.OT12 = BitField(self, 0x00001000, "OT12", "Port x configuration bits (y = 0..15)")
        self.OT11 = BitField(self, 0x00000800, "OT11", "Port x configuration bits (y = 0..15)")
        self.OT10 = BitField(self, 0x00000400, "OT10", "Port x configuration bits (y = 0..15)")
        self.OT9 = BitField(self, 0x00000200, "OT9", "Port x configuration bits (y = 0..15)")
        self.OT8 = BitField(self, 0x00000100, "OT8", "Port x configuration bits (y = 0..15)")
        self.OT7 = BitField(self, 0x00000080, "OT7", "Port x configuration bits (y = 0..15)")
        self.OT6 = BitField(self, 0x00000040, "OT6", "Port x configuration bits (y = 0..15)")
        self.OT5 = BitField(self, 0x00000020, "OT5", "Port x configuration bits (y = 0..15)")
        self.OT4 = BitField(self, 0x00000010, "OT4", "Port x configuration bits (y = 0..15)")
        self.OT3 = BitField(self, 0x00000008, "OT3", "Port x configuration bits (y = 0..15)")
        self.OT2 = BitField(self, 0x00000004, "OT2", "Port x configuration bits (y = 0..15)")
        self.OT1 = BitField(self, 0x00000002, "OT1", "Port x configuration bits (y = 0..15)")
        self.OT0 = BitField(self, 0x00000001, "OT0", "Port x configuration bits (y = 0..15)")
        self.OT = Subscriptor(self, "OT{}")

class SA_GPIOB_OSPEEDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xC0, "OSPEEDR", "GPIO port output speed register")
        self.OSPEEDR15 = BitField(self, 0xC0000000, "OSPEEDR15", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR14 = BitField(self, 0x30000000, "OSPEEDR14", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR13 = BitField(self, 0x0C000000, "OSPEEDR13", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR12 = BitField(self, 0x03000000, "OSPEEDR12", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR11 = BitField(self, 0x00C00000, "OSPEEDR11", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR10 = BitField(self, 0x00300000, "OSPEEDR10", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR9 = BitField(self, 0x000C0000, "OSPEEDR9", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR8 = BitField(self, 0x00030000, "OSPEEDR8", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR7 = BitField(self, 0x0000C000, "OSPEEDR7", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR6 = BitField(self, 0x00003000, "OSPEEDR6", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR5 = BitField(self, 0x00000C00, "OSPEEDR5", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR4 = BitField(self, 0x00000300, "OSPEEDR4", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR3 = BitField(self, 0x000000C0, "OSPEEDR3", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR2 = BitField(self, 0x00000030, "OSPEEDR2", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR1 = BitField(self, 0x0000000C, "OSPEEDR1", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR0 = BitField(self, 0x00000003, "OSPEEDR0", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR = Subscriptor(self, "OSPEEDR{}")

class SA_GPIOB_PUPDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x100, "PUPDR", "GPIO port pull-up/pull-down register")
        self.PUPDR15 = BitField(self, 0xC0000000, "PUPDR15", "Port x configuration bits (y = 0..15)")
        self.PUPDR14 = BitField(self, 0x30000000, "PUPDR14", "Port x configuration bits (y = 0..15)")
        self.PUPDR13 = BitField(self, 0x0C000000, "PUPDR13", "Port x configuration bits (y = 0..15)")
        self.PUPDR12 = BitField(self, 0x03000000, "PUPDR12", "Port x configuration bits (y = 0..15)")
        self.PUPDR11 = BitField(self, 0x00C00000, "PUPDR11", "Port x configuration bits (y = 0..15)")
        self.PUPDR10 = BitField(self, 0x00300000, "PUPDR10", "Port x configuration bits (y = 0..15)")
        self.PUPDR9 = BitField(self, 0x000C0000, "PUPDR9", "Port x configuration bits (y = 0..15)")
        self.PUPDR8 = BitField(self, 0x00030000, "PUPDR8", "Port x configuration bits (y = 0..15)")
        self.PUPDR7 = BitField(self, 0x0000C000, "PUPDR7", "Port x configuration bits (y = 0..15)")
        self.PUPDR6 = BitField(self, 0x00003000, "PUPDR6", "Port x configuration bits (y = 0..15)")
        self.PUPDR5 = BitField(self, 0x00000C00, "PUPDR5", "Port x configuration bits (y = 0..15)")
        self.PUPDR4 = BitField(self, 0x00000300, "PUPDR4", "Port x configuration bits (y = 0..15)")
        self.PUPDR3 = BitField(self, 0x000000C0, "PUPDR3", "Port x configuration bits (y = 0..15)")
        self.PUPDR2 = BitField(self, 0x00000030, "PUPDR2", "Port x configuration bits (y = 0..15)")
        self.PUPDR1 = BitField(self, 0x0000000C, "PUPDR1", "Port x configuration bits (y = 0..15)")
        self.PUPDR0 = BitField(self, 0x00000003, "PUPDR0", "Port x configuration bits (y = 0..15)")
        self.PUPDR = Subscriptor(self, "PUPDR{}")

class SA_GPIOB_IDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IDR", "GPIO port input data register")
        self.IDR15 = BitField(self, 0x00008000, "IDR15", "Port input data (y = 0..15)")
        self.IDR14 = BitField(self, 0x00004000, "IDR14", "Port input data (y = 0..15)")
        self.IDR13 = BitField(self, 0x00002000, "IDR13", "Port input data (y = 0..15)")
        self.IDR12 = BitField(self, 0x00001000, "IDR12", "Port input data (y = 0..15)")
        self.IDR11 = BitField(self, 0x00000800, "IDR11", "Port input data (y = 0..15)")
        self.IDR10 = BitField(self, 0x00000400, "IDR10", "Port input data (y = 0..15)")
        self.IDR9 = BitField(self, 0x00000200, "IDR9", "Port input data (y = 0..15)")
        self.IDR8 = BitField(self, 0x00000100, "IDR8", "Port input data (y = 0..15)")
        self.IDR7 = BitField(self, 0x00000080, "IDR7", "Port input data (y = 0..15)")
        self.IDR6 = BitField(self, 0x00000040, "IDR6", "Port input data (y = 0..15)")
        self.IDR5 = BitField(self, 0x00000020, "IDR5", "Port input data (y = 0..15)")
        self.IDR4 = BitField(self, 0x00000010, "IDR4", "Port input data (y = 0..15)")
        self.IDR3 = BitField(self, 0x00000008, "IDR3", "Port input data (y = 0..15)")
        self.IDR2 = BitField(self, 0x00000004, "IDR2", "Port input data (y = 0..15)")
        self.IDR1 = BitField(self, 0x00000002, "IDR1", "Port input data (y = 0..15)")
        self.IDR0 = BitField(self, 0x00000001, "IDR0", "Port input data (y = 0..15)")
        self.IDR = Subscriptor(self, "IDR{}")

class SA_GPIOB_ODR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ODR", "GPIO port output data register")
        self.ODR15 = BitField(self, 0x00008000, "ODR15", "Port output data (y = 0..15)")
        self.ODR14 = BitField(self, 0x00004000, "ODR14", "Port output data (y = 0..15)")
        self.ODR13 = BitField(self, 0x00002000, "ODR13", "Port output data (y = 0..15)")
        self.ODR12 = BitField(self, 0x00001000, "ODR12", "Port output data (y = 0..15)")
        self.ODR11 = BitField(self, 0x00000800, "ODR11", "Port output data (y = 0..15)")
        self.ODR10 = BitField(self, 0x00000400, "ODR10", "Port output data (y = 0..15)")
        self.ODR9 = BitField(self, 0x00000200, "ODR9", "Port output data (y = 0..15)")
        self.ODR8 = BitField(self, 0x00000100, "ODR8", "Port output data (y = 0..15)")
        self.ODR7 = BitField(self, 0x00000080, "ODR7", "Port output data (y = 0..15)")
        self.ODR6 = BitField(self, 0x00000040, "ODR6", "Port output data (y = 0..15)")
        self.ODR5 = BitField(self, 0x00000020, "ODR5", "Port output data (y = 0..15)")
        self.ODR4 = BitField(self, 0x00000010, "ODR4", "Port output data (y = 0..15)")
        self.ODR3 = BitField(self, 0x00000008, "ODR3", "Port output data (y = 0..15)")
        self.ODR2 = BitField(self, 0x00000004, "ODR2", "Port output data (y = 0..15)")
        self.ODR1 = BitField(self, 0x00000002, "ODR1", "Port output data (y = 0..15)")
        self.ODR0 = BitField(self, 0x00000001, "ODR0", "Port output data (y = 0..15)")
        self.ODR = Subscriptor(self, "ODR{}")

class SA_GPIOB_BSRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BSRR", "GPIO port bit set/reset register")
        self.BR15 = BitField(self, 0x80000000, "BR15", "Port x reset bit y (y = 0..15)")
        self.BR14 = BitField(self, 0x40000000, "BR14", "Port x reset bit y (y = 0..15)")
        self.BR13 = BitField(self, 0x20000000, "BR13", "Port x reset bit y (y = 0..15)")
        self.BR12 = BitField(self, 0x10000000, "BR12", "Port x reset bit y (y = 0..15)")
        self.BR11 = BitField(self, 0x08000000, "BR11", "Port x reset bit y (y = 0..15)")
        self.BR10 = BitField(self, 0x04000000, "BR10", "Port x reset bit y (y = 0..15)")
        self.BR9 = BitField(self, 0x02000000, "BR9", "Port x reset bit y (y = 0..15)")
        self.BR8 = BitField(self, 0x01000000, "BR8", "Port x reset bit y (y = 0..15)")
        self.BR7 = BitField(self, 0x00800000, "BR7", "Port x reset bit y (y = 0..15)")
        self.BR6 = BitField(self, 0x00400000, "BR6", "Port x reset bit y (y = 0..15)")
        self.BR5 = BitField(self, 0x00200000, "BR5", "Port x reset bit y (y = 0..15)")
        self.BR4 = BitField(self, 0x00100000, "BR4", "Port x reset bit y (y = 0..15)")
        self.BR3 = BitField(self, 0x00080000, "BR3", "Port x reset bit y (y = 0..15)")
        self.BR2 = BitField(self, 0x00040000, "BR2", "Port x reset bit y (y = 0..15)")
        self.BR1 = BitField(self, 0x00020000, "BR1", "Port x reset bit y (y = 0..15)")
        self.BR0 = BitField(self, 0x00010000, "BR0", "Port x set bit y (y= 0..15)")
        self.BS15 = BitField(self, 0x00008000, "BS15", "Port x set bit y (y= 0..15)")
        self.BS14 = BitField(self, 0x00004000, "BS14", "Port x set bit y (y= 0..15)")
        self.BS13 = BitField(self, 0x00002000, "BS13", "Port x set bit y (y= 0..15)")
        self.BS12 = BitField(self, 0x00001000, "BS12", "Port x set bit y (y= 0..15)")
        self.BS11 = BitField(self, 0x00000800, "BS11", "Port x set bit y (y= 0..15)")
        self.BS10 = BitField(self, 0x00000400, "BS10", "Port x set bit y (y= 0..15)")
        self.BS9 = BitField(self, 0x00000200, "BS9", "Port x set bit y (y= 0..15)")
        self.BS8 = BitField(self, 0x00000100, "BS8", "Port x set bit y (y= 0..15)")
        self.BS7 = BitField(self, 0x00000080, "BS7", "Port x set bit y (y= 0..15)")
        self.BS6 = BitField(self, 0x00000040, "BS6", "Port x set bit y (y= 0..15)")
        self.BS5 = BitField(self, 0x00000020, "BS5", "Port x set bit y (y= 0..15)")
        self.BS4 = BitField(self, 0x00000010, "BS4", "Port x set bit y (y= 0..15)")
        self.BS3 = BitField(self, 0x00000008, "BS3", "Port x set bit y (y= 0..15)")
        self.BS2 = BitField(self, 0x00000004, "BS2", "Port x set bit y (y= 0..15)")
        self.BS1 = BitField(self, 0x00000002, "BS1", "Port x set bit y (y= 0..15)")
        self.BS0 = BitField(self, 0x00000001, "BS0", "Port x set bit y (y= 0..15)")
        self.BR = Subscriptor(self, "BR{}")
        self.BS = Subscriptor(self, "BS{}")

class SA_GPIOB_LCKR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "LCKR", "GPIO port configuration lock register")
        self.LCKK = BitField(self, 0x00010000, "LCKK", "Port x lock bit y (y= 0..15)")
        self.LCK15 = BitField(self, 0x00008000, "LCK15", "Port x lock bit y (y= 0..15)")
        self.LCK14 = BitField(self, 0x00004000, "LCK14", "Port x lock bit y (y= 0..15)")
        self.LCK13 = BitField(self, 0x00002000, "LCK13", "Port x lock bit y (y= 0..15)")
        self.LCK12 = BitField(self, 0x00001000, "LCK12", "Port x lock bit y (y= 0..15)")
        self.LCK11 = BitField(self, 0x00000800, "LCK11", "Port x lock bit y (y= 0..15)")
        self.LCK10 = BitField(self, 0x00000400, "LCK10", "Port x lock bit y (y= 0..15)")
        self.LCK9 = BitField(self, 0x00000200, "LCK9", "Port x lock bit y (y= 0..15)")
        self.LCK8 = BitField(self, 0x00000100, "LCK8", "Port x lock bit y (y= 0..15)")
        self.LCK7 = BitField(self, 0x00000080, "LCK7", "Port x lock bit y (y= 0..15)")
        self.LCK6 = BitField(self, 0x00000040, "LCK6", "Port x lock bit y (y= 0..15)")
        self.LCK5 = BitField(self, 0x00000020, "LCK5", "Port x lock bit y (y= 0..15)")
        self.LCK4 = BitField(self, 0x00000010, "LCK4", "Port x lock bit y (y= 0..15)")
        self.LCK3 = BitField(self, 0x00000008, "LCK3", "Port x lock bit y (y= 0..15)")
        self.LCK2 = BitField(self, 0x00000004, "LCK2", "Port x lock bit y (y= 0..15)")
        self.LCK1 = BitField(self, 0x00000002, "LCK1", "Port x lock bit y (y= 0..15)")
        self.LCK0 = BitField(self, 0x00000001, "LCK0", "Port x lock bit y (y= 0..15)")
        self.LCK = Subscriptor(self, "LCK{}")

class SA_GPIOB_AFRL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AFRL", "GPIO alternate function low register")
        self.AFRL7 = BitField(self, 0xF0000000, "AFRL7", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL6 = BitField(self, 0x0F000000, "AFRL6", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL5 = BitField(self, 0x00F00000, "AFRL5", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL4 = BitField(self, 0x000F0000, "AFRL4", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL3 = BitField(self, 0x0000F000, "AFRL3", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL2 = BitField(self, 0x00000F00, "AFRL2", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL1 = BitField(self, 0x000000F0, "AFRL1", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL0 = BitField(self, 0x0000000F, "AFRL0", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL = Subscriptor(self, "AFRL{}")

class SA_GPIOB_AFRH(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AFRH", "GPIO alternate function high register")
        self.AFRH15 = BitField(self, 0xF0000000, "AFRH15", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH14 = BitField(self, 0x0F000000, "AFRH14", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH13 = BitField(self, 0x00F00000, "AFRH13", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH12 = BitField(self, 0x000F0000, "AFRH12", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH11 = BitField(self, 0x0000F000, "AFRH11", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH10 = BitField(self, 0x00000F00, "AFRH10", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH9 = BitField(self, 0x000000F0, "AFRH9", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH8 = BitField(self, 0x0000000F, "AFRH8", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH = Subscriptor(self, "AFRH{}")

class SA_GPIOB_BRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BRR", "GPIO port bit reset register")
        self.BR0 = BitField(self, 0x00000001, "BR0", "Port Reset bit")
        self.BR1 = BitField(self, 0x00000002, "BR1", "Port Reset bit")
        self.BR2 = BitField(self, 0x00000004, "BR2", "Port Reset bit")
        self.BR3 = BitField(self, 0x00000008, "BR3", "Port Reset bit")
        self.BR4 = BitField(self, 0x00000010, "BR4", "Port Reset bit")
        self.BR5 = BitField(self, 0x00000020, "BR5", "Port Reset bit")
        self.BR6 = BitField(self, 0x00000040, "BR6", "Port Reset bit")
        self.BR7 = BitField(self, 0x00000080, "BR7", "Port Reset bit")
        self.BR8 = BitField(self, 0x00000100, "BR8", "Port Reset bit")
        self.BR9 = BitField(self, 0x00000200, "BR9", "Port Reset bit")
        self.BR10 = BitField(self, 0x00000400, "BR10", "Port Reset bit")
        self.BR11 = BitField(self, 0x00000800, "BR11", "Port Reset bit")
        self.BR12 = BitField(self, 0x00001000, "BR12", "Port Reset bit")
        self.BR13 = BitField(self, 0x00002000, "BR13", "Port Reset bit")
        self.BR14 = BitField(self, 0x00004000, "BR14", "Port Reset bit")
        self.BR15 = BitField(self, 0x00008000, "BR15", "Port Reset bit")
        self.BR = Subscriptor(self, "BR{}")

class SA_GPIOB(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "General-purpose I/Os")
        self.MODER = SA_GPIOB_MODER(self, 0x0)
        self.OTYPER = SA_GPIOB_OTYPER(self, 0x4)
        self.OSPEEDR = SA_GPIOB_OSPEEDR(self, 0x8)
        self.PUPDR = SA_GPIOB_PUPDR(self, 0xC)
        self.IDR = SA_GPIOB_IDR(self, 0x10)
        self.ODR = SA_GPIOB_ODR(self, 0x14)
        self.BSRR = SA_GPIOB_BSRR(self, 0x18)
        self.LCKR = SA_GPIOB_LCKR(self, 0x1C)
        self.AFRL = SA_GPIOB_AFRL(self, 0x20)
        self.AFRH = SA_GPIOB_AFRH(self, 0x24)
        self.BRR = SA_GPIOB_BRR(self, 0x28)

GPIOB = SA_GPIOB(0x48000400, "GPIOB")

class SA_GPIOC_MODER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "MODER", "GPIO port mode register")
        self.MODER15 = BitField(self, 0xC0000000, "MODER15", "Port x configuration bits (y = 0..15)")
        self.MODER14 = BitField(self, 0x30000000, "MODER14", "Port x configuration bits (y = 0..15)")
        self.MODER13 = BitField(self, 0x0C000000, "MODER13", "Port x configuration bits (y = 0..15)")
        self.MODER12 = BitField(self, 0x03000000, "MODER12", "Port x configuration bits (y = 0..15)")
        self.MODER11 = BitField(self, 0x00C00000, "MODER11", "Port x configuration bits (y = 0..15)")
        self.MODER10 = BitField(self, 0x00300000, "MODER10", "Port x configuration bits (y = 0..15)")
        self.MODER9 = BitField(self, 0x000C0000, "MODER9", "Port x configuration bits (y = 0..15)")
        self.MODER8 = BitField(self, 0x00030000, "MODER8", "Port x configuration bits (y = 0..15)")
        self.MODER7 = BitField(self, 0x0000C000, "MODER7", "Port x configuration bits (y = 0..15)")
        self.MODER6 = BitField(self, 0x00003000, "MODER6", "Port x configuration bits (y = 0..15)")
        self.MODER5 = BitField(self, 0x00000C00, "MODER5", "Port x configuration bits (y = 0..15)")
        self.MODER4 = BitField(self, 0x00000300, "MODER4", "Port x configuration bits (y = 0..15)")
        self.MODER3 = BitField(self, 0x000000C0, "MODER3", "Port x configuration bits (y = 0..15)")
        self.MODER2 = BitField(self, 0x00000030, "MODER2", "Port x configuration bits (y = 0..15)")
        self.MODER1 = BitField(self, 0x0000000C, "MODER1", "Port x configuration bits (y = 0..15)")
        self.MODER0 = BitField(self, 0x00000003, "MODER0", "Port x configuration bits (y = 0..15)")
        self.MODER = Subscriptor(self, "MODER{}")

class SA_GPIOC_OTYPER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OTYPER", "GPIO port output type register")
        self.OT15 = BitField(self, 0x00008000, "OT15", "Port x configuration bits (y = 0..15)")
        self.OT14 = BitField(self, 0x00004000, "OT14", "Port x configuration bits (y = 0..15)")
        self.OT13 = BitField(self, 0x00002000, "OT13", "Port x configuration bits (y = 0..15)")
        self.OT12 = BitField(self, 0x00001000, "OT12", "Port x configuration bits (y = 0..15)")
        self.OT11 = BitField(self, 0x00000800, "OT11", "Port x configuration bits (y = 0..15)")
        self.OT10 = BitField(self, 0x00000400, "OT10", "Port x configuration bits (y = 0..15)")
        self.OT9 = BitField(self, 0x00000200, "OT9", "Port x configuration bits (y = 0..15)")
        self.OT8 = BitField(self, 0x00000100, "OT8", "Port x configuration bits (y = 0..15)")
        self.OT7 = BitField(self, 0x00000080, "OT7", "Port x configuration bits (y = 0..15)")
        self.OT6 = BitField(self, 0x00000040, "OT6", "Port x configuration bits (y = 0..15)")
        self.OT5 = BitField(self, 0x00000020, "OT5", "Port x configuration bits (y = 0..15)")
        self.OT4 = BitField(self, 0x00000010, "OT4", "Port x configuration bits (y = 0..15)")
        self.OT3 = BitField(self, 0x00000008, "OT3", "Port x configuration bits (y = 0..15)")
        self.OT2 = BitField(self, 0x00000004, "OT2", "Port x configuration bits (y = 0..15)")
        self.OT1 = BitField(self, 0x00000002, "OT1", "Port x configuration bits (y = 0..15)")
        self.OT0 = BitField(self, 0x00000001, "OT0", "Port x configuration bits (y = 0..15)")
        self.OT = Subscriptor(self, "OT{}")

class SA_GPIOC_OSPEEDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OSPEEDR", "GPIO port output speed register")
        self.OSPEEDR15 = BitField(self, 0xC0000000, "OSPEEDR15", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR14 = BitField(self, 0x30000000, "OSPEEDR14", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR13 = BitField(self, 0x0C000000, "OSPEEDR13", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR12 = BitField(self, 0x03000000, "OSPEEDR12", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR11 = BitField(self, 0x00C00000, "OSPEEDR11", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR10 = BitField(self, 0x00300000, "OSPEEDR10", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR9 = BitField(self, 0x000C0000, "OSPEEDR9", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR8 = BitField(self, 0x00030000, "OSPEEDR8", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR7 = BitField(self, 0x0000C000, "OSPEEDR7", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR6 = BitField(self, 0x00003000, "OSPEEDR6", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR5 = BitField(self, 0x00000C00, "OSPEEDR5", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR4 = BitField(self, 0x00000300, "OSPEEDR4", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR3 = BitField(self, 0x000000C0, "OSPEEDR3", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR2 = BitField(self, 0x00000030, "OSPEEDR2", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR1 = BitField(self, 0x0000000C, "OSPEEDR1", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR0 = BitField(self, 0x00000003, "OSPEEDR0", "Port x configuration bits (y = 0..15)")
        self.OSPEEDR = Subscriptor(self, "OSPEEDR{}")

class SA_GPIOC_PUPDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PUPDR", "GPIO port pull-up/pull-down register")
        self.PUPDR15 = BitField(self, 0xC0000000, "PUPDR15", "Port x configuration bits (y = 0..15)")
        self.PUPDR14 = BitField(self, 0x30000000, "PUPDR14", "Port x configuration bits (y = 0..15)")
        self.PUPDR13 = BitField(self, 0x0C000000, "PUPDR13", "Port x configuration bits (y = 0..15)")
        self.PUPDR12 = BitField(self, 0x03000000, "PUPDR12", "Port x configuration bits (y = 0..15)")
        self.PUPDR11 = BitField(self, 0x00C00000, "PUPDR11", "Port x configuration bits (y = 0..15)")
        self.PUPDR10 = BitField(self, 0x00300000, "PUPDR10", "Port x configuration bits (y = 0..15)")
        self.PUPDR9 = BitField(self, 0x000C0000, "PUPDR9", "Port x configuration bits (y = 0..15)")
        self.PUPDR8 = BitField(self, 0x00030000, "PUPDR8", "Port x configuration bits (y = 0..15)")
        self.PUPDR7 = BitField(self, 0x0000C000, "PUPDR7", "Port x configuration bits (y = 0..15)")
        self.PUPDR6 = BitField(self, 0x00003000, "PUPDR6", "Port x configuration bits (y = 0..15)")
        self.PUPDR5 = BitField(self, 0x00000C00, "PUPDR5", "Port x configuration bits (y = 0..15)")
        self.PUPDR4 = BitField(self, 0x00000300, "PUPDR4", "Port x configuration bits (y = 0..15)")
        self.PUPDR3 = BitField(self, 0x000000C0, "PUPDR3", "Port x configuration bits (y = 0..15)")
        self.PUPDR2 = BitField(self, 0x00000030, "PUPDR2", "Port x configuration bits (y = 0..15)")
        self.PUPDR1 = BitField(self, 0x0000000C, "PUPDR1", "Port x configuration bits (y = 0..15)")
        self.PUPDR0 = BitField(self, 0x00000003, "PUPDR0", "Port x configuration bits (y = 0..15)")
        self.PUPDR = Subscriptor(self, "PUPDR{}")

class SA_GPIOC_IDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IDR", "GPIO port input data register")
        self.IDR15 = BitField(self, 0x00008000, "IDR15", "Port input data (y = 0..15)")
        self.IDR14 = BitField(self, 0x00004000, "IDR14", "Port input data (y = 0..15)")
        self.IDR13 = BitField(self, 0x00002000, "IDR13", "Port input data (y = 0..15)")
        self.IDR12 = BitField(self, 0x00001000, "IDR12", "Port input data (y = 0..15)")
        self.IDR11 = BitField(self, 0x00000800, "IDR11", "Port input data (y = 0..15)")
        self.IDR10 = BitField(self, 0x00000400, "IDR10", "Port input data (y = 0..15)")
        self.IDR9 = BitField(self, 0x00000200, "IDR9", "Port input data (y = 0..15)")
        self.IDR8 = BitField(self, 0x00000100, "IDR8", "Port input data (y = 0..15)")
        self.IDR7 = BitField(self, 0x00000080, "IDR7", "Port input data (y = 0..15)")
        self.IDR6 = BitField(self, 0x00000040, "IDR6", "Port input data (y = 0..15)")
        self.IDR5 = BitField(self, 0x00000020, "IDR5", "Port input data (y = 0..15)")
        self.IDR4 = BitField(self, 0x00000010, "IDR4", "Port input data (y = 0..15)")
        self.IDR3 = BitField(self, 0x00000008, "IDR3", "Port input data (y = 0..15)")
        self.IDR2 = BitField(self, 0x00000004, "IDR2", "Port input data (y = 0..15)")
        self.IDR1 = BitField(self, 0x00000002, "IDR1", "Port input data (y = 0..15)")
        self.IDR0 = BitField(self, 0x00000001, "IDR0", "Port input data (y = 0..15)")
        self.IDR = Subscriptor(self, "IDR{}")

class SA_GPIOC_ODR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ODR", "GPIO port output data register")
        self.ODR15 = BitField(self, 0x00008000, "ODR15", "Port output data (y = 0..15)")
        self.ODR14 = BitField(self, 0x00004000, "ODR14", "Port output data (y = 0..15)")
        self.ODR13 = BitField(self, 0x00002000, "ODR13", "Port output data (y = 0..15)")
        self.ODR12 = BitField(self, 0x00001000, "ODR12", "Port output data (y = 0..15)")
        self.ODR11 = BitField(self, 0x00000800, "ODR11", "Port output data (y = 0..15)")
        self.ODR10 = BitField(self, 0x00000400, "ODR10", "Port output data (y = 0..15)")
        self.ODR9 = BitField(self, 0x00000200, "ODR9", "Port output data (y = 0..15)")
        self.ODR8 = BitField(self, 0x00000100, "ODR8", "Port output data (y = 0..15)")
        self.ODR7 = BitField(self, 0x00000080, "ODR7", "Port output data (y = 0..15)")
        self.ODR6 = BitField(self, 0x00000040, "ODR6", "Port output data (y = 0..15)")
        self.ODR5 = BitField(self, 0x00000020, "ODR5", "Port output data (y = 0..15)")
        self.ODR4 = BitField(self, 0x00000010, "ODR4", "Port output data (y = 0..15)")
        self.ODR3 = BitField(self, 0x00000008, "ODR3", "Port output data (y = 0..15)")
        self.ODR2 = BitField(self, 0x00000004, "ODR2", "Port output data (y = 0..15)")
        self.ODR1 = BitField(self, 0x00000002, "ODR1", "Port output data (y = 0..15)")
        self.ODR0 = BitField(self, 0x00000001, "ODR0", "Port output data (y = 0..15)")
        self.ODR = Subscriptor(self, "ODR{}")

class SA_GPIOC_BSRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BSRR", "GPIO port bit set/reset register")
        self.BR15 = BitField(self, 0x80000000, "BR15", "Port x reset bit y (y = 0..15)")
        self.BR14 = BitField(self, 0x40000000, "BR14", "Port x reset bit y (y = 0..15)")
        self.BR13 = BitField(self, 0x20000000, "BR13", "Port x reset bit y (y = 0..15)")
        self.BR12 = BitField(self, 0x10000000, "BR12", "Port x reset bit y (y = 0..15)")
        self.BR11 = BitField(self, 0x08000000, "BR11", "Port x reset bit y (y = 0..15)")
        self.BR10 = BitField(self, 0x04000000, "BR10", "Port x reset bit y (y = 0..15)")
        self.BR9 = BitField(self, 0x02000000, "BR9", "Port x reset bit y (y = 0..15)")
        self.BR8 = BitField(self, 0x01000000, "BR8", "Port x reset bit y (y = 0..15)")
        self.BR7 = BitField(self, 0x00800000, "BR7", "Port x reset bit y (y = 0..15)")
        self.BR6 = BitField(self, 0x00400000, "BR6", "Port x reset bit y (y = 0..15)")
        self.BR5 = BitField(self, 0x00200000, "BR5", "Port x reset bit y (y = 0..15)")
        self.BR4 = BitField(self, 0x00100000, "BR4", "Port x reset bit y (y = 0..15)")
        self.BR3 = BitField(self, 0x00080000, "BR3", "Port x reset bit y (y = 0..15)")
        self.BR2 = BitField(self, 0x00040000, "BR2", "Port x reset bit y (y = 0..15)")
        self.BR1 = BitField(self, 0x00020000, "BR1", "Port x reset bit y (y = 0..15)")
        self.BR0 = BitField(self, 0x00010000, "BR0", "Port x set bit y (y= 0..15)")
        self.BS15 = BitField(self, 0x00008000, "BS15", "Port x set bit y (y= 0..15)")
        self.BS14 = BitField(self, 0x00004000, "BS14", "Port x set bit y (y= 0..15)")
        self.BS13 = BitField(self, 0x00002000, "BS13", "Port x set bit y (y= 0..15)")
        self.BS12 = BitField(self, 0x00001000, "BS12", "Port x set bit y (y= 0..15)")
        self.BS11 = BitField(self, 0x00000800, "BS11", "Port x set bit y (y= 0..15)")
        self.BS10 = BitField(self, 0x00000400, "BS10", "Port x set bit y (y= 0..15)")
        self.BS9 = BitField(self, 0x00000200, "BS9", "Port x set bit y (y= 0..15)")
        self.BS8 = BitField(self, 0x00000100, "BS8", "Port x set bit y (y= 0..15)")
        self.BS7 = BitField(self, 0x00000080, "BS7", "Port x set bit y (y= 0..15)")
        self.BS6 = BitField(self, 0x00000040, "BS6", "Port x set bit y (y= 0..15)")
        self.BS5 = BitField(self, 0x00000020, "BS5", "Port x set bit y (y= 0..15)")
        self.BS4 = BitField(self, 0x00000010, "BS4", "Port x set bit y (y= 0..15)")
        self.BS3 = BitField(self, 0x00000008, "BS3", "Port x set bit y (y= 0..15)")
        self.BS2 = BitField(self, 0x00000004, "BS2", "Port x set bit y (y= 0..15)")
        self.BS1 = BitField(self, 0x00000002, "BS1", "Port x set bit y (y= 0..15)")
        self.BS0 = BitField(self, 0x00000001, "BS0", "Port x set bit y (y= 0..15)")
        self.BR = Subscriptor(self, "BR{}")
        self.BS = Subscriptor(self, "BS{}")

class SA_GPIOC_LCKR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "LCKR", "GPIO port configuration lock register")
        self.LCKK = BitField(self, 0x00010000, "LCKK", "Port x lock bit y (y= 0..15)")
        self.LCK15 = BitField(self, 0x00008000, "LCK15", "Port x lock bit y (y= 0..15)")
        self.LCK14 = BitField(self, 0x00004000, "LCK14", "Port x lock bit y (y= 0..15)")
        self.LCK13 = BitField(self, 0x00002000, "LCK13", "Port x lock bit y (y= 0..15)")
        self.LCK12 = BitField(self, 0x00001000, "LCK12", "Port x lock bit y (y= 0..15)")
        self.LCK11 = BitField(self, 0x00000800, "LCK11", "Port x lock bit y (y= 0..15)")
        self.LCK10 = BitField(self, 0x00000400, "LCK10", "Port x lock bit y (y= 0..15)")
        self.LCK9 = BitField(self, 0x00000200, "LCK9", "Port x lock bit y (y= 0..15)")
        self.LCK8 = BitField(self, 0x00000100, "LCK8", "Port x lock bit y (y= 0..15)")
        self.LCK7 = BitField(self, 0x00000080, "LCK7", "Port x lock bit y (y= 0..15)")
        self.LCK6 = BitField(self, 0x00000040, "LCK6", "Port x lock bit y (y= 0..15)")
        self.LCK5 = BitField(self, 0x00000020, "LCK5", "Port x lock bit y (y= 0..15)")
        self.LCK4 = BitField(self, 0x00000010, "LCK4", "Port x lock bit y (y= 0..15)")
        self.LCK3 = BitField(self, 0x00000008, "LCK3", "Port x lock bit y (y= 0..15)")
        self.LCK2 = BitField(self, 0x00000004, "LCK2", "Port x lock bit y (y= 0..15)")
        self.LCK1 = BitField(self, 0x00000002, "LCK1", "Port x lock bit y (y= 0..15)")
        self.LCK0 = BitField(self, 0x00000001, "LCK0", "Port x lock bit y (y= 0..15)")
        self.LCK = Subscriptor(self, "LCK{}")

class SA_GPIOC_AFRL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AFRL", "GPIO alternate function low register")
        self.AFRL7 = BitField(self, 0xF0000000, "AFRL7", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL6 = BitField(self, 0x0F000000, "AFRL6", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL5 = BitField(self, 0x00F00000, "AFRL5", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL4 = BitField(self, 0x000F0000, "AFRL4", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL3 = BitField(self, 0x0000F000, "AFRL3", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL2 = BitField(self, 0x00000F00, "AFRL2", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL1 = BitField(self, 0x000000F0, "AFRL1", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL0 = BitField(self, 0x0000000F, "AFRL0", "Alternate function selection for port x bit y (y = 0..7)")
        self.AFRL = Subscriptor(self, "AFRL{}")

class SA_GPIOC_AFRH(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AFRH", "GPIO alternate function high register")
        self.AFRH15 = BitField(self, 0xF0000000, "AFRH15", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH14 = BitField(self, 0x0F000000, "AFRH14", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH13 = BitField(self, 0x00F00000, "AFRH13", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH12 = BitField(self, 0x000F0000, "AFRH12", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH11 = BitField(self, 0x0000F000, "AFRH11", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH10 = BitField(self, 0x00000F00, "AFRH10", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH9 = BitField(self, 0x000000F0, "AFRH9", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH8 = BitField(self, 0x0000000F, "AFRH8", "Alternate function selection for port x bit y (y = 8..15)")
        self.AFRH = Subscriptor(self, "AFRH{}")

class SA_GPIOC_BRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BRR", "GPIO port bit reset register")
        self.BR0 = BitField(self, 0x00000001, "BR0", "Port Reset bit")
        self.BR1 = BitField(self, 0x00000002, "BR1", "Port Reset bit")
        self.BR2 = BitField(self, 0x00000004, "BR2", "Port Reset bit")
        self.BR3 = BitField(self, 0x00000008, "BR3", "Port Reset bit")
        self.BR4 = BitField(self, 0x00000010, "BR4", "Port Reset bit")
        self.BR5 = BitField(self, 0x00000020, "BR5", "Port Reset bit")
        self.BR6 = BitField(self, 0x00000040, "BR6", "Port Reset bit")
        self.BR7 = BitField(self, 0x00000080, "BR7", "Port Reset bit")
        self.BR8 = BitField(self, 0x00000100, "BR8", "Port Reset bit")
        self.BR9 = BitField(self, 0x00000200, "BR9", "Port Reset bit")
        self.BR10 = BitField(self, 0x00000400, "BR10", "Port Reset bit")
        self.BR11 = BitField(self, 0x00000800, "BR11", "Port Reset bit")
        self.BR12 = BitField(self, 0x00001000, "BR12", "Port Reset bit")
        self.BR13 = BitField(self, 0x00002000, "BR13", "Port Reset bit")
        self.BR14 = BitField(self, 0x00004000, "BR14", "Port Reset bit")
        self.BR15 = BitField(self, 0x00008000, "BR15", "Port Reset bit")
        self.BR = Subscriptor(self, "BR{}")

class SA_GPIOC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "General-purpose I/Os")
        self.MODER = SA_GPIOC_MODER(self, 0x0)
        self.OTYPER = SA_GPIOC_OTYPER(self, 0x4)
        self.OSPEEDR = SA_GPIOC_OSPEEDR(self, 0x8)
        self.PUPDR = SA_GPIOC_PUPDR(self, 0xC)
        self.IDR = SA_GPIOC_IDR(self, 0x10)
        self.ODR = SA_GPIOC_ODR(self, 0x14)
        self.BSRR = SA_GPIOC_BSRR(self, 0x18)
        self.LCKR = SA_GPIOC_LCKR(self, 0x1C)
        self.AFRL = SA_GPIOC_AFRL(self, 0x20)
        self.AFRH = SA_GPIOC_AFRH(self, 0x24)
        self.BRR = SA_GPIOC_BRR(self, 0x28)

GPIOC = SA_GPIOC(0x48000800, "GPIOC")
GPIOD = SA_GPIOC(0x48000C00, "GPIOD")
GPIOE = SA_GPIOC(0x48001000, "GPIOE")
GPIOF = SA_GPIOC(0x48001400, "GPIOF")
GPIOG = SA_GPIOC(0x48001800, "GPIOG")

class SA_TIM15_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "control register 1")
        self.CEN = BitField(self, 0x00000001, "CEN", "Counter enable")
        self.UDIS = BitField(self, 0x00000002, "UDIS", "Update disable")
        self.URS = BitField(self, 0x00000004, "URS", "Update request source")
        self.OPM = BitField(self, 0x00000008, "OPM", "One-pulse mode")
        self.ARPE = BitField(self, 0x00000080, "ARPE", "Auto-reload preload enable")
        self.CKD = BitField(self, 0x00000300, "CKD", "Clock division")
        self.UIFREMAP = BitField(self, 0x00000800, "UIFREMAP", "UIF status bit remapping")
        self.DITHEN = BitField(self, 0x00001000, "DITHEN", "Dithering Enable")

class SA_TIM15_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "control register 2")
        self.OIS2 = BitField(self, 0x00000400, "OIS2", "Output idle state 2 (OC2 output)")
        self.OIS1N = BitField(self, 0x00000200, "OIS1N", "Output Idle state 1")
        self.OIS1 = BitField(self, 0x00000100, "OIS1", "Output Idle state 1")
        self.TI1S = BitField(self, 0x00000080, "TI1S", "TI1 selection")
        self.MMS = BitField(self, 0x00000070, "MMS", "Master mode selection")
        self.CCDS = BitField(self, 0x00000008, "CCDS", "Capture/compare DMA selection")
        self.CCUS = BitField(self, 0x00000004, "CCUS", "Capture/compare control update selection")
        self.CCPC = BitField(self, 0x00000001, "CCPC", "Capture/compare preloaded control")
        self.OIS = Subscriptor(self, "OIS{}")

class SA_TIM15_SMCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SMCR", "slave mode control register")
        self.MSM = BitField(self, 0x00000080, "MSM", "Master/Slave mode")
        self.TS = BitField(self, 0x00300070, "TS", "Trigger selection")
        self.SMS = BitField(self, 0x00010007, "SMS", "Slave mode selection")

class SA_TIM15_DIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DIER", "DMA/Interrupt enable register")
        self.TDE = BitField(self, 0x00004000, "TDE", "Trigger DMA request enable")
        self.COMDE = BitField(self, 0x00002000, "COMDE", "COM DMA request enable")
        self.CC2DE = BitField(self, 0x00000400, "CC2DE", "Capture/Compare 2 DMA request enable")
        self.CC1DE = BitField(self, 0x00000200, "CC1DE", "Capture/Compare 1 DMA request enable")
        self.UDE = BitField(self, 0x00000100, "UDE", "Update DMA request enable")
        self.BIE = BitField(self, 0x00000080, "BIE", "Break interrupt enable")
        self.TIE = BitField(self, 0x00000040, "TIE", "Trigger interrupt enable")
        self.COMIE = BitField(self, 0x00000020, "COMIE", "COM interrupt enable")
        self.CC2IE = BitField(self, 0x00000004, "CC2IE", "Capture/Compare 2 interrupt enable")
        self.CC1IE = BitField(self, 0x00000002, "CC1IE", "Capture/Compare 1 interrupt enable")
        self.UIE = BitField(self, 0x00000001, "UIE", "Update interrupt enable")
        self.CCDE = Subscriptor(self, "CC{}DE")
        self.CCIE = Subscriptor(self, "CC{}IE")

class SA_TIM15_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.CC2OF = BitField(self, 0x00000400, "CC2OF", "Capture/Compare 2 overcapture flag")
        self.CC1OF = BitField(self, 0x00000200, "CC1OF", "Capture/Compare 1 overcapture flag")
        self.BIF = BitField(self, 0x00000080, "BIF", "Break interrupt flag")
        self.TIF = BitField(self, 0x00000040, "TIF", "Trigger interrupt flag")
        self.COMIF = BitField(self, 0x00000020, "COMIF", "COM interrupt flag")
        self.CC2IF = BitField(self, 0x00000004, "CC2IF", "Capture/compare 2 interrupt flag")
        self.CC1IF = BitField(self, 0x00000002, "CC1IF", "Capture/compare 1 interrupt flag")
        self.UIF = BitField(self, 0x00000001, "UIF", "Update interrupt flag")
        self.CCIF = Subscriptor(self, "CC{}IF")
        self.CCOF = Subscriptor(self, "CC{}OF")

class SA_TIM15_EGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EGR", "event generation register")
        self.BG = BitField(self, 0x00000080, "BG", "Break generation")
        self.TG = BitField(self, 0x00000040, "TG", "Trigger generation")
        self.COMG = BitField(self, 0x00000020, "COMG", "Capture/Compare control update generation")
        self.CC2G = BitField(self, 0x00000004, "CC2G", "Capture/compare 2 generation")
        self.CC1G = BitField(self, 0x00000002, "CC1G", "Capture/compare 1 generation")
        self.UG = BitField(self, 0x00000001, "UG", "Update generation")
        self.CCG = Subscriptor(self, "CC{}G")

class SA_TIM15_CCMR1_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Output", "capture/compare mode register (output mode)")
        self.OC2M = BitField(self, 0x01007000, "OC2M", "OC2M")
        self.OC2PE = BitField(self, 0x00000800, "OC2PE", "OC2PE")
        self.OC2FE = BitField(self, 0x00000400, "OC2FE", "OC2FE")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "CC2S")
        self.OC1CE = BitField(self, 0x00000080, "OC1CE", "OC1CE")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.CCS = Subscriptor(self, "CC{}S")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM15_CCMR1_Input(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Input", "capture/compare mode register 1 (input mode)")
        self.IC2F = BitField(self, 0x0000F000, "IC2F", "IC2F")
        self.IC2PSC = BitField(self, 0x00000C00, "IC2PSC", "IC2PSC")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "CC2S")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.IC1PSC = BitField(self, 0x0000000C, "IC1PSC", "Input capture 1 prescaler")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.ICPSC = Subscriptor(self, "IC{}PSC")

class SA_TIM15_CCER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCER", "capture/compare enable register")
        self.CC2NP = BitField(self, 0x00000080, "CC2NP", "Capture/Compare 2 complementary output polarity")
        self.CC2P = BitField(self, 0x00000020, "CC2P", "Capture/Compare 2 output polarity")
        self.CC2E = BitField(self, 0x00000010, "CC2E", "Capture/Compare 2 output enable")
        self.CC1NP = BitField(self, 0x00000008, "CC1NP", "Capture/Compare 1 output Polarity")
        self.CC1NE = BitField(self, 0x00000004, "CC1NE", "Capture/Compare 1 complementary output enable")
        self.CC1P = BitField(self, 0x00000002, "CC1P", "Capture/Compare 1 output Polarity")
        self.CC1E = BitField(self, 0x00000001, "CC1E", "Capture/Compare 1 output enable")
        self.CCP = Subscriptor(self, "CC{}P")
        self.CCE = Subscriptor(self, "CC{}E")
        self.CCNP = Subscriptor(self, "CC{}NP")

class SA_TIM15_CNT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNT", "counter")
        self.CNT = BitField(self, 0x0000FFFF, "CNT", "counter value")
        self.UIFCPY = BitField(self, 0x80000000, "UIFCPY", "UIF Copy")

class SA_TIM15_PSC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PSC", "prescaler")
        self.PSC = BitField(self, 0x0000FFFF, "PSC", "Prescaler value")

class SA_TIM15_ARR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "ARR", "auto-reload register")
        self.ARR = BitField(self, 0x0000FFFF, "ARR", "Auto-reload value")

class SA_TIM15_RCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RCR", "repetition counter register")
        self.REP = BitField(self, 0x000000FF, "REP", "Repetition counter value")

class SA_TIM15_CCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR1", "capture/compare register 1")
        self.CCR1 = BitField(self, 0x0000FFFF, "CCR1", "Capture/Compare 1 value")

class SA_TIM15_CCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR2", "capture/compare register 2")
        self.CCR2 = BitField(self, 0x0000FFFF, "CCR2", "Capture/Compare 1 value")

class SA_TIM15_BDTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTR", "break and dead-time register")
        self.DTG = BitField(self, 0x000000FF, "DTG", "Dead-time generator setup")
        self.LOCK = BitField(self, 0x00000300, "LOCK", "Lock configuration")
        self.OSSI = BitField(self, 0x00000400, "OSSI", "Off-state selection for Idle mode")
        self.OSSR = BitField(self, 0x00000800, "OSSR", "Off-state selection for Run mode")
        self.BKE = BitField(self, 0x00001000, "BKE", "Break enable")
        self.BKP = BitField(self, 0x00002000, "BKP", "Break polarity")
        self.AOE = BitField(self, 0x00004000, "AOE", "Automatic output enable")
        self.MOE = BitField(self, 0x00008000, "MOE", "Main output enable")
        self.BKF = BitField(self, 0x000F0000, "BKF", "Break filter")
        self.BKDSRM = BitField(self, 0x04000000, "BKDSRM", "BKDSRM")
        self.BKBID = BitField(self, 0x10000000, "BKBID", "BKBID")

class SA_TIM15_DTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTR2", "timer Deadtime Register 2")
        self.DTGF = BitField(self, 0x000000FF, "DTGF", "Dead-time generator setup")
        self.DTAE = BitField(self, 0x00010000, "DTAE", "Deadtime Asymmetric Enable")
        self.DTPE = BitField(self, 0x00020000, "DTPE", "Deadtime Preload Enable")

class SA_TIM15_TISEL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TISEL", "TIM timer input selection register")
        self.TI1SEL = BitField(self, 0x0000000F, "TI1SEL", "TI1[0] to TI1[15] input selection")
        self.TI2SEL = BitField(self, 0x00000F00, "TI2SEL", "TI2[0] to TI2[15] input selection")
        self.TISEL = Subscriptor(self, "TI{}SEL")

class SA_TIM15_AF1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF1", "TIM alternate function option register 1")
        self.BKCMP4P = BitField(self, 0x00002000, "BKCMP4P", "BRK COMP4 input polarity")
        self.BKCMP3P = BitField(self, 0x00001000, "BKCMP3P", "BRK COMP3 input polarity")
        self.BKCMP2P = BitField(self, 0x00000800, "BKCMP2P", "BRK COMP2 input polarity")
        self.BKCMP1P = BitField(self, 0x00000400, "BKCMP1P", "BRK COMP1 input polarity")
        self.BKINP = BitField(self, 0x00000200, "BKINP", "BRK BKIN input polarity")
        self.BKCMP7E = BitField(self, 0x00000080, "BKCMP7E", "BRK COMP7 enable")
        self.BKCMP6E = BitField(self, 0x00000040, "BKCMP6E", "BRK COMP6 enable")
        self.BKCMP5E = BitField(self, 0x00000020, "BKCMP5E", "BRK COMP5 enable")
        self.BKCMP4E = BitField(self, 0x00000010, "BKCMP4E", "BRK COMP4 enable")
        self.BKCMP3E = BitField(self, 0x00000008, "BKCMP3E", "BRK COMP3 enable")
        self.BKCMP2E = BitField(self, 0x00000004, "BKCMP2E", "BRK COMP2 enable")
        self.BKCMP1E = BitField(self, 0x00000002, "BKCMP1E", "BRK COMP1 enable")
        self.BKINE = BitField(self, 0x00000001, "BKINE", "BRK BKIN input enable")
        self.BKCMPP = Subscriptor(self, "BKCMP{}P")
        self.BKCMPE = Subscriptor(self, "BKCMP{}E")

class SA_TIM15_AF2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF2", "TIM alternate function option register 2")
        self.OCRSEL = BitField(self, 0x00070000, "OCRSEL", "OCREF_CLR source selection")

class SA_TIM15_DCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DCR", "DMA control register")
        self.DBL = BitField(self, 0x00001F00, "DBL", "DMA burst length")
        self.DBA = BitField(self, 0x0000001F, "DBA", "DMA base address")

class SA_TIM15_DMAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DMAR", "DMA address for full transfer")
        self.DMAB = BitField(self, 0xFFFFFFFF, "DMAB", "DMA register for burst accesses")

class SA_TIM15_CCMR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1", "capture/compare mode register")
        self.OC2M = BitField(self, 0x01007000, "OC2M", "OC2M")
        self.OC2PE = BitField(self, 0x00000800, "OC2PE", "OC2PE")
        self.OC2FE = BitField(self, 0x00000400, "OC2FE", "OC2FE")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "CC2S")
        self.OC1CE = BitField(self, 0x00000080, "OC1CE", "OC1CE")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.IC2F = BitField(self, 0x0000F000, "IC2F", "IC2F")
        self.IC2PSC = BitField(self, 0x00000C00, "IC2PSC", "IC2PSC")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.IC1PSC = BitField(self, 0x0000000C, "IC1PSC", "Input capture 1 prescaler")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.ICPSC = Subscriptor(self, "IC{}PSC")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM15(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "General purpose timers")
        self.CR1 = SA_TIM15_CR1(self, 0x0)
        self.CR2 = SA_TIM15_CR2(self, 0x4)
        self.SMCR = SA_TIM15_SMCR(self, 0x8)
        self.DIER = SA_TIM15_DIER(self, 0xC)
        self.SR = SA_TIM15_SR(self, 0x10)
        self.EGR = SA_TIM15_EGR(self, 0x14)
        self.CCMR1_Output = SA_TIM15_CCMR1_Output(self, 0x18)
        self.CCMR1_Input = SA_TIM15_CCMR1_Input(self, 0x18)
        self.CCER = SA_TIM15_CCER(self, 0x20)
        self.CNT = SA_TIM15_CNT(self, 0x24)
        self.PSC = SA_TIM15_PSC(self, 0x28)
        self.ARR = SA_TIM15_ARR(self, 0x2C)
        self.RCR = SA_TIM15_RCR(self, 0x30)
        self.CCR1 = SA_TIM15_CCR1(self, 0x34)
        self.CCR2 = SA_TIM15_CCR2(self, 0x38)
        self.BDTR = SA_TIM15_BDTR(self, 0x44)
        self.DTR2 = SA_TIM15_DTR2(self, 0x54)
        self.TISEL = SA_TIM15_TISEL(self, 0x5C)
        self.AF1 = SA_TIM15_AF1(self, 0x60)
        self.AF2 = SA_TIM15_AF2(self, 0x64)
        self.DCR = SA_TIM15_DCR(self, 0x3DC)
        self.DMAR = SA_TIM15_DMAR(self, 0x3E0)
        self.CCMR1 = SA_TIM15_CCMR1(self, 0x18)
        self.CCR = Subscriptor(self, "CCR{}")
        self.AF = Subscriptor(self, "AF{}")

TIM15 = SA_TIM15(0x40014000, "TIM15")

class SA_TIM16_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "control register 1")
        self.CEN = BitField(self, 0x00000001, "CEN", "Counter enable")
        self.UDIS = BitField(self, 0x00000002, "UDIS", "Update disable")
        self.URS = BitField(self, 0x00000004, "URS", "Update request source")
        self.OPM = BitField(self, 0x00000008, "OPM", "One-pulse mode")
        self.ARPE = BitField(self, 0x00000080, "ARPE", "Auto-reload preload enable")
        self.CKD = BitField(self, 0x00000300, "CKD", "Clock division")
        self.UIFREMAP = BitField(self, 0x00000800, "UIFREMAP", "UIF status bit remapping")
        self.DITHEN = BitField(self, 0x00001000, "DITHEN", "Dithering Enable")

class SA_TIM16_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "control register 2")
        self.OIS1N = BitField(self, 0x00000200, "OIS1N", "Output Idle state 1")
        self.OIS1 = BitField(self, 0x00000100, "OIS1", "Output Idle state 1")
        self.CCDS = BitField(self, 0x00000008, "CCDS", "Capture/compare DMA selection")
        self.CCUS = BitField(self, 0x00000004, "CCUS", "Capture/compare control update selection")
        self.CCPC = BitField(self, 0x00000001, "CCPC", "Capture/compare preloaded control")

class SA_TIM16_DIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DIER", "DMA/Interrupt enable register")
        self.COMDE = BitField(self, 0x00002000, "COMDE", "COM DMA request enable")
        self.CC1DE = BitField(self, 0x00000200, "CC1DE", "Capture/Compare 1 DMA request enable")
        self.UDE = BitField(self, 0x00000100, "UDE", "Update DMA request enable")
        self.BIE = BitField(self, 0x00000080, "BIE", "Break interrupt enable")
        self.COMIE = BitField(self, 0x00000020, "COMIE", "COM interrupt enable")
        self.CC1IE = BitField(self, 0x00000002, "CC1IE", "Capture/Compare 1 interrupt enable")
        self.UIE = BitField(self, 0x00000001, "UIE", "Update interrupt enable")

class SA_TIM16_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.CC1OF = BitField(self, 0x00000200, "CC1OF", "Capture/Compare 1 overcapture flag")
        self.BIF = BitField(self, 0x00000080, "BIF", "Break interrupt flag")
        self.COMIF = BitField(self, 0x00000020, "COMIF", "COM interrupt flag")
        self.CC1IF = BitField(self, 0x00000002, "CC1IF", "Capture/compare 1 interrupt flag")
        self.UIF = BitField(self, 0x00000001, "UIF", "Update interrupt flag")

class SA_TIM16_EGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EGR", "event generation register")
        self.BG = BitField(self, 0x00000080, "BG", "Break generation")
        self.COMG = BitField(self, 0x00000020, "COMG", "Capture/Compare control update generation")
        self.CC1G = BitField(self, 0x00000002, "CC1G", "Capture/compare 1 generation")
        self.UG = BitField(self, 0x00000001, "UG", "Update generation")

class SA_TIM16_CCMR1_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Output", "capture/compare mode register (output mode)")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")

class SA_TIM16_CCMR1_Input(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Input", "capture/compare mode register 1 (input mode)")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.IC1PSC = BitField(self, 0x0000000C, "IC1PSC", "Input capture 1 prescaler")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")

class SA_TIM16_CCER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCER", "capture/compare enable register")
        self.CC1NP = BitField(self, 0x00000008, "CC1NP", "Capture/Compare 1 output Polarity")
        self.CC1NE = BitField(self, 0x00000004, "CC1NE", "Capture/Compare 1 complementary output enable")
        self.CC1P = BitField(self, 0x00000002, "CC1P", "Capture/Compare 1 output Polarity")
        self.CC1E = BitField(self, 0x00000001, "CC1E", "Capture/Compare 1 output enable")

class SA_TIM16_CNT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNT", "counter")
        self.CNT = BitField(self, 0x0000FFFF, "CNT", "counter value")
        self.UIFCPY = BitField(self, 0x80000000, "UIFCPY", "UIF Copy")

class SA_TIM16_PSC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PSC", "prescaler")
        self.PSC = BitField(self, 0x0000FFFF, "PSC", "Prescaler value")

class SA_TIM16_ARR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "ARR", "auto-reload register")
        self.ARR = BitField(self, 0x0000FFFF, "ARR", "Auto-reload value")

class SA_TIM16_RCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RCR", "repetition counter register")
        self.REP = BitField(self, 0x000000FF, "REP", "Repetition counter value")

class SA_TIM16_CCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR1", "capture/compare register 1")
        self.CCR1 = BitField(self, 0x0000FFFF, "CCR1", "Capture/Compare 1 value")

class SA_TIM16_BDTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTR", "break and dead-time register")
        self.DTG = BitField(self, 0x000000FF, "DTG", "Dead-time generator setup")
        self.LOCK = BitField(self, 0x00000300, "LOCK", "Lock configuration")
        self.OSSI = BitField(self, 0x00000400, "OSSI", "Off-state selection for Idle mode")
        self.OSSR = BitField(self, 0x00000800, "OSSR", "Off-state selection for Run mode")
        self.BKE = BitField(self, 0x00001000, "BKE", "Break enable")
        self.BKP = BitField(self, 0x00002000, "BKP", "Break polarity")
        self.AOE = BitField(self, 0x00004000, "AOE", "Automatic output enable")
        self.MOE = BitField(self, 0x00008000, "MOE", "Main output enable")
        self.BKF = BitField(self, 0x000F0000, "BKF", "Break filter")
        self.BKDSRM = BitField(self, 0x04000000, "BKDSRM", "BKDSRM")
        self.BKBID = BitField(self, 0x10000000, "BKBID", "BKBID")

class SA_TIM16_DTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTR2", "timer Deadtime Register 2")
        self.DTGF = BitField(self, 0x000000FF, "DTGF", "Dead-time generator setup")
        self.DTAE = BitField(self, 0x00010000, "DTAE", "Deadtime Asymmetric Enable")
        self.DTPE = BitField(self, 0x00020000, "DTPE", "Deadtime Preload Enable")

class SA_TIM16_TISEL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TISEL", "TIM timer input selection register")
        self.TI1SEL = BitField(self, 0x0000000F, "TI1SEL", "TI1[0] to TI1[15] input selection")

class SA_TIM16_AF1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF1", "TIM alternate function option register 1")
        self.BKCMP4P = BitField(self, 0x00002000, "BKCMP4P", "BRK COMP4 input polarity")
        self.BKCMP3P = BitField(self, 0x00001000, "BKCMP3P", "BRK COMP3 input polarity")
        self.BKCMP2P = BitField(self, 0x00000800, "BKCMP2P", "BRK COMP2 input polarity")
        self.BKCMP1P = BitField(self, 0x00000400, "BKCMP1P", "BRK COMP1 input polarity")
        self.BKINP = BitField(self, 0x00000200, "BKINP", "BRK BKIN input polarity")
        self.BKCMP7E = BitField(self, 0x00000080, "BKCMP7E", "BRK COMP7 enable")
        self.BKCMP6E = BitField(self, 0x00000040, "BKCMP6E", "BRK COMP6 enable")
        self.BKCMP5E = BitField(self, 0x00000020, "BKCMP5E", "BRK COMP5 enable")
        self.BKCMP4E = BitField(self, 0x00000010, "BKCMP4E", "BRK COMP4 enable")
        self.BKCMP3E = BitField(self, 0x00000008, "BKCMP3E", "BRK COMP3 enable")
        self.BKCMP2E = BitField(self, 0x00000004, "BKCMP2E", "BRK COMP2 enable")
        self.BKCMP1E = BitField(self, 0x00000002, "BKCMP1E", "BRK COMP1 enable")
        self.BKINE = BitField(self, 0x00000001, "BKINE", "BRK BKIN input enable")
        self.BKCMPP = Subscriptor(self, "BKCMP{}P")
        self.BKCMPE = Subscriptor(self, "BKCMP{}E")

class SA_TIM16_AF2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF2", "TIM alternate function option register 2")
        self.OCRSEL = BitField(self, 0x00070000, "OCRSEL", "OCREF_CLR source selection")

class SA_TIM16_OR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OR1", "TIM option register 1")
        self.HSE32EN = BitField(self, 0x00000001, "HSE32EN", "HSE Divided by 32 enable")

class SA_TIM16_DCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DCR", "DMA control register")
        self.DBL = BitField(self, 0x00001F00, "DBL", "DMA burst length")
        self.DBA = BitField(self, 0x0000001F, "DBA", "DMA base address")

class SA_TIM16_DMAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DMAR", "DMA address for full transfer")
        self.DMAB = BitField(self, 0xFFFFFFFF, "DMAB", "DMA register for burst accesses")

class SA_TIM16_CCMR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1", "capture/compare mode register")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.IC1PSC = BitField(self, 0x0000000C, "IC1PSC", "Input capture 1 prescaler")

class SA_TIM16(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "General purpose timers")
        self.CR1 = SA_TIM16_CR1(self, 0x0)
        self.CR2 = SA_TIM16_CR2(self, 0x4)
        self.DIER = SA_TIM16_DIER(self, 0xC)
        self.SR = SA_TIM16_SR(self, 0x10)
        self.EGR = SA_TIM16_EGR(self, 0x14)
        self.CCMR1_Output = SA_TIM16_CCMR1_Output(self, 0x18)
        self.CCMR1_Input = SA_TIM16_CCMR1_Input(self, 0x18)
        self.CCER = SA_TIM16_CCER(self, 0x20)
        self.CNT = SA_TIM16_CNT(self, 0x24)
        self.PSC = SA_TIM16_PSC(self, 0x28)
        self.ARR = SA_TIM16_ARR(self, 0x2C)
        self.RCR = SA_TIM16_RCR(self, 0x30)
        self.CCR1 = SA_TIM16_CCR1(self, 0x34)
        self.BDTR = SA_TIM16_BDTR(self, 0x44)
        self.DTR2 = SA_TIM16_DTR2(self, 0x54)
        self.TISEL = SA_TIM16_TISEL(self, 0x5C)
        self.AF1 = SA_TIM16_AF1(self, 0x60)
        self.AF2 = SA_TIM16_AF2(self, 0x64)
        self.OR1 = SA_TIM16_OR1(self, 0x68)
        self.DCR = SA_TIM16_DCR(self, 0x3DC)
        self.DMAR = SA_TIM16_DMAR(self, 0x3E0)
        self.CCMR1 = SA_TIM16_CCMR1(self, 0x18)
        self.AF = Subscriptor(self, "AF{}")

TIM16 = SA_TIM16(0x40014400, "TIM16")
TIM17 = SA_TIM16(0x40014800, "TIM17")

class SA_TIM1_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "control register 1")
        self.DITHEN = BitField(self, 0x00001000, "DITHEN", "Dithering Enable")
        self.UIFREMAP = BitField(self, 0x00000800, "UIFREMAP", "UIF status bit remapping")
        self.CKD = BitField(self, 0x00000300, "CKD", "Clock division")
        self.ARPE = BitField(self, 0x00000080, "ARPE", "Auto-reload preload enable")
        self.CMS = BitField(self, 0x00000060, "CMS", "Center-aligned mode selection")
        self.DIR = BitField(self, 0x00000010, "DIR", "Direction")
        self.OPM = BitField(self, 0x00000008, "OPM", "One-pulse mode")
        self.URS = BitField(self, 0x00000004, "URS", "Update request source")
        self.UDIS = BitField(self, 0x00000002, "UDIS", "Update disable")
        self.CEN = BitField(self, 0x00000001, "CEN", "Counter enable")

class SA_TIM1_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "control register 2")
        self.MMS2 = BitField(self, 0x00F00000, "MMS2", "Master mode selection 2")
        self.OIS6 = BitField(self, 0x00040000, "OIS6", "Output Idle state 6 (OC6 output)")
        self.OIS5 = BitField(self, 0x00010000, "OIS5", "Output Idle state 5 (OC5 output)")
        self.OIS4N = BitField(self, 0x00008000, "OIS4N", "Output Idle state 4 (OC4N output)")
        self.OIS4 = BitField(self, 0x00004000, "OIS4", "Output Idle state 4")
        self.OIS3N = BitField(self, 0x00002000, "OIS3N", "Output Idle state 3")
        self.OIS3 = BitField(self, 0x00001000, "OIS3", "Output Idle state 3")
        self.OIS2N = BitField(self, 0x00000800, "OIS2N", "Output Idle state 2")
        self.OIS2 = BitField(self, 0x00000400, "OIS2", "Output Idle state 2")
        self.OIS1N = BitField(self, 0x00000200, "OIS1N", "Output Idle state 1")
        self.OIS1 = BitField(self, 0x00000100, "OIS1", "Output Idle state 1")
        self.TI1S = BitField(self, 0x00000080, "TI1S", "TI1 selection")
        self.MMS = BitField(self, 0x02000070, "MMS", "Master mode selection")
        self.CCDS = BitField(self, 0x00000008, "CCDS", "Capture/compare DMA selection")
        self.CCUS = BitField(self, 0x00000004, "CCUS", "Capture/compare control update selection")
        self.CCPC = BitField(self, 0x00000001, "CCPC", "Capture/compare preloaded control")
        self.OISN = Subscriptor(self, "OIS{}N")
        self.OIS = Subscriptor(self, "OIS{}")

class SA_TIM1_SMCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SMCR", "slave mode control register")
        self.SMSPS = BitField(self, 0x02000000, "SMSPS", "SMS Preload Source")
        self.SMSPE = BitField(self, 0x01000000, "SMSPE", "SMS Preload Enable")
        self.ETP = BitField(self, 0x00008000, "ETP", "External trigger polarity")
        self.ECE = BitField(self, 0x00004000, "ECE", "External clock enable")
        self.ETPS = BitField(self, 0x00003000, "ETPS", "External trigger prescaler")
        self.ETF = BitField(self, 0x00000F00, "ETF", "External trigger filter")
        self.MSM = BitField(self, 0x00000080, "MSM", "Master/Slave mode")
        self.TS = BitField(self, 0x00300070, "TS", "Trigger selection")
        self.OCCS = BitField(self, 0x00000008, "OCCS", "OCREF clear selection")
        self.SMS = BitField(self, 0x00010007, "SMS", "Slave mode selection")

class SA_TIM1_DIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DIER", "DMA/Interrupt enable register")
        self.TERRIE = BitField(self, 0x00800000, "TERRIE", "Transition Error interrupt enable")
        self.IERRIE = BitField(self, 0x00400000, "IERRIE", "Index Error interrupt enable")
        self.DIRIE = BitField(self, 0x00200000, "DIRIE", "Direction Change interrupt enable")
        self.IDXIE = BitField(self, 0x00100000, "IDXIE", "Index interrupt enable")
        self.TDE = BitField(self, 0x00004000, "TDE", "Trigger DMA request enable")
        self.COMDE = BitField(self, 0x00002000, "COMDE", "COM DMA request enable")
        self.CC4DE = BitField(self, 0x00001000, "CC4DE", "Capture/Compare 4 DMA request enable")
        self.CC3DE = BitField(self, 0x00000800, "CC3DE", "Capture/Compare 3 DMA request enable")
        self.CC2DE = BitField(self, 0x00000400, "CC2DE", "Capture/Compare 2 DMA request enable")
        self.CC1DE = BitField(self, 0x00000200, "CC1DE", "Capture/Compare 1 DMA request enable")
        self.UDE = BitField(self, 0x00000100, "UDE", "Update DMA request enable")
        self.TIE = BitField(self, 0x00000040, "TIE", "Trigger interrupt enable")
        self.CC4IE = BitField(self, 0x00000010, "CC4IE", "Capture/Compare 4 interrupt enable")
        self.CC3IE = BitField(self, 0x00000008, "CC3IE", "Capture/Compare 3 interrupt enable")
        self.CC2IE = BitField(self, 0x00000004, "CC2IE", "Capture/Compare 2 interrupt enable")
        self.CC1IE = BitField(self, 0x00000002, "CC1IE", "Capture/Compare 1 interrupt enable")
        self.UIE = BitField(self, 0x00000001, "UIE", "Update interrupt enable")
        self.BIE = BitField(self, 0x00000080, "BIE", "Break interrupt enable")
        self.COMIE = BitField(self, 0x00000020, "COMIE", "COM interrupt enable")
        self.CCDE = Subscriptor(self, "CC{}DE")
        self.CCIE = Subscriptor(self, "CC{}IE")

class SA_TIM1_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.TERRF = BitField(self, 0x00800000, "TERRF", "Transition Error interrupt flag")
        self.IERRF = BitField(self, 0x00400000, "IERRF", "Index Error interrupt flag")
        self.DIRF = BitField(self, 0x00200000, "DIRF", "Direction Change interrupt flag")
        self.IDXF = BitField(self, 0x00100000, "IDXF", "Index interrupt flag")
        self.CC6IF = BitField(self, 0x00020000, "CC6IF", "Compare 6 interrupt flag")
        self.CC5IF = BitField(self, 0x00010000, "CC5IF", "Compare 5 interrupt flag")
        self.SBIF = BitField(self, 0x00002000, "SBIF", "System Break interrupt flag")
        self.CC4OF = BitField(self, 0x00001000, "CC4OF", "Capture/Compare 4 overcapture flag")
        self.CC3OF = BitField(self, 0x00000800, "CC3OF", "Capture/Compare 3 overcapture flag")
        self.CC2OF = BitField(self, 0x00000400, "CC2OF", "Capture/compare 2 overcapture flag")
        self.CC1OF = BitField(self, 0x00000200, "CC1OF", "Capture/Compare 1 overcapture flag")
        self.B2IF = BitField(self, 0x00000100, "B2IF", "Break 2 interrupt flag")
        self.BIF = BitField(self, 0x00000080, "BIF", "Break interrupt flag")
        self.TIF = BitField(self, 0x00000040, "TIF", "Trigger interrupt flag")
        self.COMIF = BitField(self, 0x00000020, "COMIF", "COM interrupt flag")
        self.CC4IF = BitField(self, 0x00000010, "CC4IF", "Capture/Compare 4 interrupt flag")
        self.CC3IF = BitField(self, 0x00000008, "CC3IF", "Capture/Compare 3 interrupt flag")
        self.CC2IF = BitField(self, 0x00000004, "CC2IF", "Capture/Compare 2 interrupt flag")
        self.CC1IF = BitField(self, 0x00000002, "CC1IF", "Capture/compare 1 interrupt flag")
        self.UIF = BitField(self, 0x00000001, "UIF", "Update interrupt flag")
        self.CCIF = Subscriptor(self, "CC{}IF")
        self.CCOF = Subscriptor(self, "CC{}OF")

class SA_TIM1_EGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EGR", "event generation register")
        self.B2G = BitField(self, 0x00000100, "B2G", "Break 2 generation")
        self.BG = BitField(self, 0x00000080, "BG", "Break generation")
        self.TG = BitField(self, 0x00000040, "TG", "Trigger generation")
        self.COMG = BitField(self, 0x00000020, "COMG", "Capture/Compare control update generation")
        self.CC4G = BitField(self, 0x00000010, "CC4G", "Capture/compare 4 generation")
        self.CC3G = BitField(self, 0x00000008, "CC3G", "Capture/compare 3 generation")
        self.CC2G = BitField(self, 0x00000004, "CC2G", "Capture/compare 2 generation")
        self.CC1G = BitField(self, 0x00000002, "CC1G", "Capture/compare 1 generation")
        self.UG = BitField(self, 0x00000001, "UG", "Update generation")
        self.CCG = Subscriptor(self, "CC{}G")

class SA_TIM1_CCMR1_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Output", "capture/compare mode register 1 (output mode)")
        self.OC2CE = BitField(self, 0x00008000, "OC2CE", "Output Compare 2 clear enable")
        self.OC2M = BitField(self, 0x01007000, "OC2M", "Output Compare 2 mode")
        self.OC2PE = BitField(self, 0x00000800, "OC2PE", "Output Compare 2 preload enable")
        self.OC2FE = BitField(self, 0x00000400, "OC2FE", "Output Compare 2 fast enable")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "Capture/Compare 2 selection")
        self.OC1CE = BitField(self, 0x00000080, "OC1CE", "Output Compare 1 clear enable")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.CCS = Subscriptor(self, "CC{}S")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM1_CCMR1_Input(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Input", "capture/compare mode register 1 (input mode)")
        self.IC2F = BitField(self, 0x0000F000, "IC2F", "Input capture 2 filter")
        self.IC2PSC = BitField(self, 0x00000C00, "IC2PSC", "Input capture 2 prescaler")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "Capture/Compare 2 selection")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.ICPCS = BitField(self, 0x0000000C, "ICPCS", "Input capture 1 prescaler")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")

class SA_TIM1_CCMR2_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR2_Output", "capture/compare mode register 2 (output mode)")
        self.OC4CE = BitField(self, 0x00008000, "OC4CE", "Output compare 4 clear enable")
        self.OC4M = BitField(self, 0x01007000, "OC4M", "Output compare 4 mode")
        self.OC4PE = BitField(self, 0x00000800, "OC4PE", "Output compare 4 preload enable")
        self.OC4FE = BitField(self, 0x00000400, "OC4FE", "Output compare 4 fast enable")
        self.CC4S = BitField(self, 0x00000300, "CC4S", "Capture/Compare 4 selection")
        self.OC3CE = BitField(self, 0x00000080, "OC3CE", "Output compare 3 clear enable")
        self.OC3M = BitField(self, 0x00010070, "OC3M", "Output compare 3 mode")
        self.OC3PE = BitField(self, 0x00000008, "OC3PE", "Output compare 3 preload enable")
        self.OC3FE = BitField(self, 0x00000004, "OC3FE", "Output compare 3 fast enable")
        self.CC3S = BitField(self, 0x00000003, "CC3S", "Capture/Compare 3 selection")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.CCS = Subscriptor(self, "CC{}S")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM1_CCMR2_Input(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR2_Input", "capture/compare mode register 2 (input mode)")
        self.IC4F = BitField(self, 0x0000F000, "IC4F", "Input capture 4 filter")
        self.IC4PSC = BitField(self, 0x00000C00, "IC4PSC", "Input capture 4 prescaler")
        self.CC4S = BitField(self, 0x00000300, "CC4S", "Capture/Compare 4 selection")
        self.IC3F = BitField(self, 0x000000F0, "IC3F", "Input capture 3 filter")
        self.IC3PSC = BitField(self, 0x0000000C, "IC3PSC", "Input capture 3 prescaler")
        self.CC3S = BitField(self, 0x00000003, "CC3S", "Capture/compare 3 selection")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.ICPSC = Subscriptor(self, "IC{}PSC")

class SA_TIM1_CCER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCER", "capture/compare enable register")
        self.CC6P = BitField(self, 0x00200000, "CC6P", "Capture/Compare 6 output polarity")
        self.CC6E = BitField(self, 0x00100000, "CC6E", "Capture/Compare 6 output enable")
        self.CC5P = BitField(self, 0x00020000, "CC5P", "Capture/Compare 5 output polarity")
        self.CC5E = BitField(self, 0x00010000, "CC5E", "Capture/Compare 5 output enable")
        self.CC4NP = BitField(self, 0x00008000, "CC4NP", "Capture/Compare 4 complementary output polarity")
        self.CC4NE = BitField(self, 0x00004000, "CC4NE", "Capture/Compare 4 complementary output enable")
        self.CC4P = BitField(self, 0x00002000, "CC4P", "Capture/Compare 3 output Polarity")
        self.CC4E = BitField(self, 0x00001000, "CC4E", "Capture/Compare 4 output enable")
        self.CC3NP = BitField(self, 0x00000800, "CC3NP", "Capture/Compare 3 output Polarity")
        self.CC3NE = BitField(self, 0x00000400, "CC3NE", "Capture/Compare 3 complementary output enable")
        self.CC3P = BitField(self, 0x00000200, "CC3P", "Capture/Compare 3 output Polarity")
        self.CC3E = BitField(self, 0x00000100, "CC3E", "Capture/Compare 3 output enable")
        self.CC2NP = BitField(self, 0x00000080, "CC2NP", "Capture/Compare 2 output Polarity")
        self.CC2NE = BitField(self, 0x00000040, "CC2NE", "Capture/Compare 2 complementary output enable")
        self.CC2P = BitField(self, 0x00000020, "CC2P", "Capture/Compare 2 output Polarity")
        self.CC2E = BitField(self, 0x00000010, "CC2E", "Capture/Compare 2 output enable")
        self.CC1NP = BitField(self, 0x00000008, "CC1NP", "Capture/Compare 1 output Polarity")
        self.CC1NE = BitField(self, 0x00000004, "CC1NE", "Capture/Compare 1 complementary output enable")
        self.CC1P = BitField(self, 0x00000002, "CC1P", "Capture/Compare 1 output Polarity")
        self.CC1E = BitField(self, 0x00000001, "CC1E", "Capture/Compare 1 output enable")
        self.CCNP = Subscriptor(self, "CC{}NP")
        self.CCE = Subscriptor(self, "CC{}E")
        self.CCP = Subscriptor(self, "CC{}P")
        self.CCNE = Subscriptor(self, "CC{}NE")

class SA_TIM1_CNT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNT", "counter")
        self.UIFCPY = BitField(self, 0x80000000, "UIFCPY", "UIFCPY")
        self.CNT = BitField(self, 0x0000FFFF, "CNT", "counter value")

class SA_TIM1_PSC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PSC", "prescaler")
        self.PSC = BitField(self, 0x0000FFFF, "PSC", "Prescaler value")

class SA_TIM1_ARR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "ARR", "auto-reload register")
        self.ARR = BitField(self, 0x0000FFFF, "ARR", "Auto-reload value")

class SA_TIM1_RCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RCR", "repetition counter register")
        self.REP = BitField(self, 0x0000FFFF, "REP", "Repetition counter value")

class SA_TIM1_CCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR1", "capture/compare register 1")
        self.CCR1 = BitField(self, 0x0000FFFF, "CCR1", "Capture/Compare 1 value")

class SA_TIM1_CCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR2", "capture/compare register 2")
        self.CCR2 = BitField(self, 0x0000FFFF, "CCR2", "Capture/Compare 2 value")

class SA_TIM1_CCR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR3", "capture/compare register 3")
        self.CCR3 = BitField(self, 0x0000FFFF, "CCR3", "Capture/Compare value")

class SA_TIM1_CCR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR4", "capture/compare register 4")
        self.CCR4 = BitField(self, 0x0000FFFF, "CCR4", "Capture/Compare value")

class SA_TIM1_BDTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTR", "break and dead-time register")
        self.BK2ID = BitField(self, 0x20000000, "BK2ID", "BK2ID")
        self.BKBID = BitField(self, 0x10000000, "BKBID", "BKBID")
        self.BK2DSRM = BitField(self, 0x08000000, "BK2DSRM", "BK2DSRM")
        self.BKDSRM = BitField(self, 0x04000000, "BKDSRM", "BKDSRM")
        self.BK2P = BitField(self, 0x02000000, "BK2P", "Break 2 polarity")
        self.BK2E = BitField(self, 0x01000000, "BK2E", "Break 2 Enable")
        self.BK2F = BitField(self, 0x00F00000, "BK2F", "Break 2 filter")
        self.BKF = BitField(self, 0x000F0000, "BKF", "Break filter")
        self.MOE = BitField(self, 0x00008000, "MOE", "Main output enable")
        self.AOE = BitField(self, 0x00004000, "AOE", "Automatic output enable")
        self.BKP = BitField(self, 0x00002000, "BKP", "Break polarity")
        self.BKE = BitField(self, 0x00001000, "BKE", "Break enable")
        self.OSSR = BitField(self, 0x00000800, "OSSR", "Off-state selection for Run mode")
        self.OSSI = BitField(self, 0x00000400, "OSSI", "Off-state selection for Idle mode")
        self.LOCK = BitField(self, 0x00000300, "LOCK", "Lock configuration")
        self.DTG = BitField(self, 0x000000FF, "DTG", "Dead-time generator setup")

class SA_TIM1_CCR5(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR5", "capture/compare register 4")
        self.CCR5 = BitField(self, 0x0000FFFF, "CCR5", "Capture/Compare value")
        self.GC5C1 = BitField(self, 0x20000000, "GC5C1", "Group Channel 5 and Channel 1")
        self.GC5C2 = BitField(self, 0x40000000, "GC5C2", "Group Channel 5 and Channel 2")
        self.GC5C3 = BitField(self, 0x80000000, "GC5C3", "Group Channel 5 and Channel 3")
        self.GC5C = Subscriptor(self, "GC5C{}")

class SA_TIM1_CCR6(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR6", "capture/compare register 4")
        self.CCR6 = BitField(self, 0x0000FFFF, "CCR6", "Capture/Compare value")

class SA_TIM1_CCMR3_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR3_Output", "capture/compare mode register 2 (output mode)")
        self.OC6M_bit3 = BitField(self, 0x01000000, "OC6M_bit3", "Output Compare 6 mode bit 3")
        self.OC5M_bit3 = BitField(self, 0x00070000, "OC5M_bit3", "Output Compare 5 mode bit 3")
        self.OC6CE = BitField(self, 0x00008000, "OC6CE", "Output compare 6 clear enable")
        self.OC6M = BitField(self, 0x00007000, "OC6M", "Output compare 6 mode")
        self.OC6PE = BitField(self, 0x00000800, "OC6PE", "Output compare 6 preload enable")
        self.OC6FE = BitField(self, 0x00000400, "OC6FE", "Output compare 6 fast enable")
        self.OC5CE = BitField(self, 0x00000080, "OC5CE", "Output compare 5 clear enable")
        self.OC5M = BitField(self, 0x00000070, "OC5M", "Output compare 5 mode")
        self.OC5PE = BitField(self, 0x00000008, "OC5PE", "Output compare 5 preload enable")
        self.OC5FE = BitField(self, 0x00000004, "OC5FE", "Output compare 5 fast enable")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM1_DTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTR2", "timer Deadtime Register 2")
        self.DTPE = BitField(self, 0x00020000, "DTPE", "Deadtime Preload Enable")
        self.DTAE = BitField(self, 0x00010000, "DTAE", "Deadtime Asymmetric Enable")
        self.DTGF = BitField(self, 0x000000FF, "DTGF", "Dead-time falling edge generator setup")

class SA_TIM1_ECR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ECR", "DMA control register")
        self.IE = BitField(self, 0x00000001, "IE", "Index Enable")
        self.IDIR = BitField(self, 0x00000006, "IDIR", "Index Direction")
        self.IBLK = BitField(self, 0x00000018, "IBLK", "Index Blanking")
        self.FIDX = BitField(self, 0x00000020, "FIDX", "First Index")
        self.IPOS = BitField(self, 0x000000C0, "IPOS", "Index Positioning")
        self.PW = BitField(self, 0x00FF0000, "PW", "Pulse width")
        self.PWPRSC = BitField(self, 0x07000000, "PWPRSC", "Pulse Width prescaler")

class SA_TIM1_TISEL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TISEL", "TIM timer input selection register")
        self.TI1SEL = BitField(self, 0x0000000F, "TI1SEL", "TI1[0] to TI1[15] input selection")
        self.TI2SEL = BitField(self, 0x00000F00, "TI2SEL", "TI2[0] to TI2[15] input selection")
        self.TI3SEL = BitField(self, 0x000F0000, "TI3SEL", "TI3[0] to TI3[15] input selection")
        self.TI4SEL = BitField(self, 0x0F000000, "TI4SEL", "TI4[0] to TI4[15] input selection")
        self.TISEL = Subscriptor(self, "TI{}SEL")

class SA_TIM1_AF1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF1", "TIM alternate function option register 1")
        self.ETRSEL = BitField(self, 0x0003C000, "ETRSEL", "ETR source selection")
        self.BKCMP4P = BitField(self, 0x00002000, "BKCMP4P", "BRK COMP4 input polarity")
        self.BKCMP3P = BitField(self, 0x00001000, "BKCMP3P", "BRK COMP3 input polarity")
        self.BKCMP2P = BitField(self, 0x00000800, "BKCMP2P", "BRK COMP2 input polarity")
        self.BKCMP1P = BitField(self, 0x00000400, "BKCMP1P", "BRK COMP1 input polarity")
        self.BKINP = BitField(self, 0x00000200, "BKINP", "BRK BKIN input polarity")
        self.BKCMP7E = BitField(self, 0x00000080, "BKCMP7E", "BRK COMP7 enable")
        self.BKCMP6E = BitField(self, 0x00000040, "BKCMP6E", "BRK COMP6 enable")
        self.BKCMP5E = BitField(self, 0x00000020, "BKCMP5E", "BRK COMP5 enable")
        self.BKCMP4E = BitField(self, 0x00000010, "BKCMP4E", "BRK COMP4 enable")
        self.BKCMP3E = BitField(self, 0x00000008, "BKCMP3E", "BRK COMP3 enable")
        self.BKCMP2E = BitField(self, 0x00000004, "BKCMP2E", "BRK COMP2 enable")
        self.BKCMP1E = BitField(self, 0x00000002, "BKCMP1E", "BRK COMP1 enable")
        self.BKINE = BitField(self, 0x00000001, "BKINE", "BRK BKIN input enable")
        self.BKCMPP = Subscriptor(self, "BKCMP{}P")
        self.BKCMPE = Subscriptor(self, "BKCMP{}E")

class SA_TIM1_AF2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF2", "TIM alternate function option register 2")
        self.OCRSEL = BitField(self, 0x00070000, "OCRSEL", "OCREF_CLR source selection")
        self.BK2CMP4P = BitField(self, 0x00002000, "BK2CMP4P", "BRK2 COMP4 input polarity")
        self.BK2CMP3P = BitField(self, 0x00001000, "BK2CMP3P", "BRK2 COMP3 input polarity")
        self.BK2CMP2P = BitField(self, 0x00000800, "BK2CMP2P", "BRK2 COMP2 input polarity")
        self.BK2CMP1P = BitField(self, 0x00000400, "BK2CMP1P", "BRK2 COMP1 input polarity")
        self.BK2INP = BitField(self, 0x00000200, "BK2INP", "BRK2 BKIN input polarity")
        self.BK2CMP7E = BitField(self, 0x00000080, "BK2CMP7E", "BRK2 COMP7 enable")
        self.BK2CMP6E = BitField(self, 0x00000040, "BK2CMP6E", "BRK2 COMP6 enable")
        self.BK2CMP5E = BitField(self, 0x00000020, "BK2CMP5E", "BRK2 COMP5 enable")
        self.BK2CMP4E = BitField(self, 0x00000010, "BK2CMP4E", "BRK2 COMP4 enable")
        self.BK2CMP3E = BitField(self, 0x00000008, "BK2CMP3E", "BRK2 COMP3 enable")
        self.BK2CMP2E = BitField(self, 0x00000004, "BK2CMP2E", "BRK2 COMP2 enable")
        self.BK2CMP1E = BitField(self, 0x00000002, "BK2CMP1E", "BRK2 COMP1 enable")
        self.BKINE = BitField(self, 0x00000001, "BKINE", "BRK BKIN input enable")
        self.BK2CMPP = Subscriptor(self, "BK2CMP{}P")
        self.BK2CMPE = Subscriptor(self, "BK2CMP{}E")

class SA_TIM1_DCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DCR", "control register")
        self.DBL = BitField(self, 0x00001F00, "DBL", "DMA burst length")
        self.DBA = BitField(self, 0x0000001F, "DBA", "DMA base address")

class SA_TIM1_DMAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DMAR", "DMA address for full transfer")
        self.DMAB = BitField(self, 0xFFFFFFFF, "DMAB", "DMA register for burst accesses")

class SA_TIM1_CCMR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1", "capture/compare mode register 1")
        self.OC2CE = BitField(self, 0x00008000, "OC2CE", "Output Compare 2 clear enable")
        self.OC2M = BitField(self, 0x01007000, "OC2M", "Output Compare 2 mode")
        self.OC2PE = BitField(self, 0x00000800, "OC2PE", "Output Compare 2 preload enable")
        self.OC2FE = BitField(self, 0x00000400, "OC2FE", "Output Compare 2 fast enable")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "Capture/Compare 2 selection")
        self.OC1CE = BitField(self, 0x00000080, "OC1CE", "Output Compare 1 clear enable")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.IC2F = BitField(self, 0x0000F000, "IC2F", "Input capture 2 filter")
        self.IC2PSC = BitField(self, 0x00000C00, "IC2PSC", "Input capture 2 prescaler")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.ICPCS = BitField(self, 0x0000000C, "ICPCS", "Input capture 1 prescaler")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM1_CCMR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR2", "capture/compare mode register 2")
        self.OC4CE = BitField(self, 0x00008000, "OC4CE", "Output compare 4 clear enable")
        self.OC4M = BitField(self, 0x01007000, "OC4M", "Output compare 4 mode")
        self.OC4PE = BitField(self, 0x00000800, "OC4PE", "Output compare 4 preload enable")
        self.OC4FE = BitField(self, 0x00000400, "OC4FE", "Output compare 4 fast enable")
        self.CC4S = BitField(self, 0x00000300, "CC4S", "Capture/Compare 4 selection")
        self.OC3CE = BitField(self, 0x00000080, "OC3CE", "Output compare 3 clear enable")
        self.OC3M = BitField(self, 0x00010070, "OC3M", "Output compare 3 mode")
        self.OC3PE = BitField(self, 0x00000008, "OC3PE", "Output compare 3 preload enable")
        self.OC3FE = BitField(self, 0x00000004, "OC3FE", "Output compare 3 fast enable")
        self.CC3S = BitField(self, 0x00000003, "CC3S", "Capture/compare 3 selection")
        self.IC4F = BitField(self, 0x0000F000, "IC4F", "Input capture 4 filter")
        self.IC4PSC = BitField(self, 0x00000C00, "IC4PSC", "Input capture 4 prescaler")
        self.IC3F = BitField(self, 0x000000F0, "IC3F", "Input capture 3 filter")
        self.IC3PSC = BitField(self, 0x0000000C, "IC3PSC", "Input capture 3 prescaler")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.ICPSC = Subscriptor(self, "IC{}PSC")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM1_CCMR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR3", "capture/compare mode register 2")
        self.OC6M_bit3 = BitField(self, 0x01000000, "OC6M_bit3", "Output Compare 6 mode bit 3")
        self.OC5M_bit3 = BitField(self, 0x00070000, "OC5M_bit3", "Output Compare 5 mode bit 3")
        self.OC6CE = BitField(self, 0x00008000, "OC6CE", "Output compare 6 clear enable")
        self.OC6M = BitField(self, 0x00007000, "OC6M", "Output compare 6 mode")
        self.OC6PE = BitField(self, 0x00000800, "OC6PE", "Output compare 6 preload enable")
        self.OC6FE = BitField(self, 0x00000400, "OC6FE", "Output compare 6 fast enable")
        self.OC5CE = BitField(self, 0x00000080, "OC5CE", "Output compare 5 clear enable")
        self.OC5M = BitField(self, 0x00000070, "OC5M", "Output compare 5 mode")
        self.OC5PE = BitField(self, 0x00000008, "OC5PE", "Output compare 5 preload enable")
        self.OC5FE = BitField(self, 0x00000004, "OC5FE", "Output compare 5 fast enable")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Advanced-timers")
        self.CR1 = SA_TIM1_CR1(self, 0x0)
        self.CR2 = SA_TIM1_CR2(self, 0x4)
        self.SMCR = SA_TIM1_SMCR(self, 0x8)
        self.DIER = SA_TIM1_DIER(self, 0xC)
        self.SR = SA_TIM1_SR(self, 0x10)
        self.EGR = SA_TIM1_EGR(self, 0x14)
        self.CCMR1_Output = SA_TIM1_CCMR1_Output(self, 0x18)
        self.CCMR1_Input = SA_TIM1_CCMR1_Input(self, 0x18)
        self.CCMR2_Output = SA_TIM1_CCMR2_Output(self, 0x1C)
        self.CCMR2_Input = SA_TIM1_CCMR2_Input(self, 0x1C)
        self.CCER = SA_TIM1_CCER(self, 0x20)
        self.CNT = SA_TIM1_CNT(self, 0x24)
        self.PSC = SA_TIM1_PSC(self, 0x28)
        self.ARR = SA_TIM1_ARR(self, 0x2C)
        self.RCR = SA_TIM1_RCR(self, 0x30)
        self.CCR1 = SA_TIM1_CCR1(self, 0x34)
        self.CCR2 = SA_TIM1_CCR2(self, 0x38)
        self.CCR3 = SA_TIM1_CCR3(self, 0x3C)
        self.CCR4 = SA_TIM1_CCR4(self, 0x40)
        self.BDTR = SA_TIM1_BDTR(self, 0x44)
        self.CCR5 = SA_TIM1_CCR5(self, 0x48)
        self.CCR6 = SA_TIM1_CCR6(self, 0x4C)
        self.CCMR3_Output = SA_TIM1_CCMR3_Output(self, 0x50)
        self.DTR2 = SA_TIM1_DTR2(self, 0x54)
        self.ECR = SA_TIM1_ECR(self, 0x58)
        self.TISEL = SA_TIM1_TISEL(self, 0x5C)
        self.AF1 = SA_TIM1_AF1(self, 0x60)
        self.AF2 = SA_TIM1_AF2(self, 0x64)
        self.DCR = SA_TIM1_DCR(self, 0x3DC)
        self.DMAR = SA_TIM1_DMAR(self, 0x3E0)
        self.CCMR1 = SA_TIM1_CCMR1(self, 0x18)
        self.CCMR2 = SA_TIM1_CCMR2(self, 0x1C)
        self.CCMR3 = SA_TIM1_CCMR3(self, 0x50)
        self.AF = Subscriptor(self, "AF{}")
        self.CCMR_Output = Subscriptor(self, "CCMR{}_Output")
        self.CCMR_Input = Subscriptor(self, "CCMR{}_Input")
        self.CCMR = Subscriptor(self, "CCMR{}")
        self.CCR = Subscriptor(self, "CCR{}")

TIM1 = SA_TIM1(0x40012C00, "TIM1")
TIM20 = SA_TIM1(0x40015000, "TIM20")
TIM8 = SA_TIM1(0x40013400, "TIM8")

class SA_TIM2_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "control register 1")
        self.DITHEN = BitField(self, 0x00001000, "DITHEN", "Dithering Enable")
        self.UIFREMAP = BitField(self, 0x00000800, "UIFREMAP", "UIF status bit remapping")
        self.CKD = BitField(self, 0x00000300, "CKD", "Clock division")
        self.ARPE = BitField(self, 0x00000080, "ARPE", "Auto-reload preload enable")
        self.CMS = BitField(self, 0x00000060, "CMS", "Center-aligned mode selection")
        self.DIR = BitField(self, 0x00000010, "DIR", "Direction")
        self.OPM = BitField(self, 0x00000008, "OPM", "One-pulse mode")
        self.URS = BitField(self, 0x00000004, "URS", "Update request source")
        self.UDIS = BitField(self, 0x00000002, "UDIS", "Update disable")
        self.CEN = BitField(self, 0x00000001, "CEN", "Counter enable")

class SA_TIM2_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "control register 2")
        self.MMS2 = BitField(self, 0x00F00000, "MMS2", "Master mode selection 2")
        self.OIS6 = BitField(self, 0x00040000, "OIS6", "Output Idle state 6 (OC6 output)")
        self.OIS5 = BitField(self, 0x00010000, "OIS5", "Output Idle state 5 (OC5 output)")
        self.OIS4N = BitField(self, 0x00008000, "OIS4N", "Output Idle state 4 (OC4N output)")
        self.OIS4 = BitField(self, 0x00004000, "OIS4", "Output Idle state 4")
        self.OIS3N = BitField(self, 0x00002000, "OIS3N", "Output Idle state 3")
        self.OIS3 = BitField(self, 0x00001000, "OIS3", "Output Idle state 3")
        self.OIS2N = BitField(self, 0x00000800, "OIS2N", "Output Idle state 2")
        self.OIS2 = BitField(self, 0x00000400, "OIS2", "Output Idle state 2")
        self.OIS1N = BitField(self, 0x00000200, "OIS1N", "Output Idle state 1")
        self.OIS1 = BitField(self, 0x00000100, "OIS1", "Output Idle state 1")
        self.TI1S = BitField(self, 0x00000080, "TI1S", "TI1 selection")
        self.MMS = BitField(self, 0x02000070, "MMS", "Master mode selection")
        self.CCDS = BitField(self, 0x00000008, "CCDS", "Capture/compare DMA selection")
        self.CCUS = BitField(self, 0x00000004, "CCUS", "Capture/compare control update selection")
        self.CCPC = BitField(self, 0x00000001, "CCPC", "Capture/compare preloaded control")
        self.OISN = Subscriptor(self, "OIS{}N")
        self.OIS = Subscriptor(self, "OIS{}")

class SA_TIM2_SMCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SMCR", "slave mode control register")
        self.SMSPS = BitField(self, 0x02000000, "SMSPS", "SMS Preload Source")
        self.SMSPE = BitField(self, 0x01000000, "SMSPE", "SMS Preload Enable")
        self.ETP = BitField(self, 0x00008000, "ETP", "External trigger polarity")
        self.ECE = BitField(self, 0x00004000, "ECE", "External clock enable")
        self.ETPS = BitField(self, 0x00003000, "ETPS", "External trigger prescaler")
        self.ETF = BitField(self, 0x00000F00, "ETF", "External trigger filter")
        self.MSM = BitField(self, 0x00000080, "MSM", "Master/Slave mode")
        self.TS = BitField(self, 0x00300070, "TS", "Trigger selection")
        self.OCCS = BitField(self, 0x00000008, "OCCS", "OCREF clear selection")
        self.SMS = BitField(self, 0x00010007, "SMS", "Slave mode selection")

class SA_TIM2_DIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DIER", "DMA/Interrupt enable register")
        self.TERRIE = BitField(self, 0x00800000, "TERRIE", "Transition Error interrupt enable")
        self.IERRIE = BitField(self, 0x00400000, "IERRIE", "Index Error interrupt enable")
        self.DIRIE = BitField(self, 0x00200000, "DIRIE", "Direction Change interrupt enable")
        self.IDXIE = BitField(self, 0x00100000, "IDXIE", "Index interrupt enable")
        self.TDE = BitField(self, 0x00004000, "TDE", "Trigger DMA request enable")
        self.COMDE = BitField(self, 0x00002000, "COMDE", "COM DMA request enable")
        self.CC4DE = BitField(self, 0x00001000, "CC4DE", "Capture/Compare 4 DMA request enable")
        self.CC3DE = BitField(self, 0x00000800, "CC3DE", "Capture/Compare 3 DMA request enable")
        self.CC2DE = BitField(self, 0x00000400, "CC2DE", "Capture/Compare 2 DMA request enable")
        self.CC1DE = BitField(self, 0x00000200, "CC1DE", "Capture/Compare 1 DMA request enable")
        self.UDE = BitField(self, 0x00000100, "UDE", "Update DMA request enable")
        self.TIE = BitField(self, 0x00000040, "TIE", "Trigger interrupt enable")
        self.CC4IE = BitField(self, 0x00000010, "CC4IE", "Capture/Compare 4 interrupt enable")
        self.CC3IE = BitField(self, 0x00000008, "CC3IE", "Capture/Compare 3 interrupt enable")
        self.CC2IE = BitField(self, 0x00000004, "CC2IE", "Capture/Compare 2 interrupt enable")
        self.CC1IE = BitField(self, 0x00000002, "CC1IE", "Capture/Compare 1 interrupt enable")
        self.UIE = BitField(self, 0x00000001, "UIE", "Update interrupt enable")
        self.BIE = BitField(self, 0x00000080, "BIE", "Break interrupt enable")
        self.COMIE = BitField(self, 0x00000020, "COMIE", "COM interrupt enable")
        self.CCDE = Subscriptor(self, "CC{}DE")
        self.CCIE = Subscriptor(self, "CC{}IE")

class SA_TIM2_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.TERRF = BitField(self, 0x00800000, "TERRF", "Transition Error interrupt flag")
        self.IERRF = BitField(self, 0x00400000, "IERRF", "Index Error interrupt flag")
        self.DIRF = BitField(self, 0x00200000, "DIRF", "Direction Change interrupt flag")
        self.IDXF = BitField(self, 0x00100000, "IDXF", "Index interrupt flag")
        self.CC6IF = BitField(self, 0x00020000, "CC6IF", "Compare 6 interrupt flag")
        self.CC5IF = BitField(self, 0x00010000, "CC5IF", "Compare 5 interrupt flag")
        self.SBIF = BitField(self, 0x00002000, "SBIF", "System Break interrupt flag")
        self.CC4OF = BitField(self, 0x00001000, "CC4OF", "Capture/Compare 4 overcapture flag")
        self.CC3OF = BitField(self, 0x00000800, "CC3OF", "Capture/Compare 3 overcapture flag")
        self.CC2OF = BitField(self, 0x00000400, "CC2OF", "Capture/compare 2 overcapture flag")
        self.CC1OF = BitField(self, 0x00000200, "CC1OF", "Capture/Compare 1 overcapture flag")
        self.B2IF = BitField(self, 0x00000100, "B2IF", "Break 2 interrupt flag")
        self.BIF = BitField(self, 0x00000080, "BIF", "Break interrupt flag")
        self.TIF = BitField(self, 0x00000040, "TIF", "Trigger interrupt flag")
        self.COMIF = BitField(self, 0x00000020, "COMIF", "COM interrupt flag")
        self.CC4IF = BitField(self, 0x00000010, "CC4IF", "Capture/Compare 4 interrupt flag")
        self.CC3IF = BitField(self, 0x00000008, "CC3IF", "Capture/Compare 3 interrupt flag")
        self.CC2IF = BitField(self, 0x00000004, "CC2IF", "Capture/Compare 2 interrupt flag")
        self.CC1IF = BitField(self, 0x00000002, "CC1IF", "Capture/compare 1 interrupt flag")
        self.UIF = BitField(self, 0x00000001, "UIF", "Update interrupt flag")
        self.CCIF = Subscriptor(self, "CC{}IF")
        self.CCOF = Subscriptor(self, "CC{}OF")

class SA_TIM2_EGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EGR", "event generation register")
        self.B2G = BitField(self, 0x00000100, "B2G", "Break 2 generation")
        self.BG = BitField(self, 0x00000080, "BG", "Break generation")
        self.TG = BitField(self, 0x00000040, "TG", "Trigger generation")
        self.COMG = BitField(self, 0x00000020, "COMG", "Capture/Compare control update generation")
        self.CC4G = BitField(self, 0x00000010, "CC4G", "Capture/compare 4 generation")
        self.CC3G = BitField(self, 0x00000008, "CC3G", "Capture/compare 3 generation")
        self.CC2G = BitField(self, 0x00000004, "CC2G", "Capture/compare 2 generation")
        self.CC1G = BitField(self, 0x00000002, "CC1G", "Capture/compare 1 generation")
        self.UG = BitField(self, 0x00000001, "UG", "Update generation")
        self.CCG = Subscriptor(self, "CC{}G")

class SA_TIM2_CCMR1_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Output", "capture/compare mode register 1 (output mode)")
        self.OC2CE = BitField(self, 0x00008000, "OC2CE", "Output Compare 2 clear enable")
        self.OC2M = BitField(self, 0x01007000, "OC2M", "Output Compare 2 mode")
        self.OC2PE = BitField(self, 0x00000800, "OC2PE", "Output Compare 2 preload enable")
        self.OC2FE = BitField(self, 0x00000400, "OC2FE", "Output Compare 2 fast enable")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "Capture/Compare 2 selection")
        self.OC1CE = BitField(self, 0x00000080, "OC1CE", "Output Compare 1 clear enable")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.CCS = Subscriptor(self, "CC{}S")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM2_CCMR1_Input(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1_Input", "capture/compare mode register 1 (input mode)")
        self.IC2F = BitField(self, 0x0000F000, "IC2F", "Input capture 2 filter")
        self.IC2PSC = BitField(self, 0x00000C00, "IC2PSC", "Input capture 2 prescaler")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "Capture/Compare 2 selection")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.ICPCS = BitField(self, 0x0000000C, "ICPCS", "Input capture 1 prescaler")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")

class SA_TIM2_CCMR2_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR2_Output", "capture/compare mode register 2 (output mode)")
        self.OC4CE = BitField(self, 0x00008000, "OC4CE", "Output compare 4 clear enable")
        self.OC4M = BitField(self, 0x01007000, "OC4M", "Output compare 4 mode")
        self.OC4PE = BitField(self, 0x00000800, "OC4PE", "Output compare 4 preload enable")
        self.OC4FE = BitField(self, 0x00000400, "OC4FE", "Output compare 4 fast enable")
        self.CC4S = BitField(self, 0x00000300, "CC4S", "Capture/Compare 4 selection")
        self.OC3CE = BitField(self, 0x00000080, "OC3CE", "Output compare 3 clear enable")
        self.OC3M = BitField(self, 0x00010070, "OC3M", "Output compare 3 mode")
        self.OC3PE = BitField(self, 0x00000008, "OC3PE", "Output compare 3 preload enable")
        self.OC3FE = BitField(self, 0x00000004, "OC3FE", "Output compare 3 fast enable")
        self.CC3S = BitField(self, 0x00000003, "CC3S", "Capture/Compare 3 selection")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.CCS = Subscriptor(self, "CC{}S")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM2_CCMR2_Input(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR2_Input", "capture/compare mode register 2 (input mode)")
        self.IC4F = BitField(self, 0x0000F000, "IC4F", "Input capture 4 filter")
        self.IC4PSC = BitField(self, 0x00000C00, "IC4PSC", "Input capture 4 prescaler")
        self.CC4S = BitField(self, 0x00000300, "CC4S", "Capture/Compare 4 selection")
        self.IC3F = BitField(self, 0x000000F0, "IC3F", "Input capture 3 filter")
        self.IC3PSC = BitField(self, 0x0000000C, "IC3PSC", "Input capture 3 prescaler")
        self.CC3S = BitField(self, 0x00000003, "CC3S", "Capture/compare 3 selection")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.ICPSC = Subscriptor(self, "IC{}PSC")

class SA_TIM2_CCER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCER", "capture/compare enable register")
        self.CC6P = BitField(self, 0x00200000, "CC6P", "Capture/Compare 6 output polarity")
        self.CC6E = BitField(self, 0x00100000, "CC6E", "Capture/Compare 6 output enable")
        self.CC5P = BitField(self, 0x00020000, "CC5P", "Capture/Compare 5 output polarity")
        self.CC5E = BitField(self, 0x00010000, "CC5E", "Capture/Compare 5 output enable")
        self.CC4NP = BitField(self, 0x00008000, "CC4NP", "Capture/Compare 4 complementary output polarity")
        self.CC4NE = BitField(self, 0x00004000, "CC4NE", "Capture/Compare 4 complementary output enable")
        self.CC4P = BitField(self, 0x00002000, "CC4P", "Capture/Compare 3 output Polarity")
        self.CC4E = BitField(self, 0x00001000, "CC4E", "Capture/Compare 4 output enable")
        self.CC3NP = BitField(self, 0x00000800, "CC3NP", "Capture/Compare 3 output Polarity")
        self.CC3NE = BitField(self, 0x00000400, "CC3NE", "Capture/Compare 3 complementary output enable")
        self.CC3P = BitField(self, 0x00000200, "CC3P", "Capture/Compare 3 output Polarity")
        self.CC3E = BitField(self, 0x00000100, "CC3E", "Capture/Compare 3 output enable")
        self.CC2NP = BitField(self, 0x00000080, "CC2NP", "Capture/Compare 2 output Polarity")
        self.CC2NE = BitField(self, 0x00000040, "CC2NE", "Capture/Compare 2 complementary output enable")
        self.CC2P = BitField(self, 0x00000020, "CC2P", "Capture/Compare 2 output Polarity")
        self.CC2E = BitField(self, 0x00000010, "CC2E", "Capture/Compare 2 output enable")
        self.CC1NP = BitField(self, 0x00000008, "CC1NP", "Capture/Compare 1 output Polarity")
        self.CC1NE = BitField(self, 0x00000004, "CC1NE", "Capture/Compare 1 complementary output enable")
        self.CC1P = BitField(self, 0x00000002, "CC1P", "Capture/Compare 1 output Polarity")
        self.CC1E = BitField(self, 0x00000001, "CC1E", "Capture/Compare 1 output enable")
        self.CCNP = Subscriptor(self, "CC{}NP")
        self.CCE = Subscriptor(self, "CC{}E")
        self.CCP = Subscriptor(self, "CC{}P")
        self.CCNE = Subscriptor(self, "CC{}NE")

class SA_TIM2_CNT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNT", "counter")
        self.UIFCPY = BitField(self, 0x80000000, "UIFCPY", "UIFCPY")
        self.CNT = BitField(self, 0x0000FFFF, "CNT", "counter value")

class SA_TIM2_PSC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PSC", "prescaler")
        self.PSC = BitField(self, 0x0000FFFF, "PSC", "Prescaler value")

class SA_TIM2_ARR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "ARR", "auto-reload register")
        self.ARR = BitField(self, 0x0000FFFF, "ARR", "Auto-reload value")

class SA_TIM2_RCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RCR", "repetition counter register")
        self.REP = BitField(self, 0x0000FFFF, "REP", "Repetition counter value")

class SA_TIM2_CCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR1", "capture/compare register 1")
        self.CCR1 = BitField(self, 0x0000FFFF, "CCR1", "Capture/Compare 1 value")

class SA_TIM2_CCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR2", "capture/compare register 2")
        self.CCR2 = BitField(self, 0x0000FFFF, "CCR2", "Capture/Compare 2 value")

class SA_TIM2_CCR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR3", "capture/compare register 3")
        self.CCR3 = BitField(self, 0x0000FFFF, "CCR3", "Capture/Compare value")

class SA_TIM2_CCR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR4", "capture/compare register 4")
        self.CCR4 = BitField(self, 0x0000FFFF, "CCR4", "Capture/Compare value")

class SA_TIM2_BDTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTR", "break and dead-time register")
        self.BK2ID = BitField(self, 0x20000000, "BK2ID", "BK2ID")
        self.BKBID = BitField(self, 0x10000000, "BKBID", "BKBID")
        self.BK2DSRM = BitField(self, 0x08000000, "BK2DSRM", "BK2DSRM")
        self.BKDSRM = BitField(self, 0x04000000, "BKDSRM", "BKDSRM")
        self.BK2P = BitField(self, 0x02000000, "BK2P", "Break 2 polarity")
        self.BK2E = BitField(self, 0x01000000, "BK2E", "Break 2 Enable")
        self.BK2F = BitField(self, 0x00F00000, "BK2F", "Break 2 filter")
        self.BKF = BitField(self, 0x000F0000, "BKF", "Break filter")
        self.MOE = BitField(self, 0x00008000, "MOE", "Main output enable")
        self.AOE = BitField(self, 0x00004000, "AOE", "Automatic output enable")
        self.BKP = BitField(self, 0x00002000, "BKP", "Break polarity")
        self.BKE = BitField(self, 0x00001000, "BKE", "Break enable")
        self.OSSR = BitField(self, 0x00000800, "OSSR", "Off-state selection for Run mode")
        self.OSSI = BitField(self, 0x00000400, "OSSI", "Off-state selection for Idle mode")
        self.LOCK = BitField(self, 0x00000300, "LOCK", "Lock configuration")
        self.DTG = BitField(self, 0x000000FF, "DTG", "Dead-time generator setup")

class SA_TIM2_CCR5(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR5", "capture/compare register 4")
        self.CCR5 = BitField(self, 0x0000FFFF, "CCR5", "Capture/Compare value")
        self.GC5C1 = BitField(self, 0x20000000, "GC5C1", "Group Channel 5 and Channel 1")
        self.GC5C2 = BitField(self, 0x40000000, "GC5C2", "Group Channel 5 and Channel 2")
        self.GC5C3 = BitField(self, 0x80000000, "GC5C3", "Group Channel 5 and Channel 3")
        self.GC5C = Subscriptor(self, "GC5C{}")

class SA_TIM2_CCR6(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR6", "capture/compare register 4")
        self.CCR6 = BitField(self, 0x0000FFFF, "CCR6", "Capture/Compare value")

class SA_TIM2_CCMR3_Output(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR3_Output", "capture/compare mode register 2 (output mode)")
        self.OC6M_bit3 = BitField(self, 0x01000000, "OC6M_bit3", "Output Compare 6 mode bit 3")
        self.OC5M_bit3 = BitField(self, 0x00070000, "OC5M_bit3", "Output Compare 5 mode bit 3")
        self.OC6CE = BitField(self, 0x00008000, "OC6CE", "Output compare 6 clear enable")
        self.OC6M = BitField(self, 0x00007000, "OC6M", "Output compare 6 mode")
        self.OC6PE = BitField(self, 0x00000800, "OC6PE", "Output compare 6 preload enable")
        self.OC6FE = BitField(self, 0x00000400, "OC6FE", "Output compare 6 fast enable")
        self.OC5CE = BitField(self, 0x00000080, "OC5CE", "Output compare 5 clear enable")
        self.OC5M = BitField(self, 0x00000070, "OC5M", "Output compare 5 mode")
        self.OC5PE = BitField(self, 0x00000008, "OC5PE", "Output compare 5 preload enable")
        self.OC5FE = BitField(self, 0x00000004, "OC5FE", "Output compare 5 fast enable")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM2_DTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTR2", "timer Deadtime Register 2")
        self.DTPE = BitField(self, 0x00020000, "DTPE", "Deadtime Preload Enable")
        self.DTAE = BitField(self, 0x00010000, "DTAE", "Deadtime Asymmetric Enable")
        self.DTGF = BitField(self, 0x000000FF, "DTGF", "Dead-time falling edge generator setup")

class SA_TIM2_ECR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ECR", "DMA control register")
        self.IE = BitField(self, 0x00000001, "IE", "Index Enable")
        self.IDIR = BitField(self, 0x00000006, "IDIR", "Index Direction")
        self.IBLK = BitField(self, 0x00000018, "IBLK", "Index Blanking")
        self.FIDX = BitField(self, 0x00000020, "FIDX", "First Index")
        self.IPOS = BitField(self, 0x000000C0, "IPOS", "Index Positioning")
        self.PW = BitField(self, 0x00FF0000, "PW", "Pulse width")
        self.PWPRSC = BitField(self, 0x07000000, "PWPRSC", "Pulse Width prescaler")

class SA_TIM2_TISEL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TISEL", "TIM timer input selection register")
        self.TI1SEL = BitField(self, 0x0000000F, "TI1SEL", "TI1[0] to TI1[15] input selection")
        self.TI2SEL = BitField(self, 0x00000F00, "TI2SEL", "TI2[0] to TI2[15] input selection")
        self.TI3SEL = BitField(self, 0x000F0000, "TI3SEL", "TI3[0] to TI3[15] input selection")
        self.TI4SEL = BitField(self, 0x0F000000, "TI4SEL", "TI4[0] to TI4[15] input selection")
        self.TISEL = Subscriptor(self, "TI{}SEL")

class SA_TIM2_AF1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF1", "TIM alternate function option register 1")
        self.ETRSEL = BitField(self, 0x0003C000, "ETRSEL", "ETR source selection")
        self.BKCMP4P = BitField(self, 0x00002000, "BKCMP4P", "BRK COMP4 input polarity")
        self.BKCMP3P = BitField(self, 0x00001000, "BKCMP3P", "BRK COMP3 input polarity")
        self.BKCMP2P = BitField(self, 0x00000800, "BKCMP2P", "BRK COMP2 input polarity")
        self.BKCMP1P = BitField(self, 0x00000400, "BKCMP1P", "BRK COMP1 input polarity")
        self.BKINP = BitField(self, 0x00000200, "BKINP", "BRK BKIN input polarity")
        self.BKCMP7E = BitField(self, 0x00000080, "BKCMP7E", "BRK COMP7 enable")
        self.BKCMP6E = BitField(self, 0x00000040, "BKCMP6E", "BRK COMP6 enable")
        self.BKCMP5E = BitField(self, 0x00000020, "BKCMP5E", "BRK COMP5 enable")
        self.BKCMP4E = BitField(self, 0x00000010, "BKCMP4E", "BRK COMP4 enable")
        self.BKCMP3E = BitField(self, 0x00000008, "BKCMP3E", "BRK COMP3 enable")
        self.BKCMP2E = BitField(self, 0x00000004, "BKCMP2E", "BRK COMP2 enable")
        self.BKCMP1E = BitField(self, 0x00000002, "BKCMP1E", "BRK COMP1 enable")
        self.BKINE = BitField(self, 0x00000001, "BKINE", "BRK BKIN input enable")
        self.BKCMPP = Subscriptor(self, "BKCMP{}P")
        self.BKCMPE = Subscriptor(self, "BKCMP{}E")

class SA_TIM2_AF2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AF2", "TIM alternate function option register 2")
        self.OCRSEL = BitField(self, 0x00070000, "OCRSEL", "OCREF_CLR source selection")
        self.BK2CMP4P = BitField(self, 0x00002000, "BK2CMP4P", "BRK2 COMP4 input polarity")
        self.BK2CMP3P = BitField(self, 0x00001000, "BK2CMP3P", "BRK2 COMP3 input polarity")
        self.BK2CMP2P = BitField(self, 0x00000800, "BK2CMP2P", "BRK2 COMP2 input polarity")
        self.BK2CMP1P = BitField(self, 0x00000400, "BK2CMP1P", "BRK2 COMP1 input polarity")
        self.BK2INP = BitField(self, 0x00000200, "BK2INP", "BRK2 BKIN input polarity")
        self.BK2CMP7E = BitField(self, 0x00000080, "BK2CMP7E", "BRK2 COMP7 enable")
        self.BK2CMP6E = BitField(self, 0x00000040, "BK2CMP6E", "BRK2 COMP6 enable")
        self.BK2CMP5E = BitField(self, 0x00000020, "BK2CMP5E", "BRK2 COMP5 enable")
        self.BK2CMP4E = BitField(self, 0x00000010, "BK2CMP4E", "BRK2 COMP4 enable")
        self.BK2CMP3E = BitField(self, 0x00000008, "BK2CMP3E", "BRK2 COMP3 enable")
        self.BK2CMP2E = BitField(self, 0x00000004, "BK2CMP2E", "BRK2 COMP2 enable")
        self.BK2CMP1E = BitField(self, 0x00000002, "BK2CMP1E", "BRK2 COMP1 enable")
        self.BKINE = BitField(self, 0x00000001, "BKINE", "BRK BKIN input enable")
        self.BK2CMPP = Subscriptor(self, "BK2CMP{}P")
        self.BK2CMPE = Subscriptor(self, "BK2CMP{}E")

class SA_TIM2_DCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DCR", "control register")
        self.DBL = BitField(self, 0x00001F00, "DBL", "DMA burst length")
        self.DBA = BitField(self, 0x0000001F, "DBA", "DMA base address")

class SA_TIM2_DMAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DMAR", "DMA address for full transfer")
        self.DMAB = BitField(self, 0xFFFFFFFF, "DMAB", "DMA register for burst accesses")

class SA_TIM2_CCMR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR1", "capture/compare mode register 1")
        self.OC2CE = BitField(self, 0x00008000, "OC2CE", "Output Compare 2 clear enable")
        self.OC2M = BitField(self, 0x01007000, "OC2M", "Output Compare 2 mode")
        self.OC2PE = BitField(self, 0x00000800, "OC2PE", "Output Compare 2 preload enable")
        self.OC2FE = BitField(self, 0x00000400, "OC2FE", "Output Compare 2 fast enable")
        self.CC2S = BitField(self, 0x00000300, "CC2S", "Capture/Compare 2 selection")
        self.OC1CE = BitField(self, 0x00000080, "OC1CE", "Output Compare 1 clear enable")
        self.OC1M = BitField(self, 0x00010070, "OC1M", "Output Compare 1 mode")
        self.OC1PE = BitField(self, 0x00000008, "OC1PE", "Output Compare 1 preload enable")
        self.OC1FE = BitField(self, 0x00000004, "OC1FE", "Output Compare 1 fast enable")
        self.CC1S = BitField(self, 0x00000003, "CC1S", "Capture/Compare 1 selection")
        self.IC2F = BitField(self, 0x0000F000, "IC2F", "Input capture 2 filter")
        self.IC2PSC = BitField(self, 0x00000C00, "IC2PSC", "Input capture 2 prescaler")
        self.IC1F = BitField(self, 0x000000F0, "IC1F", "Input capture 1 filter")
        self.ICPCS = BitField(self, 0x0000000C, "ICPCS", "Input capture 1 prescaler")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM2_CCMR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR2", "capture/compare mode register 2")
        self.OC4CE = BitField(self, 0x00008000, "OC4CE", "Output compare 4 clear enable")
        self.OC4M = BitField(self, 0x01007000, "OC4M", "Output compare 4 mode")
        self.OC4PE = BitField(self, 0x00000800, "OC4PE", "Output compare 4 preload enable")
        self.OC4FE = BitField(self, 0x00000400, "OC4FE", "Output compare 4 fast enable")
        self.CC4S = BitField(self, 0x00000300, "CC4S", "Capture/Compare 4 selection")
        self.OC3CE = BitField(self, 0x00000080, "OC3CE", "Output compare 3 clear enable")
        self.OC3M = BitField(self, 0x00010070, "OC3M", "Output compare 3 mode")
        self.OC3PE = BitField(self, 0x00000008, "OC3PE", "Output compare 3 preload enable")
        self.OC3FE = BitField(self, 0x00000004, "OC3FE", "Output compare 3 fast enable")
        self.CC3S = BitField(self, 0x00000003, "CC3S", "Capture/compare 3 selection")
        self.IC4F = BitField(self, 0x0000F000, "IC4F", "Input capture 4 filter")
        self.IC4PSC = BitField(self, 0x00000C00, "IC4PSC", "Input capture 4 prescaler")
        self.IC3F = BitField(self, 0x000000F0, "IC3F", "Input capture 3 filter")
        self.IC3PSC = BitField(self, 0x0000000C, "IC3PSC", "Input capture 3 prescaler")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.ICPSC = Subscriptor(self, "IC{}PSC")
        self.CCS = Subscriptor(self, "CC{}S")
        self.ICF = Subscriptor(self, "IC{}F")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM2_CCMR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCMR3", "capture/compare mode register 2")
        self.OC6M_bit3 = BitField(self, 0x01000000, "OC6M_bit3", "Output Compare 6 mode bit 3")
        self.OC5M_bit3 = BitField(self, 0x00070000, "OC5M_bit3", "Output Compare 5 mode bit 3")
        self.OC6CE = BitField(self, 0x00008000, "OC6CE", "Output compare 6 clear enable")
        self.OC6M = BitField(self, 0x00007000, "OC6M", "Output compare 6 mode")
        self.OC6PE = BitField(self, 0x00000800, "OC6PE", "Output compare 6 preload enable")
        self.OC6FE = BitField(self, 0x00000400, "OC6FE", "Output compare 6 fast enable")
        self.OC5CE = BitField(self, 0x00000080, "OC5CE", "Output compare 5 clear enable")
        self.OC5M = BitField(self, 0x00000070, "OC5M", "Output compare 5 mode")
        self.OC5PE = BitField(self, 0x00000008, "OC5PE", "Output compare 5 preload enable")
        self.OC5FE = BitField(self, 0x00000004, "OC5FE", "Output compare 5 fast enable")
        self.OCCE = Subscriptor(self, "OC{}CE")
        self.OCPE = Subscriptor(self, "OC{}PE")
        self.OCFE = Subscriptor(self, "OC{}FE")
        self.OCM = Subscriptor(self, "OC{}M")

class SA_TIM2(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Advanced-timers")
        self.CR1 = SA_TIM2_CR1(self, 0x0)
        self.CR2 = SA_TIM2_CR2(self, 0x4)
        self.SMCR = SA_TIM2_SMCR(self, 0x8)
        self.DIER = SA_TIM2_DIER(self, 0xC)
        self.SR = SA_TIM2_SR(self, 0x10)
        self.EGR = SA_TIM2_EGR(self, 0x14)
        self.CCMR1_Output = SA_TIM2_CCMR1_Output(self, 0x18)
        self.CCMR1_Input = SA_TIM2_CCMR1_Input(self, 0x18)
        self.CCMR2_Output = SA_TIM2_CCMR2_Output(self, 0x1C)
        self.CCMR2_Input = SA_TIM2_CCMR2_Input(self, 0x1C)
        self.CCER = SA_TIM2_CCER(self, 0x20)
        self.CNT = SA_TIM2_CNT(self, 0x24)
        self.PSC = SA_TIM2_PSC(self, 0x28)
        self.ARR = SA_TIM2_ARR(self, 0x2C)
        self.RCR = SA_TIM2_RCR(self, 0x30)
        self.CCR1 = SA_TIM2_CCR1(self, 0x34)
        self.CCR2 = SA_TIM2_CCR2(self, 0x38)
        self.CCR3 = SA_TIM2_CCR3(self, 0x3C)
        self.CCR4 = SA_TIM2_CCR4(self, 0x40)
        self.BDTR = SA_TIM2_BDTR(self, 0x44)
        self.CCR5 = SA_TIM2_CCR5(self, 0x48)
        self.CCR6 = SA_TIM2_CCR6(self, 0x4C)
        self.CCMR3_Output = SA_TIM2_CCMR3_Output(self, 0x50)
        self.DTR2 = SA_TIM2_DTR2(self, 0x54)
        self.ECR = SA_TIM2_ECR(self, 0x58)
        self.TISEL = SA_TIM2_TISEL(self, 0x5C)
        self.AF1 = SA_TIM2_AF1(self, 0x60)
        self.AF2 = SA_TIM2_AF2(self, 0x64)
        self.DCR = SA_TIM2_DCR(self, 0x3DC)
        self.DMAR = SA_TIM2_DMAR(self, 0x3E0)
        self.CCMR1 = SA_TIM2_CCMR1(self, 0x18)
        self.CCMR2 = SA_TIM2_CCMR2(self, 0x1C)
        self.CCMR3 = SA_TIM2_CCMR3(self, 0x50)
        self.AF = Subscriptor(self, "AF{}")
        self.CCMR_Output = Subscriptor(self, "CCMR{}_Output")
        self.CCMR_Input = Subscriptor(self, "CCMR{}_Input")
        self.CCMR = Subscriptor(self, "CCMR{}")
        self.CCR = Subscriptor(self, "CCR{}")

TIM2 = SA_TIM2(0x40000000, "TIM2")
TIM3 = SA_TIM2(0x40000400, "TIM3")
TIM4 = SA_TIM2(0x40000800, "TIM4")
TIM5 = SA_TIM2(0x40000C00, "TIM5")

class SA_TIM6_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "control register 1")
        self.DITHEN = BitField(self, 0x00001000, "DITHEN", "Dithering Enable")
        self.UIFREMAP = BitField(self, 0x00000800, "UIFREMAP", "UIF status bit remapping")
        self.ARPE = BitField(self, 0x00000080, "ARPE", "Auto-reload preload enable")
        self.OPM = BitField(self, 0x00000008, "OPM", "One-pulse mode")
        self.URS = BitField(self, 0x00000004, "URS", "Update request source")
        self.UDIS = BitField(self, 0x00000002, "UDIS", "Update disable")
        self.CEN = BitField(self, 0x00000001, "CEN", "Counter enable")

class SA_TIM6_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "control register 2")
        self.MMS = BitField(self, 0x00000070, "MMS", "Master mode selection")

class SA_TIM6_DIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DIER", "DMA/Interrupt enable register")
        self.UDE = BitField(self, 0x00000100, "UDE", "Update DMA request enable")
        self.UIE = BitField(self, 0x00000001, "UIE", "Update interrupt enable")

class SA_TIM6_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.UIF = BitField(self, 0x00000001, "UIF", "Update interrupt flag")

class SA_TIM6_EGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EGR", "event generation register")
        self.UG = BitField(self, 0x00000001, "UG", "Update generation")

class SA_TIM6_CNT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNT", "counter")
        self.UIFCPY = BitField(self, 0x80000000, "UIFCPY", "UIF Copy")
        self.CNT = BitField(self, 0x0000FFFF, "CNT", "Low counter value")

class SA_TIM6_PSC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PSC", "prescaler")
        self.PSC = BitField(self, 0x0000FFFF, "PSC", "Prescaler value")

class SA_TIM6_ARR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "ARR", "auto-reload register")
        self.ARR = BitField(self, 0x0000FFFF, "ARR", "Low Auto-reload value")

class SA_TIM6(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Basic-timers")
        self.CR1 = SA_TIM6_CR1(self, 0x0)
        self.CR2 = SA_TIM6_CR2(self, 0x4)
        self.DIER = SA_TIM6_DIER(self, 0xC)
        self.SR = SA_TIM6_SR(self, 0x10)
        self.EGR = SA_TIM6_EGR(self, 0x14)
        self.CNT = SA_TIM6_CNT(self, 0x24)
        self.PSC = SA_TIM6_PSC(self, 0x28)
        self.ARR = SA_TIM6_ARR(self, 0x2C)

TIM6 = SA_TIM6(0x40001000, "TIM6")
TIM7 = SA_TIM6(0x40001400, "TIM7")

class SA_LPTIMER1_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISR", "Interrupt and Status Register")
        self.DOWN = BitField(self, 0x00000040, "DOWN", "Counter direction change up to down")
        self.UP = BitField(self, 0x00000020, "UP", "Counter direction change down to up")
        self.ARROK = BitField(self, 0x00000010, "ARROK", "Autoreload register update OK")
        self.CMPOK = BitField(self, 0x00000008, "CMPOK", "Compare register update OK")
        self.EXTTRIG = BitField(self, 0x00000004, "EXTTRIG", "External trigger edge event")
        self.ARRM = BitField(self, 0x00000002, "ARRM", "Autoreload match")
        self.CMPM = BitField(self, 0x00000001, "CMPM", "Compare match")

class SA_LPTIMER1_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "Interrupt Clear Register")
        self.DOWNCF = BitField(self, 0x00000040, "DOWNCF", "Direction change to down Clear Flag")
        self.UPCF = BitField(self, 0x00000020, "UPCF", "Direction change to UP Clear Flag")
        self.ARROKCF = BitField(self, 0x00000010, "ARROKCF", "Autoreload register update OK Clear Flag")
        self.CMPOKCF = BitField(self, 0x00000008, "CMPOKCF", "Compare register update OK Clear Flag")
        self.EXTTRIGCF = BitField(self, 0x00000004, "EXTTRIGCF", "External trigger valid edge Clear Flag")
        self.ARRMCF = BitField(self, 0x00000002, "ARRMCF", "Autoreload match Clear Flag")
        self.CMPMCF = BitField(self, 0x00000001, "CMPMCF", "compare match Clear Flag")

class SA_LPTIMER1_IER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IER", "Interrupt Enable Register")
        self.DOWNIE = BitField(self, 0x00000040, "DOWNIE", "Direction change to down Interrupt Enable")
        self.UPIE = BitField(self, 0x00000020, "UPIE", "Direction change to UP Interrupt Enable")
        self.ARROKIE = BitField(self, 0x00000010, "ARROKIE", "Autoreload register update OK Interrupt Enable")
        self.CMPOKIE = BitField(self, 0x00000008, "CMPOKIE", "Compare register update OK Interrupt Enable")
        self.EXTTRIGIE = BitField(self, 0x00000004, "EXTTRIGIE", "External trigger valid edge Interrupt Enable")
        self.ARRMIE = BitField(self, 0x00000002, "ARRMIE", "Autoreload match Interrupt Enable")
        self.CMPMIE = BitField(self, 0x00000001, "CMPMIE", "Compare match Interrupt Enable")

class SA_LPTIMER1_CFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CFGR", "Configuration Register")
        self.ENC = BitField(self, 0x01000000, "ENC", "Encoder mode enable")
        self.COUNTMODE = BitField(self, 0x00800000, "COUNTMODE", "counter mode enabled")
        self.PRELOAD = BitField(self, 0x00400000, "PRELOAD", "Registers update mode")
        self.WAVPOL = BitField(self, 0x00200000, "WAVPOL", "Waveform shape polarity")
        self.WAVE = BitField(self, 0x00100000, "WAVE", "Waveform shape")
        self.TIMOUT = BitField(self, 0x00080000, "TIMOUT", "Timeout enable")
        self.TRIGEN = BitField(self, 0x00060000, "TRIGEN", "Trigger enable and polarity")
        self.TRIGSEL = BitField(self, 0x0001E000, "TRIGSEL", "Trigger selector")
        self.PRESC = BitField(self, 0x00000E00, "PRESC", "Clock prescaler")
        self.TRGFLT = BitField(self, 0x000000C0, "TRGFLT", "Configurable digital filter for trigger")
        self.CKFLT = BitField(self, 0x00000018, "CKFLT", "Configurable digital filter for external clock")
        self.CKPOL = BitField(self, 0x00000006, "CKPOL", "Clock Polarity")
        self.CKSEL = BitField(self, 0x00000001, "CKSEL", "Clock selector")

class SA_LPTIMER1_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "Control Register")
        self.RSTARE = BitField(self, 0x00000010, "RSTARE", "RSTARE")
        self.COUNTRST = BitField(self, 0x00000008, "COUNTRST", "COUNTRST")
        self.CNTSTRT = BitField(self, 0x00000004, "CNTSTRT", "Timer start in continuous mode")
        self.SNGSTRT = BitField(self, 0x00000002, "SNGSTRT", "LPTIM start in single mode")
        self.ENABLE = BitField(self, 0x00000001, "ENABLE", "LPTIM Enable")

class SA_LPTIMER1_CMP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP", "Compare Register")
        self.CMP = BitField(self, 0x0000FFFF, "CMP", "Compare value")

class SA_LPTIMER1_ARR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x1, "ARR", "Autoreload Register")
        self.ARR = BitField(self, 0x0000FFFF, "ARR", "Auto reload value")

class SA_LPTIMER1_CNT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNT", "Counter Register")
        self.CNT = BitField(self, 0x0000FFFF, "CNT", "Counter value")

class SA_LPTIMER1_OR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OR", "option register")
        self.IN1 = BitField(self, 0x0000000D, "IN1", "IN1")
        self.IN2 = BitField(self, 0x00000032, "IN2", "IN2")
        self.IN = Subscriptor(self, "IN{}")

class SA_LPTIMER1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Low power timer")
        self.ISR = SA_LPTIMER1_ISR(self, 0x0)
        self.ICR = SA_LPTIMER1_ICR(self, 0x4)
        self.IER = SA_LPTIMER1_IER(self, 0x8)
        self.CFGR = SA_LPTIMER1_CFGR(self, 0xC)
        self.CR = SA_LPTIMER1_CR(self, 0x10)
        self.CMP = SA_LPTIMER1_CMP(self, 0x14)
        self.ARR = SA_LPTIMER1_ARR(self, 0x18)
        self.CNT = SA_LPTIMER1_CNT(self, 0x1C)
        self.OR = SA_LPTIMER1_OR(self, 0x20)

LPTIMER1 = SA_LPTIMER1(0x40007C00, "LPTIMER1")

class SA_USART1_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "Control register 1")
        self.RXFFIE = BitField(self, 0x80000000, "RXFFIE", "RXFFIE")
        self.TXFEIE = BitField(self, 0x40000000, "TXFEIE", "TXFEIE")
        self.FIFOEN = BitField(self, 0x20000000, "FIFOEN", "FIFOEN")
        self.M1 = BitField(self, 0x10000000, "M1", "M1")
        self.EOBIE = BitField(self, 0x08000000, "EOBIE", "End of Block interrupt enable")
        self.RTOIE = BitField(self, 0x04000000, "RTOIE", "Receiver timeout interrupt enable")
        self.DEAT4 = BitField(self, 0x02000000, "DEAT4", "Driver Enable assertion time")
        self.DEAT3 = BitField(self, 0x01000000, "DEAT3", "DEAT3")
        self.DEAT2 = BitField(self, 0x00800000, "DEAT2", "DEAT2")
        self.DEAT1 = BitField(self, 0x00400000, "DEAT1", "DEAT1")
        self.DEAT0 = BitField(self, 0x00200000, "DEAT0", "DEAT0")
        self.DEDT4 = BitField(self, 0x00100000, "DEDT4", "Driver Enable de-assertion time")
        self.DEDT3 = BitField(self, 0x00080000, "DEDT3", "DEDT3")
        self.DEDT2 = BitField(self, 0x00040000, "DEDT2", "DEDT2")
        self.DEDT1 = BitField(self, 0x00020000, "DEDT1", "DEDT1")
        self.DEDT0 = BitField(self, 0x00010000, "DEDT0", "DEDT0")
        self.OVER8 = BitField(self, 0x00008000, "OVER8", "Oversampling mode")
        self.CMIE = BitField(self, 0x00004000, "CMIE", "Character match interrupt enable")
        self.MME = BitField(self, 0x00002000, "MME", "Mute mode enable")
        self.M0 = BitField(self, 0x00001000, "M0", "Word length")
        self.WAKE = BitField(self, 0x00000800, "WAKE", "Receiver wakeup method")
        self.PCE = BitField(self, 0x00000400, "PCE", "Parity control enable")
        self.PS = BitField(self, 0x00000200, "PS", "Parity selection")
        self.PEIE = BitField(self, 0x00000100, "PEIE", "PE interrupt enable")
        self.TXEIE = BitField(self, 0x00000080, "TXEIE", "interrupt enable")
        self.TCIE = BitField(self, 0x00000040, "TCIE", "Transmission complete interrupt enable")
        self.RXNEIE = BitField(self, 0x00000020, "RXNEIE", "RXNE interrupt enable")
        self.IDLEIE = BitField(self, 0x00000010, "IDLEIE", "IDLE interrupt enable")
        self.TE = BitField(self, 0x00000008, "TE", "Transmitter enable")
        self.RE = BitField(self, 0x00000004, "RE", "Receiver enable")
        self.UESM = BitField(self, 0x00000002, "UESM", "USART enable in Stop mode")
        self.UE = BitField(self, 0x00000001, "UE", "USART enable")
        self.M = Subscriptor(self, "M{}")
        self.DEDT = Subscriptor(self, "DEDT{}")
        self.DEAT = Subscriptor(self, "DEAT{}")

class SA_USART1_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "Control register 2")
        self.ADD4_7 = BitField(self, 0xF0000000, "ADD4_7", "Address of the USART node")
        self.ADD0_3 = BitField(self, 0x0F000000, "ADD0_3", "Address of the USART node")
        self.RTOEN = BitField(self, 0x00800000, "RTOEN", "Receiver timeout enable")
        self.ABRMOD1 = BitField(self, 0x00400000, "ABRMOD1", "Auto baud rate mode")
        self.ABRMOD0 = BitField(self, 0x00200000, "ABRMOD0", "ABRMOD0")
        self.ABREN = BitField(self, 0x00100000, "ABREN", "Auto baud rate enable")
        self.MSBFIRST = BitField(self, 0x00080000, "MSBFIRST", "Most significant bit first")
        self.TAINV = BitField(self, 0x00040000, "TAINV", "Binary data inversion")
        self.TXINV = BitField(self, 0x00020000, "TXINV", "TX pin active level inversion")
        self.RXINV = BitField(self, 0x00010000, "RXINV", "RX pin active level inversion")
        self.SWAP = BitField(self, 0x00008000, "SWAP", "Swap TX/RX pins")
        self.LINEN = BitField(self, 0x00004000, "LINEN", "LIN mode enable")
        self.STOP = BitField(self, 0x00003000, "STOP", "STOP bits")
        self.CLKEN = BitField(self, 0x00000800, "CLKEN", "Clock enable")
        self.CPOL = BitField(self, 0x00000400, "CPOL", "Clock polarity")
        self.CPHA = BitField(self, 0x00000200, "CPHA", "Clock phase")
        self.LBCL = BitField(self, 0x00000100, "LBCL", "Last bit clock pulse")
        self.LBDIE = BitField(self, 0x00000040, "LBDIE", "LIN break detection interrupt enable")
        self.LBDL = BitField(self, 0x00000020, "LBDL", "LIN break detection length")
        self.ADDM7 = BitField(self, 0x00000010, "ADDM7", "7-bit Address Detection/4-bit Address Detection")
        self.DIS_NSS = BitField(self, 0x00000008, "DIS_NSS", "DIS_NSS")
        self.SLVEN = BitField(self, 0x00000001, "SLVEN", "SLVEN")
        self.ABRMOD = Subscriptor(self, "ABRMOD{}")

class SA_USART1_CR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR3", "Control register 3")
        self.TXFTCFG = BitField(self, 0xE0000000, "TXFTCFG", "TXFTCFG")
        self.RXFTIE = BitField(self, 0x10000000, "RXFTIE", "RXFTIE")
        self.RXFTCFG = BitField(self, 0x0E000000, "RXFTCFG", "RXFTCFG")
        self.TCBGTIE = BitField(self, 0x01000000, "TCBGTIE", "TCBGTIE")
        self.TXFTIE = BitField(self, 0x00800000, "TXFTIE", "TXFTIE")
        self.WUFIE = BitField(self, 0x00400000, "WUFIE", "Wakeup from Stop mode interrupt enable")
        self.WUS = BitField(self, 0x00300000, "WUS", "Wakeup from Stop mode interrupt flag selection")
        self.SCARCNT = BitField(self, 0x000E0000, "SCARCNT", "Smartcard auto-retry count")
        self.DEP = BitField(self, 0x00008000, "DEP", "Driver enable polarity selection")
        self.DEM = BitField(self, 0x00004000, "DEM", "Driver enable mode")
        self.DDRE = BitField(self, 0x00002000, "DDRE", "DMA Disable on Reception Error")
        self.OVRDIS = BitField(self, 0x00001000, "OVRDIS", "Overrun Disable")
        self.ONEBIT = BitField(self, 0x00000800, "ONEBIT", "One sample bit method enable")
        self.CTSIE = BitField(self, 0x00000400, "CTSIE", "CTS interrupt enable")
        self.CTSE = BitField(self, 0x00000200, "CTSE", "CTS enable")
        self.RTSE = BitField(self, 0x00000100, "RTSE", "RTS enable")
        self.DMAT = BitField(self, 0x00000080, "DMAT", "DMA enable transmitter")
        self.DMAR = BitField(self, 0x00000040, "DMAR", "DMA enable receiver")
        self.SCEN = BitField(self, 0x00000020, "SCEN", "Smartcard mode enable")
        self.NACK = BitField(self, 0x00000010, "NACK", "Smartcard NACK enable")
        self.HDSEL = BitField(self, 0x00000008, "HDSEL", "Half-duplex selection")
        self.IRLP = BitField(self, 0x00000004, "IRLP", "Ir low-power")
        self.IREN = BitField(self, 0x00000002, "IREN", "Ir mode enable")
        self.EIE = BitField(self, 0x00000001, "EIE", "Error interrupt enable")

class SA_USART1_BRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BRR", "Baud rate register")
        self.DIV_Mantissa = BitField(self, 0x0000FFF0, "DIV_Mantissa", "DIV_Mantissa")
        self.DIV_Fraction = BitField(self, 0x0000000F, "DIV_Fraction", "DIV_Fraction")

class SA_USART1_GTPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "GTPR", "Guard time and prescaler register")
        self.GT = BitField(self, 0x0000FF00, "GT", "Guard time value")
        self.PSC = BitField(self, 0x000000FF, "PSC", "Prescaler value")

class SA_USART1_RTOR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RTOR", "Receiver timeout register")
        self.BLEN = BitField(self, 0xFF000000, "BLEN", "Block Length")
        self.RTO = BitField(self, 0x00FFFFFF, "RTO", "Receiver timeout value")

class SA_USART1_RQR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RQR", "Request register")
        self.TXFRQ = BitField(self, 0x00000010, "TXFRQ", "Transmit data flush request")
        self.RXFRQ = BitField(self, 0x00000008, "RXFRQ", "Receive data flush request")
        self.MMRQ = BitField(self, 0x00000004, "MMRQ", "Mute mode request")
        self.SBKRQ = BitField(self, 0x00000002, "SBKRQ", "Send break request")
        self.ABRRQ = BitField(self, 0x00000001, "ABRRQ", "Auto baud rate request")

class SA_USART1_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISR", "Interrupt & status register")
        self.TXFT = BitField(self, 0x08000000, "TXFT", "TXFT")
        self.RXFT = BitField(self, 0x04000000, "RXFT", "RXFT")
        self.TCBGT = BitField(self, 0x02000000, "TCBGT", "TCBGT")
        self.RXFF = BitField(self, 0x01000000, "RXFF", "RXFF")
        self.TXFE = BitField(self, 0x00800000, "TXFE", "TXFE")
        self.REACK = BitField(self, 0x00400000, "REACK", "REACK")
        self.TEACK = BitField(self, 0x00200000, "TEACK", "TEACK")
        self.WUF = BitField(self, 0x00100000, "WUF", "WUF")
        self.RWU = BitField(self, 0x00080000, "RWU", "RWU")
        self.SBKF = BitField(self, 0x00040000, "SBKF", "SBKF")
        self.CMF = BitField(self, 0x00020000, "CMF", "CMF")
        self.BUSY = BitField(self, 0x00010000, "BUSY", "BUSY")
        self.ABRF = BitField(self, 0x00008000, "ABRF", "ABRF")
        self.ABRE = BitField(self, 0x00004000, "ABRE", "ABRE")
        self.UDR = BitField(self, 0x00002000, "UDR", "UDR")
        self.EOBF = BitField(self, 0x00001000, "EOBF", "EOBF")
        self.RTOF = BitField(self, 0x00000800, "RTOF", "RTOF")
        self.CTS = BitField(self, 0x00000400, "CTS", "CTS")
        self.CTSIF = BitField(self, 0x00000200, "CTSIF", "CTSIF")
        self.LBDF = BitField(self, 0x00000100, "LBDF", "LBDF")
        self.TXE = BitField(self, 0x00000080, "TXE", "TXE")
        self.TC = BitField(self, 0x00000040, "TC", "TC")
        self.RXNE = BitField(self, 0x00000020, "RXNE", "RXNE")
        self.IDLE = BitField(self, 0x00000010, "IDLE", "IDLE")
        self.ORE = BitField(self, 0x00000008, "ORE", "ORE")
        self.NF = BitField(self, 0x00000004, "NF", "NF")
        self.FE = BitField(self, 0x00000002, "FE", "FE")
        self.PE = BitField(self, 0x00000001, "PE", "PE")

class SA_USART1_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "Interrupt flag clear register")
        self.WUCF = BitField(self, 0x00100000, "WUCF", "Wakeup from Stop mode clear flag")
        self.CMCF = BitField(self, 0x00020000, "CMCF", "Character match clear flag")
        self.UDRCF = BitField(self, 0x00002000, "UDRCF", "UDRCF")
        self.EOBCF = BitField(self, 0x00001000, "EOBCF", "End of block clear flag")
        self.RTOCF = BitField(self, 0x00000800, "RTOCF", "Receiver timeout clear flag")
        self.CTSCF = BitField(self, 0x00000200, "CTSCF", "CTS clear flag")
        self.LBDCF = BitField(self, 0x00000100, "LBDCF", "LIN break detection clear flag")
        self.TCBGTCF = BitField(self, 0x00000080, "TCBGTCF", "TCBGTCF")
        self.TCCF = BitField(self, 0x00000040, "TCCF", "Transmission complete clear flag")
        self.TXFECF = BitField(self, 0x00000020, "TXFECF", "TXFECF")
        self.IDLECF = BitField(self, 0x00000010, "IDLECF", "Idle line detected clear flag")
        self.ORECF = BitField(self, 0x00000008, "ORECF", "Overrun error clear flag")
        self.NCF = BitField(self, 0x00000004, "NCF", "Noise detected clear flag")
        self.FECF = BitField(self, 0x00000002, "FECF", "Framing error clear flag")
        self.PECF = BitField(self, 0x00000001, "PECF", "Parity error clear flag")

class SA_USART1_RDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RDR", "Receive data register")
        self.RDR = BitField(self, 0x000001FF, "RDR", "Receive data value")

class SA_USART1_TDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TDR", "Transmit data register")
        self.TDR = BitField(self, 0x000001FF, "TDR", "Transmit data value")

class SA_USART1_PRESC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PRESC", "USART prescaler register")
        self.PRESCALER = BitField(self, 0x0000000F, "PRESCALER", "PRESCALER")

class SA_USART1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Universal synchronous asynchronous receiver transmitter")
        self.CR1 = SA_USART1_CR1(self, 0x0)
        self.CR2 = SA_USART1_CR2(self, 0x4)
        self.CR3 = SA_USART1_CR3(self, 0x8)
        self.BRR = SA_USART1_BRR(self, 0xC)
        self.GTPR = SA_USART1_GTPR(self, 0x10)
        self.RTOR = SA_USART1_RTOR(self, 0x14)
        self.RQR = SA_USART1_RQR(self, 0x18)
        self.ISR = SA_USART1_ISR(self, 0x1C)
        self.ICR = SA_USART1_ICR(self, 0x20)
        self.RDR = SA_USART1_RDR(self, 0x24)
        self.TDR = SA_USART1_TDR(self, 0x28)
        self.PRESC = SA_USART1_PRESC(self, 0x2C)

USART1 = SA_USART1(0x40013800, "USART1")
USART2 = SA_USART1(0x40004400, "USART2")
USART3 = SA_USART1(0x40004800, "USART3")

class SA_UART4_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "Control register 1")
        self.RXFFIE = BitField(self, 0x80000000, "RXFFIE", "RXFFIE")
        self.TXFEIE = BitField(self, 0x40000000, "TXFEIE", "TXFEIE")
        self.FIFOEN = BitField(self, 0x20000000, "FIFOEN", "FIFOEN")
        self.M1 = BitField(self, 0x10000000, "M1", "M1")
        self.EOBIE = BitField(self, 0x08000000, "EOBIE", "End of Block interrupt enable")
        self.RTOIE = BitField(self, 0x04000000, "RTOIE", "Receiver timeout interrupt enable")
        self.DEAT4 = BitField(self, 0x02000000, "DEAT4", "Driver Enable assertion time")
        self.DEAT3 = BitField(self, 0x01000000, "DEAT3", "DEAT3")
        self.DEAT2 = BitField(self, 0x00800000, "DEAT2", "DEAT2")
        self.DEAT1 = BitField(self, 0x00400000, "DEAT1", "DEAT1")
        self.DEAT0 = BitField(self, 0x00200000, "DEAT0", "DEAT0")
        self.DEDT4 = BitField(self, 0x00100000, "DEDT4", "Driver Enable de-assertion time")
        self.DEDT3 = BitField(self, 0x00080000, "DEDT3", "DEDT3")
        self.DEDT2 = BitField(self, 0x00040000, "DEDT2", "DEDT2")
        self.DEDT1 = BitField(self, 0x00020000, "DEDT1", "DEDT1")
        self.DEDT0 = BitField(self, 0x00010000, "DEDT0", "DEDT0")
        self.OVER8 = BitField(self, 0x00008000, "OVER8", "Oversampling mode")
        self.CMIE = BitField(self, 0x00004000, "CMIE", "Character match interrupt enable")
        self.MME = BitField(self, 0x00002000, "MME", "Mute mode enable")
        self.M0 = BitField(self, 0x00001000, "M0", "Word length")
        self.WAKE = BitField(self, 0x00000800, "WAKE", "Receiver wakeup method")
        self.PCE = BitField(self, 0x00000400, "PCE", "Parity control enable")
        self.PS = BitField(self, 0x00000200, "PS", "Parity selection")
        self.PEIE = BitField(self, 0x00000100, "PEIE", "PE interrupt enable")
        self.TXEIE = BitField(self, 0x00000080, "TXEIE", "interrupt enable")
        self.TCIE = BitField(self, 0x00000040, "TCIE", "Transmission complete interrupt enable")
        self.RXNEIE = BitField(self, 0x00000020, "RXNEIE", "RXNE interrupt enable")
        self.IDLEIE = BitField(self, 0x00000010, "IDLEIE", "IDLE interrupt enable")
        self.TE = BitField(self, 0x00000008, "TE", "Transmitter enable")
        self.RE = BitField(self, 0x00000004, "RE", "Receiver enable")
        self.UESM = BitField(self, 0x00000002, "UESM", "USART enable in Stop mode")
        self.UE = BitField(self, 0x00000001, "UE", "USART enable")
        self.M = Subscriptor(self, "M{}")
        self.DEDT = Subscriptor(self, "DEDT{}")
        self.DEAT = Subscriptor(self, "DEAT{}")

class SA_UART4_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "Control register 2")
        self.ADD4_7 = BitField(self, 0xF0000000, "ADD4_7", "Address of the USART node")
        self.ADD0_3 = BitField(self, 0x0F000000, "ADD0_3", "Address of the USART node")
        self.RTOEN = BitField(self, 0x00800000, "RTOEN", "Receiver timeout enable")
        self.ABRMOD1 = BitField(self, 0x00400000, "ABRMOD1", "Auto baud rate mode")
        self.ABRMOD0 = BitField(self, 0x00200000, "ABRMOD0", "ABRMOD0")
        self.ABREN = BitField(self, 0x00100000, "ABREN", "Auto baud rate enable")
        self.MSBFIRST = BitField(self, 0x00080000, "MSBFIRST", "Most significant bit first")
        self.TAINV = BitField(self, 0x00040000, "TAINV", "Binary data inversion")
        self.TXINV = BitField(self, 0x00020000, "TXINV", "TX pin active level inversion")
        self.RXINV = BitField(self, 0x00010000, "RXINV", "RX pin active level inversion")
        self.SWAP = BitField(self, 0x00008000, "SWAP", "Swap TX/RX pins")
        self.LINEN = BitField(self, 0x00004000, "LINEN", "LIN mode enable")
        self.STOP = BitField(self, 0x00003000, "STOP", "STOP bits")
        self.CLKEN = BitField(self, 0x00000800, "CLKEN", "Clock enable")
        self.CPOL = BitField(self, 0x00000400, "CPOL", "Clock polarity")
        self.CPHA = BitField(self, 0x00000200, "CPHA", "Clock phase")
        self.LBCL = BitField(self, 0x00000100, "LBCL", "Last bit clock pulse")
        self.LBDIE = BitField(self, 0x00000040, "LBDIE", "LIN break detection interrupt enable")
        self.LBDL = BitField(self, 0x00000020, "LBDL", "LIN break detection length")
        self.ADDM7 = BitField(self, 0x00000010, "ADDM7", "7-bit Address Detection/4-bit Address Detection")
        self.DIS_NSS = BitField(self, 0x00000008, "DIS_NSS", "DIS_NSS")
        self.SLVEN = BitField(self, 0x00000001, "SLVEN", "SLVEN")
        self.ABRMOD = Subscriptor(self, "ABRMOD{}")

class SA_UART4_CR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR3", "Control register 3")
        self.TXFTCFG = BitField(self, 0xE0000000, "TXFTCFG", "TXFTCFG")
        self.RXFTIE = BitField(self, 0x10000000, "RXFTIE", "RXFTIE")
        self.RXFTCFG = BitField(self, 0x0E000000, "RXFTCFG", "RXFTCFG")
        self.TCBGTIE = BitField(self, 0x01000000, "TCBGTIE", "TCBGTIE")
        self.TXFTIE = BitField(self, 0x00800000, "TXFTIE", "TXFTIE")
        self.WUFIE = BitField(self, 0x00400000, "WUFIE", "Wakeup from Stop mode interrupt enable")
        self.WUS = BitField(self, 0x00300000, "WUS", "Wakeup from Stop mode interrupt flag selection")
        self.SCARCNT = BitField(self, 0x000E0000, "SCARCNT", "Smartcard auto-retry count")
        self.DEP = BitField(self, 0x00008000, "DEP", "Driver enable polarity selection")
        self.DEM = BitField(self, 0x00004000, "DEM", "Driver enable mode")
        self.DDRE = BitField(self, 0x00002000, "DDRE", "DMA Disable on Reception Error")
        self.OVRDIS = BitField(self, 0x00001000, "OVRDIS", "Overrun Disable")
        self.ONEBIT = BitField(self, 0x00000800, "ONEBIT", "One sample bit method enable")
        self.CTSIE = BitField(self, 0x00000400, "CTSIE", "CTS interrupt enable")
        self.CTSE = BitField(self, 0x00000200, "CTSE", "CTS enable")
        self.RTSE = BitField(self, 0x00000100, "RTSE", "RTS enable")
        self.DMAT = BitField(self, 0x00000080, "DMAT", "DMA enable transmitter")
        self.DMAR = BitField(self, 0x00000040, "DMAR", "DMA enable receiver")
        self.SCEN = BitField(self, 0x00000020, "SCEN", "Smartcard mode enable")
        self.NACK = BitField(self, 0x00000010, "NACK", "Smartcard NACK enable")
        self.HDSEL = BitField(self, 0x00000008, "HDSEL", "Half-duplex selection")
        self.IRLP = BitField(self, 0x00000004, "IRLP", "Ir low-power")
        self.IREN = BitField(self, 0x00000002, "IREN", "Ir mode enable")
        self.EIE = BitField(self, 0x00000001, "EIE", "Error interrupt enable")

class SA_UART4_BRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BRR", "Baud rate register")
        self.DIV_Mantissa = BitField(self, 0x0000FFF0, "DIV_Mantissa", "DIV_Mantissa")
        self.DIV_Fraction = BitField(self, 0x0000000F, "DIV_Fraction", "DIV_Fraction")

class SA_UART4_GTPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "GTPR", "Guard time and prescaler register")
        self.GT = BitField(self, 0x0000FF00, "GT", "Guard time value")
        self.PSC = BitField(self, 0x000000FF, "PSC", "Prescaler value")

class SA_UART4_RTOR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RTOR", "Receiver timeout register")
        self.BLEN = BitField(self, 0xFF000000, "BLEN", "Block Length")
        self.RTO = BitField(self, 0x00FFFFFF, "RTO", "Receiver timeout value")

class SA_UART4_RQR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RQR", "Request register")
        self.TXFRQ = BitField(self, 0x00000010, "TXFRQ", "Transmit data flush request")
        self.RXFRQ = BitField(self, 0x00000008, "RXFRQ", "Receive data flush request")
        self.MMRQ = BitField(self, 0x00000004, "MMRQ", "Mute mode request")
        self.SBKRQ = BitField(self, 0x00000002, "SBKRQ", "Send break request")
        self.ABRRQ = BitField(self, 0x00000001, "ABRRQ", "Auto baud rate request")

class SA_UART4_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xC0, "ISR", "Interrupt & status register")
        self.TXFT = BitField(self, 0x08000000, "TXFT", "TXFT")
        self.RXFT = BitField(self, 0x04000000, "RXFT", "RXFT")
        self.TCBGT = BitField(self, 0x02000000, "TCBGT", "TCBGT")
        self.RXFF = BitField(self, 0x01000000, "RXFF", "RXFF")
        self.TXFE = BitField(self, 0x00800000, "TXFE", "TXFE")
        self.REACK = BitField(self, 0x00400000, "REACK", "REACK")
        self.TEACK = BitField(self, 0x00200000, "TEACK", "TEACK")
        self.WUF = BitField(self, 0x00100000, "WUF", "WUF")
        self.RWU = BitField(self, 0x00080000, "RWU", "RWU")
        self.SBKF = BitField(self, 0x00040000, "SBKF", "SBKF")
        self.CMF = BitField(self, 0x00020000, "CMF", "CMF")
        self.BUSY = BitField(self, 0x00010000, "BUSY", "BUSY")
        self.ABRF = BitField(self, 0x00008000, "ABRF", "ABRF")
        self.ABRE = BitField(self, 0x00004000, "ABRE", "ABRE")
        self.UDR = BitField(self, 0x00002000, "UDR", "UDR")
        self.EOBF = BitField(self, 0x00001000, "EOBF", "EOBF")
        self.RTOF = BitField(self, 0x00000800, "RTOF", "RTOF")
        self.CTS = BitField(self, 0x00000400, "CTS", "CTS")
        self.CTSIF = BitField(self, 0x00000200, "CTSIF", "CTSIF")
        self.LBDF = BitField(self, 0x00000100, "LBDF", "LBDF")
        self.TXE = BitField(self, 0x00000080, "TXE", "TXE")
        self.TC = BitField(self, 0x00000040, "TC", "TC")
        self.RXNE = BitField(self, 0x00000020, "RXNE", "RXNE")
        self.IDLE = BitField(self, 0x00000010, "IDLE", "IDLE")
        self.ORE = BitField(self, 0x00000008, "ORE", "ORE")
        self.NF = BitField(self, 0x00000004, "NF", "NF")
        self.FE = BitField(self, 0x00000002, "FE", "FE")
        self.PE = BitField(self, 0x00000001, "PE", "PE")

class SA_UART4_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "Interrupt flag clear register")
        self.WUCF = BitField(self, 0x00100000, "WUCF", "Wakeup from Stop mode clear flag")
        self.CMCF = BitField(self, 0x00020000, "CMCF", "Character match clear flag")
        self.UDRCF = BitField(self, 0x00002000, "UDRCF", "UDRCF")
        self.EOBCF = BitField(self, 0x00001000, "EOBCF", "End of block clear flag")
        self.RTOCF = BitField(self, 0x00000800, "RTOCF", "Receiver timeout clear flag")
        self.CTSCF = BitField(self, 0x00000200, "CTSCF", "CTS clear flag")
        self.LBDCF = BitField(self, 0x00000100, "LBDCF", "LIN break detection clear flag")
        self.TCBGTCF = BitField(self, 0x00000080, "TCBGTCF", "TCBGTCF")
        self.TCCF = BitField(self, 0x00000040, "TCCF", "Transmission complete clear flag")
        self.TXFECF = BitField(self, 0x00000020, "TXFECF", "TXFECF")
        self.IDLECF = BitField(self, 0x00000010, "IDLECF", "Idle line detected clear flag")
        self.ORECF = BitField(self, 0x00000008, "ORECF", "Overrun error clear flag")
        self.NCF = BitField(self, 0x00000004, "NCF", "Noise detected clear flag")
        self.FECF = BitField(self, 0x00000002, "FECF", "Framing error clear flag")
        self.PECF = BitField(self, 0x00000001, "PECF", "Parity error clear flag")

class SA_UART4_RDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RDR", "Receive data register")
        self.RDR = BitField(self, 0x000001FF, "RDR", "Receive data value")

class SA_UART4_TDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TDR", "Transmit data register")
        self.TDR = BitField(self, 0x000001FF, "TDR", "Transmit data value")

class SA_UART4_PRESC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PRESC", "USART prescaler register")
        self.PRESCALER = BitField(self, 0x0000000F, "PRESCALER", "PRESCALER")

class SA_UART4(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Universal synchronous asynchronous receiver transmitter")
        self.CR1 = SA_UART4_CR1(self, 0x0)
        self.CR2 = SA_UART4_CR2(self, 0x4)
        self.CR3 = SA_UART4_CR3(self, 0x8)
        self.BRR = SA_UART4_BRR(self, 0xC)
        self.GTPR = SA_UART4_GTPR(self, 0x10)
        self.RTOR = SA_UART4_RTOR(self, 0x14)
        self.RQR = SA_UART4_RQR(self, 0x18)
        self.ISR = SA_UART4_ISR(self, 0x1C)
        self.ICR = SA_UART4_ICR(self, 0x20)
        self.RDR = SA_UART4_RDR(self, 0x24)
        self.TDR = SA_UART4_TDR(self, 0x28)
        self.PRESC = SA_UART4_PRESC(self, 0x2C)

UART4 = SA_UART4(0x40004C00, "UART4")
UART5 = SA_UART4(0x40005000, "UART5")

class SA_LPUART1_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "Control register 1")
        self.RXFFIE = BitField(self, 0x80000000, "RXFFIE", "RXFFIE")
        self.TXFEIE = BitField(self, 0x40000000, "TXFEIE", "TXFEIE")
        self.FIFOEN = BitField(self, 0x20000000, "FIFOEN", "FIFOEN")
        self.M1 = BitField(self, 0x10000000, "M1", "Word length")
        self.DEAT4 = BitField(self, 0x02000000, "DEAT4", "Driver Enable assertion time")
        self.DEAT3 = BitField(self, 0x01000000, "DEAT3", "DEAT3")
        self.DEAT2 = BitField(self, 0x00800000, "DEAT2", "DEAT2")
        self.DEAT1 = BitField(self, 0x00400000, "DEAT1", "DEAT1")
        self.DEAT0 = BitField(self, 0x00200000, "DEAT0", "DEAT0")
        self.DEDT4 = BitField(self, 0x00100000, "DEDT4", "Driver Enable de-assertion time")
        self.DEDT3 = BitField(self, 0x00080000, "DEDT3", "DEDT3")
        self.DEDT2 = BitField(self, 0x00040000, "DEDT2", "DEDT2")
        self.DEDT1 = BitField(self, 0x00020000, "DEDT1", "DEDT1")
        self.DEDT0 = BitField(self, 0x00010000, "DEDT0", "DEDT0")
        self.CMIE = BitField(self, 0x00004000, "CMIE", "Character match interrupt enable")
        self.MME = BitField(self, 0x00002000, "MME", "Mute mode enable")
        self.M0 = BitField(self, 0x00001000, "M0", "Word length")
        self.WAKE = BitField(self, 0x00000800, "WAKE", "Receiver wakeup method")
        self.PCE = BitField(self, 0x00000400, "PCE", "Parity control enable")
        self.PS = BitField(self, 0x00000200, "PS", "Parity selection")
        self.PEIE = BitField(self, 0x00000100, "PEIE", "PE interrupt enable")
        self.TXEIE = BitField(self, 0x00000080, "TXEIE", "interrupt enable")
        self.TCIE = BitField(self, 0x00000040, "TCIE", "Transmission complete interrupt enable")
        self.RXNEIE = BitField(self, 0x00000020, "RXNEIE", "RXNE interrupt enable")
        self.IDLEIE = BitField(self, 0x00000010, "IDLEIE", "IDLE interrupt enable")
        self.TE = BitField(self, 0x00000008, "TE", "Transmitter enable")
        self.RE = BitField(self, 0x00000004, "RE", "Receiver enable")
        self.UESM = BitField(self, 0x00000002, "UESM", "USART enable in Stop mode")
        self.UE = BitField(self, 0x00000001, "UE", "USART enable")
        self.M = Subscriptor(self, "M{}")
        self.DEDT = Subscriptor(self, "DEDT{}")
        self.DEAT = Subscriptor(self, "DEAT{}")

class SA_LPUART1_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "Control register 2")
        self.ADD4_7 = BitField(self, 0xF0000000, "ADD4_7", "Address of the USART node")
        self.ADD0_3 = BitField(self, 0x0F000000, "ADD0_3", "Address of the USART node")
        self.MSBFIRST = BitField(self, 0x00080000, "MSBFIRST", "Most significant bit first")
        self.TAINV = BitField(self, 0x00040000, "TAINV", "Binary data inversion")
        self.TXINV = BitField(self, 0x00020000, "TXINV", "TX pin active level inversion")
        self.RXINV = BitField(self, 0x00010000, "RXINV", "RX pin active level inversion")
        self.SWAP = BitField(self, 0x00008000, "SWAP", "Swap TX/RX pins")
        self.STOP = BitField(self, 0x00003000, "STOP", "STOP bits")
        self.ADDM7 = BitField(self, 0x00000010, "ADDM7", "7-bit Address Detection/4-bit Address Detection")

class SA_LPUART1_CR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR3", "Control register 3")
        self.TXFTCFG = BitField(self, 0xE0000000, "TXFTCFG", "TXFTCFG")
        self.RXFTIE = BitField(self, 0x10000000, "RXFTIE", "RXFTIE")
        self.RXFTCFG = BitField(self, 0x0E000000, "RXFTCFG", "RXFTCFG")
        self.TXFTIE = BitField(self, 0x00800000, "TXFTIE", "TXFTIE")
        self.WUFIE = BitField(self, 0x00400000, "WUFIE", "Wakeup from Stop mode interrupt enable")
        self.WUS = BitField(self, 0x00300000, "WUS", "Wakeup from Stop mode interrupt flag selection")
        self.DEP = BitField(self, 0x00008000, "DEP", "Driver enable polarity selection")
        self.DEM = BitField(self, 0x00004000, "DEM", "Driver enable mode")
        self.DDRE = BitField(self, 0x00002000, "DDRE", "DMA Disable on Reception Error")
        self.OVRDIS = BitField(self, 0x00001000, "OVRDIS", "Overrun Disable")
        self.CTSIE = BitField(self, 0x00000400, "CTSIE", "CTS interrupt enable")
        self.CTSE = BitField(self, 0x00000200, "CTSE", "CTS enable")
        self.RTSE = BitField(self, 0x00000100, "RTSE", "RTS enable")
        self.DMAT = BitField(self, 0x00000080, "DMAT", "DMA enable transmitter")
        self.DMAR = BitField(self, 0x00000040, "DMAR", "DMA enable receiver")
        self.HDSEL = BitField(self, 0x00000008, "HDSEL", "Half-duplex selection")
        self.EIE = BitField(self, 0x00000001, "EIE", "Error interrupt enable")

class SA_LPUART1_BRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BRR", "Baud rate register")
        self.BRR = BitField(self, 0x000FFFFF, "BRR", "BRR")

class SA_LPUART1_RQR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RQR", "Request register")
        self.TXFRQ = BitField(self, 0x00000010, "TXFRQ", "TXFRQ")
        self.RXFRQ = BitField(self, 0x00000008, "RXFRQ", "Receive data flush request")
        self.MMRQ = BitField(self, 0x00000004, "MMRQ", "Mute mode request")
        self.SBKRQ = BitField(self, 0x00000002, "SBKRQ", "Send break request")

class SA_LPUART1_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xC0, "ISR", "Interrupt & status register")
        self.TXFT = BitField(self, 0x08000000, "TXFT", "TXFT")
        self.RXFT = BitField(self, 0x04000000, "RXFT", "RXFT")
        self.RXFF = BitField(self, 0x01000000, "RXFF", "RXFF")
        self.TXFE = BitField(self, 0x00800000, "TXFE", "TXFE")
        self.REACK = BitField(self, 0x00400000, "REACK", "REACK")
        self.TEACK = BitField(self, 0x00200000, "TEACK", "TEACK")
        self.WUF = BitField(self, 0x00100000, "WUF", "WUF")
        self.RWU = BitField(self, 0x00080000, "RWU", "RWU")
        self.SBKF = BitField(self, 0x00040000, "SBKF", "SBKF")
        self.CMF = BitField(self, 0x00020000, "CMF", "CMF")
        self.BUSY = BitField(self, 0x00010000, "BUSY", "BUSY")
        self.CTS = BitField(self, 0x00000400, "CTS", "CTS")
        self.CTSIF = BitField(self, 0x00000200, "CTSIF", "CTSIF")
        self.TXE = BitField(self, 0x00000080, "TXE", "TXE")
        self.TC = BitField(self, 0x00000040, "TC", "TC")
        self.RXNE = BitField(self, 0x00000020, "RXNE", "RXNE")
        self.IDLE = BitField(self, 0x00000010, "IDLE", "IDLE")
        self.ORE = BitField(self, 0x00000008, "ORE", "ORE")
        self.NF = BitField(self, 0x00000004, "NF", "NF")
        self.FE = BitField(self, 0x00000002, "FE", "FE")
        self.PE = BitField(self, 0x00000001, "PE", "PE")

class SA_LPUART1_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "Interrupt flag clear register")
        self.WUCF = BitField(self, 0x00100000, "WUCF", "Wakeup from Stop mode clear flag")
        self.CMCF = BitField(self, 0x00020000, "CMCF", "Character match clear flag")
        self.CTSCF = BitField(self, 0x00000200, "CTSCF", "CTS clear flag")
        self.TCCF = BitField(self, 0x00000040, "TCCF", "Transmission complete clear flag")
        self.IDLECF = BitField(self, 0x00000010, "IDLECF", "Idle line detected clear flag")
        self.ORECF = BitField(self, 0x00000008, "ORECF", "Overrun error clear flag")
        self.NCF = BitField(self, 0x00000004, "NCF", "Noise detected clear flag")
        self.FECF = BitField(self, 0x00000002, "FECF", "Framing error clear flag")
        self.PECF = BitField(self, 0x00000001, "PECF", "Parity error clear flag")

class SA_LPUART1_RDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RDR", "Receive data register")
        self.RDR = BitField(self, 0x000001FF, "RDR", "Receive data value")

class SA_LPUART1_TDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TDR", "Transmit data register")
        self.TDR = BitField(self, 0x000001FF, "TDR", "Transmit data value")

class SA_LPUART1_PRESC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PRESC", "Prescaler register")
        self.PRESCALER = BitField(self, 0x0000000F, "PRESCALER", "PRESCALER")

class SA_LPUART1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Universal synchronous asynchronous receiver transmitter")
        self.CR1 = SA_LPUART1_CR1(self, 0x0)
        self.CR2 = SA_LPUART1_CR2(self, 0x4)
        self.CR3 = SA_LPUART1_CR3(self, 0x8)
        self.BRR = SA_LPUART1_BRR(self, 0xC)
        self.RQR = SA_LPUART1_RQR(self, 0x18)
        self.ISR = SA_LPUART1_ISR(self, 0x1C)
        self.ICR = SA_LPUART1_ICR(self, 0x20)
        self.RDR = SA_LPUART1_RDR(self, 0x24)
        self.TDR = SA_LPUART1_TDR(self, 0x28)
        self.PRESC = SA_LPUART1_PRESC(self, 0x2C)

LPUART1 = SA_LPUART1(0x40008000, "LPUART1")

class SA_SPI1_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "control register 1")
        self.BIDIMODE = BitField(self, 0x00008000, "BIDIMODE", "Bidirectional data mode enable")
        self.BIDIOE = BitField(self, 0x00004000, "BIDIOE", "Output enable in bidirectional mode")
        self.CRCEN = BitField(self, 0x00002000, "CRCEN", "Hardware CRC calculation enable")
        self.CRCNEXT = BitField(self, 0x00001000, "CRCNEXT", "CRC transfer next")
        self.DFF = BitField(self, 0x00000800, "DFF", "Data frame format")
        self.RXONLY = BitField(self, 0x00000400, "RXONLY", "Receive only")
        self.SSM = BitField(self, 0x00000200, "SSM", "Software slave management")
        self.SSI = BitField(self, 0x00000100, "SSI", "Internal slave select")
        self.LSBFIRST = BitField(self, 0x00000080, "LSBFIRST", "Frame format")
        self.SPE = BitField(self, 0x00000040, "SPE", "SPI enable")
        self.BR = BitField(self, 0x00000038, "BR", "Baud rate control")
        self.MSTR = BitField(self, 0x00000004, "MSTR", "Master selection")
        self.CPOL = BitField(self, 0x00000002, "CPOL", "Clock polarity")
        self.CPHA = BitField(self, 0x00000001, "CPHA", "Clock phase")

class SA_SPI1_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x700, "CR2", "control register 2")
        self.RXDMAEN = BitField(self, 0x00000001, "RXDMAEN", "Rx buffer DMA enable")
        self.TXDMAEN = BitField(self, 0x00000002, "TXDMAEN", "Tx buffer DMA enable")
        self.SSOE = BitField(self, 0x00000004, "SSOE", "SS output enable")
        self.NSSP = BitField(self, 0x00000008, "NSSP", "NSS pulse management")
        self.FRF = BitField(self, 0x00000010, "FRF", "Frame format")
        self.ERRIE = BitField(self, 0x00000020, "ERRIE", "Error interrupt enable")
        self.RXNEIE = BitField(self, 0x00000040, "RXNEIE", "RX buffer not empty interrupt enable")
        self.TXEIE = BitField(self, 0x00000080, "TXEIE", "Tx buffer empty interrupt enable")
        self.DS = BitField(self, 0x00000F00, "DS", "Data size")
        self.FRXTH = BitField(self, 0x00001000, "FRXTH", "FIFO reception threshold")
        self.LDMA_RX = BitField(self, 0x00002000, "LDMA_RX", "Last DMA transfer for reception")
        self.LDMA_TX = BitField(self, 0x00004000, "LDMA_TX", "Last DMA transfer for transmission")

class SA_SPI1_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x2, "SR", "status register")
        self.RXNE = BitField(self, 0x00000001, "RXNE", "Receive buffer not empty")
        self.TXE = BitField(self, 0x00000002, "TXE", "Transmit buffer empty")
        self.CRCERR = BitField(self, 0x00000010, "CRCERR", "CRC error flag")
        self.MODF = BitField(self, 0x00000020, "MODF", "Mode fault")
        self.OVR = BitField(self, 0x00000040, "OVR", "Overrun flag")
        self.BSY = BitField(self, 0x00000080, "BSY", "Busy flag")
        self.TIFRFE = BitField(self, 0x00000100, "TIFRFE", "TI frame format error")
        self.FRLVL = BitField(self, 0x00000600, "FRLVL", "FIFO reception level")
        self.FTLVL = BitField(self, 0x00001800, "FTLVL", "FIFO transmission level")

class SA_SPI1_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DR", "data register")
        self.DR = BitField(self, 0x0000FFFF, "DR", "Data register")

class SA_SPI1_CRCPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7, "CRCPR", "CRC polynomial register")
        self.CRCPOLY = BitField(self, 0x0000FFFF, "CRCPOLY", "CRC polynomial register")

class SA_SPI1_RXCRCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXCRCR", "RX CRC register")
        self.RxCRC = BitField(self, 0x0000FFFF, "RxCRC", "Rx CRC register")

class SA_SPI1_TXCRCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXCRCR", "TX CRC register")
        self.TxCRC = BitField(self, 0x0000FFFF, "TxCRC", "Tx CRC register")

class SA_SPI1_I2SCFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "I2SCFGR", "configuration register")
        self.CHLEN = BitField(self, 0x00000001, "CHLEN", "CHLEN")
        self.DATLEN = BitField(self, 0x00000006, "DATLEN", "DATLEN")
        self.CKPOL = BitField(self, 0x00000008, "CKPOL", "CKPOL")
        self.I2SSTD = BitField(self, 0x00000030, "I2SSTD", "I2SSTD")
        self.PCMSYNC = BitField(self, 0x00000080, "PCMSYNC", "PCMSYNC")
        self.I2SCFG = BitField(self, 0x00000300, "I2SCFG", "I2SCFG")
        self.I2SE = BitField(self, 0x00000400, "I2SE", "I2SE")
        self.I2SMOD = BitField(self, 0x00000800, "I2SMOD", "I2SMOD")

class SA_SPI1_I2SPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x2, "I2SPR", "prescaler register")
        self.I2SDIV = BitField(self, 0x000000FF, "I2SDIV", "I2SDIV")
        self.ODD = BitField(self, 0x00000100, "ODD", "ODD")
        self.MCKOE = BitField(self, 0x00000200, "MCKOE", "MCKOE")

class SA_SPI1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Serial peripheral interface/Inter-IC sound")
        self.CR1 = SA_SPI1_CR1(self, 0x0)
        self.CR2 = SA_SPI1_CR2(self, 0x4)
        self.SR = SA_SPI1_SR(self, 0x8)
        self.DR = SA_SPI1_DR(self, 0xC)
        self.CRCPR = SA_SPI1_CRCPR(self, 0x10)
        self.RXCRCR = SA_SPI1_RXCRCR(self, 0x14)
        self.TXCRCR = SA_SPI1_TXCRCR(self, 0x18)
        self.I2SCFGR = SA_SPI1_I2SCFGR(self, 0x1C)
        self.I2SPR = SA_SPI1_I2SPR(self, 0x20)

SPI1 = SA_SPI1(0x40013000, "SPI1")

class SA_SPI4_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x700, "CR1", "control register 1")
        self.BIDIMODE = BitField(self, 0x00008000, "BIDIMODE", "Bidirectional data mode enable")
        self.BIDIOE = BitField(self, 0x00004000, "BIDIOE", "Output enable in bidirectional mode")
        self.CRCEN = BitField(self, 0x00002000, "CRCEN", "Hardware CRC calculation enable")
        self.CRCNEXT = BitField(self, 0x00001000, "CRCNEXT", "CRC transfer next")
        self.DFF = BitField(self, 0x00000800, "DFF", "Data frame format")
        self.RXONLY = BitField(self, 0x00000400, "RXONLY", "Receive only")
        self.SSM = BitField(self, 0x00000200, "SSM", "Software slave management")
        self.SSI = BitField(self, 0x00000100, "SSI", "Internal slave select")
        self.LSBFIRST = BitField(self, 0x00000080, "LSBFIRST", "Frame format")
        self.SPE = BitField(self, 0x00000040, "SPE", "SPI enable")
        self.BR = BitField(self, 0x00000038, "BR", "Baud rate control")
        self.MSTR = BitField(self, 0x00000004, "MSTR", "Master selection")
        self.CPOL = BitField(self, 0x00000002, "CPOL", "Clock polarity")
        self.CPHA = BitField(self, 0x00000001, "CPHA", "Clock phase")

class SA_SPI4_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "control register 2")
        self.RXDMAEN = BitField(self, 0x00000001, "RXDMAEN", "Rx buffer DMA enable")
        self.TXDMAEN = BitField(self, 0x00000002, "TXDMAEN", "Tx buffer DMA enable")
        self.SSOE = BitField(self, 0x00000004, "SSOE", "SS output enable")
        self.NSSP = BitField(self, 0x00000008, "NSSP", "NSS pulse management")
        self.FRF = BitField(self, 0x00000010, "FRF", "Frame format")
        self.ERRIE = BitField(self, 0x00000020, "ERRIE", "Error interrupt enable")
        self.RXNEIE = BitField(self, 0x00000040, "RXNEIE", "RX buffer not empty interrupt enable")
        self.TXEIE = BitField(self, 0x00000080, "TXEIE", "Tx buffer empty interrupt enable")
        self.DS = BitField(self, 0x00000F00, "DS", "Data size")
        self.FRXTH = BitField(self, 0x00001000, "FRXTH", "FIFO reception threshold")
        self.LDMA_RX = BitField(self, 0x00002000, "LDMA_RX", "Last DMA transfer for reception")
        self.LDMA_TX = BitField(self, 0x00004000, "LDMA_TX", "Last DMA transfer for transmission")

class SA_SPI4_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x2, "SR", "status register")
        self.RXNE = BitField(self, 0x00000001, "RXNE", "Receive buffer not empty")
        self.TXE = BitField(self, 0x00000002, "TXE", "Transmit buffer empty")
        self.CRCERR = BitField(self, 0x00000010, "CRCERR", "CRC error flag")
        self.MODF = BitField(self, 0x00000020, "MODF", "Mode fault")
        self.OVR = BitField(self, 0x00000040, "OVR", "Overrun flag")
        self.BSY = BitField(self, 0x00000080, "BSY", "Busy flag")
        self.TIFRFE = BitField(self, 0x00000100, "TIFRFE", "TI frame format error")
        self.FRLVL = BitField(self, 0x00000600, "FRLVL", "FIFO reception level")
        self.FTLVL = BitField(self, 0x00001800, "FTLVL", "FIFO transmission level")

class SA_SPI4_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DR", "data register")
        self.DR = BitField(self, 0x0000FFFF, "DR", "Data register")

class SA_SPI4_CRCPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7, "CRCPR", "CRC polynomial register")
        self.CRCPOLY = BitField(self, 0x0000FFFF, "CRCPOLY", "CRC polynomial register")

class SA_SPI4_RXCRCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXCRCR", "RX CRC register")
        self.RxCRC = BitField(self, 0x0000FFFF, "RxCRC", "Rx CRC register")

class SA_SPI4_TXCRCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXCRCR", "TX CRC register")
        self.TxCRC = BitField(self, 0x0000FFFF, "TxCRC", "Tx CRC register")

class SA_SPI4_I2SCFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "I2SCFGR", "configuration register")
        self.CHLEN = BitField(self, 0x00000001, "CHLEN", "CHLEN")
        self.DATLEN = BitField(self, 0x00000006, "DATLEN", "DATLEN")
        self.CKPOL = BitField(self, 0x00000008, "CKPOL", "CKPOL")
        self.I2SSTD = BitField(self, 0x00000030, "I2SSTD", "I2SSTD")
        self.PCMSYNC = BitField(self, 0x00000080, "PCMSYNC", "PCMSYNC")
        self.I2SCFG = BitField(self, 0x00000300, "I2SCFG", "I2SCFG")
        self.I2SE = BitField(self, 0x00000400, "I2SE", "I2SE")
        self.I2SMOD = BitField(self, 0x00000800, "I2SMOD", "I2SMOD")

class SA_SPI4_I2SPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x2, "I2SPR", "prescaler register")
        self.I2SDIV = BitField(self, 0x000000FF, "I2SDIV", "I2SDIV")
        self.ODD = BitField(self, 0x00000100, "ODD", "ODD")
        self.MCKOE = BitField(self, 0x00000200, "MCKOE", "MCKOE")

class SA_SPI4(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Serial peripheral interface/Inter-IC sound")
        self.CR1 = SA_SPI4_CR1(self, 0x0)
        self.CR2 = SA_SPI4_CR2(self, 0x4)
        self.SR = SA_SPI4_SR(self, 0x8)
        self.DR = SA_SPI4_DR(self, 0xC)
        self.CRCPR = SA_SPI4_CRCPR(self, 0x10)
        self.RXCRCR = SA_SPI4_RXCRCR(self, 0x14)
        self.TXCRCR = SA_SPI4_TXCRCR(self, 0x18)
        self.I2SCFGR = SA_SPI4_I2SCFGR(self, 0x1C)
        self.I2SPR = SA_SPI4_I2SPR(self, 0x20)

SPI4 = SA_SPI4(0x40013C00, "SPI4")
SPI3 = SA_SPI4(0x40003C00, "SPI3")
SPI2 = SA_SPI4(0x40003800, "SPI2")

class SA_EXTI_IMR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFF820000, "IMR1", "Interrupt mask register")
        self.IM0 = BitField(self, 0x00000001, "IM0", "Interrupt Mask on line 0")
        self.IM1 = BitField(self, 0x00000002, "IM1", "Interrupt Mask on line 1")
        self.IM2 = BitField(self, 0x00000004, "IM2", "Interrupt Mask on line 2")
        self.IM3 = BitField(self, 0x00000008, "IM3", "Interrupt Mask on line 3")
        self.IM4 = BitField(self, 0x00000010, "IM4", "Interrupt Mask on line 4")
        self.IM5 = BitField(self, 0x00000020, "IM5", "Interrupt Mask on line 5")
        self.IM6 = BitField(self, 0x00000040, "IM6", "Interrupt Mask on line 6")
        self.IM7 = BitField(self, 0x00000080, "IM7", "Interrupt Mask on line 7")
        self.IM8 = BitField(self, 0x00000100, "IM8", "Interrupt Mask on line 8")
        self.IM9 = BitField(self, 0x00000200, "IM9", "Interrupt Mask on line 9")
        self.IM10 = BitField(self, 0x00000400, "IM10", "Interrupt Mask on line 10")
        self.IM11 = BitField(self, 0x00000800, "IM11", "Interrupt Mask on line 11")
        self.IM12 = BitField(self, 0x00001000, "IM12", "Interrupt Mask on line 12")
        self.IM13 = BitField(self, 0x00002000, "IM13", "Interrupt Mask on line 13")
        self.IM14 = BitField(self, 0x00004000, "IM14", "Interrupt Mask on line 14")
        self.IM15 = BitField(self, 0x00008000, "IM15", "Interrupt Mask on line 15")
        self.IM16 = BitField(self, 0x00010000, "IM16", "Interrupt Mask on line 16")
        self.IM17 = BitField(self, 0x00020000, "IM17", "Interrupt Mask on line 17")
        self.IM18 = BitField(self, 0x00040000, "IM18", "Interrupt Mask on line 18")
        self.IM19 = BitField(self, 0x00080000, "IM19", "Interrupt Mask on line 19")
        self.IM20 = BitField(self, 0x00100000, "IM20", "Interrupt Mask on line 20")
        self.IM21 = BitField(self, 0x00200000, "IM21", "Interrupt Mask on line 21")
        self.IM22 = BitField(self, 0x00400000, "IM22", "Interrupt Mask on line 22")
        self.IM23 = BitField(self, 0x00800000, "IM23", "Interrupt Mask on line 23")
        self.IM24 = BitField(self, 0x01000000, "IM24", "Interrupt Mask on line 24")
        self.IM25 = BitField(self, 0x02000000, "IM25", "Interrupt Mask on line 25")
        self.IM26 = BitField(self, 0x04000000, "IM26", "Interrupt Mask on line 26")
        self.IM27 = BitField(self, 0x08000000, "IM27", "Interrupt Mask on line 27")
        self.IM28 = BitField(self, 0x10000000, "IM28", "Interrupt Mask on line 28")
        self.IM29 = BitField(self, 0x20000000, "IM29", "Interrupt Mask on line 29")
        self.IM30 = BitField(self, 0x40000000, "IM30", "Interrupt Mask on line 30")
        self.IM31 = BitField(self, 0x80000000, "IM31", "Interrupt Mask on line 31")
        self.IM = Subscriptor(self, "IM{}")

class SA_EXTI_EMR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EMR1", "Event mask register")
        self.EM0 = BitField(self, 0x00000001, "EM0", "Event Mask on line 0")
        self.EM1 = BitField(self, 0x00000002, "EM1", "Event Mask on line 1")
        self.EM2 = BitField(self, 0x00000004, "EM2", "Event Mask on line 2")
        self.EM3 = BitField(self, 0x00000008, "EM3", "Event Mask on line 3")
        self.EM4 = BitField(self, 0x00000010, "EM4", "Event Mask on line 4")
        self.EM5 = BitField(self, 0x00000020, "EM5", "Event Mask on line 5")
        self.EM6 = BitField(self, 0x00000040, "EM6", "Event Mask on line 6")
        self.EM7 = BitField(self, 0x00000080, "EM7", "Event Mask on line 7")
        self.EM8 = BitField(self, 0x00000100, "EM8", "Event Mask on line 8")
        self.EM9 = BitField(self, 0x00000200, "EM9", "Event Mask on line 9")
        self.EM10 = BitField(self, 0x00000400, "EM10", "Event Mask on line 10")
        self.EM11 = BitField(self, 0x00000800, "EM11", "Event Mask on line 11")
        self.EM12 = BitField(self, 0x00001000, "EM12", "Event Mask on line 12")
        self.EM13 = BitField(self, 0x00002000, "EM13", "Event Mask on line 13")
        self.EM14 = BitField(self, 0x00004000, "EM14", "Event Mask on line 14")
        self.EM15 = BitField(self, 0x00008000, "EM15", "Event Mask on line 15")
        self.EM16 = BitField(self, 0x00010000, "EM16", "Event Mask on line 16")
        self.EM17 = BitField(self, 0x00020000, "EM17", "Event Mask on line 17")
        self.EM18 = BitField(self, 0x00040000, "EM18", "Event Mask on line 18")
        self.EM19 = BitField(self, 0x00080000, "EM19", "Event Mask on line 19")
        self.EM20 = BitField(self, 0x00100000, "EM20", "Event Mask on line 20")
        self.EM21 = BitField(self, 0x00200000, "EM21", "Event Mask on line 21")
        self.EM22 = BitField(self, 0x00400000, "EM22", "Event Mask on line 22")
        self.EM23 = BitField(self, 0x00800000, "EM23", "Event Mask on line 23")
        self.EM24 = BitField(self, 0x01000000, "EM24", "Event Mask on line 24")
        self.EM25 = BitField(self, 0x02000000, "EM25", "Event Mask on line 25")
        self.EM26 = BitField(self, 0x04000000, "EM26", "Event Mask on line 26")
        self.EM27 = BitField(self, 0x08000000, "EM27", "Event Mask on line 27")
        self.EM28 = BitField(self, 0x10000000, "EM28", "Event Mask on line 28")
        self.EM29 = BitField(self, 0x20000000, "EM29", "Event Mask on line 29")
        self.EM30 = BitField(self, 0x40000000, "EM30", "Event Mask on line 30")
        self.EM31 = BitField(self, 0x80000000, "EM31", "Event Mask on line 31")
        self.EM = Subscriptor(self, "EM{}")

class SA_EXTI_RTSR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RTSR1", "Rising Trigger selection register")
        self.RT0 = BitField(self, 0x00000001, "RT0", "Rising trigger event configuration of line 0")
        self.RT1 = BitField(self, 0x00000002, "RT1", "Rising trigger event configuration of line 1")
        self.RT2 = BitField(self, 0x00000004, "RT2", "Rising trigger event configuration of line 2")
        self.RT3 = BitField(self, 0x00000008, "RT3", "Rising trigger event configuration of line 3")
        self.RT4 = BitField(self, 0x00000010, "RT4", "Rising trigger event configuration of line 4")
        self.RT5 = BitField(self, 0x00000020, "RT5", "Rising trigger event configuration of line 5")
        self.RT6 = BitField(self, 0x00000040, "RT6", "Rising trigger event configuration of line 6")
        self.RT7 = BitField(self, 0x00000080, "RT7", "Rising trigger event configuration of line 7")
        self.RT8 = BitField(self, 0x00000100, "RT8", "Rising trigger event configuration of line 8")
        self.RT9 = BitField(self, 0x00000200, "RT9", "Rising trigger event configuration of line 9")
        self.RT10 = BitField(self, 0x00000400, "RT10", "Rising trigger event configuration of line 10")
        self.RT11 = BitField(self, 0x00000800, "RT11", "Rising trigger event configuration of line 11")
        self.RT12 = BitField(self, 0x00001000, "RT12", "Rising trigger event configuration of line 12")
        self.RT13 = BitField(self, 0x00002000, "RT13", "Rising trigger event configuration of line 13")
        self.RT14 = BitField(self, 0x00004000, "RT14", "Rising trigger event configuration of line 14")
        self.RT15 = BitField(self, 0x00008000, "RT15", "Rising trigger event configuration of line 15")
        self.RT16 = BitField(self, 0x00010000, "RT16", "Rising trigger event configuration of line 16")
        self.RT18 = BitField(self, 0x00040000, "RT18", "Rising trigger event configuration of line 18")
        self.RT19 = BitField(self, 0x00080000, "RT19", "Rising trigger event configuration of line 19")
        self.RT20 = BitField(self, 0x00100000, "RT20", "Rising trigger event configuration of line 20")
        self.RT21 = BitField(self, 0x00200000, "RT21", "Rising trigger event configuration of line 21")
        self.RT22 = BitField(self, 0x00400000, "RT22", "Rising trigger event configuration of line 22")
        self.RT = BitField(self, 0xE0000000, "RT", "RT")

class SA_EXTI_FTSR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FTSR1", "Falling Trigger selection register")
        self.FT0 = BitField(self, 0x00000001, "FT0", "Falling trigger event configuration of line 0")
        self.FT1 = BitField(self, 0x00000002, "FT1", "Falling trigger event configuration of line 1")
        self.FT2 = BitField(self, 0x00000004, "FT2", "Falling trigger event configuration of line 2")
        self.FT3 = BitField(self, 0x00000008, "FT3", "Falling trigger event configuration of line 3")
        self.FT4 = BitField(self, 0x00000010, "FT4", "Falling trigger event configuration of line 4")
        self.FT5 = BitField(self, 0x00000020, "FT5", "Falling trigger event configuration of line 5")
        self.FT6 = BitField(self, 0x00000040, "FT6", "Falling trigger event configuration of line 6")
        self.FT7 = BitField(self, 0x00000080, "FT7", "Falling trigger event configuration of line 7")
        self.FT8 = BitField(self, 0x00000100, "FT8", "Falling trigger event configuration of line 8")
        self.FT9 = BitField(self, 0x00000200, "FT9", "Falling trigger event configuration of line 9")
        self.FT10 = BitField(self, 0x00000400, "FT10", "Falling trigger event configuration of line 10")
        self.FT11 = BitField(self, 0x00000800, "FT11", "Falling trigger event configuration of line 11")
        self.FT12 = BitField(self, 0x00001000, "FT12", "Falling trigger event configuration of line 12")
        self.FT13 = BitField(self, 0x00002000, "FT13", "Falling trigger event configuration of line 13")
        self.FT14 = BitField(self, 0x00004000, "FT14", "Falling trigger event configuration of line 14")
        self.FT15 = BitField(self, 0x00008000, "FT15", "Falling trigger event configuration of line 15")
        self.FT16 = BitField(self, 0x00010000, "FT16", "Falling trigger event configuration of line 16")
        self.FT18 = BitField(self, 0x00040000, "FT18", "Falling trigger event configuration of line 18")
        self.FT19 = BitField(self, 0x00080000, "FT19", "Falling trigger event configuration of line 19")
        self.FT20 = BitField(self, 0x00100000, "FT20", "Falling trigger event configuration of line 20")
        self.FT21 = BitField(self, 0x00200000, "FT21", "Falling trigger event configuration of line 21")
        self.FT22 = BitField(self, 0x00400000, "FT22", "Falling trigger event configuration of line 22")
        self.FT = Subscriptor(self, "FT{}")

class SA_EXTI_SWIER1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SWIER1", "Software interrupt event register")
        self.SWI0 = BitField(self, 0x00000001, "SWI0", "Software Interrupt on line 0")
        self.SWI1 = BitField(self, 0x00000002, "SWI1", "Software Interrupt on line 1")
        self.SWI2 = BitField(self, 0x00000004, "SWI2", "Software Interrupt on line 2")
        self.SWI3 = BitField(self, 0x00000008, "SWI3", "Software Interrupt on line 3")
        self.SWI4 = BitField(self, 0x00000010, "SWI4", "Software Interrupt on line 4")
        self.SWI5 = BitField(self, 0x00000020, "SWI5", "Software Interrupt on line 5")
        self.SWI6 = BitField(self, 0x00000040, "SWI6", "Software Interrupt on line 6")
        self.SWI7 = BitField(self, 0x00000080, "SWI7", "Software Interrupt on line 7")
        self.SWI8 = BitField(self, 0x00000100, "SWI8", "Software Interrupt on line 8")
        self.SWI9 = BitField(self, 0x00000200, "SWI9", "Software Interrupt on line 9")
        self.SWI10 = BitField(self, 0x00000400, "SWI10", "Software Interrupt on line 10")
        self.SWI11 = BitField(self, 0x00000800, "SWI11", "Software Interrupt on line 11")
        self.SWI12 = BitField(self, 0x00001000, "SWI12", "Software Interrupt on line 12")
        self.SWI13 = BitField(self, 0x00002000, "SWI13", "Software Interrupt on line 13")
        self.SWI14 = BitField(self, 0x00004000, "SWI14", "Software Interrupt on line 14")
        self.SWI15 = BitField(self, 0x00008000, "SWI15", "Software Interrupt on line 15")
        self.SWI16 = BitField(self, 0x00010000, "SWI16", "Software Interrupt on line 16")
        self.SWI18 = BitField(self, 0x00040000, "SWI18", "Software Interrupt on line 18")
        self.SWI19 = BitField(self, 0x00080000, "SWI19", "Software Interrupt on line 19")
        self.SWI20 = BitField(self, 0x00100000, "SWI20", "Software Interrupt on line 20")
        self.SWI21 = BitField(self, 0x00200000, "SWI21", "Software Interrupt on line 21")
        self.SWI22 = BitField(self, 0x00400000, "SWI22", "Software Interrupt on line 22")
        self.SWI = Subscriptor(self, "SWI{}")

class SA_EXTI_PR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PR1", "Pending register")
        self.PIF0 = BitField(self, 0x00000001, "PIF0", "Pending bit 0")
        self.PIF1 = BitField(self, 0x00000002, "PIF1", "Pending bit 1")
        self.PIF2 = BitField(self, 0x00000004, "PIF2", "Pending bit 2")
        self.PIF3 = BitField(self, 0x00000008, "PIF3", "Pending bit 3")
        self.PIF4 = BitField(self, 0x00000010, "PIF4", "Pending bit 4")
        self.PIF5 = BitField(self, 0x00000020, "PIF5", "Pending bit 5")
        self.PIF6 = BitField(self, 0x00000040, "PIF6", "Pending bit 6")
        self.PIF7 = BitField(self, 0x00000080, "PIF7", "Pending bit 7")
        self.PIF8 = BitField(self, 0x00000100, "PIF8", "Pending bit 8")
        self.PIF9 = BitField(self, 0x00000200, "PIF9", "Pending bit 9")
        self.PIF10 = BitField(self, 0x00000400, "PIF10", "Pending bit 10")
        self.PIF11 = BitField(self, 0x00000800, "PIF11", "Pending bit 11")
        self.PIF12 = BitField(self, 0x00001000, "PIF12", "Pending bit 12")
        self.PIF13 = BitField(self, 0x00002000, "PIF13", "Pending bit 13")
        self.PIF14 = BitField(self, 0x00004000, "PIF14", "Pending bit 14")
        self.PIF15 = BitField(self, 0x00008000, "PIF15", "Pending bit 15")
        self.PIF16 = BitField(self, 0x00010000, "PIF16", "Pending bit 16")
        self.PIF17 = BitField(self, 0x00020000, "PIF17", "Pending bit 17")
        self.PIF18 = BitField(self, 0x00040000, "PIF18", "Pending bit 18")
        self.PIF19 = BitField(self, 0x00080000, "PIF19", "Pending bit 19")
        self.PIF20 = BitField(self, 0x00100000, "PIF20", "Pending bit 20")
        self.PIF21 = BitField(self, 0x00200000, "PIF21", "Pending bit 21")
        self.PIF22 = BitField(self, 0x00400000, "PIF22", "Pending bit 22")
        self.PIF29 = BitField(self, 0x20000000, "PIF29", "Pending bit 29")
        self.PIF30 = BitField(self, 0x40000000, "PIF30", "Pending bit 30")
        self.PIF31 = BitField(self, 0x80000000, "PIF31", "Pending bit 31")
        self.PIF = Subscriptor(self, "PIF{}")

class SA_EXTI_IMR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFF87, "IMR2", "Interrupt mask register")
        self.IM32 = BitField(self, 0x00000001, "IM32", "Interrupt Mask on external/internal line 32")
        self.IM33 = BitField(self, 0x00000002, "IM33", "Interrupt Mask on external/internal line 33")
        self.IM34 = BitField(self, 0x00000004, "IM34", "Interrupt Mask on external/internal line 34")
        self.IM35 = BitField(self, 0x00000008, "IM35", "Interrupt Mask on external/internal line 35")
        self.IM36 = BitField(self, 0x00000010, "IM36", "Interrupt Mask on external/internal line 36")
        self.IM37 = BitField(self, 0x00000020, "IM37", "Interrupt Mask on external/internal line 37")
        self.IM38 = BitField(self, 0x00000040, "IM38", "Interrupt Mask on external/internal line 38")
        self.IM39 = BitField(self, 0x00000080, "IM39", "Interrupt Mask on external/internal line 39")
        self.IM40 = BitField(self, 0x00000100, "IM40", "Interrupt Mask on external/internal line 40")
        self.IM41 = BitField(self, 0x00000200, "IM41", "Interrupt Mask on external/internal line 41")
        self.IM42 = BitField(self, 0x00000400, "IM42", "Interrupt Mask on external/internal line 42")
        self.IM43 = BitField(self, 0x00000800, "IM43", "Interrupt Mask on external/internal line 43")
        self.IM = Subscriptor(self, "IM{}")

class SA_EXTI_EMR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EMR2", "Event mask register")
        self.EM32 = BitField(self, 0x00000001, "EM32", "Event mask on external/internal line 32")
        self.EM33 = BitField(self, 0x00000002, "EM33", "Event mask on external/internal line 33")
        self.EM34 = BitField(self, 0x00000004, "EM34", "Event mask on external/internal line 34")
        self.EM35 = BitField(self, 0x00000008, "EM35", "Event mask on external/internal line 35")
        self.EM36 = BitField(self, 0x00000010, "EM36", "Event mask on external/internal line 36")
        self.EM37 = BitField(self, 0x00000020, "EM37", "Event mask on external/internal line 37")
        self.EM38 = BitField(self, 0x00000040, "EM38", "Event mask on external/internal line 38")
        self.EM39 = BitField(self, 0x00000080, "EM39", "Event mask on external/internal line 39")
        self.EM40 = BitField(self, 0x00000100, "EM40", "Event mask on external/internal line 40")
        self.EM = Subscriptor(self, "EM{}")

class SA_EXTI_RTSR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RTSR2", "Rising Trigger selection register")
        self.RT32 = BitField(self, 0x00000001, "RT32", "Rising trigger event configuration bit of line 32")
        self.RT33 = BitField(self, 0x00000002, "RT33", "Rising trigger event configuration bit of line 32")
        self.RT38 = BitField(self, 0x00000040, "RT38", "Rising trigger event configuration bit of line 38")
        self.RT39 = BitField(self, 0x00000080, "RT39", "Rising trigger event configuration bit of line 39")
        self.RT40 = BitField(self, 0x00000100, "RT40", "Rising trigger event configuration bit of line 40")
        self.RT41 = BitField(self, 0x00000200, "RT41", "Rising trigger event configuration bit of line 41")
        self.RT = Subscriptor(self, "RT{}")

class SA_EXTI_FTSR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FTSR2", "Falling Trigger selection register")
        self.FT35 = BitField(self, 0x00000008, "FT35", "Falling trigger event configuration bit of line 35")
        self.FT36 = BitField(self, 0x00000010, "FT36", "Falling trigger event configuration bit of line 36")
        self.FT37 = BitField(self, 0x00000020, "FT37", "Falling trigger event configuration bit of line 37")
        self.FT38 = BitField(self, 0x00000040, "FT38", "Falling trigger event configuration bit of line 38")
        self.FT = Subscriptor(self, "FT{}")

class SA_EXTI_SWIER2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SWIER2", "Software interrupt event register")
        self.SWI35 = BitField(self, 0x00000008, "SWI35", "Software interrupt on line 35")
        self.SWI36 = BitField(self, 0x00000010, "SWI36", "Software interrupt on line 36")
        self.SWI37 = BitField(self, 0x00000020, "SWI37", "Software interrupt on line 37")
        self.SWI38 = BitField(self, 0x00000040, "SWI38", "Software interrupt on line 38")
        self.SWI = Subscriptor(self, "SWI{}")

class SA_EXTI_PR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PR2", "Pending register")
        self.PIF35 = BitField(self, 0x00000008, "PIF35", "Pending interrupt flag on line 35")
        self.PIF36 = BitField(self, 0x00000010, "PIF36", "Pending interrupt flag on line 36")
        self.PIF37 = BitField(self, 0x00000020, "PIF37", "Pending interrupt flag on line 37")
        self.PIF38 = BitField(self, 0x00000040, "PIF38", "Pending interrupt flag on line 38")
        self.PIF = Subscriptor(self, "PIF{}")

class SA_EXTI(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "External interrupt/event controller")
        self.IMR1 = SA_EXTI_IMR1(self, 0x0)
        self.EMR1 = SA_EXTI_EMR1(self, 0x4)
        self.RTSR1 = SA_EXTI_RTSR1(self, 0x8)
        self.FTSR1 = SA_EXTI_FTSR1(self, 0xC)
        self.SWIER1 = SA_EXTI_SWIER1(self, 0x10)
        self.PR1 = SA_EXTI_PR1(self, 0x14)
        self.IMR2 = SA_EXTI_IMR2(self, 0x20)
        self.EMR2 = SA_EXTI_EMR2(self, 0x24)
        self.RTSR2 = SA_EXTI_RTSR2(self, 0x28)
        self.FTSR2 = SA_EXTI_FTSR2(self, 0x2C)
        self.SWIER2 = SA_EXTI_SWIER2(self, 0x30)
        self.PR2 = SA_EXTI_PR2(self, 0x34)
        self.SWIER = Subscriptor(self, "SWIER{}")
        self.FTSR = Subscriptor(self, "FTSR{}")
        self.RTSR = Subscriptor(self, "RTSR{}")
        self.PR = Subscriptor(self, "PR{}")
        self.IMR = Subscriptor(self, "IMR{}")
        self.EMR = Subscriptor(self, "EMR{}")

EXTI = SA_EXTI(0x40010400, "EXTI")

class SA_RTC_TR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TR", "time register")
        self.PM = BitField(self, 0x00400000, "PM", "AM/PM notation")
        self.HT = BitField(self, 0x00300000, "HT", "Hour tens in BCD format")
        self.HU = BitField(self, 0x000F0000, "HU", "Hour units in BCD format")
        self.MNT = BitField(self, 0x00007000, "MNT", "Minute tens in BCD format")
        self.MNU = BitField(self, 0x00000F00, "MNU", "Minute units in BCD format")
        self.ST = BitField(self, 0x00000070, "ST", "Second tens in BCD format")
        self.SU = BitField(self, 0x0000000F, "SU", "Second units in BCD format")

class SA_RTC_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x2101, "DR", "date register")
        self.YT = BitField(self, 0x00F00000, "YT", "Year tens in BCD format")
        self.YU = BitField(self, 0x000F0000, "YU", "Year units in BCD format")
        self.WDU = BitField(self, 0x0000E000, "WDU", "Week day units")
        self.MT = BitField(self, 0x00001000, "MT", "Month tens in BCD format")
        self.MU = BitField(self, 0x00000F00, "MU", "Month units in BCD format")
        self.DT = BitField(self, 0x00000030, "DT", "Date tens in BCD format")
        self.DU = BitField(self, 0x0000000F, "DU", "Date units in BCD format")

class SA_RTC_SSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SSR", "sub second register")
        self.SS = BitField(self, 0x0000FFFF, "SS", "Sub second value")

class SA_RTC_ICSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7, "ICSR", "initialization and status register")
        self.ALRAWF = BitField(self, 0x00000001, "ALRAWF", "Alarm A write flag")
        self.ALRBWF = BitField(self, 0x00000002, "ALRBWF", "Alarm B write flag")
        self.WUTWF = BitField(self, 0x00000004, "WUTWF", "Wakeup timer write flag")
        self.SHPF = BitField(self, 0x00000008, "SHPF", "Shift operation pending")
        self.INITS = BitField(self, 0x00000010, "INITS", "Initialization status flag")
        self.RSF = BitField(self, 0x00000020, "RSF", "Registers synchronization flag")
        self.INITF = BitField(self, 0x00000040, "INITF", "Initialization flag")
        self.INIT = BitField(self, 0x00000080, "INIT", "Initialization mode")
        self.RECALPF = BitField(self, 0x00010000, "RECALPF", "Recalibration pending Flag")

class SA_RTC_PRER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7F00FF, "PRER", "prescaler register")
        self.PREDIV_A = BitField(self, 0x007F0000, "PREDIV_A", "Asynchronous prescaler factor")
        self.PREDIV_S = BitField(self, 0x00007FFF, "PREDIV_S", "Synchronous prescaler factor")

class SA_RTC_WUTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "WUTR", "wakeup timer register")
        self.WUT = BitField(self, 0x0000FFFF, "WUT", "Wakeup auto-reload value bits")

class SA_RTC_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "control register")
        self.WCKSEL = BitField(self, 0x00000007, "WCKSEL", "Wakeup clock selection")
        self.TSEDGE = BitField(self, 0x00000008, "TSEDGE", "Time-stamp event active edge")
        self.REFCKON = BitField(self, 0x00000010, "REFCKON", "Reference clock detection enable (50 or 60 Hz)")
        self.BYPSHAD = BitField(self, 0x00000020, "BYPSHAD", "Bypass the shadow registers")
        self.FMT = BitField(self, 0x00000040, "FMT", "Hour format")
        self.ALRAE = BitField(self, 0x00000100, "ALRAE", "Alarm A enable")
        self.ALRBE = BitField(self, 0x00000200, "ALRBE", "Alarm B enable")
        self.WUTE = BitField(self, 0x00000400, "WUTE", "Wakeup timer enable")
        self.TSE = BitField(self, 0x00000800, "TSE", "Time stamp enable")
        self.ALRAIE = BitField(self, 0x00001000, "ALRAIE", "Alarm A interrupt enable")
        self.ALRBIE = BitField(self, 0x00002000, "ALRBIE", "Alarm B interrupt enable")
        self.WUTIE = BitField(self, 0x00004000, "WUTIE", "Wakeup timer interrupt enable")
        self.TSIE = BitField(self, 0x00008000, "TSIE", "Time-stamp interrupt enable")
        self.ADD1H = BitField(self, 0x00010000, "ADD1H", "Add 1 hour (summer time change)")
        self.SUB1H = BitField(self, 0x00020000, "SUB1H", "Subtract 1 hour (winter time change)")
        self.BKP = BitField(self, 0x00040000, "BKP", "Backup")
        self.COSEL = BitField(self, 0x00080000, "COSEL", "Calibration output selection")
        self.POL = BitField(self, 0x00100000, "POL", "Output polarity")
        self.OSEL = BitField(self, 0x00600000, "OSEL", "Output selection")
        self.COE = BitField(self, 0x00800000, "COE", "Calibration output enable")
        self.ITSE = BitField(self, 0x01000000, "ITSE", "timestamp on internal event enable")
        self.TAMPTS = BitField(self, 0x02000000, "TAMPTS", "TAMPTS")
        self.TAMPOE = BitField(self, 0x04000000, "TAMPOE", "TAMPOE")
        self.TAMPALRM_PU = BitField(self, 0x20000000, "TAMPALRM_PU", "TAMPALRM_PU")
        self.TAMPALRM_TYPE = BitField(self, 0x40000000, "TAMPALRM_TYPE", "TAMPALRM_TYPE")
        self.OUT2EN = BitField(self, 0x80000000, "OUT2EN", "OUT2EN")

class SA_RTC_WPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "WPR", "write protection register")
        self.KEY = BitField(self, 0x000000FF, "KEY", "Write protection key")

class SA_RTC_CALR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CALR", "calibration register")
        self.CALP = BitField(self, 0x00008000, "CALP", "Increase frequency of RTC by 488.5 ppm")
        self.CALW8 = BitField(self, 0x00004000, "CALW8", "Use an 8-second calibration cycle period")
        self.CALW16 = BitField(self, 0x00002000, "CALW16", "Use a 16-second calibration cycle period")
        self.CALM = BitField(self, 0x000001FF, "CALM", "Calibration minus")

class SA_RTC_SHIFTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SHIFTR", "shift control register")
        self.ADD1S = BitField(self, 0x80000000, "ADD1S", "Add one second")
        self.SUBFS = BitField(self, 0x00007FFF, "SUBFS", "Subtract a fraction of a second")

class SA_RTC_TSTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TSTR", "time stamp time register")
        self.SU = BitField(self, 0x0000000F, "SU", "Second units in BCD format")
        self.ST = BitField(self, 0x00000070, "ST", "Second tens in BCD format")
        self.MNU = BitField(self, 0x00000F00, "MNU", "Minute units in BCD format")
        self.MNT = BitField(self, 0x00007000, "MNT", "Minute tens in BCD format")
        self.HU = BitField(self, 0x000F0000, "HU", "Hour units in BCD format")
        self.HT = BitField(self, 0x00300000, "HT", "Hour tens in BCD format")
        self.PM = BitField(self, 0x00400000, "PM", "AM/PM notation")

class SA_RTC_TSDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TSDR", "time stamp date register")
        self.WDU = BitField(self, 0x0000E000, "WDU", "Week day units")
        self.MT = BitField(self, 0x00001000, "MT", "Month tens in BCD format")
        self.MU = BitField(self, 0x00000F00, "MU", "Month units in BCD format")
        self.DT = BitField(self, 0x00000030, "DT", "Date tens in BCD format")
        self.DU = BitField(self, 0x0000000F, "DU", "Date units in BCD format")

class SA_RTC_TSSSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TSSSR", "timestamp sub second register")
        self.SS = BitField(self, 0x0000FFFF, "SS", "Sub second value")

class SA_RTC_ALRMAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ALRMAR", "alarm A register")
        self.MSK4 = BitField(self, 0x80000000, "MSK4", "Alarm A date mask")
        self.WDSEL = BitField(self, 0x40000000, "WDSEL", "Week day selection")
        self.DT = BitField(self, 0x30000000, "DT", "Date tens in BCD format")
        self.DU = BitField(self, 0x0F000000, "DU", "Date units or day in BCD format")
        self.MSK3 = BitField(self, 0x00800000, "MSK3", "Alarm A hours mask")
        self.PM = BitField(self, 0x00400000, "PM", "AM/PM notation")
        self.HT = BitField(self, 0x00300000, "HT", "Hour tens in BCD format")
        self.HU = BitField(self, 0x000F0000, "HU", "Hour units in BCD format")
        self.MSK2 = BitField(self, 0x00008000, "MSK2", "Alarm A minutes mask")
        self.MNT = BitField(self, 0x00007000, "MNT", "Minute tens in BCD format")
        self.MNU = BitField(self, 0x00000F00, "MNU", "Minute units in BCD format")
        self.MSK1 = BitField(self, 0x00000080, "MSK1", "Alarm A seconds mask")
        self.ST = BitField(self, 0x00000070, "ST", "Second tens in BCD format")
        self.SU = BitField(self, 0x0000000F, "SU", "Second units in BCD format")
        self.MSK = Subscriptor(self, "MSK{}")

class SA_RTC_ALRMASSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ALRMASSR", "alarm A sub second register")
        self.MASKSS = BitField(self, 0x0F000000, "MASKSS", "Mask the most-significant bits starting at this bit")
        self.SS = BitField(self, 0x00007FFF, "SS", "Sub seconds value")

class SA_RTC_ALRMBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ALRMBR", "alarm B register")
        self.MSK4 = BitField(self, 0x80000000, "MSK4", "Alarm B date mask")
        self.WDSEL = BitField(self, 0x40000000, "WDSEL", "Week day selection")
        self.DT = BitField(self, 0x30000000, "DT", "Date tens in BCD format")
        self.DU = BitField(self, 0x0F000000, "DU", "Date units or day in BCD format")
        self.MSK3 = BitField(self, 0x00800000, "MSK3", "Alarm B hours mask")
        self.PM = BitField(self, 0x00400000, "PM", "AM/PM notation")
        self.HT = BitField(self, 0x00300000, "HT", "Hour tens in BCD format")
        self.HU = BitField(self, 0x000F0000, "HU", "Hour units in BCD format")
        self.MSK2 = BitField(self, 0x00008000, "MSK2", "Alarm B minutes mask")
        self.MNT = BitField(self, 0x00007000, "MNT", "Minute tens in BCD format")
        self.MNU = BitField(self, 0x00000F00, "MNU", "Minute units in BCD format")
        self.MSK1 = BitField(self, 0x00000080, "MSK1", "Alarm B seconds mask")
        self.ST = BitField(self, 0x00000070, "ST", "Second tens in BCD format")
        self.SU = BitField(self, 0x0000000F, "SU", "Second units in BCD format")
        self.MSK = Subscriptor(self, "MSK{}")

class SA_RTC_ALRMBSSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ALRMBSSR", "alarm B sub second register")
        self.MASKSS = BitField(self, 0x0F000000, "MASKSS", "Mask the most-significant bits starting at this bit")
        self.SS = BitField(self, 0x00007FFF, "SS", "Sub seconds value")

class SA_RTC_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.ALRAF = BitField(self, 0x00000001, "ALRAF", "ALRAF")
        self.ALRBF = BitField(self, 0x00000002, "ALRBF", "ALRBF")
        self.WUTF = BitField(self, 0x00000004, "WUTF", "WUTF")
        self.TSF = BitField(self, 0x00000008, "TSF", "TSF")
        self.TSOVF = BitField(self, 0x00000010, "TSOVF", "TSOVF")
        self.ITSF = BitField(self, 0x00000020, "ITSF", "ITSF")

class SA_RTC_MISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MISR", "status register")
        self.ALRAMF = BitField(self, 0x00000001, "ALRAMF", "ALRAMF")
        self.ALRBMF = BitField(self, 0x00000002, "ALRBMF", "ALRBMF")
        self.WUTMF = BitField(self, 0x00000004, "WUTMF", "WUTMF")
        self.TSMF = BitField(self, 0x00000008, "TSMF", "TSMF")
        self.TSOVMF = BitField(self, 0x00000010, "TSOVMF", "TSOVMF")
        self.ITSMF = BitField(self, 0x00000020, "ITSMF", "ITSMF")

class SA_RTC_SCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SCR", "status register")
        self.CALRAF = BitField(self, 0x00000001, "CALRAF", "CALRAF")
        self.CALRBF = BitField(self, 0x00000002, "CALRBF", "CALRBF")
        self.CWUTF = BitField(self, 0x00000004, "CWUTF", "CWUTF")
        self.CTSF = BitField(self, 0x00000008, "CTSF", "CTSF")
        self.CTSOVF = BitField(self, 0x00000010, "CTSOVF", "CTSOVF")
        self.CITSF = BitField(self, 0x00000020, "CITSF", "CITSF")

class SA_RTC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Real-time clock")
        self.TR = SA_RTC_TR(self, 0x0)
        self.DR = SA_RTC_DR(self, 0x4)
        self.SSR = SA_RTC_SSR(self, 0x8)
        self.ICSR = SA_RTC_ICSR(self, 0xC)
        self.PRER = SA_RTC_PRER(self, 0x10)
        self.WUTR = SA_RTC_WUTR(self, 0x14)
        self.CR = SA_RTC_CR(self, 0x18)
        self.WPR = SA_RTC_WPR(self, 0x24)
        self.CALR = SA_RTC_CALR(self, 0x28)
        self.SHIFTR = SA_RTC_SHIFTR(self, 0x2C)
        self.TSTR = SA_RTC_TSTR(self, 0x30)
        self.TSDR = SA_RTC_TSDR(self, 0x34)
        self.TSSSR = SA_RTC_TSSSR(self, 0x38)
        self.ALRMAR = SA_RTC_ALRMAR(self, 0x40)
        self.ALRMASSR = SA_RTC_ALRMASSR(self, 0x44)
        self.ALRMBR = SA_RTC_ALRMBR(self, 0x48)
        self.ALRMBSSR = SA_RTC_ALRMBSSR(self, 0x4C)
        self.SR = SA_RTC_SR(self, 0x50)
        self.MISR = SA_RTC_MISR(self, 0x54)
        self.SCR = SA_RTC_SCR(self, 0x5C)

RTC = SA_RTC(0x40002800, "RTC")

class SA_FMC_BCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x30D0, "BCR1", "SRAM/NOR-Flash chip-select control register 1")
        self.MBKEN = BitField(self, 0x00000001, "MBKEN", "MBKEN")
        self.MUXEN = BitField(self, 0x00000002, "MUXEN", "MUXEN")
        self.MTYP = BitField(self, 0x0000000C, "MTYP", "MTYP")
        self.MWID = BitField(self, 0x00000030, "MWID", "MWID")
        self.FACCEN = BitField(self, 0x00000040, "FACCEN", "FACCEN")
        self.BURSTEN = BitField(self, 0x00000100, "BURSTEN", "BURSTEN")
        self.WAITPOL = BitField(self, 0x00000200, "WAITPOL", "WAITPOL")
        self.WAITCFG = BitField(self, 0x00000800, "WAITCFG", "WAITCFG")
        self.WREN = BitField(self, 0x00001000, "WREN", "WREN")
        self.WAITEN = BitField(self, 0x00002000, "WAITEN", "WAITEN")
        self.EXTMOD = BitField(self, 0x00004000, "EXTMOD", "EXTMOD")
        self.ASYNCWAIT = BitField(self, 0x00008000, "ASYNCWAIT", "ASYNCWAIT")
        self.CPSIZE = BitField(self, 0x00070000, "CPSIZE", "CPSIZE")
        self.CBURSTRW = BitField(self, 0x00080000, "CBURSTRW", "CBURSTRW")
        self.CCLKEN = BitField(self, 0x00100000, "CCLKEN", "CCLKEN")
        self.WFDIS = BitField(self, 0x00200000, "WFDIS", "WFDIS")
        self.NBLSET = BitField(self, 0x00C00000, "NBLSET", "NBLSET")

class SA_FMC_BTR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "BTR1", "SRAM/NOR-Flash chip-select timing register 1")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.DATLAT = BitField(self, 0x0F000000, "DATLAT", "DATLAT")
        self.CLKDIV = BitField(self, 0x00F00000, "CLKDIV", "CLKDIV")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC_BCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x30D0, "BCR2", "SRAM/NOR-Flash chip-select control register 2")
        self.MBKEN = BitField(self, 0x00000001, "MBKEN", "MBKEN")
        self.MUXEN = BitField(self, 0x00000002, "MUXEN", "MUXEN")
        self.MTYP = BitField(self, 0x0000000C, "MTYP", "MTYP")
        self.MWID = BitField(self, 0x00000030, "MWID", "MWID")
        self.FACCEN = BitField(self, 0x00000040, "FACCEN", "FACCEN")
        self.BURSTEN = BitField(self, 0x00000100, "BURSTEN", "BURSTEN")
        self.WAITPOL = BitField(self, 0x00000200, "WAITPOL", "WAITPOL")
        self.WAITCFG = BitField(self, 0x00000800, "WAITCFG", "WAITCFG")
        self.WREN = BitField(self, 0x00001000, "WREN", "WREN")
        self.WAITEN = BitField(self, 0x00002000, "WAITEN", "WAITEN")
        self.EXTMOD = BitField(self, 0x00004000, "EXTMOD", "EXTMOD")
        self.ASYNCWAIT = BitField(self, 0x00008000, "ASYNCWAIT", "ASYNCWAIT")
        self.CPSIZE = BitField(self, 0x00070000, "CPSIZE", "CPSIZE")
        self.CBURSTRW = BitField(self, 0x00080000, "CBURSTRW", "CBURSTRW")
        self.CCLKEN = BitField(self, 0x00100000, "CCLKEN", "CCLKEN")
        self.WFDIS = BitField(self, 0x00200000, "WFDIS", "WFDIS")
        self.NBLSET = BitField(self, 0x00C00000, "NBLSET", "NBLSET")

class SA_FMC_BTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "BTR2", "SRAM/NOR-Flash chip-select timing register 2")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.DATLAT = BitField(self, 0x0F000000, "DATLAT", "DATLAT")
        self.CLKDIV = BitField(self, 0x00F00000, "CLKDIV", "CLKDIV")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC_BCR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x30D0, "BCR3", "SRAM/NOR-Flash chip-select control register 3")
        self.MBKEN = BitField(self, 0x00000001, "MBKEN", "MBKEN")
        self.MUXEN = BitField(self, 0x00000002, "MUXEN", "MUXEN")
        self.MTYP = BitField(self, 0x0000000C, "MTYP", "MTYP")
        self.MWID = BitField(self, 0x00000030, "MWID", "MWID")
        self.FACCEN = BitField(self, 0x00000040, "FACCEN", "FACCEN")
        self.BURSTEN = BitField(self, 0x00000100, "BURSTEN", "BURSTEN")
        self.WAITPOL = BitField(self, 0x00000200, "WAITPOL", "WAITPOL")
        self.WAITCFG = BitField(self, 0x00000800, "WAITCFG", "WAITCFG")
        self.WREN = BitField(self, 0x00001000, "WREN", "WREN")
        self.WAITEN = BitField(self, 0x00002000, "WAITEN", "WAITEN")
        self.EXTMOD = BitField(self, 0x00004000, "EXTMOD", "EXTMOD")
        self.ASYNCWAIT = BitField(self, 0x00008000, "ASYNCWAIT", "ASYNCWAIT")
        self.CPSIZE = BitField(self, 0x00070000, "CPSIZE", "CPSIZE")
        self.CBURSTRW = BitField(self, 0x00080000, "CBURSTRW", "CBURSTRW")
        self.CCLKEN = BitField(self, 0x00100000, "CCLKEN", "CCLKEN")
        self.WFDIS = BitField(self, 0x00200000, "WFDIS", "WFDIS")
        self.NBLSET = BitField(self, 0x00C00000, "NBLSET", "NBLSET")

class SA_FMC_BTR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "BTR3", "SRAM/NOR-Flash chip-select timing register 3")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.DATLAT = BitField(self, 0x0F000000, "DATLAT", "DATLAT")
        self.CLKDIV = BitField(self, 0x00F00000, "CLKDIV", "CLKDIV")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC_BCR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x30D0, "BCR4", "SRAM/NOR-Flash chip-select control register 4")
        self.MBKEN = BitField(self, 0x00000001, "MBKEN", "MBKEN")
        self.MUXEN = BitField(self, 0x00000002, "MUXEN", "MUXEN")
        self.MTYP = BitField(self, 0x0000000C, "MTYP", "MTYP")
        self.MWID = BitField(self, 0x00000030, "MWID", "MWID")
        self.FACCEN = BitField(self, 0x00000040, "FACCEN", "FACCEN")
        self.BURSTEN = BitField(self, 0x00000100, "BURSTEN", "BURSTEN")
        self.WAITPOL = BitField(self, 0x00000200, "WAITPOL", "WAITPOL")
        self.WAITCFG = BitField(self, 0x00000800, "WAITCFG", "WAITCFG")
        self.WREN = BitField(self, 0x00001000, "WREN", "WREN")
        self.WAITEN = BitField(self, 0x00002000, "WAITEN", "WAITEN")
        self.EXTMOD = BitField(self, 0x00004000, "EXTMOD", "EXTMOD")
        self.ASYNCWAIT = BitField(self, 0x00008000, "ASYNCWAIT", "ASYNCWAIT")
        self.CPSIZE = BitField(self, 0x00070000, "CPSIZE", "CPSIZE")
        self.CBURSTRW = BitField(self, 0x00080000, "CBURSTRW", "CBURSTRW")
        self.CCLKEN = BitField(self, 0x00100000, "CCLKEN", "CCLKEN")
        self.WFDIS = BitField(self, 0x00200000, "WFDIS", "WFDIS")
        self.NBLSET = BitField(self, 0x00C00000, "NBLSET", "NBLSET")

class SA_FMC_BTR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFFF, "BTR4", "SRAM/NOR-Flash chip-select timing register 4")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.DATLAT = BitField(self, 0x0F000000, "DATLAT", "DATLAT")
        self.CLKDIV = BitField(self, 0x00F00000, "CLKDIV", "CLKDIV")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC_PCSCNTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PCSCNTR", "PSRAM chip select counter register")
        self.CSCOUNT = BitField(self, 0x0000FFFF, "CSCOUNT", "CSCOUNT")
        self.CNTB1EN = BitField(self, 0x00010000, "CNTB1EN", "CNTB1EN")
        self.CNTB2EN = BitField(self, 0x00020000, "CNTB2EN", "CNTB2EN")
        self.CNTB3EN = BitField(self, 0x00040000, "CNTB3EN", "CNTB3EN")
        self.CNTB4EN = BitField(self, 0x00080000, "CNTB4EN", "CNTB4EN")
        self.CNTBEN = Subscriptor(self, "CNTB{}EN")

class SA_FMC_PCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x18, "PCR", "PC Card/NAND Flash control register 3")
        self.ECCPS = BitField(self, 0x000E0000, "ECCPS", "ECCPS")
        self.TAR = BitField(self, 0x0001E000, "TAR", "TAR")
        self.TCLR = BitField(self, 0x00001E00, "TCLR", "TCLR")
        self.ECCEN = BitField(self, 0x00000040, "ECCEN", "ECCEN")
        self.PWID = BitField(self, 0x00000030, "PWID", "PWID")
        self.PTYP = BitField(self, 0x00000008, "PTYP", "PTYP")
        self.PBKEN = BitField(self, 0x00000004, "PBKEN", "PBKEN")
        self.PWAITEN = BitField(self, 0x00000002, "PWAITEN", "PWAITEN")

class SA_FMC_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x40, "SR", "FIFO status and interrupt register 3")
        self.FEMPT = BitField(self, 0x00000040, "FEMPT", "FEMPT")
        self.IFEN = BitField(self, 0x00000020, "IFEN", "IFEN")
        self.ILEN = BitField(self, 0x00000010, "ILEN", "ILEN")
        self.IREN = BitField(self, 0x00000008, "IREN", "IREN")
        self.IFS = BitField(self, 0x00000004, "IFS", "IFS")
        self.ILS = BitField(self, 0x00000002, "ILS", "ILS")
        self.IRS = BitField(self, 0x00000001, "IRS", "IRS")

class SA_FMC_PMEM(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFCFCFCFC, "PMEM", "Common memory space timing register 3")
        self.MEMHIZx = BitField(self, 0xFF000000, "MEMHIZx", "MEMHIZx")
        self.MEMHOLDx = BitField(self, 0x00FF0000, "MEMHOLDx", "MEMHOLDx")
        self.MEMWAITx = BitField(self, 0x0000FF00, "MEMWAITx", "MEMWAITx")
        self.MEMSETx = BitField(self, 0x000000FF, "MEMSETx", "MEMSETx")

class SA_FMC_PATT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFCFCFCFC, "PATT", "Attribute memory space timing register 3")
        self.ATTHIZx = BitField(self, 0xFF000000, "ATTHIZx", "ATTHIZx")
        self.ATTHOLDx = BitField(self, 0x00FF0000, "ATTHOLDx", "ATTHOLDx")
        self.ATTWAITx = BitField(self, 0x0000FF00, "ATTWAITx", "ATTWAITx")
        self.ATTSETx = BitField(self, 0x000000FF, "ATTSETx", "ATTSETx")

class SA_FMC_ECCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ECCR", "ECC result register 3")
        self.ECCx = BitField(self, 0xFFFFFFFF, "ECCx", "ECCx")

class SA_FMC_BWTR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFF, "BWTR1", "SRAM/NOR-Flash write timing registers 1")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC_BWTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFF, "BWTR2", "SRAM/NOR-Flash write timing registers 2")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC_BWTR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFF, "BWTR3", "SRAM/NOR-Flash write timing registers 3")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC_BWTR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFFFFF, "BWTR4", "SRAM/NOR-Flash write timing registers 4")
        self.DATAHLD = BitField(self, 0xC0000000, "DATAHLD", "DATAHLD")
        self.ACCMOD = BitField(self, 0x30000000, "ACCMOD", "ACCMOD")
        self.BUSTURN = BitField(self, 0x000F0000, "BUSTURN", "BUSTURN")
        self.DATAST = BitField(self, 0x0000FF00, "DATAST", "DATAST")
        self.ADDHLD = BitField(self, 0x000000F0, "ADDHLD", "ADDHLD")
        self.ADDSET = BitField(self, 0x0000000F, "ADDSET", "ADDSET")

class SA_FMC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Flexible memory controller")
        self.BCR1 = SA_FMC_BCR1(self, 0x0)
        self.BTR1 = SA_FMC_BTR1(self, 0x4)
        self.BCR2 = SA_FMC_BCR2(self, 0x8)
        self.BTR2 = SA_FMC_BTR2(self, 0xC)
        self.BCR3 = SA_FMC_BCR3(self, 0x10)
        self.BTR3 = SA_FMC_BTR3(self, 0x14)
        self.BCR4 = SA_FMC_BCR4(self, 0x18)
        self.BTR4 = SA_FMC_BTR4(self, 0x1C)
        self.PCSCNTR = SA_FMC_PCSCNTR(self, 0x20)
        self.PCR = SA_FMC_PCR(self, 0x80)
        self.SR = SA_FMC_SR(self, 0x84)
        self.PMEM = SA_FMC_PMEM(self, 0x88)
        self.PATT = SA_FMC_PATT(self, 0x8C)
        self.ECCR = SA_FMC_ECCR(self, 0x94)
        self.BWTR1 = SA_FMC_BWTR1(self, 0x104)
        self.BWTR2 = SA_FMC_BWTR2(self, 0x10C)
        self.BWTR3 = SA_FMC_BWTR3(self, 0x114)
        self.BWTR4 = SA_FMC_BWTR4(self, 0x11C)
        self.BCR = Subscriptor(self, "BCR{}")
        self.BTR = Subscriptor(self, "BTR{}")
        self.BWTR = Subscriptor(self, "BWTR{}")

FMC = SA_FMC(0xA0000000, "FMC")

class SA_DMA1_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISR", "interrupt status register")
        self.TEIF8 = BitField(self, 0x80000000, "TEIF8", "TEIF8")
        self.HTIF8 = BitField(self, 0x40000000, "HTIF8", "HTIF8")
        self.TCIF8 = BitField(self, 0x20000000, "TCIF8", "TCIF8")
        self.GIF8 = BitField(self, 0x10000000, "GIF8", "GIF8")
        self.TEIF7 = BitField(self, 0x08000000, "TEIF7", "TEIF7")
        self.HTIF7 = BitField(self, 0x04000000, "HTIF7", "HTIF7")
        self.TCIF7 = BitField(self, 0x02000000, "TCIF7", "TCIF7")
        self.GIF7 = BitField(self, 0x01000000, "GIF7", "GIF7")
        self.TEIF6 = BitField(self, 0x00800000, "TEIF6", "TEIF6")
        self.HTIF6 = BitField(self, 0x00400000, "HTIF6", "HTIF6")
        self.TCIF6 = BitField(self, 0x00200000, "TCIF6", "TCIF6")
        self.GIF6 = BitField(self, 0x00100000, "GIF6", "GIF6")
        self.TEIF5 = BitField(self, 0x00080000, "TEIF5", "TEIF5")
        self.HTIF5 = BitField(self, 0x00040000, "HTIF5", "HTIF5")
        self.TCIF5 = BitField(self, 0x00020000, "TCIF5", "TCIF5")
        self.GIF5 = BitField(self, 0x00010000, "GIF5", "GIF5")
        self.TEIF4 = BitField(self, 0x00008000, "TEIF4", "TEIF4")
        self.HTIF4 = BitField(self, 0x00004000, "HTIF4", "HTIF4")
        self.TCIF4 = BitField(self, 0x00002000, "TCIF4", "TCIF4")
        self.GIF4 = BitField(self, 0x00001000, "GIF4", "GIF4")
        self.TEIF3 = BitField(self, 0x00000800, "TEIF3", "TEIF3")
        self.HTIF3 = BitField(self, 0x00000400, "HTIF3", "HTIF3")
        self.TCIF3 = BitField(self, 0x00000200, "TCIF3", "TCIF3")
        self.GIF3 = BitField(self, 0x00000100, "GIF3", "GIF3")
        self.TEIF2 = BitField(self, 0x00000080, "TEIF2", "TEIF2")
        self.HTIF2 = BitField(self, 0x00000040, "HTIF2", "HTIF2")
        self.TCIF2 = BitField(self, 0x00000020, "TCIF2", "TCIF2")
        self.GIF2 = BitField(self, 0x00000010, "GIF2", "GIF2")
        self.TEIF1 = BitField(self, 0x00000008, "TEIF1", "TEIF1")
        self.HTIF1 = BitField(self, 0x00000004, "HTIF1", "HTIF1")
        self.TCIF1 = BitField(self, 0x00000002, "TCIF1", "TCIF1")
        self.GIF1 = BitField(self, 0x00000001, "GIF1", "GIF1")
        self.HTIF = Subscriptor(self, "HTIF{}")
        self.TEIF = Subscriptor(self, "TEIF{}")
        self.TCIF = Subscriptor(self, "TCIF{}")
        self.GIF = Subscriptor(self, "GIF{}")

class SA_DMA1_IFCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IFCR", "DMA interrupt flag clear register")
        self.TEIF8 = BitField(self, 0x80000000, "TEIF8", "TEIF8")
        self.HTIF8 = BitField(self, 0x40000000, "HTIF8", "HTIF8")
        self.TCIF8 = BitField(self, 0x20000000, "TCIF8", "TCIF8")
        self.GIF8 = BitField(self, 0x10000000, "GIF8", "GIF8")
        self.TEIF7 = BitField(self, 0x08000000, "TEIF7", "TEIF7")
        self.HTIF7 = BitField(self, 0x04000000, "HTIF7", "HTIF7")
        self.TCIF7 = BitField(self, 0x02000000, "TCIF7", "TCIF7")
        self.GIF7 = BitField(self, 0x01000000, "GIF7", "GIF7")
        self.TEIF6 = BitField(self, 0x00800000, "TEIF6", "TEIF6")
        self.HTIF6 = BitField(self, 0x00400000, "HTIF6", "HTIF6")
        self.TCIF6 = BitField(self, 0x00200000, "TCIF6", "TCIF6")
        self.GIF6 = BitField(self, 0x00100000, "GIF6", "GIF6")
        self.TEIF5 = BitField(self, 0x00080000, "TEIF5", "TEIF5")
        self.HTIF5 = BitField(self, 0x00040000, "HTIF5", "HTIF5")
        self.TCIF5 = BitField(self, 0x00020000, "TCIF5", "TCIF5")
        self.GIF5 = BitField(self, 0x00010000, "GIF5", "GIF5")
        self.TEIF4 = BitField(self, 0x00008000, "TEIF4", "TEIF4")
        self.HTIF4 = BitField(self, 0x00004000, "HTIF4", "HTIF4")
        self.TCIF4 = BitField(self, 0x00002000, "TCIF4", "TCIF4")
        self.GIF4 = BitField(self, 0x00001000, "GIF4", "GIF4")
        self.TEIF3 = BitField(self, 0x00000800, "TEIF3", "TEIF3")
        self.HTIF3 = BitField(self, 0x00000400, "HTIF3", "HTIF3")
        self.TCIF3 = BitField(self, 0x00000200, "TCIF3", "TCIF3")
        self.GIF3 = BitField(self, 0x00000100, "GIF3", "GIF3")
        self.TEIF2 = BitField(self, 0x00000080, "TEIF2", "TEIF2")
        self.HTIF2 = BitField(self, 0x00000040, "HTIF2", "HTIF2")
        self.TCIF2 = BitField(self, 0x00000020, "TCIF2", "TCIF2")
        self.GIF2 = BitField(self, 0x00000010, "GIF2", "GIF2")
        self.TEIF1 = BitField(self, 0x00000008, "TEIF1", "TEIF1")
        self.HTIF1 = BitField(self, 0x00000004, "HTIF1", "HTIF1")
        self.TCIF1 = BitField(self, 0x00000002, "TCIF1", "TCIF1")
        self.GIF1 = BitField(self, 0x00000001, "GIF1", "GIF1")
        self.HTIF = Subscriptor(self, "HTIF{}")
        self.TEIF = Subscriptor(self, "TEIF{}")
        self.TCIF = Subscriptor(self, "TCIF{}")
        self.GIF = Subscriptor(self, "GIF{}")

class SA_DMA1_CCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR1", "DMA channel 1 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR2", "DMA channel 2 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CCR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR3", "DMA channel 3 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CCR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR4", "DMA channel 3 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CCR5(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR5", "DMA channel 4 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CCR6(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR6", "DMA channel 5 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CCR7(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR7", "DMA channel 6 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CCR8(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR8", "DMA channel 7 configuration register")
        self.EN = BitField(self, 0x00000001, "EN", "channel enable")
        self.TCIE = BitField(self, 0x00000002, "TCIE", "TCIE")
        self.HTIE = BitField(self, 0x00000004, "HTIE", "HTIE")
        self.TEIE = BitField(self, 0x00000008, "TEIE", "TEIE")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.CIRC = BitField(self, 0x00000020, "CIRC", "CIRC")
        self.PINC = BitField(self, 0x00000040, "PINC", "PINC")
        self.MINC = BitField(self, 0x00000080, "MINC", "MINC")
        self.PSIZE = BitField(self, 0x00000300, "PSIZE", "PSIZE")
        self.MSIZE = BitField(self, 0x00000C00, "MSIZE", "MSIZE")
        self.PL = BitField(self, 0x00003000, "PL", "PL")
        self.MEM2MEM = BitField(self, 0x00004000, "MEM2MEM", "MEM2MEM")

class SA_DMA1_CNDTR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR1", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CNDTR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR2", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CNDTR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR3", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CNDTR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR4", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CNDTR5(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR5", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CNDTR6(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR6", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CNDTR7(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR7", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CNDTR8(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNDTR8", "channel x number of data to transfer register")
        self.NDT = BitField(self, 0x0000FFFF, "NDT", "Number of data items to transfer")

class SA_DMA1_CPAR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR1", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CPAR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR2", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CPAR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR3", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CPAR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR4", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CPAR5(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR5", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CPAR6(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR6", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CPAR7(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR7", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CPAR8(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPAR8", "DMA channel x peripheral address register")
        self.PA = BitField(self, 0xFFFFFFFF, "PA", "Peripheral address")

class SA_DMA1_CMAR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR1", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1_CMAR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR2", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1_CMAR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR3", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1_CMAR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR4", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1_CMAR5(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR5", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1_CMAR6(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR6", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1_CMAR7(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR7", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1_CMAR8(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMAR8", "DMA channel x memory address register")
        self.MA = BitField(self, 0xFFFFFFFF, "MA", "Memory 1 address (used in case of Double buffer mode)")

class SA_DMA1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "DMA controller")
        self.ISR = SA_DMA1_ISR(self, 0x0)
        self.IFCR = SA_DMA1_IFCR(self, 0x4)
        self.CCR1 = SA_DMA1_CCR1(self, 0x8)
        self.CCR2 = SA_DMA1_CCR2(self, 0x1C)
        self.CCR3 = SA_DMA1_CCR3(self, 0x30)
        self.CCR4 = SA_DMA1_CCR4(self, 0x44)
        self.CCR5 = SA_DMA1_CCR5(self, 0x58)
        self.CCR6 = SA_DMA1_CCR6(self, 0x6C)
        self.CCR7 = SA_DMA1_CCR7(self, 0x80)
        self.CCR8 = SA_DMA1_CCR8(self, 0x94)
        self.CNDTR1 = SA_DMA1_CNDTR1(self, 0xC)
        self.CNDTR2 = SA_DMA1_CNDTR2(self, 0x20)
        self.CNDTR3 = SA_DMA1_CNDTR3(self, 0x34)
        self.CNDTR4 = SA_DMA1_CNDTR4(self, 0x48)
        self.CNDTR5 = SA_DMA1_CNDTR5(self, 0x5C)
        self.CNDTR6 = SA_DMA1_CNDTR6(self, 0x70)
        self.CNDTR7 = SA_DMA1_CNDTR7(self, 0x84)
        self.CNDTR8 = SA_DMA1_CNDTR8(self, 0x98)
        self.CPAR1 = SA_DMA1_CPAR1(self, 0x10)
        self.CPAR2 = SA_DMA1_CPAR2(self, 0x24)
        self.CPAR3 = SA_DMA1_CPAR3(self, 0x38)
        self.CPAR4 = SA_DMA1_CPAR4(self, 0x4C)
        self.CPAR5 = SA_DMA1_CPAR5(self, 0x60)
        self.CPAR6 = SA_DMA1_CPAR6(self, 0x74)
        self.CPAR7 = SA_DMA1_CPAR7(self, 0x88)
        self.CPAR8 = SA_DMA1_CPAR8(self, 0x9C)
        self.CMAR1 = SA_DMA1_CMAR1(self, 0x14)
        self.CMAR2 = SA_DMA1_CMAR2(self, 0x28)
        self.CMAR3 = SA_DMA1_CMAR3(self, 0x3C)
        self.CMAR4 = SA_DMA1_CMAR4(self, 0x50)
        self.CMAR5 = SA_DMA1_CMAR5(self, 0x64)
        self.CMAR6 = SA_DMA1_CMAR6(self, 0x78)
        self.CMAR7 = SA_DMA1_CMAR7(self, 0x8C)
        self.CMAR8 = SA_DMA1_CMAR8(self, 0xA0)
        self.CCR = Subscriptor(self, "CCR{}")
        self.CMAR = Subscriptor(self, "CMAR{}")
        self.CNDTR = Subscriptor(self, "CNDTR{}")
        self.CPAR = Subscriptor(self, "CPAR{}")

DMA1 = SA_DMA1(0x40020000, "DMA1")
DMA2 = SA_DMA1(0x40020400, "DMA2")

class SA_DMAMUX_C0CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C0CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C1CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C1CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C2CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C2CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C3CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C3CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C4CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C4CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C5CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C5CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C6CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C6CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C7CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C7CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C8CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C8CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C9CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C9CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C10CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C10CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C11CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C11CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C12CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C12CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C13CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C13CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C14CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C14CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_C15CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C15CR", "DMAMux - DMA request line multiplexer channel x control register")
        self.DMAREQ_ID = BitField(self, 0x0000007F, "DMAREQ_ID", "Input DMA request line selected")
        self.SOIE = BitField(self, 0x00000100, "SOIE", "Interrupt enable at synchronization event overrun")
        self.EGE = BitField(self, 0x00000200, "EGE", "Event generation enable/disable")
        self.SE = BitField(self, 0x00010000, "SE", "Synchronous operating mode enable/disable")
        self.SPOL = BitField(self, 0x00060000, "SPOL", "Synchronization event type selector Defines the synchronization event on the selected synchronization input:")
        self.NBREQ = BitField(self, 0x00F80000, "NBREQ", "Number of DMA requests to forward Defines the number of DMA requests forwarded before output event is generated. In synchronous mode, it also defines the number of DMA requests to forward after a synchronization event, then stop forwarding. The actual number of DMA requests forwarded is NBREQ+1. Note: This field can only be written when both SE and EGE bits are reset.")
        self.SYNC_ID = BitField(self, 0x1F000000, "SYNC_ID", "Synchronization input selected")

class SA_DMAMUX_RG0CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RG0CR", "DMAMux - DMA request generator channel x control register")
        self.SIG_ID = BitField(self, 0x0000001F, "SIG_ID", "DMA request trigger input selected")
        self.OIE = BitField(self, 0x00000100, "OIE", "Interrupt enable at trigger event overrun")
        self.GE = BitField(self, 0x00010000, "GE", "DMA request generator channel enable/disable")
        self.GPOL = BitField(self, 0x00060000, "GPOL", "DMA request generator trigger event type selection Defines the trigger event on the selected DMA request trigger input")
        self.GNBREQ = BitField(self, 0x00F80000, "GNBREQ", "Number of DMA requests to generate Defines the number of DMA requests generated after a trigger event, then stop generating. The actual number of generated DMA requests is GNBREQ+1. Note: This field can only be written when GE bit is reset.")

class SA_DMAMUX_RG1CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RG1CR", "DMAMux - DMA request generator channel x control register")
        self.SIG_ID = BitField(self, 0x0000001F, "SIG_ID", "DMA request trigger input selected")
        self.OIE = BitField(self, 0x00000100, "OIE", "Interrupt enable at trigger event overrun")
        self.GE = BitField(self, 0x00010000, "GE", "DMA request generator channel enable/disable")
        self.GPOL = BitField(self, 0x00060000, "GPOL", "DMA request generator trigger event type selection Defines the trigger event on the selected DMA request trigger input")
        self.GNBREQ = BitField(self, 0x00F80000, "GNBREQ", "Number of DMA requests to generate Defines the number of DMA requests generated after a trigger event, then stop generating. The actual number of generated DMA requests is GNBREQ+1. Note: This field can only be written when GE bit is reset.")

class SA_DMAMUX_RG2CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RG2CR", "DMAMux - DMA request generator channel x control register")
        self.SIG_ID = BitField(self, 0x0000001F, "SIG_ID", "DMA request trigger input selected")
        self.OIE = BitField(self, 0x00000100, "OIE", "Interrupt enable at trigger event overrun")
        self.GE = BitField(self, 0x00010000, "GE", "DMA request generator channel enable/disable")
        self.GPOL = BitField(self, 0x00060000, "GPOL", "DMA request generator trigger event type selection Defines the trigger event on the selected DMA request trigger input")
        self.GNBREQ = BitField(self, 0x00F80000, "GNBREQ", "Number of DMA requests to generate Defines the number of DMA requests generated after a trigger event, then stop generating. The actual number of generated DMA requests is GNBREQ+1. Note: This field can only be written when GE bit is reset.")

class SA_DMAMUX_RG3CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RG3CR", "DMAMux - DMA request generator channel x control register")
        self.SIG_ID = BitField(self, 0x0000001F, "SIG_ID", "DMA request trigger input selected")
        self.OIE = BitField(self, 0x00000100, "OIE", "Interrupt enable at trigger event overrun")
        self.GE = BitField(self, 0x00010000, "GE", "DMA request generator channel enable/disable")
        self.GPOL = BitField(self, 0x00060000, "GPOL", "DMA request generator trigger event type selection Defines the trigger event on the selected DMA request trigger input")
        self.GNBREQ = BitField(self, 0x00F80000, "GNBREQ", "Number of DMA requests to generate Defines the number of DMA requests generated after a trigger event, then stop generating. The actual number of generated DMA requests is GNBREQ+1. Note: This field can only be written when GE bit is reset.")

class SA_DMAMUX_RGSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RGSR", "DMAMux - DMA request generator status register")
        self.OF = BitField(self, 0x0000000F, "OF", "Trigger event overrun flag The flag is set when a trigger event occurs on DMA request generator channel x, while the DMA request generator counter value is lower than GNBREQ. The flag is cleared by writing 1 to the corresponding COFx bit in DMAMUX_RGCFR register.")

class SA_DMAMUX_RGCFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RGCFR", "DMAMux - DMA request generator clear flag register")
        self.COF = BitField(self, 0x0000000F, "COF", "Clear trigger event overrun flag Upon setting, this bit clears the corresponding overrun flag OFx in the DMAMUX_RGCSR register.")

class SA_DMAMUX_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CSR", "DMAMUX request line multiplexer interrupt channel status register")
        self.SOF = BitField(self, 0x0000FFFF, "SOF", "Synchronization overrun event flag")

class SA_DMAMUX_CFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CFR", "DMAMUX request line multiplexer interrupt clear flag register")
        self.CSOF = BitField(self, 0x0000FFFF, "CSOF", "Clear synchronization overrun event flag")

class SA_DMAMUX(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "DMAMUX")
        self.C0CR = SA_DMAMUX_C0CR(self, 0x0)
        self.C1CR = SA_DMAMUX_C1CR(self, 0x4)
        self.C2CR = SA_DMAMUX_C2CR(self, 0x8)
        self.C3CR = SA_DMAMUX_C3CR(self, 0xC)
        self.C4CR = SA_DMAMUX_C4CR(self, 0x10)
        self.C5CR = SA_DMAMUX_C5CR(self, 0x14)
        self.C6CR = SA_DMAMUX_C6CR(self, 0x18)
        self.C7CR = SA_DMAMUX_C7CR(self, 0x1C)
        self.C8CR = SA_DMAMUX_C8CR(self, 0x20)
        self.C9CR = SA_DMAMUX_C9CR(self, 0x24)
        self.C10CR = SA_DMAMUX_C10CR(self, 0x28)
        self.C11CR = SA_DMAMUX_C11CR(self, 0x2C)
        self.C12CR = SA_DMAMUX_C12CR(self, 0x30)
        self.C13CR = SA_DMAMUX_C13CR(self, 0x34)
        self.C14CR = SA_DMAMUX_C14CR(self, 0x38)
        self.C15CR = SA_DMAMUX_C15CR(self, 0x3C)
        self.RG0CR = SA_DMAMUX_RG0CR(self, 0x100)
        self.RG1CR = SA_DMAMUX_RG1CR(self, 0x104)
        self.RG2CR = SA_DMAMUX_RG2CR(self, 0x108)
        self.RG3CR = SA_DMAMUX_RG3CR(self, 0x10C)
        self.RGSR = SA_DMAMUX_RGSR(self, 0x140)
        self.RGCFR = SA_DMAMUX_RGCFR(self, 0x144)
        self.CSR = SA_DMAMUX_CSR(self, 0x80)
        self.CFR = SA_DMAMUX_CFR(self, 0x84)
        self.CCR = Subscriptor(self, "C{}CR")
        self.RGCR = Subscriptor(self, "RG{}CR")

DMAMUX = SA_DMAMUX(0x40020800, "DMAMUX")

class SA_SYSCFG_MEMRMP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MEMRMP", "Remap Memory register")
        self.MEM_MODE = BitField(self, 0x00000007, "MEM_MODE", "Memory mapping selection")
        self.FB_mode = BitField(self, 0x00000100, "FB_mode", "User Flash Bank mode")

class SA_SYSCFG_CFGR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7C000001, "CFGR1", "peripheral mode configuration register")
        self.BOOSTEN = BitField(self, 0x00000100, "BOOSTEN", "BOOSTEN")
        self.ANASWVDD = BitField(self, 0x00000200, "ANASWVDD", "GPIO analog switch control voltage selection")
        self.I2C_PB6_FMP = BitField(self, 0x00010000, "I2C_PB6_FMP", "FM+ drive capability on PB6")
        self.I2C_PB7_FMP = BitField(self, 0x00020000, "I2C_PB7_FMP", "FM+ drive capability on PB6")
        self.I2C_PB8_FMP = BitField(self, 0x00040000, "I2C_PB8_FMP", "FM+ drive capability on PB6")
        self.I2C_PB9_FMP = BitField(self, 0x00080000, "I2C_PB9_FMP", "FM+ drive capability on PB6")
        self.I2C1_FMP = BitField(self, 0x00100000, "I2C1_FMP", "I2C1 FM+ drive capability enable")
        self.I2C2_FMP = BitField(self, 0x00200000, "I2C2_FMP", "I2C1 FM+ drive capability enable")
        self.I2C3_FMP = BitField(self, 0x00400000, "I2C3_FMP", "I2C1 FM+ drive capability enable")
        self.I2C4_FMP = BitField(self, 0x00800000, "I2C4_FMP", "I2C1 FM+ drive capability enable")
        self.FPU_IE = BitField(self, 0xFC000000, "FPU_IE", "FPU Interrupts Enable")
        self.I2C_FMP = Subscriptor(self, "I2C{}_FMP")
        self.I2C_PB_FMP = Subscriptor(self, "I2C_PB{}_FMP")

class SA_SYSCFG_EXTICR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EXTICR1", "external interrupt configuration register 1")
        self.EXTI3 = BitField(self, 0x0000F000, "EXTI3", "EXTI x configuration (x = 0 to 3)")
        self.EXTI2 = BitField(self, 0x00000F00, "EXTI2", "EXTI x configuration (x = 0 to 3)")
        self.EXTI1 = BitField(self, 0x000000F0, "EXTI1", "EXTI x configuration (x = 0 to 3)")
        self.EXTI0 = BitField(self, 0x0000000F, "EXTI0", "EXTI x configuration (x = 0 to 3)")
        self.EXTI = Subscriptor(self, "EXTI{}")

class SA_SYSCFG_EXTICR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EXTICR2", "external interrupt configuration register 2")
        self.EXTI7 = BitField(self, 0x0000F000, "EXTI7", "EXTI x configuration (x = 4 to 7)")
        self.EXTI6 = BitField(self, 0x00000F00, "EXTI6", "EXTI x configuration (x = 4 to 7)")
        self.EXTI5 = BitField(self, 0x000000F0, "EXTI5", "EXTI x configuration (x = 4 to 7)")
        self.EXTI4 = BitField(self, 0x0000000F, "EXTI4", "EXTI x configuration (x = 4 to 7)")
        self.EXTI = Subscriptor(self, "EXTI{}")

class SA_SYSCFG_EXTICR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EXTICR3", "external interrupt configuration register 3")
        self.EXTI11 = BitField(self, 0x0000F000, "EXTI11", "EXTI x configuration (x = 8 to 11)")
        self.EXTI10 = BitField(self, 0x00000F00, "EXTI10", "EXTI10")
        self.EXTI9 = BitField(self, 0x000000F0, "EXTI9", "EXTI x configuration (x = 8 to 11)")
        self.EXTI8 = BitField(self, 0x0000000F, "EXTI8", "EXTI x configuration (x = 8 to 11)")
        self.EXTI = Subscriptor(self, "EXTI{}")

class SA_SYSCFG_EXTICR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EXTICR4", "external interrupt configuration register 4")
        self.EXTI15 = BitField(self, 0x0000F000, "EXTI15", "EXTI x configuration (x = 12 to 15)")
        self.EXTI14 = BitField(self, 0x00000F00, "EXTI14", "EXTI x configuration (x = 12 to 15)")
        self.EXTI13 = BitField(self, 0x000000F0, "EXTI13", "EXTI x configuration (x = 12 to 15)")
        self.EXTI12 = BitField(self, 0x0000000F, "EXTI12", "EXTI x configuration (x = 12 to 15)")
        self.EXTI = Subscriptor(self, "EXTI{}")

class SA_SYSCFG_SCSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SCSR", "CCM SRAM control and status register")
        self.CCMER = BitField(self, 0x00000001, "CCMER", "CCM SRAM Erase")
        self.CCMBSY = BitField(self, 0x00000002, "CCMBSY", "CCM SRAM busy by erase operation")

class SA_SYSCFG_CFGR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CFGR2", "configuration register 2")
        self.CLL = BitField(self, 0x00000001, "CLL", "Core Lockup Lock")
        self.SPL = BitField(self, 0x00000002, "SPL", "SRAM Parity Lock")
        self.PVDL = BitField(self, 0x00000004, "PVDL", "PVD Lock")
        self.ECCL = BitField(self, 0x00000008, "ECCL", "ECC Lock")
        self.SPF = BitField(self, 0x00000100, "SPF", "SRAM Parity Flag")

class SA_SYSCFG_SWPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SWPR", "SRAM Write protection register 1")
        self.Page0_WP = BitField(self, 0x00000001, "Page0_WP", "Write protection")
        self.Page1_WP = BitField(self, 0x00000002, "Page1_WP", "Write protection")
        self.Page2_WP = BitField(self, 0x00000004, "Page2_WP", "Write protection")
        self.Page3_WP = BitField(self, 0x00000008, "Page3_WP", "Write protection")
        self.Page4_WP = BitField(self, 0x00000010, "Page4_WP", "Write protection")
        self.Page5_WP = BitField(self, 0x00000020, "Page5_WP", "Write protection")
        self.Page6_WP = BitField(self, 0x00000040, "Page6_WP", "Write protection")
        self.Page7_WP = BitField(self, 0x00000080, "Page7_WP", "Write protection")
        self.Page8_WP = BitField(self, 0x00000100, "Page8_WP", "Write protection")
        self.Page9_WP = BitField(self, 0x00000200, "Page9_WP", "Write protection")
        self.Page10_WP = BitField(self, 0x00000400, "Page10_WP", "Write protection")
        self.Page11_WP = BitField(self, 0x00000800, "Page11_WP", "Write protection")
        self.Page12_WP = BitField(self, 0x00001000, "Page12_WP", "Write protection")
        self.Page13_WP = BitField(self, 0x00002000, "Page13_WP", "Write protection")
        self.Page14_WP = BitField(self, 0x00004000, "Page14_WP", "Write protection")
        self.Page15_WP = BitField(self, 0x00008000, "Page15_WP", "Write protection")
        self.Page16_WP = BitField(self, 0x00010000, "Page16_WP", "Write protection")
        self.Page17_WP = BitField(self, 0x00020000, "Page17_WP", "Write protection")
        self.Page18_WP = BitField(self, 0x00040000, "Page18_WP", "Write protection")
        self.Page19_WP = BitField(self, 0x00080000, "Page19_WP", "Write protection")
        self.Page20_WP = BitField(self, 0x00100000, "Page20_WP", "Write protection")
        self.Page21_WP = BitField(self, 0x00200000, "Page21_WP", "Write protection")
        self.Page22_WP = BitField(self, 0x00400000, "Page22_WP", "Write protection")
        self.Page23_WP = BitField(self, 0x00800000, "Page23_WP", "Write protection")
        self.Page24_WP = BitField(self, 0x01000000, "Page24_WP", "Write protection")
        self.Page25_WP = BitField(self, 0x02000000, "Page25_WP", "Write protection")
        self.Page26_WP = BitField(self, 0x04000000, "Page26_WP", "Write protection")
        self.Page27_WP = BitField(self, 0x08000000, "Page27_WP", "Write protection")
        self.Page28_WP = BitField(self, 0x10000000, "Page28_WP", "Write protection")
        self.Page29_WP = BitField(self, 0x20000000, "Page29_WP", "Write protection")
        self.Page30_WP = BitField(self, 0x40000000, "Page30_WP", "Write protection")
        self.Page31_WP = BitField(self, 0x80000000, "Page31_WP", "Write protection")
        self.Page_WP = Subscriptor(self, "Page{}_WP")

class SA_SYSCFG_SKR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SKR", "SRAM2 Key Register")
        self.KEY = BitField(self, 0x000000FF, "KEY", "SRAM2 Key for software erase")

class SA_SYSCFG(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "System configuration controller")
        self.MEMRMP = SA_SYSCFG_MEMRMP(self, 0x0)
        self.CFGR1 = SA_SYSCFG_CFGR1(self, 0x4)
        self.EXTICR1 = SA_SYSCFG_EXTICR1(self, 0x8)
        self.EXTICR2 = SA_SYSCFG_EXTICR2(self, 0xC)
        self.EXTICR3 = SA_SYSCFG_EXTICR3(self, 0x10)
        self.EXTICR4 = SA_SYSCFG_EXTICR4(self, 0x14)
        self.SCSR = SA_SYSCFG_SCSR(self, 0x18)
        self.CFGR2 = SA_SYSCFG_CFGR2(self, 0x1C)
        self.SWPR = SA_SYSCFG_SWPR(self, 0x20)
        self.SKR = SA_SYSCFG_SKR(self, 0x24)
        self.EXTICR = Subscriptor(self, "EXTICR{}")
        self.CFGR = Subscriptor(self, "CFGR{}")

SYSCFG = SA_SYSCFG(0x40010000, "SYSCFG")

class SA_VREFBUF_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x2, "CSR", "VREF_BUF Control and Status Register")
        self.ENVR = BitField(self, 0x00000001, "ENVR", "Enable Voltage Reference")
        self.HIZ = BitField(self, 0x00000002, "HIZ", "High impedence mode for the VREF_BUF")
        self.VRR = BitField(self, 0x00000008, "VRR", "Voltage reference buffer ready")
        self.VRS = BitField(self, 0x00000030, "VRS", "Voltage reference scale")

class SA_VREFBUF_CCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR", "VREF_BUF Calibration Control Register")
        self.TRIM = BitField(self, 0x0000003F, "TRIM", "Trimming code")

class SA_VREFBUF(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Voltage reference buffer")
        self.CSR = SA_VREFBUF_CSR(self, 0x0)
        self.CCR = SA_VREFBUF_CCR(self, 0x4)

VREFBUF = SA_VREFBUF(0x40010030, "VREFBUF")

class SA_COMP_C1CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C1CSR", "Comparator control/status register")
        self.EN = BitField(self, 0x00000001, "EN", "EN")
        self.INMSEL = BitField(self, 0x00000070, "INMSEL", "INMSEL")
        self.INPSEL = BitField(self, 0x00000100, "INPSEL", "INPSEL")
        self.POL = BitField(self, 0x00008000, "POL", "POL")
        self.HYST = BitField(self, 0x00070000, "HYST", "HYST")
        self.BLANKSEL = BitField(self, 0x00380000, "BLANKSEL", "BLANKSEL")
        self.BRGEN = BitField(self, 0x00400000, "BRGEN", "BRGEN")
        self.SCALEN = BitField(self, 0x00800000, "SCALEN", "SCALEN")
        self.VALUE = BitField(self, 0x40000000, "VALUE", "VALUE")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_COMP_C2CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C2CSR", "Comparator control/status register")
        self.EN = BitField(self, 0x00000001, "EN", "EN")
        self.INMSEL = BitField(self, 0x00000070, "INMSEL", "INMSEL")
        self.INPSEL = BitField(self, 0x00000100, "INPSEL", "INPSEL")
        self.POL = BitField(self, 0x00008000, "POL", "POL")
        self.HYST = BitField(self, 0x00070000, "HYST", "HYST")
        self.BLANKSEL = BitField(self, 0x00380000, "BLANKSEL", "BLANKSEL")
        self.BRGEN = BitField(self, 0x00400000, "BRGEN", "BRGEN")
        self.SCALEN = BitField(self, 0x00800000, "SCALEN", "SCALEN")
        self.VALUE = BitField(self, 0x40000000, "VALUE", "VALUE")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_COMP_C3CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C3CSR", "Comparator control/status register")
        self.EN = BitField(self, 0x00000001, "EN", "EN")
        self.INMSEL = BitField(self, 0x00000070, "INMSEL", "INMSEL")
        self.INPSEL = BitField(self, 0x00000100, "INPSEL", "INPSEL")
        self.POL = BitField(self, 0x00008000, "POL", "POL")
        self.HYST = BitField(self, 0x00070000, "HYST", "HYST")
        self.BLANKSEL = BitField(self, 0x00380000, "BLANKSEL", "BLANKSEL")
        self.BRGEN = BitField(self, 0x00400000, "BRGEN", "BRGEN")
        self.SCALEN = BitField(self, 0x00800000, "SCALEN", "SCALEN")
        self.VALUE = BitField(self, 0x40000000, "VALUE", "VALUE")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_COMP_C4CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C4CSR", "Comparator control/status register")
        self.EN = BitField(self, 0x00000001, "EN", "EN")
        self.INMSEL = BitField(self, 0x00000070, "INMSEL", "INMSEL")
        self.INPSEL = BitField(self, 0x00000100, "INPSEL", "INPSEL")
        self.POL = BitField(self, 0x00008000, "POL", "POL")
        self.HYST = BitField(self, 0x00070000, "HYST", "HYST")
        self.BLANKSEL = BitField(self, 0x00380000, "BLANKSEL", "BLANKSEL")
        self.BRGEN = BitField(self, 0x00400000, "BRGEN", "BRGEN")
        self.SCALEN = BitField(self, 0x00800000, "SCALEN", "SCALEN")
        self.VALUE = BitField(self, 0x40000000, "VALUE", "VALUE")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_COMP_C5CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C5CSR", "Comparator control/status register")
        self.EN = BitField(self, 0x00000001, "EN", "EN")
        self.INMSEL = BitField(self, 0x00000070, "INMSEL", "INMSEL")
        self.INPSEL = BitField(self, 0x00000100, "INPSEL", "INPSEL")
        self.POL = BitField(self, 0x00008000, "POL", "POL")
        self.HYST = BitField(self, 0x00070000, "HYST", "HYST")
        self.BLANKSEL = BitField(self, 0x00380000, "BLANKSEL", "BLANKSEL")
        self.BRGEN = BitField(self, 0x00400000, "BRGEN", "BRGEN")
        self.SCALEN = BitField(self, 0x00800000, "SCALEN", "SCALEN")
        self.VALUE = BitField(self, 0x40000000, "VALUE", "VALUE")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_COMP_C6CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C6CSR", "Comparator control/status register")
        self.EN = BitField(self, 0x00000001, "EN", "EN")
        self.INMSEL = BitField(self, 0x00000070, "INMSEL", "INMSEL")
        self.INPSEL = BitField(self, 0x00000100, "INPSEL", "INPSEL")
        self.POL = BitField(self, 0x00008000, "POL", "POL")
        self.HYST = BitField(self, 0x00070000, "HYST", "HYST")
        self.BLANKSEL = BitField(self, 0x00380000, "BLANKSEL", "BLANKSEL")
        self.BRGEN = BitField(self, 0x00400000, "BRGEN", "BRGEN")
        self.SCALEN = BitField(self, 0x00800000, "SCALEN", "SCALEN")
        self.VALUE = BitField(self, 0x40000000, "VALUE", "VALUE")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_COMP_C7CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "C7CSR", "Comparator control/status register")
        self.EN = BitField(self, 0x00000001, "EN", "EN")
        self.INMSEL = BitField(self, 0x00000070, "INMSEL", "INMSEL")
        self.INPSEL = BitField(self, 0x00000100, "INPSEL", "INPSEL")
        self.POL = BitField(self, 0x00008000, "POL", "POL")
        self.HYST = BitField(self, 0x00070000, "HYST", "HYST")
        self.BLANKSEL = BitField(self, 0x00380000, "BLANKSEL", "BLANKSEL")
        self.BRGEN = BitField(self, 0x00400000, "BRGEN", "BRGEN")
        self.SCALEN = BitField(self, 0x00800000, "SCALEN", "SCALEN")
        self.VALUE = BitField(self, 0x40000000, "VALUE", "VALUE")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_COMP(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Comparator control and status register")
        self.C1CSR = SA_COMP_C1CSR(self, 0x0)
        self.C2CSR = SA_COMP_C2CSR(self, 0x4)
        self.C3CSR = SA_COMP_C3CSR(self, 0x8)
        self.C4CSR = SA_COMP_C4CSR(self, 0xC)
        self.C5CSR = SA_COMP_C5CSR(self, 0x10)
        self.C6CSR = SA_COMP_C6CSR(self, 0x14)
        self.C7CSR = SA_COMP_C7CSR(self, 0x18)
        self.CCSR = Subscriptor(self, "C{}CSR")

COMP = SA_COMP(0x40010200, "COMP")

class SA_OPAMP_OPAMP1_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP1_CSR", "OPAMP1 control/status register")
        self.OPAEN = BitField(self, 0x00000001, "OPAEN", "Operational amplifier Enable")
        self.FORCE_VP = BitField(self, 0x00000002, "FORCE_VP", "FORCE_VP")
        self.VP_SEL = BitField(self, 0x0000000C, "VP_SEL", "VP_SEL")
        self.USERTRIM = BitField(self, 0x00000010, "USERTRIM", "USERTRIM")
        self.VM_SEL = BitField(self, 0x00000060, "VM_SEL", "VM_SEL")
        self.OPAHSM = BitField(self, 0x00000080, "OPAHSM", "OPAHSM")
        self.OPAINTOEN = BitField(self, 0x00000100, "OPAINTOEN", "OPAINTOEN")
        self.CALON = BitField(self, 0x00000800, "CALON", "CALON")
        self.CALSEL = BitField(self, 0x00003000, "CALSEL", "CALSEL")
        self.PGA_GAIN = BitField(self, 0x0007C000, "PGA_GAIN", "PGA_GAIN")
        self.TRIMOFFSETP = BitField(self, 0x00F80000, "TRIMOFFSETP", "TRIMOFFSETP")
        self.TRIMOFFSETN = BitField(self, 0x1F000000, "TRIMOFFSETN", "TRIMOFFSETN")
        self.CALOUT = BitField(self, 0x40000000, "CALOUT", "CALOUT")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP2_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP2_CSR", "OPAMP2 control/status register")
        self.OPAEN = BitField(self, 0x00000001, "OPAEN", "Operational amplifier Enable")
        self.FORCE_VP = BitField(self, 0x00000002, "FORCE_VP", "FORCE_VP")
        self.VP_SEL = BitField(self, 0x0000000C, "VP_SEL", "VP_SEL")
        self.USERTRIM = BitField(self, 0x00000010, "USERTRIM", "USERTRIM")
        self.VM_SEL = BitField(self, 0x00000060, "VM_SEL", "VM_SEL")
        self.OPAHSM = BitField(self, 0x00000080, "OPAHSM", "OPAHSM")
        self.OPAINTOEN = BitField(self, 0x00000100, "OPAINTOEN", "OPAINTOEN")
        self.CALON = BitField(self, 0x00000800, "CALON", "CALON")
        self.CALSEL = BitField(self, 0x00003000, "CALSEL", "CALSEL")
        self.PGA_GAIN = BitField(self, 0x0007C000, "PGA_GAIN", "PGA_GAIN")
        self.TRIMOFFSETP = BitField(self, 0x00F80000, "TRIMOFFSETP", "TRIMOFFSETP")
        self.TRIMOFFSETN = BitField(self, 0x1F000000, "TRIMOFFSETN", "TRIMOFFSETN")
        self.CALOUT = BitField(self, 0x40000000, "CALOUT", "CALOUT")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP3_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP3_CSR", "OPAMP3 control/status register")
        self.OPAEN = BitField(self, 0x00000001, "OPAEN", "Operational amplifier Enable")
        self.FORCE_VP = BitField(self, 0x00000002, "FORCE_VP", "FORCE_VP")
        self.VP_SEL = BitField(self, 0x0000000C, "VP_SEL", "VP_SEL")
        self.USERTRIM = BitField(self, 0x00000010, "USERTRIM", "USERTRIM")
        self.VM_SEL = BitField(self, 0x00000060, "VM_SEL", "VM_SEL")
        self.OPAHSM = BitField(self, 0x00000080, "OPAHSM", "OPAHSM")
        self.OPAINTOEN = BitField(self, 0x00000100, "OPAINTOEN", "OPAINTOEN")
        self.CALON = BitField(self, 0x00000800, "CALON", "CALON")
        self.CALSEL = BitField(self, 0x00003000, "CALSEL", "CALSEL")
        self.PGA_GAIN = BitField(self, 0x0007C000, "PGA_GAIN", "PGA_GAIN")
        self.TRIMOFFSETP = BitField(self, 0x00F80000, "TRIMOFFSETP", "TRIMOFFSETP")
        self.TRIMOFFSETN = BitField(self, 0x1F000000, "TRIMOFFSETN", "TRIMOFFSETN")
        self.CALOUT = BitField(self, 0x40000000, "CALOUT", "CALOUT")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP4_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP4_CSR", "OPAMP4 control/status register")
        self.OPAEN = BitField(self, 0x00000001, "OPAEN", "Operational amplifier Enable")
        self.FORCE_VP = BitField(self, 0x00000002, "FORCE_VP", "FORCE_VP")
        self.VP_SEL = BitField(self, 0x0000000C, "VP_SEL", "VP_SEL")
        self.USERTRIM = BitField(self, 0x00000010, "USERTRIM", "USERTRIM")
        self.VM_SEL = BitField(self, 0x00000060, "VM_SEL", "VM_SEL")
        self.OPAHSM = BitField(self, 0x00000080, "OPAHSM", "OPAHSM")
        self.OPAINTOEN = BitField(self, 0x00000100, "OPAINTOEN", "OPAINTOEN")
        self.CALON = BitField(self, 0x00000800, "CALON", "CALON")
        self.CALSEL = BitField(self, 0x00003000, "CALSEL", "CALSEL")
        self.PGA_GAIN = BitField(self, 0x0007C000, "PGA_GAIN", "PGA_GAIN")
        self.TRIMOFFSETP = BitField(self, 0x00F80000, "TRIMOFFSETP", "TRIMOFFSETP")
        self.TRIMOFFSETN = BitField(self, 0x1F000000, "TRIMOFFSETN", "TRIMOFFSETN")
        self.CALOUT = BitField(self, 0x40000000, "CALOUT", "CALOUT")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP5_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP5_CSR", "OPAMP5 control/status register")
        self.OPAEN = BitField(self, 0x00000001, "OPAEN", "Operational amplifier Enable")
        self.FORCE_VP = BitField(self, 0x00000002, "FORCE_VP", "FORCE_VP")
        self.VP_SEL = BitField(self, 0x0000000C, "VP_SEL", "VP_SEL")
        self.USERTRIM = BitField(self, 0x00000010, "USERTRIM", "USERTRIM")
        self.VM_SEL = BitField(self, 0x00000060, "VM_SEL", "VM_SEL")
        self.OPAHSM = BitField(self, 0x00000080, "OPAHSM", "OPAHSM")
        self.OPAINTOEN = BitField(self, 0x00000100, "OPAINTOEN", "OPAINTOEN")
        self.CALON = BitField(self, 0x00000800, "CALON", "CALON")
        self.CALSEL = BitField(self, 0x00003000, "CALSEL", "CALSEL")
        self.PGA_GAIN = BitField(self, 0x0007C000, "PGA_GAIN", "PGA_GAIN")
        self.TRIMOFFSETP = BitField(self, 0x00F80000, "TRIMOFFSETP", "TRIMOFFSETP")
        self.TRIMOFFSETN = BitField(self, 0x1F000000, "TRIMOFFSETN", "TRIMOFFSETN")
        self.CALOUT = BitField(self, 0x40000000, "CALOUT", "CALOUT")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP6_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP6_CSR", "OPAMP6 control/status register")
        self.OPAEN = BitField(self, 0x00000001, "OPAEN", "Operational amplifier Enable")
        self.FORCE_VP = BitField(self, 0x00000002, "FORCE_VP", "FORCE_VP")
        self.VP_SEL = BitField(self, 0x0000000C, "VP_SEL", "VP_SEL")
        self.USERTRIM = BitField(self, 0x00000010, "USERTRIM", "USERTRIM")
        self.VM_SEL = BitField(self, 0x00000060, "VM_SEL", "VM_SEL")
        self.OPAHSM = BitField(self, 0x00000080, "OPAHSM", "OPAHSM")
        self.OPAINTOEN = BitField(self, 0x00000100, "OPAINTOEN", "OPAINTOEN")
        self.CALON = BitField(self, 0x00000800, "CALON", "CALON")
        self.CALSEL = BitField(self, 0x00003000, "CALSEL", "CALSEL")
        self.PGA_GAIN = BitField(self, 0x0007C000, "PGA_GAIN", "PGA_GAIN")
        self.TRIMOFFSETP = BitField(self, 0x00F80000, "TRIMOFFSETP", "TRIMOFFSETP")
        self.TRIMOFFSETN = BitField(self, 0x1F000000, "TRIMOFFSETN", "TRIMOFFSETN")
        self.CALOUT = BitField(self, 0x40000000, "CALOUT", "CALOUT")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP1_TCMR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP1_TCMR", "OPAMP1 control/status register")
        self.VMS_SEL = BitField(self, 0x00000001, "VMS_SEL", "VMS_SEL")
        self.VPS_SEL = BitField(self, 0x00000006, "VPS_SEL", "VPS_SEL")
        self.T1CM_EN = BitField(self, 0x00000008, "T1CM_EN", "T1CM_EN")
        self.T8CM_EN = BitField(self, 0x00000010, "T8CM_EN", "T8CM_EN")
        self.T20CM_EN = BitField(self, 0x00000020, "T20CM_EN", "T20CM_EN")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP2_TCMR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP2_TCMR", "OPAMP2 control/status register")
        self.VMS_SEL = BitField(self, 0x00000001, "VMS_SEL", "VMS_SEL")
        self.VPS_SEL = BitField(self, 0x00000006, "VPS_SEL", "VPS_SEL")
        self.T1CM_EN = BitField(self, 0x00000008, "T1CM_EN", "T1CM_EN")
        self.T8CM_EN = BitField(self, 0x00000010, "T8CM_EN", "T8CM_EN")
        self.T20CM_EN = BitField(self, 0x00000020, "T20CM_EN", "T20CM_EN")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP3_TCMR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP3_TCMR", "OPAMP3 control/status register")
        self.VMS_SEL = BitField(self, 0x00000001, "VMS_SEL", "VMS_SEL")
        self.VPS_SEL = BitField(self, 0x00000006, "VPS_SEL", "VPS_SEL")
        self.T1CM_EN = BitField(self, 0x00000008, "T1CM_EN", "T1CM_EN")
        self.T8CM_EN = BitField(self, 0x00000010, "T8CM_EN", "T8CM_EN")
        self.T20CM_EN = BitField(self, 0x00000020, "T20CM_EN", "T20CM_EN")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP4_TCMR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP4_TCMR", "OPAMP4 control/status register")
        self.VMS_SEL = BitField(self, 0x00000001, "VMS_SEL", "VMS_SEL")
        self.VPS_SEL = BitField(self, 0x00000006, "VPS_SEL", "VPS_SEL")
        self.T1CM_EN = BitField(self, 0x00000008, "T1CM_EN", "T1CM_EN")
        self.T8CM_EN = BitField(self, 0x00000010, "T8CM_EN", "T8CM_EN")
        self.T20CM_EN = BitField(self, 0x00000020, "T20CM_EN", "T20CM_EN")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP5_TCMR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP5_TCMR", "OPAMP5 control/status register")
        self.VMS_SEL = BitField(self, 0x00000001, "VMS_SEL", "VMS_SEL")
        self.VPS_SEL = BitField(self, 0x00000006, "VPS_SEL", "VPS_SEL")
        self.T1CM_EN = BitField(self, 0x00000008, "T1CM_EN", "T1CM_EN")
        self.T8CM_EN = BitField(self, 0x00000010, "T8CM_EN", "T8CM_EN")
        self.T20CM_EN = BitField(self, 0x00000020, "T20CM_EN", "T20CM_EN")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP_OPAMP6_TCMR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OPAMP6_TCMR", "OPAMP6 control/status register")
        self.VMS_SEL = BitField(self, 0x00000001, "VMS_SEL", "VMS_SEL")
        self.VPS_SEL = BitField(self, 0x00000006, "VPS_SEL", "VPS_SEL")
        self.T1CM_EN = BitField(self, 0x00000008, "T1CM_EN", "T1CM_EN")
        self.T8CM_EN = BitField(self, 0x00000010, "T8CM_EN", "T8CM_EN")
        self.T20CM_EN = BitField(self, 0x00000020, "T20CM_EN", "T20CM_EN")
        self.LOCK = BitField(self, 0x80000000, "LOCK", "LOCK")

class SA_OPAMP(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Operational amplifiers")
        self.OPAMP1_CSR = SA_OPAMP_OPAMP1_CSR(self, 0x0)
        self.OPAMP2_CSR = SA_OPAMP_OPAMP2_CSR(self, 0x4)
        self.OPAMP3_CSR = SA_OPAMP_OPAMP3_CSR(self, 0x8)
        self.OPAMP4_CSR = SA_OPAMP_OPAMP4_CSR(self, 0xC)
        self.OPAMP5_CSR = SA_OPAMP_OPAMP5_CSR(self, 0x10)
        self.OPAMP6_CSR = SA_OPAMP_OPAMP6_CSR(self, 0x14)
        self.OPAMP1_TCMR = SA_OPAMP_OPAMP1_TCMR(self, 0x18)
        self.OPAMP2_TCMR = SA_OPAMP_OPAMP2_TCMR(self, 0x1C)
        self.OPAMP3_TCMR = SA_OPAMP_OPAMP3_TCMR(self, 0x20)
        self.OPAMP4_TCMR = SA_OPAMP_OPAMP4_TCMR(self, 0x24)
        self.OPAMP5_TCMR = SA_OPAMP_OPAMP5_TCMR(self, 0x28)
        self.OPAMP6_TCMR = SA_OPAMP_OPAMP6_TCMR(self, 0x2C)
        self.OPAMP_CSR = Subscriptor(self, "OPAMP{}_CSR")
        self.OPAMP_TCMR = Subscriptor(self, "OPAMP{}_TCMR")

OPAMP = SA_OPAMP(0x40010300, "OPAMP")

class SA_HRTIM_Master_MCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MCR", "Master Timer Control Register")
        self.BRSTDMA = BitField(self, 0xC0000000, "BRSTDMA", "Burst DMA Update")
        self.MREPU = BitField(self, 0x20000000, "MREPU", "Master Timer Repetition update")
        self.PREEN = BitField(self, 0x08000000, "PREEN", "Preload enable")
        self.DACSYNC = BitField(self, 0x06000000, "DACSYNC", "AC Synchronization")
        self.TFCEN = BitField(self, 0x00400000, "TFCEN", "Timer F counter enable")
        self.TECEN = BitField(self, 0x00200000, "TECEN", "Timer E counter enable")
        self.TDCEN = BitField(self, 0x00100000, "TDCEN", "Timer D counter enable")
        self.TCCEN = BitField(self, 0x00080000, "TCCEN", "Timer C counter enable")
        self.TBCEN = BitField(self, 0x00040000, "TBCEN", "Timer B counter enable")
        self.TACEN = BitField(self, 0x00020000, "TACEN", "Timer A counter enable")
        self.MCEN = BitField(self, 0x00010000, "MCEN", "Master Counter enable")
        self.SYNC_SRC = BitField(self, 0x0000C000, "SYNC_SRC", "Synchronization source")
        self.SYNC_OUT = BitField(self, 0x00003000, "SYNC_OUT", "Synchronization output")
        self.SYNCSTRTM = BitField(self, 0x00000800, "SYNCSTRTM", "Synchronization Starts Master")
        self.SYNCRSTM = BitField(self, 0x00000400, "SYNCRSTM", "Synchronization Resets Master")
        self.SYNC_IN = BitField(self, 0x00000300, "SYNC_IN", "synchronization input")
        self.INTLVD = BitField(self, 0x000000C0, "INTLVD", "Interleaved mode")
        self.HALF = BitField(self, 0x00000020, "HALF", "Half mode enable")
        self.RETRIG = BitField(self, 0x00000010, "RETRIG", "Master Re-triggerable mode")
        self.CONT = BitField(self, 0x00000008, "CONT", "Master Continuous mode")
        self.CK_PSC = BitField(self, 0x00000007, "CK_PSC", "HRTIM Master Clock prescaler")

class SA_HRTIM_Master_MISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MISR", "Master Timer Interrupt Status Register")
        self.MUPD = BitField(self, 0x00000040, "MUPD", "Master Update Interrupt Flag")
        self.SYNC = BitField(self, 0x00000020, "SYNC", "Sync Input Interrupt Flag")
        self.MREP = BitField(self, 0x00000010, "MREP", "Master Repetition Interrupt Flag")
        self.MCMP4 = BitField(self, 0x00000008, "MCMP4", "Master Compare 4 Interrupt Flag")
        self.MCMP3 = BitField(self, 0x00000004, "MCMP3", "Master Compare 3 Interrupt Flag")
        self.MCMP2 = BitField(self, 0x00000002, "MCMP2", "Master Compare 2 Interrupt Flag")
        self.MCMP1 = BitField(self, 0x00000001, "MCMP1", "Master Compare 1 Interrupt Flag")
        self.MCMP = Subscriptor(self, "MCMP{}")

class SA_HRTIM_Master_MICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MICR", "Master Timer Interrupt Clear Register")
        self.MUPDC = BitField(self, 0x00000040, "MUPDC", "Master update Interrupt flag clear")
        self.SYNCC = BitField(self, 0x00000020, "SYNCC", "Sync Input Interrupt flag clear")
        self.MREPC = BitField(self, 0x00000010, "MREPC", "Repetition Interrupt flag clear")
        self.MCMP4C = BitField(self, 0x00000008, "MCMP4C", "Master Compare 4 Interrupt flag clear")
        self.MCMP3C = BitField(self, 0x00000004, "MCMP3C", "Master Compare 3 Interrupt flag clear")
        self.MCMP2C = BitField(self, 0x00000002, "MCMP2C", "Master Compare 2 Interrupt flag clear")
        self.MCMP1C = BitField(self, 0x00000001, "MCMP1C", "Master Compare 1 Interrupt flag clear")
        self.MCMPC = Subscriptor(self, "MCMP{}C")

class SA_HRTIM_Master_MDIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MDIER", "HRTIM Master Timer DMA / Interrupt Enable Register")
        self.MUPDDE = BitField(self, 0x00400000, "MUPDDE", "MUPDDE")
        self.SYNCDE = BitField(self, 0x00200000, "SYNCDE", "SYNCDE")
        self.MREPDE = BitField(self, 0x00100000, "MREPDE", "MREPDE")
        self.MCMP4DE = BitField(self, 0x00080000, "MCMP4DE", "MCMP4DE")
        self.MCMP3DE = BitField(self, 0x00040000, "MCMP3DE", "MCMP3DE")
        self.MCMP2DE = BitField(self, 0x00020000, "MCMP2DE", "MCMP2DE")
        self.MCMP1DE = BitField(self, 0x00010000, "MCMP1DE", "MCMP1DE")
        self.MUPDIE = BitField(self, 0x00000040, "MUPDIE", "MUPDIE")
        self.SYNCIE = BitField(self, 0x00000020, "SYNCIE", "SYNCIE")
        self.MREPIE = BitField(self, 0x00000010, "MREPIE", "MREPIE")
        self.MCMP4IE = BitField(self, 0x00000008, "MCMP4IE", "MCMP4IE")
        self.MCMP3IE = BitField(self, 0x00000004, "MCMP3IE", "MCMP3IE")
        self.MCMP2IE = BitField(self, 0x00000002, "MCMP2IE", "MCMP2IE")
        self.MCMP1IE = BitField(self, 0x00000001, "MCMP1IE", "MCMP1IE")
        self.MCMPIE = Subscriptor(self, "MCMP{}IE")
        self.MCMPDE = Subscriptor(self, "MCMP{}DE")

class SA_HRTIM_Master_MCNTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MCNTR", "Master Timer Counter Register")
        self.MCNT = BitField(self, 0x0000FFFF, "MCNT", "Counter value")

class SA_HRTIM_Master_MPER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "MPER", "Master Timer Period Register")
        self.MPER = BitField(self, 0x0000FFFF, "MPER", "Master Timer Period value")

class SA_HRTIM_Master_MREP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MREP", "Master Timer Repetition Register")
        self.MREP = BitField(self, 0x000000FF, "MREP", "Master Timer Repetition counter value")

class SA_HRTIM_Master_MCMP1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MCMP1R", "Master Timer Compare 1 Register")
        self.MCMP1 = BitField(self, 0x0000FFFF, "MCMP1", "Master Timer Compare 1 value")

class SA_HRTIM_Master_MCMP2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MCMP2R", "Master Timer Compare 2 Register")
        self.MCMP2 = BitField(self, 0x0000FFFF, "MCMP2", "Master Timer Compare 2 value")

class SA_HRTIM_Master_MCMP3R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MCMP3R", "Master Timer Compare 3 Register")
        self.MCMP3 = BitField(self, 0x0000FFFF, "MCMP3", "Master Timer Compare 3 value")

class SA_HRTIM_Master_MCMP4R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MCMP4R", "Master Timer Compare 4 Register")
        self.MCMP4 = BitField(self, 0x0000FFFF, "MCMP4", "Master Timer Compare 4 value")

class SA_HRTIM_Master(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: Master Timers")
        self.MCR = SA_HRTIM_Master_MCR(self, 0x0)
        self.MISR = SA_HRTIM_Master_MISR(self, 0x4)
        self.MICR = SA_HRTIM_Master_MICR(self, 0x8)
        self.MDIER = SA_HRTIM_Master_MDIER(self, 0xC)
        self.MCNTR = SA_HRTIM_Master_MCNTR(self, 0x10)
        self.MPER = SA_HRTIM_Master_MPER(self, 0x14)
        self.MREP = SA_HRTIM_Master_MREP(self, 0x18)
        self.MCMP1R = SA_HRTIM_Master_MCMP1R(self, 0x1C)
        self.MCMP2R = SA_HRTIM_Master_MCMP2R(self, 0x24)
        self.MCMP3R = SA_HRTIM_Master_MCMP3R(self, 0x28)
        self.MCMP4R = SA_HRTIM_Master_MCMP4R(self, 0x2C)
        self.MCMPR = Subscriptor(self, "MCMP{}R")

HRTIM_Master = SA_HRTIM_Master(0x40016800, "HRTIM_Master")

class SA_HRTIM_TIMA_TIMACR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMACR", "Timerx Control Register")
        self.UPDGAT = BitField(self, 0xF0000000, "UPDGAT", "Update Gating")
        self.PREEN = BitField(self, 0x08000000, "PREEN", "Preload enable")
        self.DACSYNC = BitField(self, 0x06000000, "DACSYNC", "AC Synchronization")
        self.MSTU = BitField(self, 0x01000000, "MSTU", "Master Timer update")
        self.TEU = BitField(self, 0x00800000, "TEU", "TEU")
        self.TDU = BitField(self, 0x00400000, "TDU", "TDU")
        self.TCU = BitField(self, 0x00200000, "TCU", "TCU")
        self.TBU = BitField(self, 0x00100000, "TBU", "TBU")
        self.TxRSTU = BitField(self, 0x00040000, "TxRSTU", "Timerx reset update")
        self.TxREPU = BitField(self, 0x00020000, "TxREPU", "Timer x Repetition update")
        self.TFU = BitField(self, 0x00010000, "TFU", "TFU")
        self.DELCMP4 = BitField(self, 0x0000C000, "DELCMP4", "Delayed CMP4 mode")
        self.DELCMP2 = BitField(self, 0x00003000, "DELCMP2", "Delayed CMP2 mode")
        self.SYNCSTRTx = BitField(self, 0x00000800, "SYNCSTRTx", "Synchronization Starts Timer x")
        self.SYNCRSTx = BitField(self, 0x00000400, "SYNCRSTx", "Synchronization Resets Timer x")
        self.RSYNCU = BitField(self, 0x00000200, "RSYNCU", "Re-Synchronized Update")
        self.INTLVD = BitField(self, 0x00000180, "INTLVD", "Interleaved mode")
        self.PSHPLL = BitField(self, 0x00000040, "PSHPLL", "Push-Pull mode enable")
        self.HALF = BitField(self, 0x00000020, "HALF", "Half mode enable")
        self.RETRIG = BitField(self, 0x00000010, "RETRIG", "Re-triggerable mode")
        self.CONT = BitField(self, 0x00000008, "CONT", "Continuous mode")
        self.CK_PSCx = BitField(self, 0x00000007, "CK_PSCx", "HRTIM Timer x Clock prescaler")

class SA_HRTIM_TIMA_TIMAISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMAISR", "Timerx Interrupt Status Register")
        self.O2CPY = BitField(self, 0x00200000, "O2CPY", "Output 2 Copy")
        self.O1CPY = BitField(self, 0x00100000, "O1CPY", "Output 1 Copy")
        self.O2STAT = BitField(self, 0x00080000, "O2STAT", "Output 2 State")
        self.O1STAT = BitField(self, 0x00040000, "O1STAT", "Output 1 State")
        self.IPPSTAT = BitField(self, 0x00020000, "IPPSTAT", "Idle Push Pull Status")
        self.CPPSTAT = BitField(self, 0x00010000, "CPPSTAT", "Current Push Pull Status")
        self.DLYPRT = BitField(self, 0x00004000, "DLYPRT", "Delayed Protection Flag")
        self.RST = BitField(self, 0x00002000, "RST", "Reset Interrupt Flag")
        self.RSTx2 = BitField(self, 0x00001000, "RSTx2", "Output 2 Reset Interrupt Flag")
        self.SETx2 = BitField(self, 0x00000800, "SETx2", "Output 2 Set Interrupt Flag")
        self.RSTx1 = BitField(self, 0x00000400, "RSTx1", "Output 1 Reset Interrupt Flag")
        self.SETx1 = BitField(self, 0x00000200, "SETx1", "Output 1 Set Interrupt Flag")
        self.CPT2 = BitField(self, 0x00000100, "CPT2", "Capture2 Interrupt Flag")
        self.CPT1 = BitField(self, 0x00000080, "CPT1", "Capture1 Interrupt Flag")
        self.UPD = BitField(self, 0x00000040, "UPD", "Update Interrupt Flag")
        self.REP = BitField(self, 0x00000010, "REP", "Repetition Interrupt Flag")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Compare 4 Interrupt Flag")
        self.CMP3 = BitField(self, 0x00000004, "CMP3", "Compare 3 Interrupt Flag")
        self.CMP2 = BitField(self, 0x00000002, "CMP2", "Compare 2 Interrupt Flag")
        self.CMP1 = BitField(self, 0x00000001, "CMP1", "Compare 1 Interrupt Flag")
        self.RSTx = Subscriptor(self, "RSTx{}")
        self.OSTAT = Subscriptor(self, "O{}STAT")
        self.OCPY = Subscriptor(self, "O{}CPY")
        self.SETx = Subscriptor(self, "SETx{}")
        self.CPT = Subscriptor(self, "CPT{}")
        self.CMP = Subscriptor(self, "CMP{}")

class SA_HRTIM_TIMA_TIMAICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMAICR", "Timerx Interrupt Clear Register")
        self.DLYPRTC = BitField(self, 0x00004000, "DLYPRTC", "Delayed Protection Flag Clear")
        self.RSTC = BitField(self, 0x00002000, "RSTC", "Reset Interrupt flag Clear")
        self.RSTx2C = BitField(self, 0x00001000, "RSTx2C", "Output 2 Reset flag Clear")
        self.SET2xC = BitField(self, 0x00000800, "SET2xC", "Output 2 Set flag Clear")
        self.RSTx1C = BitField(self, 0x00000400, "RSTx1C", "Output 1 Reset flag Clear")
        self.SET1xC = BitField(self, 0x00000200, "SET1xC", "Output 1 Set flag Clear")
        self.CPT2C = BitField(self, 0x00000100, "CPT2C", "Capture2 Interrupt flag Clear")
        self.CPT1C = BitField(self, 0x00000080, "CPT1C", "Capture1 Interrupt flag Clear")
        self.UPDC = BitField(self, 0x00000040, "UPDC", "Update Interrupt flag Clear")
        self.REPC = BitField(self, 0x00000010, "REPC", "Repetition Interrupt flag Clear")
        self.CMP4C = BitField(self, 0x00000008, "CMP4C", "Compare 4 Interrupt flag Clear")
        self.CMP3C = BitField(self, 0x00000004, "CMP3C", "Compare 3 Interrupt flag Clear")
        self.CMP2C = BitField(self, 0x00000002, "CMP2C", "Compare 2 Interrupt flag Clear")
        self.CMP1C = BitField(self, 0x00000001, "CMP1C", "Compare 1 Interrupt flag Clear")
        self.CPTC = Subscriptor(self, "CPT{}C")
        self.SETxC = Subscriptor(self, "SET{}xC")
        self.CMPC = Subscriptor(self, "CMP{}C")
        self.RSTxC = Subscriptor(self, "RSTx{}C")

class SA_HRTIM_TIMA_TIMADIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMADIER", "TIMxDIER")
        self.DLYPRTDE = BitField(self, 0x40000000, "DLYPRTDE", "DLYPRTDE")
        self.RSTDE = BitField(self, 0x20000000, "RSTDE", "RSTDE")
        self.RSTx2DE = BitField(self, 0x10000000, "RSTx2DE", "RSTx2DE")
        self.SETx2DE = BitField(self, 0x08000000, "SETx2DE", "SETx2DE")
        self.RSTx1DE = BitField(self, 0x04000000, "RSTx1DE", "RSTx1DE")
        self.SET1xDE = BitField(self, 0x02000000, "SET1xDE", "SET1xDE")
        self.CPT2DE = BitField(self, 0x01000000, "CPT2DE", "CPT2DE")
        self.CPT1DE = BitField(self, 0x00800000, "CPT1DE", "CPT1DE")
        self.UPDDE = BitField(self, 0x00400000, "UPDDE", "UPDDE")
        self.REPDE = BitField(self, 0x00100000, "REPDE", "REPDE")
        self.CMP4DE = BitField(self, 0x00080000, "CMP4DE", "CMP4DE")
        self.CMP3DE = BitField(self, 0x00040000, "CMP3DE", "CMP3DE")
        self.CMP2DE = BitField(self, 0x00020000, "CMP2DE", "CMP2DE")
        self.CMP1DE = BitField(self, 0x00010000, "CMP1DE", "CMP1DE")
        self.DLYPRTIE = BitField(self, 0x00004000, "DLYPRTIE", "DLYPRTIE")
        self.RSTIE = BitField(self, 0x00002000, "RSTIE", "RSTIE")
        self.RSTx2IE = BitField(self, 0x00001000, "RSTx2IE", "RSTx2IE")
        self.SETx2IE = BitField(self, 0x00000800, "SETx2IE", "SETx2IE")
        self.RSTx1IE = BitField(self, 0x00000400, "RSTx1IE", "RSTx1IE")
        self.SET1xIE = BitField(self, 0x00000200, "SET1xIE", "SET1xIE")
        self.CPT2IE = BitField(self, 0x00000100, "CPT2IE", "CPT2IE")
        self.CPT1IE = BitField(self, 0x00000080, "CPT1IE", "CPT1IE")
        self.UPDIE = BitField(self, 0x00000040, "UPDIE", "UPDIE")
        self.REPIE = BitField(self, 0x00000010, "REPIE", "REPIE")
        self.CMP4IE = BitField(self, 0x00000008, "CMP4IE", "CMP4IE")
        self.CMP3IE = BitField(self, 0x00000004, "CMP3IE", "CMP3IE")
        self.CMP2IE = BitField(self, 0x00000002, "CMP2IE", "CMP2IE")
        self.CMP1IE = BitField(self, 0x00000001, "CMP1IE", "CMP1IE")
        self.RSTxIE = Subscriptor(self, "RSTx{}IE")
        self.CMPDE = Subscriptor(self, "CMP{}DE")
        self.RSTxDE = Subscriptor(self, "RSTx{}DE")
        self.CPTDE = Subscriptor(self, "CPT{}DE")
        self.CPTIE = Subscriptor(self, "CPT{}IE")
        self.CMPIE = Subscriptor(self, "CMP{}IE")

class SA_HRTIM_TIMA_CNTAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNTAR", "Timerx Counter Register")
        self.CNTx = BitField(self, 0x0000FFFF, "CNTx", "Timerx Counter value")

class SA_HRTIM_TIMA_PERAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "PERAR", "Timerx Period Register")
        self.PERx = BitField(self, 0x0000FFFF, "PERx", "Timerx Period value")

class SA_HRTIM_TIMA_REPAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "REPAR", "Timerx Repetition Register")
        self.REPx = BitField(self, 0x000000FF, "REPx", "Timerx Repetition counter value")

class SA_HRTIM_TIMA_CMP1AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1AR", "Timerx Compare 1 Register")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMA_CMP1CAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1CAR", "Timerx Compare 1 Compound Register")
        self.REPx = BitField(self, 0x00FF0000, "REPx", "Timerx Repetition value (aliased from HRTIM_REPx register)")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMA_CMP2AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP2AR", "Timerx Compare 2 Register")
        self.CMP2x = BitField(self, 0x0000FFFF, "CMP2x", "Timerx Compare 2 value")

class SA_HRTIM_TIMA_CMP3AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP3AR", "Timerx Compare 3 Register")
        self.CMP3x = BitField(self, 0x0000FFFF, "CMP3x", "Timerx Compare 3 value")

class SA_HRTIM_TIMA_CMP4AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP4AR", "Timerx Compare 4 Register")
        self.CMP4x = BitField(self, 0x0000FFFF, "CMP4x", "Timerx Compare 4 value")

class SA_HRTIM_TIMA_CPT1AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1AR", "Timerx Capture 1 Register")
        self.CPT1x = BitField(self, 0x0000FFFF, "CPT1x", "Timerx Capture 1 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMA_CPT2AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2AR", "Timerx Capture 2 Register")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")
        self.CPT2x = BitField(self, 0x0000FFFF, "CPT2x", "Timerx Capture 2 value")

class SA_HRTIM_TIMA_DTAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTAR", "Timerx Deadtime Register")
        self.DTFLKx = BitField(self, 0x80000000, "DTFLKx", "Deadtime Falling Lock")
        self.DTFSLKx = BitField(self, 0x40000000, "DTFSLKx", "Deadtime Falling Sign Lock")
        self.SDTFx = BitField(self, 0x02000000, "SDTFx", "Sign Deadtime Falling value")
        self.DTFx = BitField(self, 0x01FF0000, "DTFx", "Deadtime Falling value")
        self.DTRLKx = BitField(self, 0x00008000, "DTRLKx", "Deadtime Rising Lock")
        self.DTRSLKx = BitField(self, 0x00004000, "DTRSLKx", "Deadtime Rising Sign Lock")
        self.DTPRSC = BitField(self, 0x00001C00, "DTPRSC", "Deadtime Prescaler")
        self.SDTRx = BitField(self, 0x00000200, "SDTRx", "Sign Deadtime Rising value")
        self.DTRx = BitField(self, 0x000001FF, "DTRx", "Deadtime Rising value")

class SA_HRTIM_TIMA_SETA1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETA1R", "Timerx Output1 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "Registers update (transfer preload to active)")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "External Event 1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "Timer Event 9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "Timer Event 8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "Timer Event 7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "Timer Event 6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "Timer Event 5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "Timer Event 4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "Timer Event 3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "Timer Event 2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "Timer Event 1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "Master Compare 4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "Master Compare 3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "Master Compare 2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "Master Compare 1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "Master Period")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "Timer A compare 4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "Timer A compare 3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "Timer A compare 2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "Timer A compare 1")
        self.PER = BitField(self, 0x00000004, "PER", "Timer A Period")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "Timer A resynchronizaton")
        self.SST = BitField(self, 0x00000001, "SST", "Software Set trigger")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMA_RSTA1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTA1R", "Timerx Output1 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMA_SETA2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETA2R", "Timerx Output2 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SST = BitField(self, 0x00000001, "SST", "SST")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMA_RSTA2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTA2R", "Timerx Output2 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMA_EEFAR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFAR1", "Timerx External Event Filtering Register 1")
        self.EE5FLTR = BitField(self, 0x1E000000, "EE5FLTR", "External Event 5 filter")
        self.EE5LTCH = BitField(self, 0x01000000, "EE5LTCH", "External Event 5 latch")
        self.EE4FLTR = BitField(self, 0x00780000, "EE4FLTR", "External Event 4 filter")
        self.EE4LTCH = BitField(self, 0x00040000, "EE4LTCH", "External Event 4 latch")
        self.EE3FLTR = BitField(self, 0x0001E000, "EE3FLTR", "External Event 3 filter")
        self.EE3LTCH = BitField(self, 0x00001000, "EE3LTCH", "External Event 3 latch")
        self.EE2FLTR = BitField(self, 0x00000780, "EE2FLTR", "External Event 2 filter")
        self.EE2LTCH = BitField(self, 0x00000040, "EE2LTCH", "External Event 2 latch")
        self.EE1FLTR = BitField(self, 0x0000001E, "EE1FLTR", "External Event 1 filter")
        self.EE1LTCH = BitField(self, 0x00000001, "EE1LTCH", "External Event 1 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMA_EEFAR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFAR2", "Timerx External Event Filtering Register 2")
        self.EE10FLTR = BitField(self, 0x1E000000, "EE10FLTR", "External Event 10 filter")
        self.EE10LTCH = BitField(self, 0x01000000, "EE10LTCH", "External Event 10 latch")
        self.EE9FLTR = BitField(self, 0x00780000, "EE9FLTR", "External Event 9 filter")
        self.EE9LTCH = BitField(self, 0x00040000, "EE9LTCH", "External Event 9 latch")
        self.EE8FLTR = BitField(self, 0x0001E000, "EE8FLTR", "External Event 8 filter")
        self.EE8LTCH = BitField(self, 0x00001000, "EE8LTCH", "External Event 8 latch")
        self.EE7FLTR = BitField(self, 0x00000780, "EE7FLTR", "External Event 7 filter")
        self.EE7LTCH = BitField(self, 0x00000040, "EE7LTCH", "External Event 7 latch")
        self.EE6FLTR = BitField(self, 0x0000001E, "EE6FLTR", "External Event 6 filter")
        self.EE6LTCH = BitField(self, 0x00000001, "EE6LTCH", "External Event 6 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMA_RSTAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTAR", "TimerA Reset Register")
        self.TIMFCPM2 = BitField(self, 0x80000000, "TIMFCPM2", "Timer F Compare 2")
        self.TIMECMP4 = BitField(self, 0x40000000, "TIMECMP4", "Timer E Compare 4")
        self.TIMECMP2 = BitField(self, 0x20000000, "TIMECMP2", "Timer E Compare 2")
        self.TIMECMP1 = BitField(self, 0x10000000, "TIMECMP1", "Timer E Compare 1")
        self.TIMDCMP4 = BitField(self, 0x08000000, "TIMDCMP4", "Timer D Compare 4")
        self.TIMDCMP2 = BitField(self, 0x04000000, "TIMDCMP2", "Timer D Compare 2")
        self.TIMDCMP1 = BitField(self, 0x02000000, "TIMDCMP1", "Timer D Compare 1")
        self.TIMCCMP4 = BitField(self, 0x01000000, "TIMCCMP4", "Timer C Compare 4")
        self.TIMCCMP2 = BitField(self, 0x00800000, "TIMCCMP2", "Timer C Compare 2")
        self.TIMCCMP1 = BitField(self, 0x00400000, "TIMCCMP1", "Timer C Compare 1")
        self.TIMBCMP4 = BitField(self, 0x00200000, "TIMBCMP4", "Timer B Compare 4")
        self.TIMBCMP2 = BitField(self, 0x00100000, "TIMBCMP2", "Timer B Compare 2")
        self.TIMBCMP1 = BitField(self, 0x00080000, "TIMBCMP1", "Timer B Compare 1")
        self.EXTEVNT10 = BitField(self, 0x00040000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x00020000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x00010000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x00008000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x00004000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x00002000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x00001000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00000800, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00000400, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00000200, "EXTEVNT1", "External Event 1")
        self.MSTCMP4 = BitField(self, 0x00000100, "MSTCMP4", "Master compare 4")
        self.MSTCMP3 = BitField(self, 0x00000080, "MSTCMP3", "Master compare 3")
        self.MSTCMP2 = BitField(self, 0x00000040, "MSTCMP2", "Master compare 2")
        self.MSTCMP1 = BitField(self, 0x00000020, "MSTCMP1", "Master compare 1")
        self.MSTPER = BitField(self, 0x00000010, "MSTPER", "Master timer Period")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Timer A compare 4 reset")
        self.CMP2 = BitField(self, 0x00000004, "CMP2", "Timer A compare 2 reset")
        self.UPDT = BitField(self, 0x00000002, "UPDT", "Timer A Update reset")
        self.TIMFCMP1 = BitField(self, 0x00000001, "TIMFCMP1", "Timer A Update reset")
        self.TIMDCMP = Subscriptor(self, "TIMDCMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMCCMP = Subscriptor(self, "TIMCCMP{}")
        self.TIMBCMP = Subscriptor(self, "TIMBCMP{}")
        self.TIMECMP = Subscriptor(self, "TIMECMP{}")

class SA_HRTIM_TIMA_CHPAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CHPAR", "Timerx Chopper Register")
        self.STRTPW = BitField(self, 0x00000780, "STRTPW", "STRTPW")
        self.CHPDTY = BitField(self, 0x00000070, "CHPDTY", "Timerx chopper duty cycle value")
        self.CHPFRQ = BitField(self, 0x0000000F, "CHPFRQ", "Timerx carrier frequency value")

class SA_HRTIM_TIMA_CPT1ACR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1ACR", "Timerx Capture 2 Control Register")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TFCMP2 = BitField(self, 0x00008000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x00004000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x00002000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x00001000, "TF1SET", "TF1SET")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMA_CPT2ACR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2ACR", "CPT2xCR")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TFCMP2 = BitField(self, 0x00008000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x00004000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x00002000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x00001000, "TF1SET", "TF1SET")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMA_OUTAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OUTAR", "Timerx Output Register")
        self.DIDL2 = BitField(self, 0x00800000, "DIDL2", "Output 2 Deadtime upon burst mode Idle entry")
        self.CHP2 = BitField(self, 0x00400000, "CHP2", "Output 2 Chopper enable")
        self.FAULT2 = BitField(self, 0x00300000, "FAULT2", "Output 2 Fault state")
        self.IDLES2 = BitField(self, 0x00080000, "IDLES2", "Output 2 Idle State")
        self.IDLEM2 = BitField(self, 0x00040000, "IDLEM2", "Output 2 Idle mode")
        self.POL2 = BitField(self, 0x00020000, "POL2", "Output 2 polarity")
        self.BIAR = BitField(self, 0x00004000, "BIAR", "Balanced Idle Automatic Resume")
        self.DLYPRT = BitField(self, 0x00001C00, "DLYPRT", "Delayed Protection")
        self.DLYPRTEN = BitField(self, 0x00000200, "DLYPRTEN", "Delayed Protection Enable")
        self.DTEN = BitField(self, 0x00000100, "DTEN", "Deadtime enable")
        self.DIDL1 = BitField(self, 0x00000080, "DIDL1", "Output 1 Deadtime upon burst mode Idle entry")
        self.CHP1 = BitField(self, 0x00000040, "CHP1", "Output 1 Chopper enable")
        self.FAULT1 = BitField(self, 0x00000030, "FAULT1", "Output 1 Fault state")
        self.IDLES1 = BitField(self, 0x00000008, "IDLES1", "Output 1 Idle State")
        self.IDLEM1 = BitField(self, 0x00000004, "IDLEM1", "Output 1 Idle mode")
        self.POL1 = BitField(self, 0x00000002, "POL1", "Output 1 polarity")
        self.POL = Subscriptor(self, "POL{}")
        self.DIDL = Subscriptor(self, "DIDL{}")
        self.FAULT = Subscriptor(self, "FAULT{}")
        self.CHP = Subscriptor(self, "CHP{}")
        self.IDLES = Subscriptor(self, "IDLES{}")
        self.IDLEM = Subscriptor(self, "IDLEM{}")

class SA_HRTIM_TIMA_FLTAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTAR", "Timerx Fault Register")
        self.FLTLCK = BitField(self, 0x80000000, "FLTLCK", "Fault sources Lock")
        self.FLT6EN = BitField(self, 0x00000020, "FLT6EN", "Fault 6 enable")
        self.FLT5EN = BitField(self, 0x00000010, "FLT5EN", "Fault 5 enable")
        self.FLT4EN = BitField(self, 0x00000008, "FLT4EN", "Fault 4 enable")
        self.FLT3EN = BitField(self, 0x00000004, "FLT3EN", "Fault 3 enable")
        self.FLT2EN = BitField(self, 0x00000002, "FLT2EN", "Fault 2 enable")
        self.FLT1EN = BitField(self, 0x00000001, "FLT1EN", "Fault 1 enable")
        self.FLTEN = Subscriptor(self, "FLT{}EN")

class SA_HRTIM_TIMA_TIMACR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMACR2", "HRTIM Timerx Control Register 2")
        self.TRGHLF = BitField(self, 0x00100000, "TRGHLF", "Triggered-half mode")
        self.GTCMP3 = BitField(self, 0x00020000, "GTCMP3", "Greater than Compare 3 PWM mode")
        self.GTCMP1 = BitField(self, 0x00010000, "GTCMP1", "Greater than Compare 1 PWM mode")
        self.FEROM = BitField(self, 0x0000C000, "FEROM", "Fault and Event Roll-Over Mode")
        self.BMROM = BitField(self, 0x00003000, "BMROM", "Burst Mode Roll-Over Mode")
        self.ADROM = BitField(self, 0x00000C00, "ADROM", "ADC Roll-Over Mode")
        self.OUTROM = BitField(self, 0x00000300, "OUTROM", "Output Roll-Over Mode")
        self.ROM = BitField(self, 0x000000C0, "ROM", "Roll-Over Mode")
        self.UDM = BitField(self, 0x00000010, "UDM", "Up-Down Mode")
        self.DCDR = BitField(self, 0x00000004, "DCDR", "Dual Channel DAC Reset trigger")
        self.DCDS = BitField(self, 0x00000002, "DCDS", "Dual Channel DAC Step trigger")
        self.DCDE = BitField(self, 0x00000001, "DCDE", "Dual Channel DAC trigger enable")

class SA_HRTIM_TIMA_AEEFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AEEFR3", "HRTIM Timerx External Event Filtering Register 3")
        self.EEVACNT = BitField(self, 0x00003F00, "EEVACNT", "External Event A counter")
        self.EEVASEL = BitField(self, 0x000000F0, "EEVASEL", "External Event A Selection")
        self.EEVARSTM = BitField(self, 0x00000004, "EEVARSTM", "External Event A Reset Mode")
        self.EEVACRES = BitField(self, 0x00000002, "EEVACRES", "External Event A Counter Reset")
        self.EEVACE = BitField(self, 0x00000001, "EEVACE", "External Event A Counter Enable")

class SA_HRTIM_TIMA(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: TIMA")
        self.TIMACR = SA_HRTIM_TIMA_TIMACR(self, 0x0)
        self.TIMAISR = SA_HRTIM_TIMA_TIMAISR(self, 0x4)
        self.TIMAICR = SA_HRTIM_TIMA_TIMAICR(self, 0x8)
        self.TIMADIER = SA_HRTIM_TIMA_TIMADIER(self, 0xC)
        self.CNTAR = SA_HRTIM_TIMA_CNTAR(self, 0x10)
        self.PERAR = SA_HRTIM_TIMA_PERAR(self, 0x14)
        self.REPAR = SA_HRTIM_TIMA_REPAR(self, 0x18)
        self.CMP1AR = SA_HRTIM_TIMA_CMP1AR(self, 0x1C)
        self.CMP1CAR = SA_HRTIM_TIMA_CMP1CAR(self, 0x20)
        self.CMP2AR = SA_HRTIM_TIMA_CMP2AR(self, 0x24)
        self.CMP3AR = SA_HRTIM_TIMA_CMP3AR(self, 0x28)
        self.CMP4AR = SA_HRTIM_TIMA_CMP4AR(self, 0x2C)
        self.CPT1AR = SA_HRTIM_TIMA_CPT1AR(self, 0x30)
        self.CPT2AR = SA_HRTIM_TIMA_CPT2AR(self, 0x34)
        self.DTAR = SA_HRTIM_TIMA_DTAR(self, 0x38)
        self.SETA1R = SA_HRTIM_TIMA_SETA1R(self, 0x3C)
        self.RSTA1R = SA_HRTIM_TIMA_RSTA1R(self, 0x40)
        self.SETA2R = SA_HRTIM_TIMA_SETA2R(self, 0x44)
        self.RSTA2R = SA_HRTIM_TIMA_RSTA2R(self, 0x48)
        self.EEFAR1 = SA_HRTIM_TIMA_EEFAR1(self, 0x4C)
        self.EEFAR2 = SA_HRTIM_TIMA_EEFAR2(self, 0x50)
        self.RSTAR = SA_HRTIM_TIMA_RSTAR(self, 0x54)
        self.CHPAR = SA_HRTIM_TIMA_CHPAR(self, 0x58)
        self.CPT1ACR = SA_HRTIM_TIMA_CPT1ACR(self, 0x5C)
        self.CPT2ACR = SA_HRTIM_TIMA_CPT2ACR(self, 0x60)
        self.OUTAR = SA_HRTIM_TIMA_OUTAR(self, 0x64)
        self.FLTAR = SA_HRTIM_TIMA_FLTAR(self, 0x68)
        self.TIMACR2 = SA_HRTIM_TIMA_TIMACR2(self, 0x6C)
        self.AEEFR3 = SA_HRTIM_TIMA_AEEFR3(self, 0x70)
        self.CMPAR = Subscriptor(self, "CMP{}AR")
        self.CPTACR = Subscriptor(self, "CPT{}ACR")
        self.EEFAR = Subscriptor(self, "EEFAR{}")
        self.SETAR = Subscriptor(self, "SETA{}R")
        self.CPTAR = Subscriptor(self, "CPT{}AR")

HRTIM_TIMA = SA_HRTIM_TIMA(0x40016880, "HRTIM_TIMA")

class SA_HRTIM_TIMB_TIMBCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMBCR", "Timerx Control Register")
        self.UPDGAT = BitField(self, 0xF0000000, "UPDGAT", "Update Gating")
        self.PREEN = BitField(self, 0x08000000, "PREEN", "Preload enable")
        self.DACSYNC = BitField(self, 0x06000000, "DACSYNC", "AC Synchronization")
        self.MSTU = BitField(self, 0x01000000, "MSTU", "Master Timer update")
        self.TEU = BitField(self, 0x00800000, "TEU", "TEU")
        self.TDU = BitField(self, 0x00400000, "TDU", "TDU")
        self.TCU = BitField(self, 0x00200000, "TCU", "TCU")
        self.TAU = BitField(self, 0x00080000, "TAU", "TAU")
        self.TxRSTU = BitField(self, 0x00040000, "TxRSTU", "Timerx reset update")
        self.TxREPU = BitField(self, 0x00020000, "TxREPU", "Timer x Repetition update")
        self.TFU = BitField(self, 0x00010000, "TFU", "TFU")
        self.DELCMP4 = BitField(self, 0x0000C000, "DELCMP4", "Delayed CMP4 mode")
        self.DELCMP2 = BitField(self, 0x00003000, "DELCMP2", "Delayed CMP2 mode")
        self.SYNCSTRTx = BitField(self, 0x00000800, "SYNCSTRTx", "Synchronization Starts Timer x")
        self.SYNCRSTx = BitField(self, 0x00000400, "SYNCRSTx", "Synchronization Resets Timer x")
        self.RSYNCU = BitField(self, 0x00000200, "RSYNCU", "Re-Synchronized Update")
        self.INTLVD = BitField(self, 0x00000180, "INTLVD", "Interleaved mode")
        self.PSHPLL = BitField(self, 0x00000040, "PSHPLL", "Push-Pull mode enable")
        self.HALF = BitField(self, 0x00000020, "HALF", "Half mode enable")
        self.RETRIG = BitField(self, 0x00000010, "RETRIG", "Re-triggerable mode")
        self.CONT = BitField(self, 0x00000008, "CONT", "Continuous mode")
        self.CK_PSCx = BitField(self, 0x00000007, "CK_PSCx", "HRTIM Timer x Clock prescaler")

class SA_HRTIM_TIMB_TIMBISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMBISR", "Timerx Interrupt Status Register")
        self.O2CPY = BitField(self, 0x00200000, "O2CPY", "Output 2 Copy")
        self.O1CPY = BitField(self, 0x00100000, "O1CPY", "Output 1 Copy")
        self.O2STAT = BitField(self, 0x00080000, "O2STAT", "Output 2 State")
        self.O1STAT = BitField(self, 0x00040000, "O1STAT", "Output 1 State")
        self.IPPSTAT = BitField(self, 0x00020000, "IPPSTAT", "Idle Push Pull Status")
        self.CPPSTAT = BitField(self, 0x00010000, "CPPSTAT", "Current Push Pull Status")
        self.DLYPRT = BitField(self, 0x00004000, "DLYPRT", "Delayed Protection Flag")
        self.RST = BitField(self, 0x00002000, "RST", "Reset Interrupt Flag")
        self.RSTx2 = BitField(self, 0x00001000, "RSTx2", "Output 2 Reset Interrupt Flag")
        self.SETx2 = BitField(self, 0x00000800, "SETx2", "Output 2 Set Interrupt Flag")
        self.RSTx1 = BitField(self, 0x00000400, "RSTx1", "Output 1 Reset Interrupt Flag")
        self.SETx1 = BitField(self, 0x00000200, "SETx1", "Output 1 Set Interrupt Flag")
        self.CPT2 = BitField(self, 0x00000100, "CPT2", "Capture2 Interrupt Flag")
        self.CPT1 = BitField(self, 0x00000080, "CPT1", "Capture1 Interrupt Flag")
        self.UPD = BitField(self, 0x00000040, "UPD", "Update Interrupt Flag")
        self.REP = BitField(self, 0x00000010, "REP", "Repetition Interrupt Flag")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Compare 4 Interrupt Flag")
        self.CMP3 = BitField(self, 0x00000004, "CMP3", "Compare 3 Interrupt Flag")
        self.CMP2 = BitField(self, 0x00000002, "CMP2", "Compare 2 Interrupt Flag")
        self.CMP1 = BitField(self, 0x00000001, "CMP1", "Compare 1 Interrupt Flag")
        self.RSTx = Subscriptor(self, "RSTx{}")
        self.OSTAT = Subscriptor(self, "O{}STAT")
        self.OCPY = Subscriptor(self, "O{}CPY")
        self.SETx = Subscriptor(self, "SETx{}")
        self.CPT = Subscriptor(self, "CPT{}")
        self.CMP = Subscriptor(self, "CMP{}")

class SA_HRTIM_TIMB_TIMBICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMBICR", "Timerx Interrupt Clear Register")
        self.DLYPRTC = BitField(self, 0x00004000, "DLYPRTC", "Delayed Protection Flag Clear")
        self.RSTC = BitField(self, 0x00002000, "RSTC", "Reset Interrupt flag Clear")
        self.RSTx2C = BitField(self, 0x00001000, "RSTx2C", "Output 2 Reset flag Clear")
        self.SET2xC = BitField(self, 0x00000800, "SET2xC", "Output 2 Set flag Clear")
        self.RSTx1C = BitField(self, 0x00000400, "RSTx1C", "Output 1 Reset flag Clear")
        self.SET1xC = BitField(self, 0x00000200, "SET1xC", "Output 1 Set flag Clear")
        self.CPT2C = BitField(self, 0x00000100, "CPT2C", "Capture2 Interrupt flag Clear")
        self.CPT1C = BitField(self, 0x00000080, "CPT1C", "Capture1 Interrupt flag Clear")
        self.UPDC = BitField(self, 0x00000040, "UPDC", "Update Interrupt flag Clear")
        self.REPC = BitField(self, 0x00000010, "REPC", "Repetition Interrupt flag Clear")
        self.CMP4C = BitField(self, 0x00000008, "CMP4C", "Compare 4 Interrupt flag Clear")
        self.CMP3C = BitField(self, 0x00000004, "CMP3C", "Compare 3 Interrupt flag Clear")
        self.CMP2C = BitField(self, 0x00000002, "CMP2C", "Compare 2 Interrupt flag Clear")
        self.CMP1C = BitField(self, 0x00000001, "CMP1C", "Compare 1 Interrupt flag Clear")
        self.CPTC = Subscriptor(self, "CPT{}C")
        self.SETxC = Subscriptor(self, "SET{}xC")
        self.CMPC = Subscriptor(self, "CMP{}C")
        self.RSTxC = Subscriptor(self, "RSTx{}C")

class SA_HRTIM_TIMB_TIMBDIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMBDIER", "TIMxDIER")
        self.DLYPRTDE = BitField(self, 0x40000000, "DLYPRTDE", "DLYPRTDE")
        self.RSTDE = BitField(self, 0x20000000, "RSTDE", "RSTDE")
        self.RSTx2DE = BitField(self, 0x10000000, "RSTx2DE", "RSTx2DE")
        self.SETx2DE = BitField(self, 0x08000000, "SETx2DE", "SETx2DE")
        self.RSTx1DE = BitField(self, 0x04000000, "RSTx1DE", "RSTx1DE")
        self.SET1xDE = BitField(self, 0x02000000, "SET1xDE", "SET1xDE")
        self.CPT2DE = BitField(self, 0x01000000, "CPT2DE", "CPT2DE")
        self.CPT1DE = BitField(self, 0x00800000, "CPT1DE", "CPT1DE")
        self.UPDDE = BitField(self, 0x00400000, "UPDDE", "UPDDE")
        self.REPDE = BitField(self, 0x00100000, "REPDE", "REPDE")
        self.CMP4DE = BitField(self, 0x00080000, "CMP4DE", "CMP4DE")
        self.CMP3DE = BitField(self, 0x00040000, "CMP3DE", "CMP3DE")
        self.CMP2DE = BitField(self, 0x00020000, "CMP2DE", "CMP2DE")
        self.CMP1DE = BitField(self, 0x00010000, "CMP1DE", "CMP1DE")
        self.DLYPRTIE = BitField(self, 0x00004000, "DLYPRTIE", "DLYPRTIE")
        self.RSTIE = BitField(self, 0x00002000, "RSTIE", "RSTIE")
        self.RSTx2IE = BitField(self, 0x00001000, "RSTx2IE", "RSTx2IE")
        self.SETx2IE = BitField(self, 0x00000800, "SETx2IE", "SETx2IE")
        self.RSTx1IE = BitField(self, 0x00000400, "RSTx1IE", "RSTx1IE")
        self.SET1xIE = BitField(self, 0x00000200, "SET1xIE", "SET1xIE")
        self.CPT2IE = BitField(self, 0x00000100, "CPT2IE", "CPT2IE")
        self.CPT1IE = BitField(self, 0x00000080, "CPT1IE", "CPT1IE")
        self.UPDIE = BitField(self, 0x00000040, "UPDIE", "UPDIE")
        self.REPIE = BitField(self, 0x00000010, "REPIE", "REPIE")
        self.CMP4IE = BitField(self, 0x00000008, "CMP4IE", "CMP4IE")
        self.CMP3IE = BitField(self, 0x00000004, "CMP3IE", "CMP3IE")
        self.CMP2IE = BitField(self, 0x00000002, "CMP2IE", "CMP2IE")
        self.CMP1IE = BitField(self, 0x00000001, "CMP1IE", "CMP1IE")
        self.RSTxIE = Subscriptor(self, "RSTx{}IE")
        self.CMPDE = Subscriptor(self, "CMP{}DE")
        self.RSTxDE = Subscriptor(self, "RSTx{}DE")
        self.CPTDE = Subscriptor(self, "CPT{}DE")
        self.CPTIE = Subscriptor(self, "CPT{}IE")
        self.CMPIE = Subscriptor(self, "CMP{}IE")

class SA_HRTIM_TIMB_CNTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNTR", "Timerx Counter Register")
        self.CNTx = BitField(self, 0x0000FFFF, "CNTx", "Timerx Counter value")

class SA_HRTIM_TIMB_PERBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "PERBR", "Timerx Period Register")
        self.PERx = BitField(self, 0x0000FFFF, "PERx", "Timerx Period value")

class SA_HRTIM_TIMB_REPBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "REPBR", "Timerx Repetition Register")
        self.REPx = BitField(self, 0x000000FF, "REPx", "Timerx Repetition counter value")

class SA_HRTIM_TIMB_CMP1BR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1BR", "Timerx Compare 1 Register")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMB_CMP1CBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1CBR", "Timerx Compare 1 Compound Register")
        self.REPx = BitField(self, 0x00FF0000, "REPx", "Timerx Repetition value (aliased from HRTIM_REPx register)")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMB_CMP2BR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP2BR", "Timerx Compare 2 Register")
        self.CMP2x = BitField(self, 0x0000FFFF, "CMP2x", "Timerx Compare 2 value")

class SA_HRTIM_TIMB_CMP3BR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP3BR", "Timerx Compare 3 Register")
        self.CMP3x = BitField(self, 0x0000FFFF, "CMP3x", "Timerx Compare 3 value")

class SA_HRTIM_TIMB_CMP4BR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP4BR", "Timerx Compare 4 Register")
        self.CMP4x = BitField(self, 0x0000FFFF, "CMP4x", "Timerx Compare 4 value")

class SA_HRTIM_TIMB_CPT1BR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1BR", "Timerx Capture 1 Register")
        self.CPT1x = BitField(self, 0x0000FFFF, "CPT1x", "Timerx Capture 1 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMB_CPT2BR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2BR", "Timerx Capture 2 Register")
        self.CPT2x = BitField(self, 0x0000FFFF, "CPT2x", "Timerx Capture 2 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMB_DTBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTBR", "Timerx Deadtime Register")
        self.DTFLKx = BitField(self, 0x80000000, "DTFLKx", "Deadtime Falling Lock")
        self.DTFSLKx = BitField(self, 0x40000000, "DTFSLKx", "Deadtime Falling Sign Lock")
        self.SDTFx = BitField(self, 0x02000000, "SDTFx", "Sign Deadtime Falling value")
        self.DTFx = BitField(self, 0x01FF0000, "DTFx", "Deadtime Falling value")
        self.DTRLKx = BitField(self, 0x00008000, "DTRLKx", "Deadtime Rising Lock")
        self.DTRSLKx = BitField(self, 0x00004000, "DTRSLKx", "Deadtime Rising Sign Lock")
        self.DTPRSC = BitField(self, 0x00001C00, "DTPRSC", "Deadtime Prescaler")
        self.SDTRx = BitField(self, 0x00000200, "SDTRx", "Sign Deadtime Rising value")
        self.DTRx = BitField(self, 0x000001FF, "DTRx", "Deadtime Rising value")

class SA_HRTIM_TIMB_SETB1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETB1R", "Timerx Output1 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "Registers update (transfer preload to active)")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "External Event 1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "Timer Event 9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "Timer Event 8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "Timer Event 7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "Timer Event 6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "Timer Event 5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "Timer Event 4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "Timer Event 3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "Timer Event 2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "Timer Event 1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "Master Compare 4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "Master Compare 3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "Master Compare 2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "Master Compare 1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "Master Period")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "Timer A compare 4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "Timer A compare 3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "Timer A compare 2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "Timer A compare 1")
        self.PER = BitField(self, 0x00000004, "PER", "Timer A Period")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "Timer A resynchronizaton")
        self.SST = BitField(self, 0x00000001, "SST", "Software Set trigger")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMB_RSTB1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTB1R", "Timerx Output1 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMB_SETB2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETB2R", "Timerx Output2 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SST = BitField(self, 0x00000001, "SST", "SST")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMB_RSTB2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTB2R", "Timerx Output2 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMB_EEFBR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFBR1", "Timerx External Event Filtering Register 1")
        self.EE5FLTR = BitField(self, 0x1E000000, "EE5FLTR", "External Event 5 filter")
        self.EE5LTCH = BitField(self, 0x01000000, "EE5LTCH", "External Event 5 latch")
        self.EE4FLTR = BitField(self, 0x00780000, "EE4FLTR", "External Event 4 filter")
        self.EE4LTCH = BitField(self, 0x00040000, "EE4LTCH", "External Event 4 latch")
        self.EE3FLTR = BitField(self, 0x0001E000, "EE3FLTR", "External Event 3 filter")
        self.EE3LTCH = BitField(self, 0x00001000, "EE3LTCH", "External Event 3 latch")
        self.EE2FLTR = BitField(self, 0x00000780, "EE2FLTR", "External Event 2 filter")
        self.EE2LTCH = BitField(self, 0x00000040, "EE2LTCH", "External Event 2 latch")
        self.EE1FLTR = BitField(self, 0x0000001E, "EE1FLTR", "External Event 1 filter")
        self.EE1LTCH = BitField(self, 0x00000001, "EE1LTCH", "External Event 1 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMB_EEFBR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFBR2", "Timerx External Event Filtering Register 2")
        self.EE10FLTR = BitField(self, 0x1E000000, "EE10FLTR", "External Event 10 filter")
        self.EE10LTCH = BitField(self, 0x01000000, "EE10LTCH", "External Event 10 latch")
        self.EE9FLTR = BitField(self, 0x00780000, "EE9FLTR", "External Event 9 filter")
        self.EE9LTCH = BitField(self, 0x00040000, "EE9LTCH", "External Event 9 latch")
        self.EE8FLTR = BitField(self, 0x0001E000, "EE8FLTR", "External Event 8 filter")
        self.EE8LTCH = BitField(self, 0x00001000, "EE8LTCH", "External Event 8 latch")
        self.EE7FLTR = BitField(self, 0x00000780, "EE7FLTR", "External Event 7 filter")
        self.EE7LTCH = BitField(self, 0x00000040, "EE7LTCH", "External Event 7 latch")
        self.EE6FLTR = BitField(self, 0x0000001E, "EE6FLTR", "External Event 6 filter")
        self.EE6LTCH = BitField(self, 0x00000001, "EE6LTCH", "External Event 6 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMB_RSTBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTBR", "TimerA Reset Register")
        self.TIMFCPM2 = BitField(self, 0x80000000, "TIMFCPM2", "Timer F Compare 2")
        self.TIMECMP4 = BitField(self, 0x40000000, "TIMECMP4", "Timer E Compare 4")
        self.TIMECMP2 = BitField(self, 0x20000000, "TIMECMP2", "Timer E Compare 2")
        self.TIMECMP1 = BitField(self, 0x10000000, "TIMECMP1", "Timer E Compare 1")
        self.TIMDCMP4 = BitField(self, 0x08000000, "TIMDCMP4", "Timer D Compare 4")
        self.TIMDCMP2 = BitField(self, 0x04000000, "TIMDCMP2", "Timer D Compare 2")
        self.TIMDCMP1 = BitField(self, 0x02000000, "TIMDCMP1", "Timer D Compare 1")
        self.TIMCCMP4 = BitField(self, 0x01000000, "TIMCCMP4", "Timer C Compare 4")
        self.TIMCCMP2 = BitField(self, 0x00800000, "TIMCCMP2", "Timer C Compare 2")
        self.TIMCCMP1 = BitField(self, 0x00400000, "TIMCCMP1", "Timer C Compare 1")
        self.TIMACMP4 = BitField(self, 0x00200000, "TIMACMP4", "Timer A Compare 4")
        self.TIMACMP2 = BitField(self, 0x00100000, "TIMACMP2", "Timer A Compare 2")
        self.TIMACMP1 = BitField(self, 0x00080000, "TIMACMP1", "Timer A Compare 1")
        self.EXTEVNT10 = BitField(self, 0x00040000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x00020000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x00010000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x00008000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x00004000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x00002000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x00001000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00000800, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00000400, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00000200, "EXTEVNT1", "External Event 1")
        self.MSTCMP4 = BitField(self, 0x00000100, "MSTCMP4", "Master compare 4")
        self.MSTCMP3 = BitField(self, 0x00000080, "MSTCMP3", "Master compare 3")
        self.MSTCMP2 = BitField(self, 0x00000040, "MSTCMP2", "Master compare 2")
        self.MSTCMP1 = BitField(self, 0x00000020, "MSTCMP1", "Master compare 1")
        self.MSTPER = BitField(self, 0x00000010, "MSTPER", "Master timer Period")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Timer A compare 4 reset")
        self.CMP2 = BitField(self, 0x00000004, "CMP2", "Timer A compare 2 reset")
        self.UPDT = BitField(self, 0x00000002, "UPDT", "Timer A Update reset")
        self.TIMFCMP1 = BitField(self, 0x00000001, "TIMFCMP1", "Timer A Update reset")
        self.TIMACMP = Subscriptor(self, "TIMACMP{}")
        self.TIMDCMP = Subscriptor(self, "TIMDCMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMCCMP = Subscriptor(self, "TIMCCMP{}")
        self.TIMECMP = Subscriptor(self, "TIMECMP{}")

class SA_HRTIM_TIMB_CHPBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CHPBR", "Timerx Chopper Register")
        self.STRTPW = BitField(self, 0x00000780, "STRTPW", "STRTPW")
        self.CHPDTY = BitField(self, 0x00000070, "CHPDTY", "Timerx chopper duty cycle value")
        self.CHPFRQ = BitField(self, 0x0000000F, "CHPFRQ", "Timerx carrier frequency value")

class SA_HRTIM_TIMB_CPT1BCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1BCR", "Timerx Capture 2 Control Register")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TFCMP2 = BitField(self, 0x00080000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x00040000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x00020000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x00010000, "TF1SET", "TF1SET")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMB_CPT2BCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2BCR", "CPT2xCR")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TFCMP2 = BitField(self, 0x00080000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x00040000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x00020000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x00010000, "TF1SET", "TF1SET")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMB_OUTBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OUTBR", "Timerx Output Register")
        self.DIDL2 = BitField(self, 0x00800000, "DIDL2", "Output 2 Deadtime upon burst mode Idle entry")
        self.CHP2 = BitField(self, 0x00400000, "CHP2", "Output 2 Chopper enable")
        self.FAULT2 = BitField(self, 0x00300000, "FAULT2", "Output 2 Fault state")
        self.IDLES2 = BitField(self, 0x00080000, "IDLES2", "Output 2 Idle State")
        self.IDLEM2 = BitField(self, 0x00040000, "IDLEM2", "Output 2 Idle mode")
        self.POL2 = BitField(self, 0x00020000, "POL2", "Output 2 polarity")
        self.BIAR = BitField(self, 0x00004000, "BIAR", "Balanced Idle Automatic Resume")
        self.DLYPRT = BitField(self, 0x00001C00, "DLYPRT", "Delayed Protection")
        self.DLYPRTEN = BitField(self, 0x00000200, "DLYPRTEN", "Delayed Protection Enable")
        self.DTEN = BitField(self, 0x00000100, "DTEN", "Deadtime enable")
        self.DIDL1 = BitField(self, 0x00000080, "DIDL1", "Output 1 Deadtime upon burst mode Idle entry")
        self.CHP1 = BitField(self, 0x00000040, "CHP1", "Output 1 Chopper enable")
        self.FAULT1 = BitField(self, 0x00000030, "FAULT1", "Output 1 Fault state")
        self.IDLES1 = BitField(self, 0x00000008, "IDLES1", "Output 1 Idle State")
        self.IDLEM1 = BitField(self, 0x00000004, "IDLEM1", "Output 1 Idle mode")
        self.POL1 = BitField(self, 0x00000002, "POL1", "Output 1 polarity")
        self.POL = Subscriptor(self, "POL{}")
        self.DIDL = Subscriptor(self, "DIDL{}")
        self.FAULT = Subscriptor(self, "FAULT{}")
        self.CHP = Subscriptor(self, "CHP{}")
        self.IDLES = Subscriptor(self, "IDLES{}")
        self.IDLEM = Subscriptor(self, "IDLEM{}")

class SA_HRTIM_TIMB_FLTBR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTBR", "Timerx Fault Register")
        self.FLTLCK = BitField(self, 0x80000000, "FLTLCK", "Fault sources Lock")
        self.FLT6EN = BitField(self, 0x00000020, "FLT6EN", "Fault 6 enable")
        self.FLT5EN = BitField(self, 0x00000010, "FLT5EN", "Fault 5 enable")
        self.FLT4EN = BitField(self, 0x00000008, "FLT4EN", "Fault 4 enable")
        self.FLT3EN = BitField(self, 0x00000004, "FLT3EN", "Fault 3 enable")
        self.FLT2EN = BitField(self, 0x00000002, "FLT2EN", "Fault 2 enable")
        self.FLT1EN = BitField(self, 0x00000001, "FLT1EN", "Fault 1 enable")
        self.FLTEN = Subscriptor(self, "FLT{}EN")

class SA_HRTIM_TIMB_TIMBCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMBCR2", "HRTIM Timerx Control Register 2")
        self.TRGHLF = BitField(self, 0x00100000, "TRGHLF", "Triggered-half mode")
        self.GTCMP3 = BitField(self, 0x00020000, "GTCMP3", "Greater than Compare 3 PWM mode")
        self.GTCMP1 = BitField(self, 0x00010000, "GTCMP1", "Greater than Compare 1 PWM mode")
        self.FEROM = BitField(self, 0x0000C000, "FEROM", "Fault and Event Roll-Over Mode")
        self.BMROM = BitField(self, 0x00003000, "BMROM", "Burst Mode Roll-Over Mode")
        self.ADROM = BitField(self, 0x00000C00, "ADROM", "ADC Roll-Over Mode")
        self.OUTROM = BitField(self, 0x00000300, "OUTROM", "Output Roll-Over Mode")
        self.ROM = BitField(self, 0x000000C0, "ROM", "Roll-Over Mode")
        self.UDM = BitField(self, 0x00000010, "UDM", "Up-Down Mode")
        self.DCDR = BitField(self, 0x00000004, "DCDR", "Dual Channel DAC Reset trigger")
        self.DCDS = BitField(self, 0x00000002, "DCDS", "Dual Channel DAC Step trigger")
        self.DCDE = BitField(self, 0x00000001, "DCDE", "Dual Channel DAC trigger enable")

class SA_HRTIM_TIMB_BEEFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BEEFR3", "HRTIM Timerx External Event Filtering Register 3")
        self.EEVACNT = BitField(self, 0x00003F00, "EEVACNT", "External Event A counter")
        self.EEVASEL = BitField(self, 0x000000F0, "EEVASEL", "External Event A Selection")
        self.EEVARSTM = BitField(self, 0x00000004, "EEVARSTM", "External Event A Reset Mode")
        self.EEVACRES = BitField(self, 0x00000002, "EEVACRES", "External Event A Counter Reset")
        self.EEVACE = BitField(self, 0x00000001, "EEVACE", "External Event A Counter Enable")

class SA_HRTIM_TIMB(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: TIMB")
        self.TIMBCR = SA_HRTIM_TIMB_TIMBCR(self, 0x0)
        self.TIMBISR = SA_HRTIM_TIMB_TIMBISR(self, 0x4)
        self.TIMBICR = SA_HRTIM_TIMB_TIMBICR(self, 0x8)
        self.TIMBDIER = SA_HRTIM_TIMB_TIMBDIER(self, 0xC)
        self.CNTR = SA_HRTIM_TIMB_CNTR(self, 0x10)
        self.PERBR = SA_HRTIM_TIMB_PERBR(self, 0x14)
        self.REPBR = SA_HRTIM_TIMB_REPBR(self, 0x18)
        self.CMP1BR = SA_HRTIM_TIMB_CMP1BR(self, 0x1C)
        self.CMP1CBR = SA_HRTIM_TIMB_CMP1CBR(self, 0x20)
        self.CMP2BR = SA_HRTIM_TIMB_CMP2BR(self, 0x24)
        self.CMP3BR = SA_HRTIM_TIMB_CMP3BR(self, 0x28)
        self.CMP4BR = SA_HRTIM_TIMB_CMP4BR(self, 0x2C)
        self.CPT1BR = SA_HRTIM_TIMB_CPT1BR(self, 0x30)
        self.CPT2BR = SA_HRTIM_TIMB_CPT2BR(self, 0x34)
        self.DTBR = SA_HRTIM_TIMB_DTBR(self, 0x38)
        self.SETB1R = SA_HRTIM_TIMB_SETB1R(self, 0x3C)
        self.RSTB1R = SA_HRTIM_TIMB_RSTB1R(self, 0x40)
        self.SETB2R = SA_HRTIM_TIMB_SETB2R(self, 0x44)
        self.RSTB2R = SA_HRTIM_TIMB_RSTB2R(self, 0x48)
        self.EEFBR1 = SA_HRTIM_TIMB_EEFBR1(self, 0x4C)
        self.EEFBR2 = SA_HRTIM_TIMB_EEFBR2(self, 0x50)
        self.RSTBR = SA_HRTIM_TIMB_RSTBR(self, 0x54)
        self.CHPBR = SA_HRTIM_TIMB_CHPBR(self, 0x58)
        self.CPT1BCR = SA_HRTIM_TIMB_CPT1BCR(self, 0x5C)
        self.CPT2BCR = SA_HRTIM_TIMB_CPT2BCR(self, 0x60)
        self.OUTBR = SA_HRTIM_TIMB_OUTBR(self, 0x64)
        self.FLTBR = SA_HRTIM_TIMB_FLTBR(self, 0x68)
        self.TIMBCR2 = SA_HRTIM_TIMB_TIMBCR2(self, 0x6C)
        self.BEEFR3 = SA_HRTIM_TIMB_BEEFR3(self, 0x70)
        self.CPTBCR = Subscriptor(self, "CPT{}BCR")
        self.EEFBR = Subscriptor(self, "EEFBR{}")
        self.CPTBR = Subscriptor(self, "CPT{}BR")
        self.CMPBR = Subscriptor(self, "CMP{}BR")
        self.SETBR = Subscriptor(self, "SETB{}R")

HRTIM_TIMB = SA_HRTIM_TIMB(0x40016900, "HRTIM_TIMB")

class SA_HRTIM_TIMC_TIMCCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMCCR", "Timerx Control Register")
        self.UPDGAT = BitField(self, 0xF0000000, "UPDGAT", "Update Gating")
        self.PREEN = BitField(self, 0x08000000, "PREEN", "Preload enable")
        self.DACSYNC = BitField(self, 0x06000000, "DACSYNC", "AC Synchronization")
        self.MSTU = BitField(self, 0x01000000, "MSTU", "Master Timer update")
        self.TEU = BitField(self, 0x00800000, "TEU", "TEU")
        self.TDU = BitField(self, 0x00400000, "TDU", "TDU")
        self.TBU = BitField(self, 0x00100000, "TBU", "TBU")
        self.TAU = BitField(self, 0x00080000, "TAU", "TAU")
        self.TxRSTU = BitField(self, 0x00040000, "TxRSTU", "Timerx reset update")
        self.TxREPU = BitField(self, 0x00020000, "TxREPU", "Timer x Repetition update")
        self.TFU = BitField(self, 0x00010000, "TFU", "TFU")
        self.DELCMP4 = BitField(self, 0x0000C000, "DELCMP4", "Delayed CMP4 mode")
        self.DELCMP2 = BitField(self, 0x00003000, "DELCMP2", "Delayed CMP2 mode")
        self.SYNCSTRTx = BitField(self, 0x00000800, "SYNCSTRTx", "Synchronization Starts Timer x")
        self.SYNCRSTx = BitField(self, 0x00000400, "SYNCRSTx", "Synchronization Resets Timer x")
        self.RSYNCU = BitField(self, 0x00000200, "RSYNCU", "Re-Synchronized Update")
        self.INTLVD = BitField(self, 0x00000180, "INTLVD", "Interleaved mode")
        self.PSHPLL = BitField(self, 0x00000040, "PSHPLL", "Push-Pull mode enable")
        self.HALF = BitField(self, 0x00000020, "HALF", "Half mode enable")
        self.RETRIG = BitField(self, 0x00000010, "RETRIG", "Re-triggerable mode")
        self.CONT = BitField(self, 0x00000008, "CONT", "Continuous mode")
        self.CK_PSCx = BitField(self, 0x00000007, "CK_PSCx", "HRTIM Timer x Clock prescaler")

class SA_HRTIM_TIMC_TIMCISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMCISR", "Timerx Interrupt Status Register")
        self.O2CPY = BitField(self, 0x00200000, "O2CPY", "Output 2 Copy")
        self.O1CPY = BitField(self, 0x00100000, "O1CPY", "Output 1 Copy")
        self.O2STAT = BitField(self, 0x00080000, "O2STAT", "Output 2 State")
        self.O1STAT = BitField(self, 0x00040000, "O1STAT", "Output 1 State")
        self.IPPSTAT = BitField(self, 0x00020000, "IPPSTAT", "Idle Push Pull Status")
        self.CPPSTAT = BitField(self, 0x00010000, "CPPSTAT", "Current Push Pull Status")
        self.DLYPRT = BitField(self, 0x00004000, "DLYPRT", "Delayed Protection Flag")
        self.RST = BitField(self, 0x00002000, "RST", "Reset Interrupt Flag")
        self.RSTx2 = BitField(self, 0x00001000, "RSTx2", "Output 2 Reset Interrupt Flag")
        self.SETx2 = BitField(self, 0x00000800, "SETx2", "Output 2 Set Interrupt Flag")
        self.RSTx1 = BitField(self, 0x00000400, "RSTx1", "Output 1 Reset Interrupt Flag")
        self.SETx1 = BitField(self, 0x00000200, "SETx1", "Output 1 Set Interrupt Flag")
        self.CPT2 = BitField(self, 0x00000100, "CPT2", "Capture2 Interrupt Flag")
        self.CPT1 = BitField(self, 0x00000080, "CPT1", "Capture1 Interrupt Flag")
        self.UPD = BitField(self, 0x00000040, "UPD", "Update Interrupt Flag")
        self.REP = BitField(self, 0x00000010, "REP", "Repetition Interrupt Flag")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Compare 4 Interrupt Flag")
        self.CMP3 = BitField(self, 0x00000004, "CMP3", "Compare 3 Interrupt Flag")
        self.CMP2 = BitField(self, 0x00000002, "CMP2", "Compare 2 Interrupt Flag")
        self.CMP1 = BitField(self, 0x00000001, "CMP1", "Compare 1 Interrupt Flag")
        self.RSTx = Subscriptor(self, "RSTx{}")
        self.OSTAT = Subscriptor(self, "O{}STAT")
        self.OCPY = Subscriptor(self, "O{}CPY")
        self.SETx = Subscriptor(self, "SETx{}")
        self.CPT = Subscriptor(self, "CPT{}")
        self.CMP = Subscriptor(self, "CMP{}")

class SA_HRTIM_TIMC_TIMCICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMCICR", "Timerx Interrupt Clear Register")
        self.DLYPRTC = BitField(self, 0x00004000, "DLYPRTC", "Delayed Protection Flag Clear")
        self.RSTC = BitField(self, 0x00002000, "RSTC", "Reset Interrupt flag Clear")
        self.RSTx2C = BitField(self, 0x00001000, "RSTx2C", "Output 2 Reset flag Clear")
        self.SET2xC = BitField(self, 0x00000800, "SET2xC", "Output 2 Set flag Clear")
        self.RSTx1C = BitField(self, 0x00000400, "RSTx1C", "Output 1 Reset flag Clear")
        self.SET1xC = BitField(self, 0x00000200, "SET1xC", "Output 1 Set flag Clear")
        self.CPT2C = BitField(self, 0x00000100, "CPT2C", "Capture2 Interrupt flag Clear")
        self.CPT1C = BitField(self, 0x00000080, "CPT1C", "Capture1 Interrupt flag Clear")
        self.UPDC = BitField(self, 0x00000040, "UPDC", "Update Interrupt flag Clear")
        self.REPC = BitField(self, 0x00000010, "REPC", "Repetition Interrupt flag Clear")
        self.CMP4C = BitField(self, 0x00000008, "CMP4C", "Compare 4 Interrupt flag Clear")
        self.CMP3C = BitField(self, 0x00000004, "CMP3C", "Compare 3 Interrupt flag Clear")
        self.CMP2C = BitField(self, 0x00000002, "CMP2C", "Compare 2 Interrupt flag Clear")
        self.CMP1C = BitField(self, 0x00000001, "CMP1C", "Compare 1 Interrupt flag Clear")
        self.CPTC = Subscriptor(self, "CPT{}C")
        self.SETxC = Subscriptor(self, "SET{}xC")
        self.CMPC = Subscriptor(self, "CMP{}C")
        self.RSTxC = Subscriptor(self, "RSTx{}C")

class SA_HRTIM_TIMC_TIMCDIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMCDIER", "TIMxDIER")
        self.DLYPRTDE = BitField(self, 0x40000000, "DLYPRTDE", "DLYPRTDE")
        self.RSTDE = BitField(self, 0x20000000, "RSTDE", "RSTDE")
        self.RSTx2DE = BitField(self, 0x10000000, "RSTx2DE", "RSTx2DE")
        self.SETx2DE = BitField(self, 0x08000000, "SETx2DE", "SETx2DE")
        self.RSTx1DE = BitField(self, 0x04000000, "RSTx1DE", "RSTx1DE")
        self.SET1xDE = BitField(self, 0x02000000, "SET1xDE", "SET1xDE")
        self.CPT2DE = BitField(self, 0x01000000, "CPT2DE", "CPT2DE")
        self.CPT1DE = BitField(self, 0x00800000, "CPT1DE", "CPT1DE")
        self.UPDDE = BitField(self, 0x00400000, "UPDDE", "UPDDE")
        self.REPDE = BitField(self, 0x00100000, "REPDE", "REPDE")
        self.CMP4DE = BitField(self, 0x00080000, "CMP4DE", "CMP4DE")
        self.CMP3DE = BitField(self, 0x00040000, "CMP3DE", "CMP3DE")
        self.CMP2DE = BitField(self, 0x00020000, "CMP2DE", "CMP2DE")
        self.CMP1DE = BitField(self, 0x00010000, "CMP1DE", "CMP1DE")
        self.DLYPRTIE = BitField(self, 0x00004000, "DLYPRTIE", "DLYPRTIE")
        self.RSTIE = BitField(self, 0x00002000, "RSTIE", "RSTIE")
        self.RSTx2IE = BitField(self, 0x00001000, "RSTx2IE", "RSTx2IE")
        self.SETx2IE = BitField(self, 0x00000800, "SETx2IE", "SETx2IE")
        self.RSTx1IE = BitField(self, 0x00000400, "RSTx1IE", "RSTx1IE")
        self.SET1xIE = BitField(self, 0x00000200, "SET1xIE", "SET1xIE")
        self.CPT2IE = BitField(self, 0x00000100, "CPT2IE", "CPT2IE")
        self.CPT1IE = BitField(self, 0x00000080, "CPT1IE", "CPT1IE")
        self.UPDIE = BitField(self, 0x00000040, "UPDIE", "UPDIE")
        self.REPIE = BitField(self, 0x00000010, "REPIE", "REPIE")
        self.CMP4IE = BitField(self, 0x00000008, "CMP4IE", "CMP4IE")
        self.CMP3IE = BitField(self, 0x00000004, "CMP3IE", "CMP3IE")
        self.CMP2IE = BitField(self, 0x00000002, "CMP2IE", "CMP2IE")
        self.CMP1IE = BitField(self, 0x00000001, "CMP1IE", "CMP1IE")
        self.RSTxIE = Subscriptor(self, "RSTx{}IE")
        self.CMPDE = Subscriptor(self, "CMP{}DE")
        self.RSTxDE = Subscriptor(self, "RSTx{}DE")
        self.CPTDE = Subscriptor(self, "CPT{}DE")
        self.CPTIE = Subscriptor(self, "CPT{}IE")
        self.CMPIE = Subscriptor(self, "CMP{}IE")

class SA_HRTIM_TIMC_CNTCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNTCR", "Timerx Counter Register")
        self.CNTx = BitField(self, 0x0000FFFF, "CNTx", "Timerx Counter value")

class SA_HRTIM_TIMC_PERCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "PERCR", "Timerx Period Register")
        self.PERx = BitField(self, 0x0000FFFF, "PERx", "Timerx Period value")

class SA_HRTIM_TIMC_REPCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "REPCR", "Timerx Repetition Register")
        self.REPx = BitField(self, 0x000000FF, "REPx", "Timerx Repetition counter value")

class SA_HRTIM_TIMC_CMP1CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1CR", "Timerx Compare 1 Register")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMC_CMP1CCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1CCR", "Timerx Compare 1 Compound Register")
        self.REPx = BitField(self, 0x00FF0000, "REPx", "Timerx Repetition value (aliased from HRTIM_REPx register)")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMC_CMP2CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP2CR", "Timerx Compare 2 Register")
        self.CMP2x = BitField(self, 0x0000FFFF, "CMP2x", "Timerx Compare 2 value")

class SA_HRTIM_TIMC_CMP3CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP3CR", "Timerx Compare 3 Register")
        self.CMP3x = BitField(self, 0x0000FFFF, "CMP3x", "Timerx Compare 3 value")

class SA_HRTIM_TIMC_CMP4CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP4CR", "Timerx Compare 4 Register")
        self.CMP4x = BitField(self, 0x0000FFFF, "CMP4x", "Timerx Compare 4 value")

class SA_HRTIM_TIMC_CPT1CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1CR", "Timerx Capture 1 Register")
        self.CPT1x = BitField(self, 0x0000FFFF, "CPT1x", "Timerx Capture 1 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMC_CPT2CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2CR", "Timerx Capture 2 Register")
        self.CPT2x = BitField(self, 0x0000FFFF, "CPT2x", "Timerx Capture 2 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMC_DTCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTCR", "Timerx Deadtime Register")
        self.DTFLKx = BitField(self, 0x80000000, "DTFLKx", "Deadtime Falling Lock")
        self.DTFSLKx = BitField(self, 0x40000000, "DTFSLKx", "Deadtime Falling Sign Lock")
        self.SDTFx = BitField(self, 0x02000000, "SDTFx", "Sign Deadtime Falling value")
        self.DTFx = BitField(self, 0x01FF0000, "DTFx", "Deadtime Falling value")
        self.DTRLKx = BitField(self, 0x00008000, "DTRLKx", "Deadtime Rising Lock")
        self.DTRSLKx = BitField(self, 0x00004000, "DTRSLKx", "Deadtime Rising Sign Lock")
        self.DTPRSC = BitField(self, 0x00001C00, "DTPRSC", "Deadtime Prescaler")
        self.SDTRx = BitField(self, 0x00000200, "SDTRx", "Sign Deadtime Rising value")
        self.DTRx = BitField(self, 0x000001FF, "DTRx", "Deadtime Rising value")

class SA_HRTIM_TIMC_SETC1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETC1R", "Timerx Output1 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "Registers update (transfer preload to active)")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "External Event 1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "Timer Event 9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "Timer Event 8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "Timer Event 7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "Timer Event 6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "Timer Event 5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "Timer Event 4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "Timer Event 3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "Timer Event 2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "Timer Event 1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "Master Compare 4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "Master Compare 3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "Master Compare 2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "Master Compare 1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "Master Period")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "Timer A compare 4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "Timer A compare 3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "Timer A compare 2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "Timer A compare 1")
        self.PER = BitField(self, 0x00000004, "PER", "Timer A Period")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "Timer A resynchronizaton")
        self.SST = BitField(self, 0x00000001, "SST", "Software Set trigger")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMC_RSTC1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTC1R", "Timerx Output1 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMC_SETC2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETC2R", "Timerx Output2 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SST = BitField(self, 0x00000001, "SST", "SST")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMC_RSTC2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTC2R", "Timerx Output2 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMC_EEFCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFCR1", "Timerx External Event Filtering Register 1")
        self.EE5FLTR = BitField(self, 0x1E000000, "EE5FLTR", "External Event 5 filter")
        self.EE5LTCH = BitField(self, 0x01000000, "EE5LTCH", "External Event 5 latch")
        self.EE4FLTR = BitField(self, 0x00780000, "EE4FLTR", "External Event 4 filter")
        self.EE4LTCH = BitField(self, 0x00040000, "EE4LTCH", "External Event 4 latch")
        self.EE3FLTR = BitField(self, 0x0001E000, "EE3FLTR", "External Event 3 filter")
        self.EE3LTCH = BitField(self, 0x00001000, "EE3LTCH", "External Event 3 latch")
        self.EE2FLTR = BitField(self, 0x00000780, "EE2FLTR", "External Event 2 filter")
        self.EE2LTCH = BitField(self, 0x00000040, "EE2LTCH", "External Event 2 latch")
        self.EE1FLTR = BitField(self, 0x0000001E, "EE1FLTR", "External Event 1 filter")
        self.EE1LTCH = BitField(self, 0x00000001, "EE1LTCH", "External Event 1 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMC_EEFCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFCR2", "Timerx External Event Filtering Register 2")
        self.EE10FLTR = BitField(self, 0x1E000000, "EE10FLTR", "External Event 10 filter")
        self.EE10LTCH = BitField(self, 0x01000000, "EE10LTCH", "External Event 10 latch")
        self.EE9FLTR = BitField(self, 0x00780000, "EE9FLTR", "External Event 9 filter")
        self.EE9LTCH = BitField(self, 0x00040000, "EE9LTCH", "External Event 9 latch")
        self.EE8FLTR = BitField(self, 0x0001E000, "EE8FLTR", "External Event 8 filter")
        self.EE8LTCH = BitField(self, 0x00001000, "EE8LTCH", "External Event 8 latch")
        self.EE7FLTR = BitField(self, 0x00000780, "EE7FLTR", "External Event 7 filter")
        self.EE7LTCH = BitField(self, 0x00000040, "EE7LTCH", "External Event 7 latch")
        self.EE6FLTR = BitField(self, 0x0000001E, "EE6FLTR", "External Event 6 filter")
        self.EE6LTCH = BitField(self, 0x00000001, "EE6LTCH", "External Event 6 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMC_RSTCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTCR", "TimerA Reset Register")
        self.TIMFCPM2 = BitField(self, 0x80000000, "TIMFCPM2", "Timer F Compare 2")
        self.TIMECMP4 = BitField(self, 0x40000000, "TIMECMP4", "Timer E Compare 4")
        self.TIMECMP2 = BitField(self, 0x20000000, "TIMECMP2", "Timer E Compare 2")
        self.TIMECMP1 = BitField(self, 0x10000000, "TIMECMP1", "Timer E Compare 1")
        self.TIMDCMP4 = BitField(self, 0x08000000, "TIMDCMP4", "Timer D Compare 4")
        self.TIMDCMP2 = BitField(self, 0x04000000, "TIMDCMP2", "Timer D Compare 2")
        self.TIMDCMP1 = BitField(self, 0x02000000, "TIMDCMP1", "Timer D Compare 1")
        self.TIMBCMP4 = BitField(self, 0x01000000, "TIMBCMP4", "Timer B Compare 4")
        self.TIMBCMP2 = BitField(self, 0x00800000, "TIMBCMP2", "Timer B Compare 2")
        self.TIMBCMP1 = BitField(self, 0x00400000, "TIMBCMP1", "Timer B Compare 1")
        self.TIMACMP4 = BitField(self, 0x00200000, "TIMACMP4", "Timer A Compare 4")
        self.TIMACMP2 = BitField(self, 0x00100000, "TIMACMP2", "Timer A Compare 2")
        self.TIMACMP1 = BitField(self, 0x00080000, "TIMACMP1", "Timer A Compare 1")
        self.EXTEVNT10 = BitField(self, 0x00040000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x00020000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x00010000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x00008000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x00004000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x00002000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x00001000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00000800, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00000400, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00000200, "EXTEVNT1", "External Event 1")
        self.MSTCMP4 = BitField(self, 0x00000100, "MSTCMP4", "Master compare 4")
        self.MSTCMP3 = BitField(self, 0x00000080, "MSTCMP3", "Master compare 3")
        self.MSTCMP2 = BitField(self, 0x00000040, "MSTCMP2", "Master compare 2")
        self.MSTCMP1 = BitField(self, 0x00000020, "MSTCMP1", "Master compare 1")
        self.MSTPER = BitField(self, 0x00000010, "MSTPER", "Master timer Period")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Timer A compare 4 reset")
        self.CMP2 = BitField(self, 0x00000004, "CMP2", "Timer A compare 2 reset")
        self.UPDT = BitField(self, 0x00000002, "UPDT", "Timer A Update reset")
        self.TIMFCMP1 = BitField(self, 0x00000001, "TIMFCMP1", "Timer A Update reset")
        self.TIMACMP = Subscriptor(self, "TIMACMP{}")
        self.TIMDCMP = Subscriptor(self, "TIMDCMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMBCMP = Subscriptor(self, "TIMBCMP{}")
        self.TIMECMP = Subscriptor(self, "TIMECMP{}")

class SA_HRTIM_TIMC_CHPCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CHPCR", "Timerx Chopper Register")
        self.STRTPW = BitField(self, 0x00000780, "STRTPW", "STRTPW")
        self.CHPDTY = BitField(self, 0x00000070, "CHPDTY", "Timerx chopper duty cycle value")
        self.CHPFRQ = BitField(self, 0x0000000F, "CHPFRQ", "Timerx carrier frequency value")

class SA_HRTIM_TIMC_CPT1CCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1CCR", "Timerx Capture 2 Control Register")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TFCMP2 = BitField(self, 0x00800000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x00400000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x00200000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x00100000, "TF1SET", "TF1SET")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMC_CPT2CCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2CCR", "CPT2xCR")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TF1CMP2 = BitField(self, 0x00800000, "TF1CMP2", "TF1CMP2")
        self.TF1CMP1 = BitField(self, 0x00400000, "TF1CMP1", "TF1CMP1")
        self.TF1RST = BitField(self, 0x00200000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x00100000, "TF1SET", "TF1SET")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TF1CMP = Subscriptor(self, "TF1CMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMC_OUTCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OUTCR", "Timerx Output Register")
        self.DIDL2 = BitField(self, 0x00800000, "DIDL2", "Output 2 Deadtime upon burst mode Idle entry")
        self.CHP2 = BitField(self, 0x00400000, "CHP2", "Output 2 Chopper enable")
        self.FAULT2 = BitField(self, 0x00300000, "FAULT2", "Output 2 Fault state")
        self.IDLES2 = BitField(self, 0x00080000, "IDLES2", "Output 2 Idle State")
        self.IDLEM2 = BitField(self, 0x00040000, "IDLEM2", "Output 2 Idle mode")
        self.POL2 = BitField(self, 0x00020000, "POL2", "Output 2 polarity")
        self.BIAR = BitField(self, 0x00004000, "BIAR", "Balanced Idle Automatic Resume")
        self.DLYPRT = BitField(self, 0x00001C00, "DLYPRT", "Delayed Protection")
        self.DLYPRTEN = BitField(self, 0x00000200, "DLYPRTEN", "Delayed Protection Enable")
        self.DTEN = BitField(self, 0x00000100, "DTEN", "Deadtime enable")
        self.DIDL1 = BitField(self, 0x00000080, "DIDL1", "Output 1 Deadtime upon burst mode Idle entry")
        self.CHP1 = BitField(self, 0x00000040, "CHP1", "Output 1 Chopper enable")
        self.FAULT1 = BitField(self, 0x00000030, "FAULT1", "Output 1 Fault state")
        self.IDLES1 = BitField(self, 0x00000008, "IDLES1", "Output 1 Idle State")
        self.IDLEM1 = BitField(self, 0x00000004, "IDLEM1", "Output 1 Idle mode")
        self.POL1 = BitField(self, 0x00000002, "POL1", "Output 1 polarity")
        self.POL = Subscriptor(self, "POL{}")
        self.DIDL = Subscriptor(self, "DIDL{}")
        self.FAULT = Subscriptor(self, "FAULT{}")
        self.CHP = Subscriptor(self, "CHP{}")
        self.IDLES = Subscriptor(self, "IDLES{}")
        self.IDLEM = Subscriptor(self, "IDLEM{}")

class SA_HRTIM_TIMC_FLTCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTCR", "Timerx Fault Register")
        self.FLTLCK = BitField(self, 0x80000000, "FLTLCK", "Fault sources Lock")
        self.FLT6EN = BitField(self, 0x00000020, "FLT6EN", "Fault 6 enable")
        self.FLT5EN = BitField(self, 0x00000010, "FLT5EN", "Fault 5 enable")
        self.FLT4EN = BitField(self, 0x00000008, "FLT4EN", "Fault 4 enable")
        self.FLT3EN = BitField(self, 0x00000004, "FLT3EN", "Fault 3 enable")
        self.FLT2EN = BitField(self, 0x00000002, "FLT2EN", "Fault 2 enable")
        self.FLT1EN = BitField(self, 0x00000001, "FLT1EN", "Fault 1 enable")
        self.FLTEN = Subscriptor(self, "FLT{}EN")

class SA_HRTIM_TIMC_TIMCCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMCCR2", "HRTIM Timerx Control Register 2")
        self.TRGHLF = BitField(self, 0x00100000, "TRGHLF", "Triggered-half mode")
        self.GTCMP3 = BitField(self, 0x00020000, "GTCMP3", "Greater than Compare 3 PWM mode")
        self.GTCMP1 = BitField(self, 0x00010000, "GTCMP1", "Greater than Compare 1 PWM mode")
        self.FEROM = BitField(self, 0x0000C000, "FEROM", "Fault and Event Roll-Over Mode")
        self.BMROM = BitField(self, 0x00003000, "BMROM", "Burst Mode Roll-Over Mode")
        self.ADROM = BitField(self, 0x00000C00, "ADROM", "ADC Roll-Over Mode")
        self.OUTROM = BitField(self, 0x00000300, "OUTROM", "Output Roll-Over Mode")
        self.ROM = BitField(self, 0x000000C0, "ROM", "Roll-Over Mode")
        self.UDM = BitField(self, 0x00000010, "UDM", "Up-Down Mode")
        self.DCDR = BitField(self, 0x00000004, "DCDR", "Dual Channel DAC Reset trigger")
        self.DCDS = BitField(self, 0x00000002, "DCDS", "Dual Channel DAC Step trigger")
        self.DCDE = BitField(self, 0x00000001, "DCDE", "Dual Channel DAC trigger enable")

class SA_HRTIM_TIMC_CEEFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CEEFR3", "HRTIM Timerx External Event Filtering Register 3")
        self.EEVACNT = BitField(self, 0x00003F00, "EEVACNT", "External Event A counter")
        self.EEVASEL = BitField(self, 0x000000F0, "EEVASEL", "External Event A Selection")
        self.EEVARSTM = BitField(self, 0x00000004, "EEVARSTM", "External Event A Reset Mode")
        self.EEVACRES = BitField(self, 0x00000002, "EEVACRES", "External Event A Counter Reset")
        self.EEVACE = BitField(self, 0x00000001, "EEVACE", "External Event A Counter Enable")

class SA_HRTIM_TIMC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: TIMC")
        self.TIMCCR = SA_HRTIM_TIMC_TIMCCR(self, 0x0)
        self.TIMCISR = SA_HRTIM_TIMC_TIMCISR(self, 0x4)
        self.TIMCICR = SA_HRTIM_TIMC_TIMCICR(self, 0x8)
        self.TIMCDIER = SA_HRTIM_TIMC_TIMCDIER(self, 0xC)
        self.CNTCR = SA_HRTIM_TIMC_CNTCR(self, 0x10)
        self.PERCR = SA_HRTIM_TIMC_PERCR(self, 0x14)
        self.REPCR = SA_HRTIM_TIMC_REPCR(self, 0x18)
        self.CMP1CR = SA_HRTIM_TIMC_CMP1CR(self, 0x1C)
        self.CMP1CCR = SA_HRTIM_TIMC_CMP1CCR(self, 0x20)
        self.CMP2CR = SA_HRTIM_TIMC_CMP2CR(self, 0x24)
        self.CMP3CR = SA_HRTIM_TIMC_CMP3CR(self, 0x28)
        self.CMP4CR = SA_HRTIM_TIMC_CMP4CR(self, 0x2C)
        self.CPT1CR = SA_HRTIM_TIMC_CPT1CR(self, 0x30)
        self.CPT2CR = SA_HRTIM_TIMC_CPT2CR(self, 0x34)
        self.DTCR = SA_HRTIM_TIMC_DTCR(self, 0x38)
        self.SETC1R = SA_HRTIM_TIMC_SETC1R(self, 0x3C)
        self.RSTC1R = SA_HRTIM_TIMC_RSTC1R(self, 0x40)
        self.SETC2R = SA_HRTIM_TIMC_SETC2R(self, 0x44)
        self.RSTC2R = SA_HRTIM_TIMC_RSTC2R(self, 0x48)
        self.EEFCR1 = SA_HRTIM_TIMC_EEFCR1(self, 0x4C)
        self.EEFCR2 = SA_HRTIM_TIMC_EEFCR2(self, 0x50)
        self.RSTCR = SA_HRTIM_TIMC_RSTCR(self, 0x54)
        self.CHPCR = SA_HRTIM_TIMC_CHPCR(self, 0x58)
        self.CPT1CCR = SA_HRTIM_TIMC_CPT1CCR(self, 0x5C)
        self.CPT2CCR = SA_HRTIM_TIMC_CPT2CCR(self, 0x60)
        self.OUTCR = SA_HRTIM_TIMC_OUTCR(self, 0x64)
        self.FLTCR = SA_HRTIM_TIMC_FLTCR(self, 0x68)
        self.TIMCCR2 = SA_HRTIM_TIMC_TIMCCR2(self, 0x6C)
        self.CEEFR3 = SA_HRTIM_TIMC_CEEFR3(self, 0x70)
        self.CPTCCR = Subscriptor(self, "CPT{}CCR")
        self.SETCR = Subscriptor(self, "SETC{}R")
        self.EEFCR = Subscriptor(self, "EEFCR{}")
        self.CPTCR = Subscriptor(self, "CPT{}CR")
        self.CMPCR = Subscriptor(self, "CMP{}CR")

HRTIM_TIMC = SA_HRTIM_TIMC(0x40016980, "HRTIM_TIMC")

class SA_HRTIM_TIMD_TIMDCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMDCR", "Timerx Control Register")
        self.UPDGAT = BitField(self, 0xF0000000, "UPDGAT", "Update Gating")
        self.PREEN = BitField(self, 0x08000000, "PREEN", "Preload enable")
        self.DACSYNC = BitField(self, 0x06000000, "DACSYNC", "AC Synchronization")
        self.MSTU = BitField(self, 0x01000000, "MSTU", "Master Timer update")
        self.TEU = BitField(self, 0x00800000, "TEU", "TEU")
        self.TCU = BitField(self, 0x00200000, "TCU", "TCU")
        self.TBU = BitField(self, 0x00100000, "TBU", "TBU")
        self.TAU = BitField(self, 0x00080000, "TAU", "TAU")
        self.TxRSTU = BitField(self, 0x00040000, "TxRSTU", "Timerx reset update")
        self.TxREPU = BitField(self, 0x00020000, "TxREPU", "Timer x Repetition update")
        self.TFU = BitField(self, 0x00010000, "TFU", "TFU")
        self.DELCMP4 = BitField(self, 0x0000C000, "DELCMP4", "Delayed CMP4 mode")
        self.DELCMP2 = BitField(self, 0x00003000, "DELCMP2", "Delayed CMP2 mode")
        self.SYNCSTRTx = BitField(self, 0x00000800, "SYNCSTRTx", "Synchronization Starts Timer x")
        self.SYNCRSTx = BitField(self, 0x00000400, "SYNCRSTx", "Synchronization Resets Timer x")
        self.RSYNCU = BitField(self, 0x00000200, "RSYNCU", "Re-Synchronized Update")
        self.INTLVD = BitField(self, 0x00000180, "INTLVD", "Interleaved mode")
        self.PSHPLL = BitField(self, 0x00000040, "PSHPLL", "Push-Pull mode enable")
        self.HALF = BitField(self, 0x00000020, "HALF", "Half mode enable")
        self.RETRIG = BitField(self, 0x00000010, "RETRIG", "Re-triggerable mode")
        self.CONT = BitField(self, 0x00000008, "CONT", "Continuous mode")
        self.CK_PSCx = BitField(self, 0x00000007, "CK_PSCx", "HRTIM Timer x Clock prescaler")

class SA_HRTIM_TIMD_TIMDISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMDISR", "Timerx Interrupt Status Register")
        self.O2CPY = BitField(self, 0x00200000, "O2CPY", "Output 2 Copy")
        self.O1CPY = BitField(self, 0x00100000, "O1CPY", "Output 1 Copy")
        self.O2STAT = BitField(self, 0x00080000, "O2STAT", "Output 2 State")
        self.O1STAT = BitField(self, 0x00040000, "O1STAT", "Output 1 State")
        self.IPPSTAT = BitField(self, 0x00020000, "IPPSTAT", "Idle Push Pull Status")
        self.CPPSTAT = BitField(self, 0x00010000, "CPPSTAT", "Current Push Pull Status")
        self.DLYPRT = BitField(self, 0x00004000, "DLYPRT", "Delayed Protection Flag")
        self.RST = BitField(self, 0x00002000, "RST", "Reset Interrupt Flag")
        self.RSTx2 = BitField(self, 0x00001000, "RSTx2", "Output 2 Reset Interrupt Flag")
        self.SETx2 = BitField(self, 0x00000800, "SETx2", "Output 2 Set Interrupt Flag")
        self.RSTx1 = BitField(self, 0x00000400, "RSTx1", "Output 1 Reset Interrupt Flag")
        self.SETx1 = BitField(self, 0x00000200, "SETx1", "Output 1 Set Interrupt Flag")
        self.CPT2 = BitField(self, 0x00000100, "CPT2", "Capture2 Interrupt Flag")
        self.CPT1 = BitField(self, 0x00000080, "CPT1", "Capture1 Interrupt Flag")
        self.UPD = BitField(self, 0x00000040, "UPD", "Update Interrupt Flag")
        self.REP = BitField(self, 0x00000010, "REP", "Repetition Interrupt Flag")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Compare 4 Interrupt Flag")
        self.CMP3 = BitField(self, 0x00000004, "CMP3", "Compare 3 Interrupt Flag")
        self.CMP2 = BitField(self, 0x00000002, "CMP2", "Compare 2 Interrupt Flag")
        self.CMP1 = BitField(self, 0x00000001, "CMP1", "Compare 1 Interrupt Flag")
        self.RSTx = Subscriptor(self, "RSTx{}")
        self.OSTAT = Subscriptor(self, "O{}STAT")
        self.OCPY = Subscriptor(self, "O{}CPY")
        self.SETx = Subscriptor(self, "SETx{}")
        self.CPT = Subscriptor(self, "CPT{}")
        self.CMP = Subscriptor(self, "CMP{}")

class SA_HRTIM_TIMD_TIMDICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMDICR", "Timerx Interrupt Clear Register")
        self.DLYPRTC = BitField(self, 0x00004000, "DLYPRTC", "Delayed Protection Flag Clear")
        self.RSTC = BitField(self, 0x00002000, "RSTC", "Reset Interrupt flag Clear")
        self.RSTx2C = BitField(self, 0x00001000, "RSTx2C", "Output 2 Reset flag Clear")
        self.SET2xC = BitField(self, 0x00000800, "SET2xC", "Output 2 Set flag Clear")
        self.RSTx1C = BitField(self, 0x00000400, "RSTx1C", "Output 1 Reset flag Clear")
        self.SET1xC = BitField(self, 0x00000200, "SET1xC", "Output 1 Set flag Clear")
        self.CPT2C = BitField(self, 0x00000100, "CPT2C", "Capture2 Interrupt flag Clear")
        self.CPT1C = BitField(self, 0x00000080, "CPT1C", "Capture1 Interrupt flag Clear")
        self.UPDC = BitField(self, 0x00000040, "UPDC", "Update Interrupt flag Clear")
        self.REPC = BitField(self, 0x00000010, "REPC", "Repetition Interrupt flag Clear")
        self.CMP4C = BitField(self, 0x00000008, "CMP4C", "Compare 4 Interrupt flag Clear")
        self.CMP3C = BitField(self, 0x00000004, "CMP3C", "Compare 3 Interrupt flag Clear")
        self.CMP2C = BitField(self, 0x00000002, "CMP2C", "Compare 2 Interrupt flag Clear")
        self.CMP1C = BitField(self, 0x00000001, "CMP1C", "Compare 1 Interrupt flag Clear")
        self.CPTC = Subscriptor(self, "CPT{}C")
        self.SETxC = Subscriptor(self, "SET{}xC")
        self.CMPC = Subscriptor(self, "CMP{}C")
        self.RSTxC = Subscriptor(self, "RSTx{}C")

class SA_HRTIM_TIMD_TIMDDIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMDDIER", "TIMxDIER")
        self.DLYPRTDE = BitField(self, 0x40000000, "DLYPRTDE", "DLYPRTDE")
        self.RSTDE = BitField(self, 0x20000000, "RSTDE", "RSTDE")
        self.RSTx2DE = BitField(self, 0x10000000, "RSTx2DE", "RSTx2DE")
        self.SETx2DE = BitField(self, 0x08000000, "SETx2DE", "SETx2DE")
        self.RSTx1DE = BitField(self, 0x04000000, "RSTx1DE", "RSTx1DE")
        self.SET1xDE = BitField(self, 0x02000000, "SET1xDE", "SET1xDE")
        self.CPT2DE = BitField(self, 0x01000000, "CPT2DE", "CPT2DE")
        self.CPT1DE = BitField(self, 0x00800000, "CPT1DE", "CPT1DE")
        self.UPDDE = BitField(self, 0x00400000, "UPDDE", "UPDDE")
        self.REPDE = BitField(self, 0x00100000, "REPDE", "REPDE")
        self.CMP4DE = BitField(self, 0x00080000, "CMP4DE", "CMP4DE")
        self.CMP3DE = BitField(self, 0x00040000, "CMP3DE", "CMP3DE")
        self.CMP2DE = BitField(self, 0x00020000, "CMP2DE", "CMP2DE")
        self.CMP1DE = BitField(self, 0x00010000, "CMP1DE", "CMP1DE")
        self.DLYPRTIE = BitField(self, 0x00004000, "DLYPRTIE", "DLYPRTIE")
        self.RSTIE = BitField(self, 0x00002000, "RSTIE", "RSTIE")
        self.RSTx2IE = BitField(self, 0x00001000, "RSTx2IE", "RSTx2IE")
        self.SETx2IE = BitField(self, 0x00000800, "SETx2IE", "SETx2IE")
        self.RSTx1IE = BitField(self, 0x00000400, "RSTx1IE", "RSTx1IE")
        self.SET1xIE = BitField(self, 0x00000200, "SET1xIE", "SET1xIE")
        self.CPT2IE = BitField(self, 0x00000100, "CPT2IE", "CPT2IE")
        self.CPT1IE = BitField(self, 0x00000080, "CPT1IE", "CPT1IE")
        self.UPDIE = BitField(self, 0x00000040, "UPDIE", "UPDIE")
        self.REPIE = BitField(self, 0x00000010, "REPIE", "REPIE")
        self.CMP4IE = BitField(self, 0x00000008, "CMP4IE", "CMP4IE")
        self.CMP3IE = BitField(self, 0x00000004, "CMP3IE", "CMP3IE")
        self.CMP2IE = BitField(self, 0x00000002, "CMP2IE", "CMP2IE")
        self.CMP1IE = BitField(self, 0x00000001, "CMP1IE", "CMP1IE")
        self.RSTxIE = Subscriptor(self, "RSTx{}IE")
        self.CMPDE = Subscriptor(self, "CMP{}DE")
        self.RSTxDE = Subscriptor(self, "RSTx{}DE")
        self.CPTDE = Subscriptor(self, "CPT{}DE")
        self.CPTIE = Subscriptor(self, "CPT{}IE")
        self.CMPIE = Subscriptor(self, "CMP{}IE")

class SA_HRTIM_TIMD_CNTDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNTDR", "Timerx Counter Register")
        self.CNTx = BitField(self, 0x0000FFFF, "CNTx", "Timerx Counter value")

class SA_HRTIM_TIMD_PERDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "PERDR", "Timerx Period Register")
        self.PERx = BitField(self, 0x0000FFFF, "PERx", "Timerx Period value")

class SA_HRTIM_TIMD_REPDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "REPDR", "Timerx Repetition Register")
        self.REPx = BitField(self, 0x000000FF, "REPx", "Timerx Repetition counter value")

class SA_HRTIM_TIMD_CMP1DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1DR", "Timerx Compare 1 Register")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMD_CMP1CDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1CDR", "Timerx Compare 1 Compound Register")
        self.REPx = BitField(self, 0x00FF0000, "REPx", "Timerx Repetition value (aliased from HRTIM_REPx register)")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMD_CMP2DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP2DR", "Timerx Compare 2 Register")
        self.CMP2x = BitField(self, 0x0000FFFF, "CMP2x", "Timerx Compare 2 value")

class SA_HRTIM_TIMD_CMP3DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP3DR", "Timerx Compare 3 Register")
        self.CMP3x = BitField(self, 0x0000FFFF, "CMP3x", "Timerx Compare 3 value")

class SA_HRTIM_TIMD_CMP4DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP4DR", "Timerx Compare 4 Register")
        self.CMP4x = BitField(self, 0x0000FFFF, "CMP4x", "Timerx Compare 4 value")

class SA_HRTIM_TIMD_CPT1DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1DR", "Timerx Capture 1 Register")
        self.CPT1x = BitField(self, 0x0000FFFF, "CPT1x", "Timerx Capture 1 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMD_CPT2DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2DR", "Timerx Capture 2 Register")
        self.CPT2x = BitField(self, 0x0000FFFF, "CPT2x", "Timerx Capture 2 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMD_DTDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTDR", "Timerx Deadtime Register")
        self.DTFLKx = BitField(self, 0x80000000, "DTFLKx", "Deadtime Falling Lock")
        self.DTFSLKx = BitField(self, 0x40000000, "DTFSLKx", "Deadtime Falling Sign Lock")
        self.SDTFx = BitField(self, 0x02000000, "SDTFx", "Sign Deadtime Falling value")
        self.DTFx = BitField(self, 0x01FF0000, "DTFx", "Deadtime Falling value")
        self.DTRLKx = BitField(self, 0x00008000, "DTRLKx", "Deadtime Rising Lock")
        self.DTRSLKx = BitField(self, 0x00004000, "DTRSLKx", "Deadtime Rising Sign Lock")
        self.DTPRSC = BitField(self, 0x00001C00, "DTPRSC", "Deadtime Prescaler")
        self.SDTRx = BitField(self, 0x00000200, "SDTRx", "Sign Deadtime Rising value")
        self.DTRx = BitField(self, 0x000001FF, "DTRx", "Deadtime Rising value")

class SA_HRTIM_TIMD_SETD1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETD1R", "Timerx Output1 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "Registers update (transfer preload to active)")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "External Event 1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "Timer Event 9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "Timer Event 8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "Timer Event 7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "Timer Event 6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "Timer Event 5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "Timer Event 4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "Timer Event 3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "Timer Event 2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "Timer Event 1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "Master Compare 4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "Master Compare 3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "Master Compare 2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "Master Compare 1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "Master Period")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "Timer A compare 4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "Timer A compare 3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "Timer A compare 2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "Timer A compare 1")
        self.PER = BitField(self, 0x00000004, "PER", "Timer A Period")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "Timer A resynchronizaton")
        self.SST = BitField(self, 0x00000001, "SST", "Software Set trigger")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMD_RSTD1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTD1R", "Timerx Output1 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMD_SETD2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETD2R", "Timerx Output2 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SST = BitField(self, 0x00000001, "SST", "SST")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMD_RSTD2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTD2R", "Timerx Output2 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMD_EEFDR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFDR1", "Timerx External Event Filtering Register 1")
        self.EE5FLTR = BitField(self, 0x1E000000, "EE5FLTR", "External Event 5 filter")
        self.EE5LTCH = BitField(self, 0x01000000, "EE5LTCH", "External Event 5 latch")
        self.EE4FLTR = BitField(self, 0x00780000, "EE4FLTR", "External Event 4 filter")
        self.EE4LTCH = BitField(self, 0x00040000, "EE4LTCH", "External Event 4 latch")
        self.EE3FLTR = BitField(self, 0x0001E000, "EE3FLTR", "External Event 3 filter")
        self.EE3LTCH = BitField(self, 0x00001000, "EE3LTCH", "External Event 3 latch")
        self.EE2FLTR = BitField(self, 0x00000780, "EE2FLTR", "External Event 2 filter")
        self.EE2LTCH = BitField(self, 0x00000040, "EE2LTCH", "External Event 2 latch")
        self.EE1FLTR = BitField(self, 0x0000001E, "EE1FLTR", "External Event 1 filter")
        self.EE1LTCH = BitField(self, 0x00000001, "EE1LTCH", "External Event 1 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMD_EEFDR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFDR2", "Timerx External Event Filtering Register 2")
        self.EE10FLTR = BitField(self, 0x1E000000, "EE10FLTR", "External Event 10 filter")
        self.EE10LTCH = BitField(self, 0x01000000, "EE10LTCH", "External Event 10 latch")
        self.EE9FLTR = BitField(self, 0x00780000, "EE9FLTR", "External Event 9 filter")
        self.EE9LTCH = BitField(self, 0x00040000, "EE9LTCH", "External Event 9 latch")
        self.EE8FLTR = BitField(self, 0x0001E000, "EE8FLTR", "External Event 8 filter")
        self.EE8LTCH = BitField(self, 0x00001000, "EE8LTCH", "External Event 8 latch")
        self.EE7FLTR = BitField(self, 0x00000780, "EE7FLTR", "External Event 7 filter")
        self.EE7LTCH = BitField(self, 0x00000040, "EE7LTCH", "External Event 7 latch")
        self.EE6FLTR = BitField(self, 0x0000001E, "EE6FLTR", "External Event 6 filter")
        self.EE6LTCH = BitField(self, 0x00000001, "EE6LTCH", "External Event 6 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMD_RSTDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTDR", "TimerA Reset Register")
        self.TIMFCPM2 = BitField(self, 0x80000000, "TIMFCPM2", "Timer F Compare 2")
        self.TIMECMP4 = BitField(self, 0x40000000, "TIMECMP4", "Timer E Compare 4")
        self.TIMECMP2 = BitField(self, 0x20000000, "TIMECMP2", "Timer E Compare 2")
        self.TIMECMP1 = BitField(self, 0x10000000, "TIMECMP1", "Timer E Compare 1")
        self.TIMCCMP4 = BitField(self, 0x08000000, "TIMCCMP4", "Timer C Compare 4")
        self.TIMCCMP2 = BitField(self, 0x04000000, "TIMCCMP2", "Timer C Compare 2")
        self.TIMCCMP1 = BitField(self, 0x02000000, "TIMCCMP1", "Timer C Compare 1")
        self.TIMBCMP4 = BitField(self, 0x01000000, "TIMBCMP4", "Timer B Compare 4")
        self.TIMBCMP2 = BitField(self, 0x00800000, "TIMBCMP2", "Timer B Compare 2")
        self.TIMBCMP1 = BitField(self, 0x00400000, "TIMBCMP1", "Timer B Compare 1")
        self.TIMACMP4 = BitField(self, 0x00200000, "TIMACMP4", "Timer A Compare 4")
        self.TIMACMP2 = BitField(self, 0x00100000, "TIMACMP2", "Timer A Compare 2")
        self.TIMACMP1 = BitField(self, 0x00080000, "TIMACMP1", "Timer A Compare 1")
        self.EXTEVNT10 = BitField(self, 0x00040000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x00020000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x00010000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x00008000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x00004000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x00002000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x00001000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00000800, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00000400, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00000200, "EXTEVNT1", "External Event 1")
        self.MSTCMP4 = BitField(self, 0x00000100, "MSTCMP4", "Master compare 4")
        self.MSTCMP3 = BitField(self, 0x00000080, "MSTCMP3", "Master compare 3")
        self.MSTCMP2 = BitField(self, 0x00000040, "MSTCMP2", "Master compare 2")
        self.MSTCMP1 = BitField(self, 0x00000020, "MSTCMP1", "Master compare 1")
        self.MSTPER = BitField(self, 0x00000010, "MSTPER", "Master timer Period")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Timer A compare 4 reset")
        self.CMP2 = BitField(self, 0x00000004, "CMP2", "Timer A compare 2 reset")
        self.UPDT = BitField(self, 0x00000002, "UPDT", "Timer A Update reset")
        self.TIMFCMP1 = BitField(self, 0x00000001, "TIMFCMP1", "Timer A Update reset")
        self.TIMACMP = Subscriptor(self, "TIMACMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMCCMP = Subscriptor(self, "TIMCCMP{}")
        self.TIMBCMP = Subscriptor(self, "TIMBCMP{}")
        self.TIMECMP = Subscriptor(self, "TIMECMP{}")

class SA_HRTIM_TIMD_CHPDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CHPDR", "Timerx Chopper Register")
        self.STRTPW = BitField(self, 0x00000780, "STRTPW", "STRTPW")
        self.CHPDTY = BitField(self, 0x00000070, "CHPDTY", "Timerx chopper duty cycle value")
        self.CHPFRQ = BitField(self, 0x0000000F, "CHPFRQ", "Timerx carrier frequency value")

class SA_HRTIM_TIMD_CPT1DCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1DCR", "Timerx Capture 2 Control Register")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TFCMP2 = BitField(self, 0x08000000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x04000000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x02000000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x01000000, "TF1SET", "TF1SET")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMD_CPT2DCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2DCR", "CPT2xCR")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "Timer E Compare 2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "Timer E Compare 1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "Timer E output 1 Reset")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "Timer E output 1 Set")
        self.TFCMP2 = BitField(self, 0x08000000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x04000000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x02000000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x01000000, "TF1SET", "TF1SET")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMD_OUTDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OUTDR", "Timerx Output Register")
        self.DIDL2 = BitField(self, 0x00800000, "DIDL2", "Output 2 Deadtime upon burst mode Idle entry")
        self.CHP2 = BitField(self, 0x00400000, "CHP2", "Output 2 Chopper enable")
        self.FAULT2 = BitField(self, 0x00300000, "FAULT2", "Output 2 Fault state")
        self.IDLES2 = BitField(self, 0x00080000, "IDLES2", "Output 2 Idle State")
        self.IDLEM2 = BitField(self, 0x00040000, "IDLEM2", "Output 2 Idle mode")
        self.POL2 = BitField(self, 0x00020000, "POL2", "Output 2 polarity")
        self.BIAR = BitField(self, 0x00004000, "BIAR", "Balanced Idle Automatic Resume")
        self.DLYPRT = BitField(self, 0x00001C00, "DLYPRT", "Delayed Protection")
        self.DLYPRTEN = BitField(self, 0x00000200, "DLYPRTEN", "Delayed Protection Enable")
        self.DTEN = BitField(self, 0x00000100, "DTEN", "Deadtime enable")
        self.DIDL1 = BitField(self, 0x00000080, "DIDL1", "Output 1 Deadtime upon burst mode Idle entry")
        self.CHP1 = BitField(self, 0x00000040, "CHP1", "Output 1 Chopper enable")
        self.FAULT1 = BitField(self, 0x00000030, "FAULT1", "Output 1 Fault state")
        self.IDLES1 = BitField(self, 0x00000008, "IDLES1", "Output 1 Idle State")
        self.IDLEM1 = BitField(self, 0x00000004, "IDLEM1", "Output 1 Idle mode")
        self.POL1 = BitField(self, 0x00000002, "POL1", "Output 1 polarity")
        self.POL = Subscriptor(self, "POL{}")
        self.DIDL = Subscriptor(self, "DIDL{}")
        self.FAULT = Subscriptor(self, "FAULT{}")
        self.CHP = Subscriptor(self, "CHP{}")
        self.IDLES = Subscriptor(self, "IDLES{}")
        self.IDLEM = Subscriptor(self, "IDLEM{}")

class SA_HRTIM_TIMD_FLTDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTDR", "Timerx Fault Register")
        self.FLTLCK = BitField(self, 0x80000000, "FLTLCK", "Fault sources Lock")
        self.FLT6EN = BitField(self, 0x00000020, "FLT6EN", "Fault 6 enable")
        self.FLT5EN = BitField(self, 0x00000010, "FLT5EN", "Fault 5 enable")
        self.FLT4EN = BitField(self, 0x00000008, "FLT4EN", "Fault 4 enable")
        self.FLT3EN = BitField(self, 0x00000004, "FLT3EN", "Fault 3 enable")
        self.FLT2EN = BitField(self, 0x00000002, "FLT2EN", "Fault 2 enable")
        self.FLT1EN = BitField(self, 0x00000001, "FLT1EN", "Fault 1 enable")
        self.FLTEN = Subscriptor(self, "FLT{}EN")

class SA_HRTIM_TIMD_TIMDCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMDCR2", "HRTIM Timerx Control Register 2")
        self.TRGHLF = BitField(self, 0x00100000, "TRGHLF", "Triggered-half mode")
        self.GTCMP3 = BitField(self, 0x00020000, "GTCMP3", "Greater than Compare 3 PWM mode")
        self.GTCMP1 = BitField(self, 0x00010000, "GTCMP1", "Greater than Compare 1 PWM mode")
        self.FEROM = BitField(self, 0x0000C000, "FEROM", "Fault and Event Roll-Over Mode")
        self.BMROM = BitField(self, 0x00003000, "BMROM", "Burst Mode Roll-Over Mode")
        self.ADROM = BitField(self, 0x00000C00, "ADROM", "ADC Roll-Over Mode")
        self.OUTROM = BitField(self, 0x00000300, "OUTROM", "Output Roll-Over Mode")
        self.ROM = BitField(self, 0x000000C0, "ROM", "Roll-Over Mode")
        self.UDM = BitField(self, 0x00000010, "UDM", "Up-Down Mode")
        self.DCDR = BitField(self, 0x00000004, "DCDR", "Dual Channel DAC Reset trigger")
        self.DCDS = BitField(self, 0x00000002, "DCDS", "Dual Channel DAC Step trigger")
        self.DCDE = BitField(self, 0x00000001, "DCDE", "Dual Channel DAC trigger enable")

class SA_HRTIM_TIMD_DEEFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DEEFR3", "HRTIM Timerx External Event Filtering Register 3")
        self.EEVACNT = BitField(self, 0x00003F00, "EEVACNT", "External Event A counter")
        self.EEVASEL = BitField(self, 0x000000F0, "EEVASEL", "External Event A Selection")
        self.EEVARSTM = BitField(self, 0x00000004, "EEVARSTM", "External Event A Reset Mode")
        self.EEVACRES = BitField(self, 0x00000002, "EEVACRES", "External Event A Counter Reset")
        self.EEVACE = BitField(self, 0x00000001, "EEVACE", "External Event A Counter Enable")

class SA_HRTIM_TIMD(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: TIMD")
        self.TIMDCR = SA_HRTIM_TIMD_TIMDCR(self, 0x0)
        self.TIMDISR = SA_HRTIM_TIMD_TIMDISR(self, 0x4)
        self.TIMDICR = SA_HRTIM_TIMD_TIMDICR(self, 0x8)
        self.TIMDDIER = SA_HRTIM_TIMD_TIMDDIER(self, 0xC)
        self.CNTDR = SA_HRTIM_TIMD_CNTDR(self, 0x10)
        self.PERDR = SA_HRTIM_TIMD_PERDR(self, 0x14)
        self.REPDR = SA_HRTIM_TIMD_REPDR(self, 0x18)
        self.CMP1DR = SA_HRTIM_TIMD_CMP1DR(self, 0x1C)
        self.CMP1CDR = SA_HRTIM_TIMD_CMP1CDR(self, 0x20)
        self.CMP2DR = SA_HRTIM_TIMD_CMP2DR(self, 0x24)
        self.CMP3DR = SA_HRTIM_TIMD_CMP3DR(self, 0x28)
        self.CMP4DR = SA_HRTIM_TIMD_CMP4DR(self, 0x2C)
        self.CPT1DR = SA_HRTIM_TIMD_CPT1DR(self, 0x30)
        self.CPT2DR = SA_HRTIM_TIMD_CPT2DR(self, 0x34)
        self.DTDR = SA_HRTIM_TIMD_DTDR(self, 0x38)
        self.SETD1R = SA_HRTIM_TIMD_SETD1R(self, 0x3C)
        self.RSTD1R = SA_HRTIM_TIMD_RSTD1R(self, 0x40)
        self.SETD2R = SA_HRTIM_TIMD_SETD2R(self, 0x44)
        self.RSTD2R = SA_HRTIM_TIMD_RSTD2R(self, 0x48)
        self.EEFDR1 = SA_HRTIM_TIMD_EEFDR1(self, 0x4C)
        self.EEFDR2 = SA_HRTIM_TIMD_EEFDR2(self, 0x50)
        self.RSTDR = SA_HRTIM_TIMD_RSTDR(self, 0x54)
        self.CHPDR = SA_HRTIM_TIMD_CHPDR(self, 0x58)
        self.CPT1DCR = SA_HRTIM_TIMD_CPT1DCR(self, 0x5C)
        self.CPT2DCR = SA_HRTIM_TIMD_CPT2DCR(self, 0x60)
        self.OUTDR = SA_HRTIM_TIMD_OUTDR(self, 0x64)
        self.FLTDR = SA_HRTIM_TIMD_FLTDR(self, 0x68)
        self.TIMDCR2 = SA_HRTIM_TIMD_TIMDCR2(self, 0x6C)
        self.DEEFR3 = SA_HRTIM_TIMD_DEEFR3(self, 0x70)
        self.CPTDCR = Subscriptor(self, "CPT{}DCR")
        self.CPTDR = Subscriptor(self, "CPT{}DR")
        self.CMPDR = Subscriptor(self, "CMP{}DR")
        self.EEFDR = Subscriptor(self, "EEFDR{}")
        self.SETDR = Subscriptor(self, "SETD{}R")

HRTIM_TIMD = SA_HRTIM_TIMD(0x40016A00, "HRTIM_TIMD")

class SA_HRTIM_TIME_TIMECR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMECR", "Timerx Control Register")
        self.UPDGAT = BitField(self, 0xF0000000, "UPDGAT", "Update Gating")
        self.PREEN = BitField(self, 0x08000000, "PREEN", "Preload enable")
        self.DACSYNC = BitField(self, 0x06000000, "DACSYNC", "AC Synchronization")
        self.MSTU = BitField(self, 0x01000000, "MSTU", "Master Timer update")
        self.TDU = BitField(self, 0x00400000, "TDU", "TDU")
        self.TCU = BitField(self, 0x00200000, "TCU", "TCU")
        self.TBU = BitField(self, 0x00100000, "TBU", "TBU")
        self.TAU = BitField(self, 0x00080000, "TAU", "TAU")
        self.TxRSTU = BitField(self, 0x00040000, "TxRSTU", "Timerx reset update")
        self.TxREPU = BitField(self, 0x00020000, "TxREPU", "Timer x Repetition update")
        self.TFU = BitField(self, 0x00010000, "TFU", "TFU")
        self.DELCMP4 = BitField(self, 0x0000C000, "DELCMP4", "Delayed CMP4 mode")
        self.DELCMP2 = BitField(self, 0x00003000, "DELCMP2", "Delayed CMP2 mode")
        self.SYNCSTRTx = BitField(self, 0x00000800, "SYNCSTRTx", "Synchronization Starts Timer x")
        self.SYNCRSTx = BitField(self, 0x00000400, "SYNCRSTx", "Synchronization Resets Timer x")
        self.RSYNCU = BitField(self, 0x00000200, "RSYNCU", "Re-Synchronized Update")
        self.INTLVD = BitField(self, 0x00000180, "INTLVD", "Interleaved mode")
        self.PSHPLL = BitField(self, 0x00000040, "PSHPLL", "Push-Pull mode enable")
        self.HALF = BitField(self, 0x00000020, "HALF", "Half mode enable")
        self.RETRIG = BitField(self, 0x00000010, "RETRIG", "Re-triggerable mode")
        self.CONT = BitField(self, 0x00000008, "CONT", "Continuous mode")
        self.CK_PSCx = BitField(self, 0x00000007, "CK_PSCx", "HRTIM Timer x Clock prescaler")

class SA_HRTIM_TIME_TIMEISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMEISR", "Timerx Interrupt Status Register")
        self.O2CPY = BitField(self, 0x00200000, "O2CPY", "Output 2 Copy")
        self.O1CPY = BitField(self, 0x00100000, "O1CPY", "Output 1 Copy")
        self.O2STAT = BitField(self, 0x00080000, "O2STAT", "Output 2 State")
        self.O1STAT = BitField(self, 0x00040000, "O1STAT", "Output 1 State")
        self.IPPSTAT = BitField(self, 0x00020000, "IPPSTAT", "Idle Push Pull Status")
        self.CPPSTAT = BitField(self, 0x00010000, "CPPSTAT", "Current Push Pull Status")
        self.DLYPRT = BitField(self, 0x00004000, "DLYPRT", "Delayed Protection Flag")
        self.RST = BitField(self, 0x00002000, "RST", "Reset Interrupt Flag")
        self.RSTx2 = BitField(self, 0x00001000, "RSTx2", "Output 2 Reset Interrupt Flag")
        self.SETx2 = BitField(self, 0x00000800, "SETx2", "Output 2 Set Interrupt Flag")
        self.RSTx1 = BitField(self, 0x00000400, "RSTx1", "Output 1 Reset Interrupt Flag")
        self.SETx1 = BitField(self, 0x00000200, "SETx1", "Output 1 Set Interrupt Flag")
        self.CPT2 = BitField(self, 0x00000100, "CPT2", "Capture2 Interrupt Flag")
        self.CPT1 = BitField(self, 0x00000080, "CPT1", "Capture1 Interrupt Flag")
        self.UPD = BitField(self, 0x00000040, "UPD", "Update Interrupt Flag")
        self.REP = BitField(self, 0x00000010, "REP", "Repetition Interrupt Flag")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Compare 4 Interrupt Flag")
        self.CMP3 = BitField(self, 0x00000004, "CMP3", "Compare 3 Interrupt Flag")
        self.CMP2 = BitField(self, 0x00000002, "CMP2", "Compare 2 Interrupt Flag")
        self.CMP1 = BitField(self, 0x00000001, "CMP1", "Compare 1 Interrupt Flag")
        self.RSTx = Subscriptor(self, "RSTx{}")
        self.OSTAT = Subscriptor(self, "O{}STAT")
        self.OCPY = Subscriptor(self, "O{}CPY")
        self.SETx = Subscriptor(self, "SETx{}")
        self.CPT = Subscriptor(self, "CPT{}")
        self.CMP = Subscriptor(self, "CMP{}")

class SA_HRTIM_TIME_TIMEICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMEICR", "Timerx Interrupt Clear Register")
        self.DLYPRTC = BitField(self, 0x00004000, "DLYPRTC", "Delayed Protection Flag Clear")
        self.RSTC = BitField(self, 0x00002000, "RSTC", "Reset Interrupt flag Clear")
        self.RSTx2C = BitField(self, 0x00001000, "RSTx2C", "Output 2 Reset flag Clear")
        self.SET2xC = BitField(self, 0x00000800, "SET2xC", "Output 2 Set flag Clear")
        self.RSTx1C = BitField(self, 0x00000400, "RSTx1C", "Output 1 Reset flag Clear")
        self.SET1xC = BitField(self, 0x00000200, "SET1xC", "Output 1 Set flag Clear")
        self.CPT2C = BitField(self, 0x00000100, "CPT2C", "Capture2 Interrupt flag Clear")
        self.CPT1C = BitField(self, 0x00000080, "CPT1C", "Capture1 Interrupt flag Clear")
        self.UPDC = BitField(self, 0x00000040, "UPDC", "Update Interrupt flag Clear")
        self.REPC = BitField(self, 0x00000010, "REPC", "Repetition Interrupt flag Clear")
        self.CMP4C = BitField(self, 0x00000008, "CMP4C", "Compare 4 Interrupt flag Clear")
        self.CMP3C = BitField(self, 0x00000004, "CMP3C", "Compare 3 Interrupt flag Clear")
        self.CMP2C = BitField(self, 0x00000002, "CMP2C", "Compare 2 Interrupt flag Clear")
        self.CMP1C = BitField(self, 0x00000001, "CMP1C", "Compare 1 Interrupt flag Clear")
        self.CPTC = Subscriptor(self, "CPT{}C")
        self.SETxC = Subscriptor(self, "SET{}xC")
        self.CMPC = Subscriptor(self, "CMP{}C")
        self.RSTxC = Subscriptor(self, "RSTx{}C")

class SA_HRTIM_TIME_TIMEDIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMEDIER", "TIMxDIER")
        self.DLYPRTDE = BitField(self, 0x40000000, "DLYPRTDE", "DLYPRTDE")
        self.RSTDE = BitField(self, 0x20000000, "RSTDE", "RSTDE")
        self.RSTx2DE = BitField(self, 0x10000000, "RSTx2DE", "RSTx2DE")
        self.SETx2DE = BitField(self, 0x08000000, "SETx2DE", "SETx2DE")
        self.RSTx1DE = BitField(self, 0x04000000, "RSTx1DE", "RSTx1DE")
        self.SET1xDE = BitField(self, 0x02000000, "SET1xDE", "SET1xDE")
        self.CPT2DE = BitField(self, 0x01000000, "CPT2DE", "CPT2DE")
        self.CPT1DE = BitField(self, 0x00800000, "CPT1DE", "CPT1DE")
        self.UPDDE = BitField(self, 0x00400000, "UPDDE", "UPDDE")
        self.REPDE = BitField(self, 0x00100000, "REPDE", "REPDE")
        self.CMP4DE = BitField(self, 0x00080000, "CMP4DE", "CMP4DE")
        self.CMP3DE = BitField(self, 0x00040000, "CMP3DE", "CMP3DE")
        self.CMP2DE = BitField(self, 0x00020000, "CMP2DE", "CMP2DE")
        self.CMP1DE = BitField(self, 0x00010000, "CMP1DE", "CMP1DE")
        self.DLYPRTIE = BitField(self, 0x00004000, "DLYPRTIE", "DLYPRTIE")
        self.RSTIE = BitField(self, 0x00002000, "RSTIE", "RSTIE")
        self.RSTx2IE = BitField(self, 0x00001000, "RSTx2IE", "RSTx2IE")
        self.SETx2IE = BitField(self, 0x00000800, "SETx2IE", "SETx2IE")
        self.RSTx1IE = BitField(self, 0x00000400, "RSTx1IE", "RSTx1IE")
        self.SET1xIE = BitField(self, 0x00000200, "SET1xIE", "SET1xIE")
        self.CPT2IE = BitField(self, 0x00000100, "CPT2IE", "CPT2IE")
        self.CPT1IE = BitField(self, 0x00000080, "CPT1IE", "CPT1IE")
        self.UPDIE = BitField(self, 0x00000040, "UPDIE", "UPDIE")
        self.REPIE = BitField(self, 0x00000010, "REPIE", "REPIE")
        self.CMP4IE = BitField(self, 0x00000008, "CMP4IE", "CMP4IE")
        self.CMP3IE = BitField(self, 0x00000004, "CMP3IE", "CMP3IE")
        self.CMP2IE = BitField(self, 0x00000002, "CMP2IE", "CMP2IE")
        self.CMP1IE = BitField(self, 0x00000001, "CMP1IE", "CMP1IE")
        self.RSTxIE = Subscriptor(self, "RSTx{}IE")
        self.CMPDE = Subscriptor(self, "CMP{}DE")
        self.RSTxDE = Subscriptor(self, "RSTx{}DE")
        self.CPTDE = Subscriptor(self, "CPT{}DE")
        self.CPTIE = Subscriptor(self, "CPT{}IE")
        self.CMPIE = Subscriptor(self, "CMP{}IE")

class SA_HRTIM_TIME_CNTER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNTER", "Timerx Counter Register")
        self.CNTx = BitField(self, 0x0000FFFF, "CNTx", "Timerx Counter value")

class SA_HRTIM_TIME_PERER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "PERER", "Timerx Period Register")
        self.PERx = BitField(self, 0x0000FFFF, "PERx", "Timerx Period value")

class SA_HRTIM_TIME_REPER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "REPER", "Timerx Repetition Register")
        self.REPx = BitField(self, 0x000000FF, "REPx", "Timerx Repetition counter value")

class SA_HRTIM_TIME_CMP1ER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1ER", "Timerx Compare 1 Register")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIME_CMP1CER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1CER", "Timerx Compare 1 Compound Register")
        self.REPx = BitField(self, 0x00FF0000, "REPx", "Timerx Repetition value (aliased from HRTIM_REPx register)")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIME_CMP2ER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP2ER", "Timerx Compare 2 Register")
        self.CMP2x = BitField(self, 0x0000FFFF, "CMP2x", "Timerx Compare 2 value")

class SA_HRTIM_TIME_CMP3ER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP3ER", "Timerx Compare 3 Register")
        self.CMP3x = BitField(self, 0x0000FFFF, "CMP3x", "Timerx Compare 3 value")

class SA_HRTIM_TIME_CMP4ER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP4ER", "Timerx Compare 4 Register")
        self.CMP4x = BitField(self, 0x0000FFFF, "CMP4x", "Timerx Compare 4 value")

class SA_HRTIM_TIME_CPT1ER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1ER", "Timerx Capture 1 Register")
        self.CPT1x = BitField(self, 0x0000FFFF, "CPT1x", "Timerx Capture 1 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIME_CPT2ER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2ER", "Timerx Capture 2 Register")
        self.CPT2x = BitField(self, 0x0000FFFF, "CPT2x", "Timerx Capture 2 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIME_DTER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTER", "Timerx Deadtime Register")
        self.DTFLKx = BitField(self, 0x80000000, "DTFLKx", "Deadtime Falling Lock")
        self.DTFSLKx = BitField(self, 0x40000000, "DTFSLKx", "Deadtime Falling Sign Lock")
        self.SDTFx = BitField(self, 0x02000000, "SDTFx", "Sign Deadtime Falling value")
        self.DTFx = BitField(self, 0x01FF0000, "DTFx", "Deadtime Falling value")
        self.DTRLKx = BitField(self, 0x00008000, "DTRLKx", "Deadtime Rising Lock")
        self.DTRSLKx = BitField(self, 0x00004000, "DTRSLKx", "Deadtime Rising Sign Lock")
        self.DTPRSC = BitField(self, 0x00001C00, "DTPRSC", "Deadtime Prescaler")
        self.SDTRx = BitField(self, 0x00000200, "SDTRx", "Sign Deadtime Rising value")
        self.DTRx = BitField(self, 0x000001FF, "DTRx", "Deadtime Rising value")

class SA_HRTIM_TIME_SETE1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETE1R", "Timerx Output1 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "Registers update (transfer preload to active)")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "External Event 1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "Timer Event 9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "Timer Event 8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "Timer Event 7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "Timer Event 6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "Timer Event 5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "Timer Event 4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "Timer Event 3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "Timer Event 2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "Timer Event 1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "Master Compare 4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "Master Compare 3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "Master Compare 2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "Master Compare 1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "Master Period")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "Timer A compare 4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "Timer A compare 3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "Timer A compare 2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "Timer A compare 1")
        self.PER = BitField(self, 0x00000004, "PER", "Timer A Period")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "Timer A resynchronizaton")
        self.SST = BitField(self, 0x00000001, "SST", "Software Set trigger")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIME_RSTE1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTE1R", "Timerx Output1 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIME_SETE2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETE2R", "Timerx Output2 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SST = BitField(self, 0x00000001, "SST", "SST")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIME_RSTE2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTE2R", "Timerx Output2 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIME_EEFER1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFER1", "Timerx External Event Filtering Register 1")
        self.EE5FLTR = BitField(self, 0x1E000000, "EE5FLTR", "External Event 5 filter")
        self.EE5LTCH = BitField(self, 0x01000000, "EE5LTCH", "External Event 5 latch")
        self.EE4FLTR = BitField(self, 0x00780000, "EE4FLTR", "External Event 4 filter")
        self.EE4LTCH = BitField(self, 0x00040000, "EE4LTCH", "External Event 4 latch")
        self.EE3FLTR = BitField(self, 0x0001E000, "EE3FLTR", "External Event 3 filter")
        self.EE3LTCH = BitField(self, 0x00001000, "EE3LTCH", "External Event 3 latch")
        self.EE2FLTR = BitField(self, 0x00000780, "EE2FLTR", "External Event 2 filter")
        self.EE2LTCH = BitField(self, 0x00000040, "EE2LTCH", "External Event 2 latch")
        self.EE1FLTR = BitField(self, 0x0000001E, "EE1FLTR", "External Event 1 filter")
        self.EE1LTCH = BitField(self, 0x00000001, "EE1LTCH", "External Event 1 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIME_EEFER2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFER2", "Timerx External Event Filtering Register 2")
        self.EE10FLTR = BitField(self, 0x1E000000, "EE10FLTR", "External Event 10 filter")
        self.EE10LTCH = BitField(self, 0x01000000, "EE10LTCH", "External Event 10 latch")
        self.EE9FLTR = BitField(self, 0x00780000, "EE9FLTR", "External Event 9 filter")
        self.EE9LTCH = BitField(self, 0x00040000, "EE9LTCH", "External Event 9 latch")
        self.EE8FLTR = BitField(self, 0x0001E000, "EE8FLTR", "External Event 8 filter")
        self.EE8LTCH = BitField(self, 0x00001000, "EE8LTCH", "External Event 8 latch")
        self.EE7FLTR = BitField(self, 0x00000780, "EE7FLTR", "External Event 7 filter")
        self.EE7LTCH = BitField(self, 0x00000040, "EE7LTCH", "External Event 7 latch")
        self.EE6FLTR = BitField(self, 0x0000001E, "EE6FLTR", "External Event 6 filter")
        self.EE6LTCH = BitField(self, 0x00000001, "EE6LTCH", "External Event 6 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIME_RSTER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTER", "TimerA Reset Register")
        self.TIMFCPM2 = BitField(self, 0x80000000, "TIMFCPM2", "Timer F Compare 2")
        self.TIMDCMP4 = BitField(self, 0x40000000, "TIMDCMP4", "Timer D Compare 4")
        self.TIMDCMP2 = BitField(self, 0x20000000, "TIMDCMP2", "Timer D Compare 2")
        self.TIMDCMP1 = BitField(self, 0x10000000, "TIMDCMP1", "Timer D Compare 1")
        self.TIMCCMP4 = BitField(self, 0x08000000, "TIMCCMP4", "Timer C Compare 4")
        self.TIMCCMP2 = BitField(self, 0x04000000, "TIMCCMP2", "Timer C Compare 2")
        self.TIMCCMP1 = BitField(self, 0x02000000, "TIMCCMP1", "Timer C Compare 1")
        self.TIMBCMP4 = BitField(self, 0x01000000, "TIMBCMP4", "Timer B Compare 4")
        self.TIMBCMP2 = BitField(self, 0x00800000, "TIMBCMP2", "Timer B Compare 2")
        self.TIMBCMP1 = BitField(self, 0x00400000, "TIMBCMP1", "Timer B Compare 1")
        self.TIMACMP4 = BitField(self, 0x00200000, "TIMACMP4", "Timer A Compare 4")
        self.TIMACMP2 = BitField(self, 0x00100000, "TIMACMP2", "Timer A Compare 2")
        self.TIMACMP1 = BitField(self, 0x00080000, "TIMACMP1", "Timer A Compare 1")
        self.EXTEVNT10 = BitField(self, 0x00040000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x00020000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x00010000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x00008000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x00004000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x00002000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x00001000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00000800, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00000400, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00000200, "EXTEVNT1", "External Event 1")
        self.MSTCMP4 = BitField(self, 0x00000100, "MSTCMP4", "Master compare 4")
        self.MSTCMP3 = BitField(self, 0x00000080, "MSTCMP3", "Master compare 3")
        self.MSTCMP2 = BitField(self, 0x00000040, "MSTCMP2", "Master compare 2")
        self.MSTCMP1 = BitField(self, 0x00000020, "MSTCMP1", "Master compare 1")
        self.MSTPER = BitField(self, 0x00000010, "MSTPER", "Master timer Period")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Timer A compare 4 reset")
        self.CMP2 = BitField(self, 0x00000004, "CMP2", "Timer A compare 2 reset")
        self.UPDT = BitField(self, 0x00000002, "UPDT", "Timer A Update reset")
        self.TIMFCMP1 = BitField(self, 0x00000001, "TIMFCMP1", "Timer A Update reset")
        self.TIMACMP = Subscriptor(self, "TIMACMP{}")
        self.TIMDCMP = Subscriptor(self, "TIMDCMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMCCMP = Subscriptor(self, "TIMCCMP{}")
        self.TIMBCMP = Subscriptor(self, "TIMBCMP{}")

class SA_HRTIM_TIME_CHPER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CHPER", "Timerx Chopper Register")
        self.STRTPW = BitField(self, 0x00000780, "STRTPW", "STRTPW")
        self.CHPDTY = BitField(self, 0x00000070, "CHPDTY", "Timerx chopper duty cycle value")
        self.CHPFRQ = BitField(self, 0x0000000F, "CHPFRQ", "Timerx carrier frequency value")

class SA_HRTIM_TIME_CPT1ECR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1ECR", "Timerx Capture 2 Control Register")
        self.TFCMP2 = BitField(self, 0x80000000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x40000000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x20000000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x10000000, "TF1SET", "TF1SET")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")

class SA_HRTIM_TIME_CPT2ECR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2ECR", "CPT2xCR")
        self.TFCMP2 = BitField(self, 0x80000000, "TFCMP2", "TFCMP2")
        self.TFCMP1 = BitField(self, 0x40000000, "TFCMP1", "TFCMP1")
        self.TF1RST = BitField(self, 0x20000000, "TF1RST", "TF1RST")
        self.TF1SET = BitField(self, 0x10000000, "TF1SET", "TF1SET")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TFCMP = Subscriptor(self, "TFCMP{}")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")

class SA_HRTIM_TIME_OUTER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OUTER", "Timerx Output Register")
        self.DIDL2 = BitField(self, 0x00800000, "DIDL2", "Output 2 Deadtime upon burst mode Idle entry")
        self.CHP2 = BitField(self, 0x00400000, "CHP2", "Output 2 Chopper enable")
        self.FAULT2 = BitField(self, 0x00300000, "FAULT2", "Output 2 Fault state")
        self.IDLES2 = BitField(self, 0x00080000, "IDLES2", "Output 2 Idle State")
        self.IDLEM2 = BitField(self, 0x00040000, "IDLEM2", "Output 2 Idle mode")
        self.POL2 = BitField(self, 0x00020000, "POL2", "Output 2 polarity")
        self.BIAR = BitField(self, 0x00004000, "BIAR", "Balanced Idle Automatic Resume")
        self.DLYPRT = BitField(self, 0x00001C00, "DLYPRT", "Delayed Protection")
        self.DLYPRTEN = BitField(self, 0x00000200, "DLYPRTEN", "Delayed Protection Enable")
        self.DTEN = BitField(self, 0x00000100, "DTEN", "Deadtime enable")
        self.DIDL1 = BitField(self, 0x00000080, "DIDL1", "Output 1 Deadtime upon burst mode Idle entry")
        self.CHP1 = BitField(self, 0x00000040, "CHP1", "Output 1 Chopper enable")
        self.FAULT1 = BitField(self, 0x00000030, "FAULT1", "Output 1 Fault state")
        self.IDLES1 = BitField(self, 0x00000008, "IDLES1", "Output 1 Idle State")
        self.IDLEM1 = BitField(self, 0x00000004, "IDLEM1", "Output 1 Idle mode")
        self.POL1 = BitField(self, 0x00000002, "POL1", "Output 1 polarity")
        self.POL = Subscriptor(self, "POL{}")
        self.DIDL = Subscriptor(self, "DIDL{}")
        self.FAULT = Subscriptor(self, "FAULT{}")
        self.CHP = Subscriptor(self, "CHP{}")
        self.IDLES = Subscriptor(self, "IDLES{}")
        self.IDLEM = Subscriptor(self, "IDLEM{}")

class SA_HRTIM_TIME_FLTER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTER", "Timerx Fault Register")
        self.FLTLCK = BitField(self, 0x80000000, "FLTLCK", "Fault sources Lock")
        self.FLT6EN = BitField(self, 0x00000020, "FLT6EN", "Fault 6 enable")
        self.FLT5EN = BitField(self, 0x00000010, "FLT5EN", "Fault 5 enable")
        self.FLT4EN = BitField(self, 0x00000008, "FLT4EN", "Fault 4 enable")
        self.FLT3EN = BitField(self, 0x00000004, "FLT3EN", "Fault 3 enable")
        self.FLT2EN = BitField(self, 0x00000002, "FLT2EN", "Fault 2 enable")
        self.FLT1EN = BitField(self, 0x00000001, "FLT1EN", "Fault 1 enable")
        self.FLTEN = Subscriptor(self, "FLT{}EN")

class SA_HRTIM_TIME_TIMECR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMECR2", "HRTIM Timerx Control Register 2")
        self.TRGHLF = BitField(self, 0x00100000, "TRGHLF", "Triggered-half mode")
        self.GTCMP3 = BitField(self, 0x00020000, "GTCMP3", "Greater than Compare 3 PWM mode")
        self.GTCMP1 = BitField(self, 0x00010000, "GTCMP1", "Greater than Compare 1 PWM mode")
        self.FEROM = BitField(self, 0x0000C000, "FEROM", "Fault and Event Roll-Over Mode")
        self.BMROM = BitField(self, 0x00003000, "BMROM", "Burst Mode Roll-Over Mode")
        self.ADROM = BitField(self, 0x00000C00, "ADROM", "ADC Roll-Over Mode")
        self.OUTROM = BitField(self, 0x00000300, "OUTROM", "Output Roll-Over Mode")
        self.ROM = BitField(self, 0x000000C0, "ROM", "Roll-Over Mode")
        self.UDM = BitField(self, 0x00000010, "UDM", "Up-Down Mode")
        self.DCDR = BitField(self, 0x00000004, "DCDR", "Dual Channel DAC Reset trigger")
        self.DCDS = BitField(self, 0x00000002, "DCDS", "Dual Channel DAC Step trigger")
        self.DCDE = BitField(self, 0x00000001, "DCDE", "Dual Channel DAC trigger enable")

class SA_HRTIM_TIME_EEEFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEEFR3", "HRTIM Timerx External Event Filtering Register 3")
        self.EEVACNT = BitField(self, 0x00003F00, "EEVACNT", "External Event A counter")
        self.EEVASEL = BitField(self, 0x000000F0, "EEVASEL", "External Event A Selection")
        self.EEVARSTM = BitField(self, 0x00000004, "EEVARSTM", "External Event A Reset Mode")
        self.EEVACRES = BitField(self, 0x00000002, "EEVACRES", "External Event A Counter Reset")
        self.EEVACE = BitField(self, 0x00000001, "EEVACE", "External Event A Counter Enable")

class SA_HRTIM_TIME(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: TIME")
        self.TIMECR = SA_HRTIM_TIME_TIMECR(self, 0x0)
        self.TIMEISR = SA_HRTIM_TIME_TIMEISR(self, 0x4)
        self.TIMEICR = SA_HRTIM_TIME_TIMEICR(self, 0x8)
        self.TIMEDIER = SA_HRTIM_TIME_TIMEDIER(self, 0xC)
        self.CNTER = SA_HRTIM_TIME_CNTER(self, 0x10)
        self.PERER = SA_HRTIM_TIME_PERER(self, 0x14)
        self.REPER = SA_HRTIM_TIME_REPER(self, 0x18)
        self.CMP1ER = SA_HRTIM_TIME_CMP1ER(self, 0x1C)
        self.CMP1CER = SA_HRTIM_TIME_CMP1CER(self, 0x20)
        self.CMP2ER = SA_HRTIM_TIME_CMP2ER(self, 0x24)
        self.CMP3ER = SA_HRTIM_TIME_CMP3ER(self, 0x28)
        self.CMP4ER = SA_HRTIM_TIME_CMP4ER(self, 0x2C)
        self.CPT1ER = SA_HRTIM_TIME_CPT1ER(self, 0x30)
        self.CPT2ER = SA_HRTIM_TIME_CPT2ER(self, 0x34)
        self.DTER = SA_HRTIM_TIME_DTER(self, 0x38)
        self.SETE1R = SA_HRTIM_TIME_SETE1R(self, 0x3C)
        self.RSTE1R = SA_HRTIM_TIME_RSTE1R(self, 0x40)
        self.SETE2R = SA_HRTIM_TIME_SETE2R(self, 0x44)
        self.RSTE2R = SA_HRTIM_TIME_RSTE2R(self, 0x48)
        self.EEFER1 = SA_HRTIM_TIME_EEFER1(self, 0x4C)
        self.EEFER2 = SA_HRTIM_TIME_EEFER2(self, 0x50)
        self.RSTER = SA_HRTIM_TIME_RSTER(self, 0x54)
        self.CHPER = SA_HRTIM_TIME_CHPER(self, 0x58)
        self.CPT1ECR = SA_HRTIM_TIME_CPT1ECR(self, 0x5C)
        self.CPT2ECR = SA_HRTIM_TIME_CPT2ECR(self, 0x60)
        self.OUTER = SA_HRTIM_TIME_OUTER(self, 0x64)
        self.FLTER = SA_HRTIM_TIME_FLTER(self, 0x68)
        self.TIMECR2 = SA_HRTIM_TIME_TIMECR2(self, 0x6C)
        self.EEEFR3 = SA_HRTIM_TIME_EEEFR3(self, 0x70)
        self.CPTECR = Subscriptor(self, "CPT{}ECR")
        self.EEFER = Subscriptor(self, "EEFER{}")
        self.CMPER = Subscriptor(self, "CMP{}ER")
        self.SETER = Subscriptor(self, "SETE{}R")
        self.CPTER = Subscriptor(self, "CPT{}ER")

HRTIM_TIME = SA_HRTIM_TIME(0x40016A80, "HRTIM_TIME")

class SA_HRTIM_TIMF_TIMFCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMFCR", "Timerx Control Register")
        self.UPDGAT = BitField(self, 0xF0000000, "UPDGAT", "Update Gating")
        self.PREEN = BitField(self, 0x08000000, "PREEN", "Preload enable")
        self.DACSYNC = BitField(self, 0x06000000, "DACSYNC", "AC Synchronization")
        self.MSTU = BitField(self, 0x01000000, "MSTU", "Master Timer update")
        self.TDU = BitField(self, 0x00400000, "TDU", "TDU")
        self.TCU = BitField(self, 0x00200000, "TCU", "TCU")
        self.TBU = BitField(self, 0x00100000, "TBU", "TBU")
        self.TAU = BitField(self, 0x00080000, "TAU", "TAU")
        self.TxRSTU = BitField(self, 0x00040000, "TxRSTU", "Timerx reset update")
        self.TxREPU = BitField(self, 0x00020000, "TxREPU", "Timer x Repetition update")
        self.DELCMP4 = BitField(self, 0x0000C000, "DELCMP4", "Delayed CMP4 mode")
        self.DELCMP2 = BitField(self, 0x00003000, "DELCMP2", "Delayed CMP2 mode")
        self.SYNCSTRTx = BitField(self, 0x00000800, "SYNCSTRTx", "Synchronization Starts Timer x")
        self.SYNCRSTx = BitField(self, 0x00000400, "SYNCRSTx", "Synchronization Resets Timer x")
        self.RSYNCU = BitField(self, 0x00000200, "RSYNCU", "Re-Synchronized Update")
        self.INTLVD = BitField(self, 0x00000180, "INTLVD", "Interleaved mode")
        self.PSHPLL = BitField(self, 0x00000040, "PSHPLL", "Push-Pull mode enable")
        self.HALF = BitField(self, 0x00000020, "HALF", "Half mode enable")
        self.RETRIG = BitField(self, 0x00000010, "RETRIG", "Re-triggerable mode")
        self.CONT = BitField(self, 0x00000008, "CONT", "Continuous mode")
        self.CK_PSCx = BitField(self, 0x00000007, "CK_PSCx", "HRTIM Timer x Clock prescaler")

class SA_HRTIM_TIMF_TIMFISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMFISR", "Timerx Interrupt Status Register")
        self.O2CPY = BitField(self, 0x00200000, "O2CPY", "Output 2 Copy")
        self.O1CPY = BitField(self, 0x00100000, "O1CPY", "Output 1 Copy")
        self.O2STAT = BitField(self, 0x00080000, "O2STAT", "Output 2 State")
        self.O1STAT = BitField(self, 0x00040000, "O1STAT", "Output 1 State")
        self.IPPSTAT = BitField(self, 0x00020000, "IPPSTAT", "Idle Push Pull Status")
        self.CPPSTAT = BitField(self, 0x00010000, "CPPSTAT", "Current Push Pull Status")
        self.DLYPRT = BitField(self, 0x00004000, "DLYPRT", "Delayed Protection Flag")
        self.RST = BitField(self, 0x00002000, "RST", "Reset Interrupt Flag")
        self.RSTx2 = BitField(self, 0x00001000, "RSTx2", "Output 2 Reset Interrupt Flag")
        self.SETx2 = BitField(self, 0x00000800, "SETx2", "Output 2 Set Interrupt Flag")
        self.RSTx1 = BitField(self, 0x00000400, "RSTx1", "Output 1 Reset Interrupt Flag")
        self.SETx1 = BitField(self, 0x00000200, "SETx1", "Output 1 Set Interrupt Flag")
        self.CPT2 = BitField(self, 0x00000100, "CPT2", "Capture2 Interrupt Flag")
        self.CPT1 = BitField(self, 0x00000080, "CPT1", "Capture1 Interrupt Flag")
        self.UPD = BitField(self, 0x00000040, "UPD", "Update Interrupt Flag")
        self.REP = BitField(self, 0x00000010, "REP", "Repetition Interrupt Flag")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Compare 4 Interrupt Flag")
        self.CMP3 = BitField(self, 0x00000004, "CMP3", "Compare 3 Interrupt Flag")
        self.CMP2 = BitField(self, 0x00000002, "CMP2", "Compare 2 Interrupt Flag")
        self.CMP1 = BitField(self, 0x00000001, "CMP1", "Compare 1 Interrupt Flag")
        self.RSTx = Subscriptor(self, "RSTx{}")
        self.OSTAT = Subscriptor(self, "O{}STAT")
        self.OCPY = Subscriptor(self, "O{}CPY")
        self.SETx = Subscriptor(self, "SETx{}")
        self.CPT = Subscriptor(self, "CPT{}")
        self.CMP = Subscriptor(self, "CMP{}")

class SA_HRTIM_TIMF_TIMFICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMFICR", "Timerx Interrupt Clear Register")
        self.DLYPRTC = BitField(self, 0x00004000, "DLYPRTC", "Delayed Protection Flag Clear")
        self.RSTC = BitField(self, 0x00002000, "RSTC", "Reset Interrupt flag Clear")
        self.RSTx2C = BitField(self, 0x00001000, "RSTx2C", "Output 2 Reset flag Clear")
        self.SET2xC = BitField(self, 0x00000800, "SET2xC", "Output 2 Set flag Clear")
        self.RSTx1C = BitField(self, 0x00000400, "RSTx1C", "Output 1 Reset flag Clear")
        self.SET1xC = BitField(self, 0x00000200, "SET1xC", "Output 1 Set flag Clear")
        self.CPT2C = BitField(self, 0x00000100, "CPT2C", "Capture2 Interrupt flag Clear")
        self.CPT1C = BitField(self, 0x00000080, "CPT1C", "Capture1 Interrupt flag Clear")
        self.UPDC = BitField(self, 0x00000040, "UPDC", "Update Interrupt flag Clear")
        self.REPC = BitField(self, 0x00000010, "REPC", "Repetition Interrupt flag Clear")
        self.CMP4C = BitField(self, 0x00000008, "CMP4C", "Compare 4 Interrupt flag Clear")
        self.CMP3C = BitField(self, 0x00000004, "CMP3C", "Compare 3 Interrupt flag Clear")
        self.CMP2C = BitField(self, 0x00000002, "CMP2C", "Compare 2 Interrupt flag Clear")
        self.CMP1C = BitField(self, 0x00000001, "CMP1C", "Compare 1 Interrupt flag Clear")
        self.CPTC = Subscriptor(self, "CPT{}C")
        self.SETxC = Subscriptor(self, "SET{}xC")
        self.CMPC = Subscriptor(self, "CMP{}C")
        self.RSTxC = Subscriptor(self, "RSTx{}C")

class SA_HRTIM_TIMF_TIMFDIER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMFDIER", "TIMxDIER")
        self.DLYPRTDE = BitField(self, 0x40000000, "DLYPRTDE", "DLYPRTDE")
        self.RSTDE = BitField(self, 0x20000000, "RSTDE", "RSTDE")
        self.RSTx2DE = BitField(self, 0x10000000, "RSTx2DE", "RSTx2DE")
        self.SETx2DE = BitField(self, 0x08000000, "SETx2DE", "SETx2DE")
        self.RSTx1DE = BitField(self, 0x04000000, "RSTx1DE", "RSTx1DE")
        self.SET1xDE = BitField(self, 0x02000000, "SET1xDE", "SET1xDE")
        self.CPT2DE = BitField(self, 0x01000000, "CPT2DE", "CPT2DE")
        self.CPT1DE = BitField(self, 0x00800000, "CPT1DE", "CPT1DE")
        self.UPDDE = BitField(self, 0x00400000, "UPDDE", "UPDDE")
        self.REPDE = BitField(self, 0x00100000, "REPDE", "REPDE")
        self.CMP4DE = BitField(self, 0x00080000, "CMP4DE", "CMP4DE")
        self.CMP3DE = BitField(self, 0x00040000, "CMP3DE", "CMP3DE")
        self.CMP2DE = BitField(self, 0x00020000, "CMP2DE", "CMP2DE")
        self.CMP1DE = BitField(self, 0x00010000, "CMP1DE", "CMP1DE")
        self.DLYPRTIE = BitField(self, 0x00004000, "DLYPRTIE", "DLYPRTIE")
        self.RSTIE = BitField(self, 0x00002000, "RSTIE", "RSTIE")
        self.RSTx2IE = BitField(self, 0x00001000, "RSTx2IE", "RSTx2IE")
        self.SETx2IE = BitField(self, 0x00000800, "SETx2IE", "SETx2IE")
        self.RSTx1IE = BitField(self, 0x00000400, "RSTx1IE", "RSTx1IE")
        self.SET1xIE = BitField(self, 0x00000200, "SET1xIE", "SET1xIE")
        self.CPT2IE = BitField(self, 0x00000100, "CPT2IE", "CPT2IE")
        self.CPT1IE = BitField(self, 0x00000080, "CPT1IE", "CPT1IE")
        self.UPDIE = BitField(self, 0x00000040, "UPDIE", "UPDIE")
        self.REPIE = BitField(self, 0x00000010, "REPIE", "REPIE")
        self.CMP4IE = BitField(self, 0x00000008, "CMP4IE", "CMP4IE")
        self.CMP3IE = BitField(self, 0x00000004, "CMP3IE", "CMP3IE")
        self.CMP2IE = BitField(self, 0x00000002, "CMP2IE", "CMP2IE")
        self.CMP1IE = BitField(self, 0x00000001, "CMP1IE", "CMP1IE")
        self.RSTxIE = Subscriptor(self, "RSTx{}IE")
        self.CMPDE = Subscriptor(self, "CMP{}DE")
        self.RSTxDE = Subscriptor(self, "RSTx{}DE")
        self.CPTDE = Subscriptor(self, "CPT{}DE")
        self.CPTIE = Subscriptor(self, "CPT{}IE")
        self.CMPIE = Subscriptor(self, "CMP{}IE")

class SA_HRTIM_TIMF_CNTFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNTFR", "Timerx Counter Register")
        self.CNTx = BitField(self, 0x0000FFFF, "CNTx", "Timerx Counter value")

class SA_HRTIM_TIMF_PERFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "PERFR", "Timerx Period Register")
        self.PERx = BitField(self, 0x0000FFFF, "PERx", "Timerx Period value")

class SA_HRTIM_TIMF_REPFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "REPFR", "Timerx Repetition Register")
        self.REPx = BitField(self, 0x000000FF, "REPx", "Timerx Repetition counter value")

class SA_HRTIM_TIMF_CMP1FR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1FR", "Timerx Compare 1 Register")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMF_CMP1CFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP1CFR", "Timerx Compare 1 Compound Register")
        self.REPx = BitField(self, 0x00FF0000, "REPx", "Timerx Repetition value (aliased from HRTIM_REPx register)")
        self.CMP1x = BitField(self, 0x0000FFFF, "CMP1x", "Timerx Compare 1 value")

class SA_HRTIM_TIMF_CMP2FR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP2FR", "Timerx Compare 2 Register")
        self.CMP2x = BitField(self, 0x0000FFFF, "CMP2x", "Timerx Compare 2 value")

class SA_HRTIM_TIMF_CMP3FR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP3FR", "Timerx Compare 3 Register")
        self.CMP3x = BitField(self, 0x0000FFFF, "CMP3x", "Timerx Compare 3 value")

class SA_HRTIM_TIMF_CMP4FR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CMP4FR", "Timerx Compare 4 Register")
        self.CMP4x = BitField(self, 0x0000FFFF, "CMP4x", "Timerx Compare 4 value")

class SA_HRTIM_TIMF_CPT1FR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1FR", "Timerx Capture 1 Register")
        self.CPT1x = BitField(self, 0x0000FFFF, "CPT1x", "Timerx Capture 1 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMF_CPT2FR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2FR", "Timerx Capture 2 Register")
        self.CPT2x = BitField(self, 0x0000FFFF, "CPT2x", "Timerx Capture 2 value")
        self.DIR = BitField(self, 0x00010000, "DIR", "Timerx Capture 1 Direction status")

class SA_HRTIM_TIMF_DTFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DTFR", "Timerx Deadtime Register")
        self.DTFLKx = BitField(self, 0x80000000, "DTFLKx", "Deadtime Falling Lock")
        self.DTFSLKx = BitField(self, 0x40000000, "DTFSLKx", "Deadtime Falling Sign Lock")
        self.SDTFx = BitField(self, 0x02000000, "SDTFx", "Sign Deadtime Falling value")
        self.DTFx = BitField(self, 0x01FF0000, "DTFx", "Deadtime Falling value")
        self.DTRLKx = BitField(self, 0x00008000, "DTRLKx", "Deadtime Rising Lock")
        self.DTRSLKx = BitField(self, 0x00004000, "DTRSLKx", "Deadtime Rising Sign Lock")
        self.DTPRSC = BitField(self, 0x00001C00, "DTPRSC", "Deadtime Prescaler")
        self.SDTRx = BitField(self, 0x00000200, "SDTRx", "Sign Deadtime Rising value")
        self.DTRx = BitField(self, 0x000001FF, "DTRx", "Deadtime Rising value")

class SA_HRTIM_TIMF_SETF1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETF1R", "Timerx Output1 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "Registers update (transfer preload to active)")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "External Event 1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "Timer Event 9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "Timer Event 8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "Timer Event 7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "Timer Event 6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "Timer Event 5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "Timer Event 4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "Timer Event 3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "Timer Event 2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "Timer Event 1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "Master Compare 4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "Master Compare 3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "Master Compare 2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "Master Compare 1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "Master Period")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "Timer A compare 4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "Timer A compare 3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "Timer A compare 2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "Timer A compare 1")
        self.PER = BitField(self, 0x00000004, "PER", "Timer A Period")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "Timer A resynchronizaton")
        self.SST = BitField(self, 0x00000001, "SST", "Software Set trigger")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMF_RSTE1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTE1R", "Timerx Output1 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMF_SETF2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SETF2R", "Timerx Output2 Set Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SST = BitField(self, 0x00000001, "SST", "SST")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMF_RSTF2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTF2R", "Timerx Output2 Reset Register")
        self.UPDATE = BitField(self, 0x80000000, "UPDATE", "UPDATE")
        self.EXTEVNT10 = BitField(self, 0x40000000, "EXTEVNT10", "EXTEVNT10")
        self.EXTEVNT9 = BitField(self, 0x20000000, "EXTEVNT9", "EXTEVNT9")
        self.EXTEVNT8 = BitField(self, 0x10000000, "EXTEVNT8", "EXTEVNT8")
        self.EXTEVNT7 = BitField(self, 0x08000000, "EXTEVNT7", "EXTEVNT7")
        self.EXTEVNT6 = BitField(self, 0x04000000, "EXTEVNT6", "EXTEVNT6")
        self.EXTEVNT5 = BitField(self, 0x02000000, "EXTEVNT5", "EXTEVNT5")
        self.EXTEVNT4 = BitField(self, 0x01000000, "EXTEVNT4", "EXTEVNT4")
        self.EXTEVNT3 = BitField(self, 0x00800000, "EXTEVNT3", "EXTEVNT3")
        self.EXTEVNT2 = BitField(self, 0x00400000, "EXTEVNT2", "EXTEVNT2")
        self.EXTEVNT1 = BitField(self, 0x00200000, "EXTEVNT1", "EXTEVNT1")
        self.TIMEVNT9 = BitField(self, 0x00100000, "TIMEVNT9", "TIMEVNT9")
        self.TIMEVNT8 = BitField(self, 0x00080000, "TIMEVNT8", "TIMEVNT8")
        self.TIMEVNT7 = BitField(self, 0x00040000, "TIMEVNT7", "TIMEVNT7")
        self.TIMEVNT6 = BitField(self, 0x00020000, "TIMEVNT6", "TIMEVNT6")
        self.TIMEVNT5 = BitField(self, 0x00010000, "TIMEVNT5", "TIMEVNT5")
        self.TIMEVNT4 = BitField(self, 0x00008000, "TIMEVNT4", "TIMEVNT4")
        self.TIMEVNT3 = BitField(self, 0x00004000, "TIMEVNT3", "TIMEVNT3")
        self.TIMEVNT2 = BitField(self, 0x00002000, "TIMEVNT2", "TIMEVNT2")
        self.TIMEVNT1 = BitField(self, 0x00001000, "TIMEVNT1", "TIMEVNT1")
        self.MSTCMP4 = BitField(self, 0x00000800, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000400, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000200, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000100, "MSTCMP1", "MSTCMP1")
        self.MSTPER = BitField(self, 0x00000080, "MSTPER", "MSTPER")
        self.CMP4 = BitField(self, 0x00000040, "CMP4", "CMP4")
        self.CMP3 = BitField(self, 0x00000020, "CMP3", "CMP3")
        self.CMP2 = BitField(self, 0x00000010, "CMP2", "CMP2")
        self.CMP1 = BitField(self, 0x00000008, "CMP1", "CMP1")
        self.PER = BitField(self, 0x00000004, "PER", "PER")
        self.RESYNC = BitField(self, 0x00000002, "RESYNC", "RESYNC")
        self.SRT = BitField(self, 0x00000001, "SRT", "SRT")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMEVNT = Subscriptor(self, "TIMEVNT{}")
        self.CMP = Subscriptor(self, "CMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")

class SA_HRTIM_TIMF_EEFFR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFFR1", "Timerx External Event Filtering Register 1")
        self.EE5FLTR = BitField(self, 0x1E000000, "EE5FLTR", "External Event 5 filter")
        self.EE5LTCH = BitField(self, 0x01000000, "EE5LTCH", "External Event 5 latch")
        self.EE4FLTR = BitField(self, 0x00780000, "EE4FLTR", "External Event 4 filter")
        self.EE4LTCH = BitField(self, 0x00040000, "EE4LTCH", "External Event 4 latch")
        self.EE3FLTR = BitField(self, 0x0001E000, "EE3FLTR", "External Event 3 filter")
        self.EE3LTCH = BitField(self, 0x00001000, "EE3LTCH", "External Event 3 latch")
        self.EE2FLTR = BitField(self, 0x00000780, "EE2FLTR", "External Event 2 filter")
        self.EE2LTCH = BitField(self, 0x00000040, "EE2LTCH", "External Event 2 latch")
        self.EE1FLTR = BitField(self, 0x0000001E, "EE1FLTR", "External Event 1 filter")
        self.EE1LTCH = BitField(self, 0x00000001, "EE1LTCH", "External Event 1 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMF_EEFFR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EEFFR2", "Timerx External Event Filtering Register 2")
        self.EE10FLTR = BitField(self, 0x1E000000, "EE10FLTR", "External Event 10 filter")
        self.EE10LTCH = BitField(self, 0x01000000, "EE10LTCH", "External Event 10 latch")
        self.EE9FLTR = BitField(self, 0x00780000, "EE9FLTR", "External Event 9 filter")
        self.EE9LTCH = BitField(self, 0x00040000, "EE9LTCH", "External Event 9 latch")
        self.EE8FLTR = BitField(self, 0x0001E000, "EE8FLTR", "External Event 8 filter")
        self.EE8LTCH = BitField(self, 0x00001000, "EE8LTCH", "External Event 8 latch")
        self.EE7FLTR = BitField(self, 0x00000780, "EE7FLTR", "External Event 7 filter")
        self.EE7LTCH = BitField(self, 0x00000040, "EE7LTCH", "External Event 7 latch")
        self.EE6FLTR = BitField(self, 0x0000001E, "EE6FLTR", "External Event 6 filter")
        self.EE6LTCH = BitField(self, 0x00000001, "EE6LTCH", "External Event 6 latch")
        self.EELTCH = Subscriptor(self, "EE{}LTCH")
        self.EEFLTR = Subscriptor(self, "EE{}FLTR")

class SA_HRTIM_TIMF_RSTFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RSTFR", "TimerA Reset Register")
        self.TIMFCPM2 = BitField(self, 0x80000000, "TIMFCPM2", "Timer F Compare 2")
        self.TIMDCMP4 = BitField(self, 0x40000000, "TIMDCMP4", "Timer D Compare 4")
        self.TIMDCMP2 = BitField(self, 0x20000000, "TIMDCMP2", "Timer D Compare 2")
        self.TIMDCMP1 = BitField(self, 0x10000000, "TIMDCMP1", "Timer D Compare 1")
        self.TIMCCMP4 = BitField(self, 0x08000000, "TIMCCMP4", "Timer C Compare 4")
        self.TIMCCMP2 = BitField(self, 0x04000000, "TIMCCMP2", "Timer C Compare 2")
        self.TIMCCMP1 = BitField(self, 0x02000000, "TIMCCMP1", "Timer C Compare 1")
        self.TIMBCMP4 = BitField(self, 0x01000000, "TIMBCMP4", "Timer B Compare 4")
        self.TIMBCMP2 = BitField(self, 0x00800000, "TIMBCMP2", "Timer B Compare 2")
        self.TIMBCMP1 = BitField(self, 0x00400000, "TIMBCMP1", "Timer B Compare 1")
        self.TIMACMP4 = BitField(self, 0x00200000, "TIMACMP4", "Timer A Compare 4")
        self.TIMACMP2 = BitField(self, 0x00100000, "TIMACMP2", "Timer A Compare 2")
        self.TIMACMP1 = BitField(self, 0x00080000, "TIMACMP1", "Timer A Compare 1")
        self.EXTEVNT10 = BitField(self, 0x00040000, "EXTEVNT10", "External Event 10")
        self.EXTEVNT9 = BitField(self, 0x00020000, "EXTEVNT9", "External Event 9")
        self.EXTEVNT8 = BitField(self, 0x00010000, "EXTEVNT8", "External Event 8")
        self.EXTEVNT7 = BitField(self, 0x00008000, "EXTEVNT7", "External Event 7")
        self.EXTEVNT6 = BitField(self, 0x00004000, "EXTEVNT6", "External Event 6")
        self.EXTEVNT5 = BitField(self, 0x00002000, "EXTEVNT5", "External Event 5")
        self.EXTEVNT4 = BitField(self, 0x00001000, "EXTEVNT4", "External Event 4")
        self.EXTEVNT3 = BitField(self, 0x00000800, "EXTEVNT3", "External Event 3")
        self.EXTEVNT2 = BitField(self, 0x00000400, "EXTEVNT2", "External Event 2")
        self.EXTEVNT1 = BitField(self, 0x00000200, "EXTEVNT1", "External Event 1")
        self.MSTCMP4 = BitField(self, 0x00000100, "MSTCMP4", "Master compare 4")
        self.MSTCMP3 = BitField(self, 0x00000080, "MSTCMP3", "Master compare 3")
        self.MSTCMP2 = BitField(self, 0x00000040, "MSTCMP2", "Master compare 2")
        self.MSTCMP1 = BitField(self, 0x00000020, "MSTCMP1", "Master compare 1")
        self.MSTPER = BitField(self, 0x00000010, "MSTPER", "Master timer Period")
        self.CMP4 = BitField(self, 0x00000008, "CMP4", "Timer A compare 4 reset")
        self.CMP2 = BitField(self, 0x00000004, "CMP2", "Timer A compare 2 reset")
        self.UPDT = BitField(self, 0x00000002, "UPDT", "Timer A Update reset")
        self.TIMFCMP1 = BitField(self, 0x00000001, "TIMFCMP1", "Timer A Update reset")
        self.TIMACMP = Subscriptor(self, "TIMACMP{}")
        self.TIMDCMP = Subscriptor(self, "TIMDCMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")
        self.EXTEVNT = Subscriptor(self, "EXTEVNT{}")
        self.TIMCCMP = Subscriptor(self, "TIMCCMP{}")
        self.TIMBCMP = Subscriptor(self, "TIMBCMP{}")

class SA_HRTIM_TIMF_CHPFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CHPFR", "Timerx Chopper Register")
        self.STRTPW = BitField(self, 0x00000780, "STRTPW", "STRTPW")
        self.CHPDTY = BitField(self, 0x00000070, "CHPDTY", "Timerx chopper duty cycle value")
        self.CHPFRQ = BitField(self, 0x0000000F, "CHPFRQ", "Timerx carrier frequency value")

class SA_HRTIM_TIMF_CPT1FCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT1FCR", "Timerx Capture 2 Control Register")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "TECMP2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "TECMP1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "TE1RST")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "TE1SET")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMF_CPT2FCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CPT2FCR", "CPT2xCR")
        self.TECMP2 = BitField(self, 0x80000000, "TECMP2", "TECMP2")
        self.TECMP1 = BitField(self, 0x40000000, "TECMP1", "TECMP1")
        self.TE1RST = BitField(self, 0x20000000, "TE1RST", "TE1RST")
        self.TE1SET = BitField(self, 0x10000000, "TE1SET", "TE1SET")
        self.TDCMP2 = BitField(self, 0x08000000, "TDCMP2", "Timer D Compare 2")
        self.TDCMP1 = BitField(self, 0x04000000, "TDCMP1", "Timer D Compare 1")
        self.TD1RST = BitField(self, 0x02000000, "TD1RST", "Timer D output 1 Reset")
        self.TD1SET = BitField(self, 0x01000000, "TD1SET", "Timer D output 1 Set")
        self.TCCMP2 = BitField(self, 0x00800000, "TCCMP2", "Timer C Compare 2")
        self.TCCMP1 = BitField(self, 0x00400000, "TCCMP1", "Timer C Compare 1")
        self.TC1RST = BitField(self, 0x00200000, "TC1RST", "Timer C output 1 Reset")
        self.TC1SET = BitField(self, 0x00100000, "TC1SET", "Timer C output 1 Set")
        self.TBCMP2 = BitField(self, 0x00080000, "TBCMP2", "Timer B Compare 2")
        self.TBCMP1 = BitField(self, 0x00040000, "TBCMP1", "Timer B Compare 1")
        self.TB1RST = BitField(self, 0x00020000, "TB1RST", "Timer B output 1 Reset")
        self.TB1SET = BitField(self, 0x00010000, "TB1SET", "Timer B output 1 Set")
        self.TACMP2 = BitField(self, 0x00008000, "TACMP2", "Timer A Compare 2")
        self.TACMP1 = BitField(self, 0x00004000, "TACMP1", "Timer A Compare 1")
        self.TA1RST = BitField(self, 0x00002000, "TA1RST", "Timer A output 1 Reset")
        self.TA1SET = BitField(self, 0x00001000, "TA1SET", "Timer A output 1 Set")
        self.EXEV10CPT = BitField(self, 0x00000800, "EXEV10CPT", "External Event 10 Capture")
        self.EXEV9CPT = BitField(self, 0x00000400, "EXEV9CPT", "External Event 9 Capture")
        self.EXEV8CPT = BitField(self, 0x00000200, "EXEV8CPT", "External Event 8 Capture")
        self.EXEV7CPT = BitField(self, 0x00000100, "EXEV7CPT", "External Event 7 Capture")
        self.EXEV6CPT = BitField(self, 0x00000080, "EXEV6CPT", "External Event 6 Capture")
        self.EXEV5CPT = BitField(self, 0x00000040, "EXEV5CPT", "External Event 5 Capture")
        self.EXEV4CPT = BitField(self, 0x00000020, "EXEV4CPT", "External Event 4 Capture")
        self.EXEV3CPT = BitField(self, 0x00000010, "EXEV3CPT", "External Event 3 Capture")
        self.EXEV2CPT = BitField(self, 0x00000008, "EXEV2CPT", "External Event 2 Capture")
        self.EXEV1CPT = BitField(self, 0x00000004, "EXEV1CPT", "External Event 1 Capture")
        self.UDPCPT = BitField(self, 0x00000002, "UDPCPT", "Update Capture")
        self.SWCPT = BitField(self, 0x00000001, "SWCPT", "Software Capture")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.EXEVCPT = Subscriptor(self, "EXEV{}CPT")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_TIMF_OUTFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OUTFR", "Timerx Output Register")
        self.DIDL2 = BitField(self, 0x00800000, "DIDL2", "Output 2 Deadtime upon burst mode Idle entry")
        self.CHP2 = BitField(self, 0x00400000, "CHP2", "Output 2 Chopper enable")
        self.FAULT2 = BitField(self, 0x00300000, "FAULT2", "Output 2 Fault state")
        self.IDLES2 = BitField(self, 0x00080000, "IDLES2", "Output 2 Idle State")
        self.IDLEM2 = BitField(self, 0x00040000, "IDLEM2", "Output 2 Idle mode")
        self.POL2 = BitField(self, 0x00020000, "POL2", "Output 2 polarity")
        self.BIAR = BitField(self, 0x00004000, "BIAR", "Balanced Idle Automatic Resume")
        self.DLYPRT = BitField(self, 0x00001C00, "DLYPRT", "Delayed Protection")
        self.DLYPRTEN = BitField(self, 0x00000200, "DLYPRTEN", "Delayed Protection Enable")
        self.DTEN = BitField(self, 0x00000100, "DTEN", "Deadtime enable")
        self.DIDL1 = BitField(self, 0x00000080, "DIDL1", "Output 1 Deadtime upon burst mode Idle entry")
        self.CHP1 = BitField(self, 0x00000040, "CHP1", "Output 1 Chopper enable")
        self.FAULT1 = BitField(self, 0x00000030, "FAULT1", "Output 1 Fault state")
        self.IDLES1 = BitField(self, 0x00000008, "IDLES1", "Output 1 Idle State")
        self.IDLEM1 = BitField(self, 0x00000004, "IDLEM1", "Output 1 Idle mode")
        self.POL1 = BitField(self, 0x00000002, "POL1", "Output 1 polarity")
        self.POL = Subscriptor(self, "POL{}")
        self.DIDL = Subscriptor(self, "DIDL{}")
        self.FAULT = Subscriptor(self, "FAULT{}")
        self.CHP = Subscriptor(self, "CHP{}")
        self.IDLES = Subscriptor(self, "IDLES{}")
        self.IDLEM = Subscriptor(self, "IDLEM{}")

class SA_HRTIM_TIMF_FLTFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTFR", "Timerx Fault Register")
        self.FLTLCK = BitField(self, 0x80000000, "FLTLCK", "Fault sources Lock")
        self.FLT6EN = BitField(self, 0x00000020, "FLT6EN", "Fault 6 enable")
        self.FLT5EN = BitField(self, 0x00000010, "FLT5EN", "Fault 5 enable")
        self.FLT4EN = BitField(self, 0x00000008, "FLT4EN", "Fault 4 enable")
        self.FLT3EN = BitField(self, 0x00000004, "FLT3EN", "Fault 3 enable")
        self.FLT2EN = BitField(self, 0x00000002, "FLT2EN", "Fault 2 enable")
        self.FLT1EN = BitField(self, 0x00000001, "FLT1EN", "Fault 1 enable")
        self.FLTEN = Subscriptor(self, "FLT{}EN")

class SA_HRTIM_TIMF_TIMFCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TIMFCR2", "HRTIM Timerx Control Register 2")
        self.TRGHLF = BitField(self, 0x00100000, "TRGHLF", "Triggered-half mode")
        self.GTCMP3 = BitField(self, 0x00020000, "GTCMP3", "Greater than Compare 3 PWM mode")
        self.GTCMP1 = BitField(self, 0x00010000, "GTCMP1", "Greater than Compare 1 PWM mode")
        self.FEROM = BitField(self, 0x0000C000, "FEROM", "Fault and Event Roll-Over Mode")
        self.BMROM = BitField(self, 0x00003000, "BMROM", "Burst Mode Roll-Over Mode")
        self.ADROM = BitField(self, 0x00000C00, "ADROM", "ADC Roll-Over Mode")
        self.OUTROM = BitField(self, 0x00000300, "OUTROM", "Output Roll-Over Mode")
        self.ROM = BitField(self, 0x000000C0, "ROM", "Roll-Over Mode")
        self.UDM = BitField(self, 0x00000010, "UDM", "Up-Down Mode")
        self.DCDR = BitField(self, 0x00000004, "DCDR", "Dual Channel DAC Reset trigger")
        self.DCDS = BitField(self, 0x00000002, "DCDS", "Dual Channel DAC Step trigger")
        self.DCDE = BitField(self, 0x00000001, "DCDE", "Dual Channel DAC trigger enable")

class SA_HRTIM_TIMF_FEEFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FEEFR3", "HRTIM Timerx External Event Filtering Register 3")
        self.EEVACNT = BitField(self, 0x00003F00, "EEVACNT", "External Event A counter")
        self.EEVASEL = BitField(self, 0x000000F0, "EEVASEL", "External Event A Selection")
        self.EEVARSTM = BitField(self, 0x00000004, "EEVARSTM", "External Event A Reset Mode")
        self.EEVACRES = BitField(self, 0x00000002, "EEVACRES", "External Event A Counter Reset")
        self.EEVACE = BitField(self, 0x00000001, "EEVACE", "External Event A Counter Enable")

class SA_HRTIM_TIMF(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: TIMF")
        self.TIMFCR = SA_HRTIM_TIMF_TIMFCR(self, 0x0)
        self.TIMFISR = SA_HRTIM_TIMF_TIMFISR(self, 0x4)
        self.TIMFICR = SA_HRTIM_TIMF_TIMFICR(self, 0x8)
        self.TIMFDIER = SA_HRTIM_TIMF_TIMFDIER(self, 0xC)
        self.CNTFR = SA_HRTIM_TIMF_CNTFR(self, 0x10)
        self.PERFR = SA_HRTIM_TIMF_PERFR(self, 0x14)
        self.REPFR = SA_HRTIM_TIMF_REPFR(self, 0x18)
        self.CMP1FR = SA_HRTIM_TIMF_CMP1FR(self, 0x1C)
        self.CMP1CFR = SA_HRTIM_TIMF_CMP1CFR(self, 0x20)
        self.CMP2FR = SA_HRTIM_TIMF_CMP2FR(self, 0x24)
        self.CMP3FR = SA_HRTIM_TIMF_CMP3FR(self, 0x28)
        self.CMP4FR = SA_HRTIM_TIMF_CMP4FR(self, 0x2C)
        self.CPT1FR = SA_HRTIM_TIMF_CPT1FR(self, 0x30)
        self.CPT2FR = SA_HRTIM_TIMF_CPT2FR(self, 0x34)
        self.DTFR = SA_HRTIM_TIMF_DTFR(self, 0x38)
        self.SETF1R = SA_HRTIM_TIMF_SETF1R(self, 0x3C)
        self.RSTE1R = SA_HRTIM_TIMF_RSTE1R(self, 0x40)
        self.SETF2R = SA_HRTIM_TIMF_SETF2R(self, 0x44)
        self.RSTF2R = SA_HRTIM_TIMF_RSTF2R(self, 0x48)
        self.EEFFR1 = SA_HRTIM_TIMF_EEFFR1(self, 0x4C)
        self.EEFFR2 = SA_HRTIM_TIMF_EEFFR2(self, 0x50)
        self.RSTFR = SA_HRTIM_TIMF_RSTFR(self, 0x54)
        self.CHPFR = SA_HRTIM_TIMF_CHPFR(self, 0x58)
        self.CPT1FCR = SA_HRTIM_TIMF_CPT1FCR(self, 0x5C)
        self.CPT2FCR = SA_HRTIM_TIMF_CPT2FCR(self, 0x60)
        self.OUTFR = SA_HRTIM_TIMF_OUTFR(self, 0x64)
        self.FLTFR = SA_HRTIM_TIMF_FLTFR(self, 0x68)
        self.TIMFCR2 = SA_HRTIM_TIMF_TIMFCR2(self, 0x6C)
        self.FEEFR3 = SA_HRTIM_TIMF_FEEFR3(self, 0x70)
        self.SETFR = Subscriptor(self, "SETF{}R")
        self.CMPFR = Subscriptor(self, "CMP{}FR")
        self.EEFFR = Subscriptor(self, "EEFFR{}")
        self.CPTFR = Subscriptor(self, "CPT{}FR")
        self.CPTFCR = Subscriptor(self, "CPT{}FCR")

HRTIM_TIMF = SA_HRTIM_TIMF(0x40016B00, "HRTIM_TIMF")

class SA_HRTIM_Common_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR1", "Control Register 1")
        self.AD4USRC = BitField(self, 0x0E000000, "AD4USRC", "ADC Trigger 4 Update Source")
        self.AD3USRC = BitField(self, 0x01C00000, "AD3USRC", "ADC Trigger 3 Update Source")
        self.AD2USRC = BitField(self, 0x00380000, "AD2USRC", "ADC Trigger 2 Update Source")
        self.AD1USRC = BitField(self, 0x00070000, "AD1USRC", "ADC Trigger 1 Update Source")
        self.TFUDIS = BitField(self, 0x00000040, "TFUDIS", "Timer f Update Disable")
        self.TEUDIS = BitField(self, 0x00000020, "TEUDIS", "Timer E Update Disable")
        self.TDUDIS = BitField(self, 0x00000010, "TDUDIS", "Timer D Update Disable")
        self.TCUDIS = BitField(self, 0x00000008, "TCUDIS", "Timer C Update Disable")
        self.TBUDIS = BitField(self, 0x00000004, "TBUDIS", "Timer B Update Disable")
        self.TAUDIS = BitField(self, 0x00000002, "TAUDIS", "Timer A Update Disable")
        self.MUDIS = BitField(self, 0x00000001, "MUDIS", "Master Update Disable")
        self.ADUSRC = Subscriptor(self, "AD{}USRC")

class SA_HRTIM_Common_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "Control Register 2")
        self.SWPF = BitField(self, 0x00200000, "SWPF", "Swap Timer F outputs")
        self.SWPE = BitField(self, 0x00100000, "SWPE", "Swap Timer E outputs")
        self.SWPD = BitField(self, 0x00080000, "SWPD", "Swap Timer D outputs")
        self.SWPC = BitField(self, 0x00040000, "SWPC", "Swap Timer C outputs")
        self.SWPB = BitField(self, 0x00020000, "SWPB", "Swap Timer B outputs")
        self.SWPA = BitField(self, 0x00010000, "SWPA", "Swap Timer A outputs")
        self.TFRST = BitField(self, 0x00004000, "TFRST", "Timer f counter software reset")
        self.TERST = BitField(self, 0x00002000, "TERST", "Timer E counter software reset")
        self.TDRST = BitField(self, 0x00001000, "TDRST", "Timer D counter software reset")
        self.TCRST = BitField(self, 0x00000800, "TCRST", "Timer C counter software reset")
        self.TBRST = BitField(self, 0x00000400, "TBRST", "Timer B counter software reset")
        self.TARST = BitField(self, 0x00000200, "TARST", "Timer A counter software reset")
        self.MRST = BitField(self, 0x00000100, "MRST", "Master Counter software reset")
        self.TFSWU = BitField(self, 0x00000040, "TFSWU", "Timer f Software Update")
        self.TESWU = BitField(self, 0x00000020, "TESWU", "Timer E Software Update")
        self.TDSWU = BitField(self, 0x00000010, "TDSWU", "Timer D Software Update")
        self.TCSWU = BitField(self, 0x00000008, "TCSWU", "Timer C Software Update")
        self.TBSWU = BitField(self, 0x00000004, "TBSWU", "Timer B Software Update")
        self.TASWU = BitField(self, 0x00000002, "TASWU", "Timer A Software update")
        self.MSWU = BitField(self, 0x00000001, "MSWU", "Master Timer Software update")

class SA_HRTIM_Common_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISR", "Interrupt Status Register")
        self.BMPER = BitField(self, 0x00020000, "BMPER", "Burst mode Period Interrupt Flag")
        self.DLLRDY = BitField(self, 0x00010000, "DLLRDY", "DLL Ready Interrupt Flag")
        self.FLT6 = BitField(self, 0x00000040, "FLT6", "Fault 6 Interrupt Flag")
        self.SYSFLT = BitField(self, 0x00000020, "SYSFLT", "System Fault Interrupt Flag")
        self.FLT5 = BitField(self, 0x00000010, "FLT5", "Fault 5 Interrupt Flag")
        self.FLT4 = BitField(self, 0x00000008, "FLT4", "Fault 4 Interrupt Flag")
        self.FLT3 = BitField(self, 0x00000004, "FLT3", "Fault 3 Interrupt Flag")
        self.FLT2 = BitField(self, 0x00000002, "FLT2", "Fault 2 Interrupt Flag")
        self.FLT1 = BitField(self, 0x00000001, "FLT1", "Fault 1 Interrupt Flag")
        self.FLT = Subscriptor(self, "FLT{}")

class SA_HRTIM_Common_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "Interrupt Clear Register")
        self.BMPERC = BitField(self, 0x00020000, "BMPERC", "Burst mode period flag Clear")
        self.DLLRDYC = BitField(self, 0x00010000, "DLLRDYC", "DLL Ready Interrupt flag Clear")
        self.FLT6C = BitField(self, 0x00000040, "FLT6C", "Fault 6 Interrupt Flag Clear")
        self.SYSFLTC = BitField(self, 0x00000020, "SYSFLTC", "System Fault Interrupt Flag Clear")
        self.FLT5C = BitField(self, 0x00000010, "FLT5C", "Fault 5 Interrupt Flag Clear")
        self.FLT4C = BitField(self, 0x00000008, "FLT4C", "Fault 4 Interrupt Flag Clear")
        self.FLT3C = BitField(self, 0x00000004, "FLT3C", "Fault 3 Interrupt Flag Clear")
        self.FLT2C = BitField(self, 0x00000002, "FLT2C", "Fault 2 Interrupt Flag Clear")
        self.FLT1C = BitField(self, 0x00000001, "FLT1C", "Fault 1 Interrupt Flag Clear")
        self.FLTC = Subscriptor(self, "FLT{}C")

class SA_HRTIM_Common_IER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IER", "Interrupt Enable Register")
        self.BMPERIE = BitField(self, 0x00020000, "BMPERIE", "Burst mode period Interrupt Enable")
        self.DLLRDYIE = BitField(self, 0x00010000, "DLLRDYIE", "DLL Ready Interrupt Enable")
        self.FLT6IE = BitField(self, 0x00000040, "FLT6IE", "Fault 6 Interrupt Enable")
        self.SYSFLTE = BitField(self, 0x00000020, "SYSFLTE", "System Fault Interrupt Enable")
        self.FLT5IE = BitField(self, 0x00000010, "FLT5IE", "Fault 5 Interrupt Enable")
        self.FLT4IE = BitField(self, 0x00000008, "FLT4IE", "Fault 4 Interrupt Enable")
        self.FLT3IE = BitField(self, 0x00000004, "FLT3IE", "Fault 3 Interrupt Enable")
        self.FLT2IE = BitField(self, 0x00000002, "FLT2IE", "Fault 2 Interrupt Enable")
        self.FLT1IE = BitField(self, 0x00000001, "FLT1IE", "Fault 1 Interrupt Enable")
        self.FLTIE = Subscriptor(self, "FLT{}IE")

class SA_HRTIM_Common_OENR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OENR", "Output Enable Register")
        self.TF2ODS = BitField(self, 0x00000800, "TF2ODS", "Timer F Output 2 disable status")
        self.TF1ODS = BitField(self, 0x00000400, "TF1ODS", "Timer F Output 1 disable status")
        self.TE2OEN = BitField(self, 0x00000200, "TE2OEN", "Timer E Output 2 Enable")
        self.TE1OEN = BitField(self, 0x00000100, "TE1OEN", "Timer E Output 1 Enable")
        self.TD2OEN = BitField(self, 0x00000080, "TD2OEN", "Timer D Output 2 Enable")
        self.TD1OEN = BitField(self, 0x00000040, "TD1OEN", "Timer D Output 1 Enable")
        self.TC2OEN = BitField(self, 0x00000020, "TC2OEN", "Timer C Output 2 Enable")
        self.TC1OEN = BitField(self, 0x00000010, "TC1OEN", "Timer C Output 1 Enable")
        self.TB2OEN = BitField(self, 0x00000008, "TB2OEN", "Timer B Output 2 Enable")
        self.TB1OEN = BitField(self, 0x00000004, "TB1OEN", "Timer B Output 1 Enable")
        self.TA2OEN = BitField(self, 0x00000002, "TA2OEN", "Timer A Output 2 Enable")
        self.TA1OEN = BitField(self, 0x00000001, "TA1OEN", "Timer A Output 1 Enable")
        self.TFODS = Subscriptor(self, "TF{}ODS")
        self.TAOEN = Subscriptor(self, "TA{}OEN")
        self.TBOEN = Subscriptor(self, "TB{}OEN")
        self.TCOEN = Subscriptor(self, "TC{}OEN")
        self.TEOEN = Subscriptor(self, "TE{}OEN")
        self.TDOEN = Subscriptor(self, "TD{}OEN")

class SA_HRTIM_Common_ODISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ODISR", "ODISR")
        self.TF2ODIS = BitField(self, 0x00000800, "TF2ODIS", "TF2ODIS")
        self.TF1ODIS = BitField(self, 0x00000400, "TF1ODIS", "TF1ODIS")
        self.TE2ODIS = BitField(self, 0x00000200, "TE2ODIS", "TE2ODIS")
        self.TE1ODIS = BitField(self, 0x00000100, "TE1ODIS", "TE1ODIS")
        self.TD2ODIS = BitField(self, 0x00000080, "TD2ODIS", "TD2ODIS")
        self.TD1ODIS = BitField(self, 0x00000040, "TD1ODIS", "TD1ODIS")
        self.TC2ODIS = BitField(self, 0x00000020, "TC2ODIS", "TC2ODIS")
        self.TC1ODIS = BitField(self, 0x00000010, "TC1ODIS", "TC1ODIS")
        self.TB2ODIS = BitField(self, 0x00000008, "TB2ODIS", "TB2ODIS")
        self.TB1ODIS = BitField(self, 0x00000004, "TB1ODIS", "TB1ODIS")
        self.TA2ODIS = BitField(self, 0x00000002, "TA2ODIS", "TA2ODIS")
        self.TA1ODIS = BitField(self, 0x00000001, "TA1ODIS", "TA1ODIS")
        self.TFODIS = Subscriptor(self, "TF{}ODIS")
        self.TDODIS = Subscriptor(self, "TD{}ODIS")
        self.TBODIS = Subscriptor(self, "TB{}ODIS")
        self.TAODIS = Subscriptor(self, "TA{}ODIS")
        self.TCODIS = Subscriptor(self, "TC{}ODIS")
        self.TEODIS = Subscriptor(self, "TE{}ODIS")

class SA_HRTIM_Common_ODSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ODSR", "Output Disable Status Register")
        self.TF2ODS = BitField(self, 0x00000800, "TF2ODS", "TF2ODS")
        self.TF1ODS = BitField(self, 0x00000400, "TF1ODS", "TF1ODS")
        self.TE2ODS = BitField(self, 0x00000200, "TE2ODS", "Timer E Output 2 disable status")
        self.TE1ODS = BitField(self, 0x00000100, "TE1ODS", "Timer E Output 1 disable status")
        self.TD2ODS = BitField(self, 0x00000080, "TD2ODS", "Timer D Output 2 disable status")
        self.TD1ODS = BitField(self, 0x00000040, "TD1ODS", "Timer D Output 1 disable status")
        self.TC2ODS = BitField(self, 0x00000020, "TC2ODS", "Timer C Output 2 disable status")
        self.TC1ODS = BitField(self, 0x00000010, "TC1ODS", "Timer C Output 1 disable status")
        self.TB2ODS = BitField(self, 0x00000008, "TB2ODS", "Timer B Output 2 disable status")
        self.TB1ODS = BitField(self, 0x00000004, "TB1ODS", "Timer B Output 1 disable status")
        self.TA2ODS = BitField(self, 0x00000002, "TA2ODS", "Timer A Output 2 disable status")
        self.TA1ODS = BitField(self, 0x00000001, "TA1ODS", "Timer A Output 1 disable status")
        self.TDODS = Subscriptor(self, "TD{}ODS")
        self.TAODS = Subscriptor(self, "TA{}ODS")
        self.TCODS = Subscriptor(self, "TC{}ODS")
        self.TFODS = Subscriptor(self, "TF{}ODS")
        self.TEODS = Subscriptor(self, "TE{}ODS")
        self.TBODS = Subscriptor(self, "TB{}ODS")

class SA_HRTIM_Common_BMCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BMCR", "Burst Mode Control Register")
        self.BMSTAT = BitField(self, 0x80000000, "BMSTAT", "Burst Mode Status")
        self.TFBM = BitField(self, 0x00400000, "TFBM", "Timer f Burst Mode")
        self.TEBM = BitField(self, 0x00200000, "TEBM", "Timer E Burst Mode")
        self.TDBM = BitField(self, 0x00100000, "TDBM", "Timer D Burst Mode")
        self.TCBM = BitField(self, 0x00080000, "TCBM", "Timer C Burst Mode")
        self.TBBM = BitField(self, 0x00040000, "TBBM", "Timer B Burst Mode")
        self.TABM = BitField(self, 0x00020000, "TABM", "Timer A Burst Mode")
        self.MTBM = BitField(self, 0x00010000, "MTBM", "Master Timer Burst Mode")
        self.BMPREN = BitField(self, 0x00000400, "BMPREN", "Burst Mode Preload Enable")
        self.BMPRSC = BitField(self, 0x000003C0, "BMPRSC", "Burst Mode Prescaler")
        self.BMCLK = BitField(self, 0x0000003C, "BMCLK", "Burst Mode Clock source")
        self.BMOM = BitField(self, 0x00000002, "BMOM", "Burst Mode operating mode")
        self.BME = BitField(self, 0x00000001, "BME", "Burst Mode enable")

class SA_HRTIM_Common_BMTRG(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BMTRG", "BMTRG")
        self.OCHPEV = BitField(self, 0x80000000, "OCHPEV", "OCHPEV")
        self.EEV8 = BitField(self, 0x40000000, "EEV8", "EEV8")
        self.EEV7 = BitField(self, 0x20000000, "EEV7", "EEV7")
        self.TDEEV8 = BitField(self, 0x10000000, "TDEEV8", "TDEEV8")
        self.TDEEV7 = BitField(self, 0x08000000, "TDEEV7", "TDEEV7")
        self.TECMP2 = BitField(self, 0x04000000, "TECMP2", "TECMP2")
        self.TECMP1 = BitField(self, 0x02000000, "TECMP1", "TECMP1")
        self.TEREP = BitField(self, 0x01000000, "TEREP", "TEREP")
        self.TERST = BitField(self, 0x00800000, "TERST", "TERST")
        self.TDCMP2 = BitField(self, 0x00400000, "TDCMP2", "TDCMP2")
        self.TDCMP1 = BitField(self, 0x00200000, "TDCMP1", "TDCMP1")
        self.TDREP = BitField(self, 0x00100000, "TDREP", "TDREP")
        self.TDRST = BitField(self, 0x00080000, "TDRST", "TDRST")
        self.TCCMP2 = BitField(self, 0x00040000, "TCCMP2", "TCCMP2")
        self.TCCMP1 = BitField(self, 0x00020000, "TCCMP1", "TCCMP1")
        self.TCREP = BitField(self, 0x00010000, "TCREP", "TCREP")
        self.TCRST = BitField(self, 0x00008000, "TCRST", "TCRST")
        self.TBCMP2 = BitField(self, 0x00004000, "TBCMP2", "TBCMP2")
        self.TBCMP1 = BitField(self, 0x00002000, "TBCMP1", "TBCMP1")
        self.TBREP = BitField(self, 0x00001000, "TBREP", "TBREP")
        self.TBRST = BitField(self, 0x00000800, "TBRST", "TBRST")
        self.TACMP2 = BitField(self, 0x00000400, "TACMP2", "TACMP2")
        self.TACMP1 = BitField(self, 0x00000200, "TACMP1", "TACMP1")
        self.TAREP = BitField(self, 0x00000100, "TAREP", "TAREP")
        self.TARST = BitField(self, 0x00000080, "TARST", "TARST")
        self.MSTCMP4 = BitField(self, 0x00000040, "MSTCMP4", "MSTCMP4")
        self.MSTCMP3 = BitField(self, 0x00000020, "MSTCMP3", "MSTCMP3")
        self.MSTCMP2 = BitField(self, 0x00000010, "MSTCMP2", "MSTCMP2")
        self.MSTCMP1 = BitField(self, 0x00000008, "MSTCMP1", "MSTCMP1")
        self.MSTREP = BitField(self, 0x00000004, "MSTREP", "MSTREP")
        self.MSTRST = BitField(self, 0x00000002, "MSTRST", "MSTRST")
        self.SW = BitField(self, 0x00000001, "SW", "SW")
        self.TACMP = Subscriptor(self, "TACMP{}")
        self.MSTCMP = Subscriptor(self, "MSTCMP{}")
        self.TDEEV = Subscriptor(self, "TDEEV{}")
        self.TDCMP = Subscriptor(self, "TDCMP{}")
        self.TBCMP = Subscriptor(self, "TBCMP{}")
        self.TCCMP = Subscriptor(self, "TCCMP{}")
        self.EEV = Subscriptor(self, "EEV{}")
        self.TECMP = Subscriptor(self, "TECMP{}")

class SA_HRTIM_Common_BMCMPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BMCMPR", "BMCMPR")
        self.BMCMP = BitField(self, 0x0000FFFF, "BMCMP", "BMCMP")

class SA_HRTIM_Common_BMPER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BMPER", "Burst Mode Period Register")
        self.BMPER = BitField(self, 0x0000FFFF, "BMPER", "Burst mode Period")

class SA_HRTIM_Common_EECR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EECR1", "Timer External Event Control Register 1")
        self.EE5FAST = BitField(self, 0x20000000, "EE5FAST", "External Event 5 Fast mode")
        self.EE5SNS = BitField(self, 0x18000000, "EE5SNS", "External Event 5 Sensitivity")
        self.EE5POL = BitField(self, 0x04000000, "EE5POL", "External Event 5 Polarity")
        self.EE5SRC = BitField(self, 0x03000000, "EE5SRC", "External Event 5 Source")
        self.EE4FAST = BitField(self, 0x00800000, "EE4FAST", "External Event 4 Fast mode")
        self.EE4SNS = BitField(self, 0x00600000, "EE4SNS", "External Event 4 Sensitivity")
        self.EE4POL = BitField(self, 0x00100000, "EE4POL", "External Event 4 Polarity")
        self.EE4SRC = BitField(self, 0x000C0000, "EE4SRC", "External Event 4 Source")
        self.EE3FAST = BitField(self, 0x00020000, "EE3FAST", "External Event 3 Fast mode")
        self.EE3SNS = BitField(self, 0x00018000, "EE3SNS", "External Event 3 Sensitivity")
        self.EE3POL = BitField(self, 0x00004000, "EE3POL", "External Event 3 Polarity")
        self.EE3SRC = BitField(self, 0x00003000, "EE3SRC", "External Event 3 Source")
        self.EE2FAST = BitField(self, 0x00000800, "EE2FAST", "External Event 2 Fast mode")
        self.EE2SNS = BitField(self, 0x00000600, "EE2SNS", "External Event 2 Sensitivity")
        self.EE2POL = BitField(self, 0x00000100, "EE2POL", "External Event 2 Polarity")
        self.EE2SRC = BitField(self, 0x000000C0, "EE2SRC", "External Event 2 Source")
        self.EE1FAST = BitField(self, 0x00000020, "EE1FAST", "External Event 1 Fast mode")
        self.EE1SNS = BitField(self, 0x00000018, "EE1SNS", "External Event 1 Sensitivity")
        self.EE1POL = BitField(self, 0x00000004, "EE1POL", "External Event 1 Polarity")
        self.EE1SRC = BitField(self, 0x00000003, "EE1SRC", "External Event 1 Source")
        self.EESRC = Subscriptor(self, "EE{}SRC")
        self.EESNS = Subscriptor(self, "EE{}SNS")
        self.EEFAST = Subscriptor(self, "EE{}FAST")
        self.EEPOL = Subscriptor(self, "EE{}POL")

class SA_HRTIM_Common_EECR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EECR2", "Timer External Event Control Register 2")
        self.EE6SRC = BitField(self, 0x00000003, "EE6SRC", "EE6SRC")
        self.EE6POL = BitField(self, 0x00000004, "EE6POL", "EE6POL")
        self.EE6SNS = BitField(self, 0x00000018, "EE6SNS", "EE6SNS")
        self.EE7SRC = BitField(self, 0x000000C0, "EE7SRC", "EE7SRC")
        self.EE7POL = BitField(self, 0x00000100, "EE7POL", "EE7POL")
        self.EE7SNS = BitField(self, 0x00000600, "EE7SNS", "EE7SNS")
        self.EE8SRC = BitField(self, 0x00003000, "EE8SRC", "EE8SRC")
        self.EE8POL = BitField(self, 0x00004000, "EE8POL", "EE8POL")
        self.EE8SNS = BitField(self, 0x00018000, "EE8SNS", "EE8SNS")
        self.EE9SRC = BitField(self, 0x000C0000, "EE9SRC", "EE9SRC")
        self.EE9POL = BitField(self, 0x00100000, "EE9POL", "EE9POL")
        self.EE9SNS = BitField(self, 0x00600000, "EE9SNS", "EE9SNS")
        self.EE10SRC = BitField(self, 0x03000000, "EE10SRC", "EE10SRC")
        self.EE10POL = BitField(self, 0x04000000, "EE10POL", "EE10POL")
        self.EE10SNS = BitField(self, 0x18000000, "EE10SNS", "EE10SNS")
        self.EESRC = Subscriptor(self, "EE{}SRC")
        self.EESNS = Subscriptor(self, "EE{}SNS")
        self.EEPOL = Subscriptor(self, "EE{}POL")

class SA_HRTIM_Common_EECR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EECR3", "Timer External Event Control Register 3")
        self.EE6F = BitField(self, 0x0000000F, "EE6F", "EE6F")
        self.EE7F = BitField(self, 0x000003C0, "EE7F", "EE7F")
        self.EE8F = BitField(self, 0x0000F000, "EE8F", "EE8F")
        self.EE9F = BitField(self, 0x003C0000, "EE9F", "EE9F")
        self.EE10F = BitField(self, 0x0F000000, "EE10F", "EE10F")
        self.EEVSD = BitField(self, 0xC0000000, "EEVSD", "EEVSD")
        self.EEF = Subscriptor(self, "EE{}F")

class SA_HRTIM_Common_ADC1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADC1R", "ADC Trigger 1 Register")
        self.AD1TEPER = BitField(self, 0x80000000, "AD1TEPER", "ADC trigger 1 on Timer E Period")
        self.AD1TEC4 = BitField(self, 0x40000000, "AD1TEC4", "ADC trigger 1 on Timer E compare 4")
        self.AD1TEC3 = BitField(self, 0x20000000, "AD1TEC3", "ADC trigger 1 on Timer E compare 3")
        self.AD1TEC2 = BitField(self, 0x10000000, "AD1TEC2", "ADC trigger 1 on Timer E compare 2")
        self.AD1TDPER = BitField(self, 0x08000000, "AD1TDPER", "ADC trigger 1 on Timer D Period")
        self.AD1TDC4 = BitField(self, 0x04000000, "AD1TDC4", "ADC trigger 1 on Timer D compare 4")
        self.AD1TDC3 = BitField(self, 0x02000000, "AD1TDC3", "ADC trigger 1 on Timer D compare 3")
        self.AD1TDC2 = BitField(self, 0x01000000, "AD1TDC2", "ADC trigger 1 on Timer D compare 2")
        self.AD1TCPER = BitField(self, 0x00800000, "AD1TCPER", "ADC trigger 1 on Timer C Period")
        self.AD1TCC4 = BitField(self, 0x00400000, "AD1TCC4", "ADC trigger 1 on Timer C compare 4")
        self.AD1TCC3 = BitField(self, 0x00200000, "AD1TCC3", "ADC trigger 1 on Timer C compare 3")
        self.AD1TCC2 = BitField(self, 0x00100000, "AD1TCC2", "ADC trigger 1 on Timer C compare 2")
        self.AD1TBRST = BitField(self, 0x00080000, "AD1TBRST", "ADC trigger 1 on Timer B Reset")
        self.AD1TBPER = BitField(self, 0x00040000, "AD1TBPER", "ADC trigger 1 on Timer B Period")
        self.AD1TBC4 = BitField(self, 0x00020000, "AD1TBC4", "ADC trigger 1 on Timer B compare 4")
        self.AD1TBC3 = BitField(self, 0x00010000, "AD1TBC3", "ADC trigger 1 on Timer B compare 3")
        self.AD1TBC2 = BitField(self, 0x00008000, "AD1TBC2", "ADC trigger 1 on Timer B compare 2")
        self.AD1TARST = BitField(self, 0x00004000, "AD1TARST", "ADC trigger 1 on Timer A Reset")
        self.AD1TAPER = BitField(self, 0x00002000, "AD1TAPER", "ADC trigger 1 on Timer A Period")
        self.AD1TAC4 = BitField(self, 0x00001000, "AD1TAC4", "ADC trigger 1 on Timer A compare 4")
        self.AD1TAC3 = BitField(self, 0x00000800, "AD1TAC3", "ADC trigger 1 on Timer A compare 3")
        self.AD1TAC2 = BitField(self, 0x00000400, "AD1TAC2", "ADC trigger 1 on Timer A compare 2")
        self.AD1EEV5 = BitField(self, 0x00000200, "AD1EEV5", "ADC trigger 1 on External Event 5")
        self.AD1EEV4 = BitField(self, 0x00000100, "AD1EEV4", "ADC trigger 1 on External Event 4")
        self.AD1EEV3 = BitField(self, 0x00000080, "AD1EEV3", "ADC trigger 1 on External Event 3")
        self.AD1EEV2 = BitField(self, 0x00000040, "AD1EEV2", "ADC trigger 1 on External Event 2")
        self.AD1EEV1 = BitField(self, 0x00000020, "AD1EEV1", "ADC trigger 1 on External Event 1")
        self.AD1MPER = BitField(self, 0x00000010, "AD1MPER", "ADC trigger 1 on Master Period")
        self.AD1MC4 = BitField(self, 0x00000008, "AD1MC4", "ADC trigger 1 on Master Compare 4")
        self.AD1MC3 = BitField(self, 0x00000004, "AD1MC3", "ADC trigger 1 on Master Compare 3")
        self.AD1MC2 = BitField(self, 0x00000002, "AD1MC2", "ADC trigger 1 on Master Compare 2")
        self.AD1MC1 = BitField(self, 0x00000001, "AD1MC1", "ADC trigger 1 on Master Compare 1")
        self.AD1TDC = Subscriptor(self, "AD1TDC{}")
        self.AD1TBC = Subscriptor(self, "AD1TBC{}")
        self.AD1EEV = Subscriptor(self, "AD1EEV{}")
        self.AD1TCC = Subscriptor(self, "AD1TCC{}")
        self.AD1MC = Subscriptor(self, "AD1MC{}")
        self.AD1TEC = Subscriptor(self, "AD1TEC{}")
        self.AD1TAC = Subscriptor(self, "AD1TAC{}")

class SA_HRTIM_Common_ADC2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADC2R", "ADC Trigger 2 Register")
        self.AD2TERST = BitField(self, 0x80000000, "AD2TERST", "ADC trigger 2 on Timer E Reset")
        self.AD2TEC4 = BitField(self, 0x40000000, "AD2TEC4", "ADC trigger 2 on Timer E compare 4")
        self.AD2TEC3 = BitField(self, 0x20000000, "AD2TEC3", "ADC trigger 2 on Timer E compare 3")
        self.AD2TEC2 = BitField(self, 0x10000000, "AD2TEC2", "ADC trigger 2 on Timer E compare 2")
        self.AD2TDRST = BitField(self, 0x08000000, "AD2TDRST", "ADC trigger 2 on Timer D Reset")
        self.AD2TDPER = BitField(self, 0x04000000, "AD2TDPER", "ADC trigger 2 on Timer D Period")
        self.AD2TDC4 = BitField(self, 0x02000000, "AD2TDC4", "ADC trigger 2 on Timer D compare 4")
        self.AD2TDC3 = BitField(self, 0x01000000, "AD2TDC3", "ADC trigger 2 on Timer D compare 3")
        self.AD2TDC2 = BitField(self, 0x00800000, "AD2TDC2", "ADC trigger 2 on Timer D compare 2")
        self.AD2TCRST = BitField(self, 0x00400000, "AD2TCRST", "ADC trigger 2 on Timer C Reset")
        self.AD2TCPER = BitField(self, 0x00200000, "AD2TCPER", "ADC trigger 2 on Timer C Period")
        self.AD2TCC4 = BitField(self, 0x00100000, "AD2TCC4", "ADC trigger 2 on Timer C compare 4")
        self.AD2TCC3 = BitField(self, 0x00080000, "AD2TCC3", "ADC trigger 2 on Timer C compare 3")
        self.AD2TCC2 = BitField(self, 0x00040000, "AD2TCC2", "ADC trigger 2 on Timer C compare 2")
        self.AD2TBPER = BitField(self, 0x00020000, "AD2TBPER", "ADC trigger 2 on Timer B Period")
        self.AD2TBC4 = BitField(self, 0x00010000, "AD2TBC4", "ADC trigger 2 on Timer B compare 4")
        self.AD2TBC3 = BitField(self, 0x00008000, "AD2TBC3", "ADC trigger 2 on Timer B compare 3")
        self.AD2TBC2 = BitField(self, 0x00004000, "AD2TBC2", "ADC trigger 2 on Timer B compare 2")
        self.AD2TAPER = BitField(self, 0x00002000, "AD2TAPER", "ADC trigger 2 on Timer A Period")
        self.AD2TAC4 = BitField(self, 0x00001000, "AD2TAC4", "ADC trigger 2 on Timer A compare 4")
        self.AD2TAC3 = BitField(self, 0x00000800, "AD2TAC3", "ADC trigger 2 on Timer A compare 3")
        self.AD2TAC2 = BitField(self, 0x00000400, "AD2TAC2", "ADC trigger 2 on Timer A compare 2")
        self.AD2EEV10 = BitField(self, 0x00000200, "AD2EEV10", "ADC trigger 2 on External Event 10")
        self.AD2EEV9 = BitField(self, 0x00000100, "AD2EEV9", "ADC trigger 2 on External Event 9")
        self.AD2EEV8 = BitField(self, 0x00000080, "AD2EEV8", "ADC trigger 2 on External Event 8")
        self.AD2EEV7 = BitField(self, 0x00000040, "AD2EEV7", "ADC trigger 2 on External Event 7")
        self.AD2EEV6 = BitField(self, 0x00000020, "AD2EEV6", "ADC trigger 2 on External Event 6")
        self.AD2MPER = BitField(self, 0x00000010, "AD2MPER", "ADC trigger 2 on Master Period")
        self.AD2MC4 = BitField(self, 0x00000008, "AD2MC4", "ADC trigger 2 on Master Compare 4")
        self.AD2MC3 = BitField(self, 0x00000004, "AD2MC3", "ADC trigger 2 on Master Compare 3")
        self.AD2MC2 = BitField(self, 0x00000002, "AD2MC2", "ADC trigger 2 on Master Compare 2")
        self.AD2MC1 = BitField(self, 0x00000001, "AD2MC1", "ADC trigger 2 on Master Compare 1")
        self.AD2TBC = Subscriptor(self, "AD2TBC{}")
        self.AD2EEV = Subscriptor(self, "AD2EEV{}")
        self.AD2TEC = Subscriptor(self, "AD2TEC{}")
        self.AD2TDC = Subscriptor(self, "AD2TDC{}")
        self.AD2TAC = Subscriptor(self, "AD2TAC{}")
        self.AD2MC = Subscriptor(self, "AD2MC{}")
        self.AD2TCC = Subscriptor(self, "AD2TCC{}")

class SA_HRTIM_Common_ADC3R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADC3R", "ADC Trigger 3 Register")
        self.AD1TEPER = BitField(self, 0x80000000, "AD1TEPER", "AD1TEPER")
        self.AD1TEC4 = BitField(self, 0x40000000, "AD1TEC4", "AD1TEC4")
        self.AD1TEC3 = BitField(self, 0x20000000, "AD1TEC3", "AD1TEC3")
        self.AD1TEC2 = BitField(self, 0x10000000, "AD1TEC2", "AD1TEC2")
        self.AD1TDPER = BitField(self, 0x08000000, "AD1TDPER", "AD1TDPER")
        self.AD1TDC4 = BitField(self, 0x04000000, "AD1TDC4", "AD1TDC4")
        self.AD1TDC3 = BitField(self, 0x02000000, "AD1TDC3", "AD1TDC3")
        self.AD1TDC2 = BitField(self, 0x01000000, "AD1TDC2", "AD1TDC2")
        self.AD1TCPER = BitField(self, 0x00800000, "AD1TCPER", "AD1TCPER")
        self.AD1TCC4 = BitField(self, 0x00400000, "AD1TCC4", "AD1TCC4")
        self.AD1TCC3 = BitField(self, 0x00200000, "AD1TCC3", "AD1TCC3")
        self.AD1TCC2 = BitField(self, 0x00100000, "AD1TCC2", "AD1TCC2")
        self.AD1TBRST = BitField(self, 0x00080000, "AD1TBRST", "AD1TBRST")
        self.AD1TBPER = BitField(self, 0x00040000, "AD1TBPER", "AD1TBPER")
        self.AD1TBC4 = BitField(self, 0x00020000, "AD1TBC4", "AD1TBC4")
        self.AD1TBC3 = BitField(self, 0x00010000, "AD1TBC3", "AD1TBC3")
        self.AD1TBC2 = BitField(self, 0x00008000, "AD1TBC2", "AD1TBC2")
        self.AD1TARST = BitField(self, 0x00004000, "AD1TARST", "AD1TARST")
        self.AD1TAPER = BitField(self, 0x00002000, "AD1TAPER", "AD1TAPER")
        self.AD1TAC4 = BitField(self, 0x00001000, "AD1TAC4", "AD1TAC4")
        self.AD1TAC3 = BitField(self, 0x00000800, "AD1TAC3", "AD1TAC3")
        self.AD1TAC2 = BitField(self, 0x00000400, "AD1TAC2", "AD1TAC2")
        self.AD1EEV5 = BitField(self, 0x00000200, "AD1EEV5", "AD1EEV5")
        self.AD1EEV4 = BitField(self, 0x00000100, "AD1EEV4", "AD1EEV4")
        self.AD1EEV3 = BitField(self, 0x00000080, "AD1EEV3", "AD1EEV3")
        self.AD1EEV2 = BitField(self, 0x00000040, "AD1EEV2", "AD1EEV2")
        self.AD1EEV1 = BitField(self, 0x00000020, "AD1EEV1", "AD1EEV1")
        self.AD1MPER = BitField(self, 0x00000010, "AD1MPER", "AD1MPER")
        self.AD1MC4 = BitField(self, 0x00000008, "AD1MC4", "AD1MC4")
        self.AD1MC3 = BitField(self, 0x00000004, "AD1MC3", "AD1MC3")
        self.AD1MC2 = BitField(self, 0x00000002, "AD1MC2", "AD1MC2")
        self.AD1MC1 = BitField(self, 0x00000001, "AD1MC1", "AD1MC1")
        self.AD1TDC = Subscriptor(self, "AD1TDC{}")
        self.AD1TBC = Subscriptor(self, "AD1TBC{}")
        self.AD1EEV = Subscriptor(self, "AD1EEV{}")
        self.AD1TCC = Subscriptor(self, "AD1TCC{}")
        self.AD1MC = Subscriptor(self, "AD1MC{}")
        self.AD1TEC = Subscriptor(self, "AD1TEC{}")
        self.AD1TAC = Subscriptor(self, "AD1TAC{}")

class SA_HRTIM_Common_ADC4R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADC4R", "ADC Trigger 4 Register")
        self.AD2TERST = BitField(self, 0x80000000, "AD2TERST", "AD2TERST")
        self.AD2TEC4 = BitField(self, 0x40000000, "AD2TEC4", "AD2TEC4")
        self.AD2TEC3 = BitField(self, 0x20000000, "AD2TEC3", "AD2TEC3")
        self.AD2TEC2 = BitField(self, 0x10000000, "AD2TEC2", "AD2TEC2")
        self.AD2TDRST = BitField(self, 0x08000000, "AD2TDRST", "AD2TDRST")
        self.AD2TDPER = BitField(self, 0x04000000, "AD2TDPER", "AD2TDPER")
        self.AD2TDC4 = BitField(self, 0x02000000, "AD2TDC4", "AD2TDC4")
        self.AD2TDC3 = BitField(self, 0x01000000, "AD2TDC3", "AD2TDC3")
        self.AD2TDC2 = BitField(self, 0x00800000, "AD2TDC2", "AD2TDC2")
        self.AD2TCRST = BitField(self, 0x00400000, "AD2TCRST", "AD2TCRST")
        self.AD2TCPER = BitField(self, 0x00200000, "AD2TCPER", "AD2TCPER")
        self.AD2TCC4 = BitField(self, 0x00100000, "AD2TCC4", "AD2TCC4")
        self.AD2TCC3 = BitField(self, 0x00080000, "AD2TCC3", "AD2TCC3")
        self.AD2TCC2 = BitField(self, 0x00040000, "AD2TCC2", "AD2TCC2")
        self.AD2TBPER = BitField(self, 0x00020000, "AD2TBPER", "AD2TBPER")
        self.AD2TBC4 = BitField(self, 0x00010000, "AD2TBC4", "AD2TBC4")
        self.AD2TBC3 = BitField(self, 0x00008000, "AD2TBC3", "AD2TBC3")
        self.AD2TBC2 = BitField(self, 0x00004000, "AD2TBC2", "AD2TBC2")
        self.AD2TAPER = BitField(self, 0x00002000, "AD2TAPER", "AD2TAPER")
        self.AD2TAC4 = BitField(self, 0x00001000, "AD2TAC4", "AD2TAC4")
        self.AD2TAC3 = BitField(self, 0x00000800, "AD2TAC3", "AD2TAC3")
        self.AD2TAC2 = BitField(self, 0x00000400, "AD2TAC2", "AD2TAC2")
        self.AD2EEV10 = BitField(self, 0x00000200, "AD2EEV10", "AD2EEV10")
        self.AD2EEV9 = BitField(self, 0x00000100, "AD2EEV9", "AD2EEV9")
        self.AD2EEV8 = BitField(self, 0x00000080, "AD2EEV8", "AD2EEV8")
        self.AD2EEV7 = BitField(self, 0x00000040, "AD2EEV7", "AD2EEV7")
        self.AD2EEV6 = BitField(self, 0x00000020, "AD2EEV6", "AD2EEV6")
        self.AD2MPER = BitField(self, 0x00000010, "AD2MPER", "AD2MPER")
        self.AD2MC4 = BitField(self, 0x00000008, "AD2MC4", "AD2MC4")
        self.AD2MC3 = BitField(self, 0x00000004, "AD2MC3", "AD2MC3")
        self.AD2MC2 = BitField(self, 0x00000002, "AD2MC2", "AD2MC2")
        self.AD2MC1 = BitField(self, 0x00000001, "AD2MC1", "AD2MC1")
        self.AD2TBC = Subscriptor(self, "AD2TBC{}")
        self.AD2EEV = Subscriptor(self, "AD2EEV{}")
        self.AD2TEC = Subscriptor(self, "AD2TEC{}")
        self.AD2TDC = Subscriptor(self, "AD2TDC{}")
        self.AD2TAC = Subscriptor(self, "AD2TAC{}")
        self.AD2MC = Subscriptor(self, "AD2MC{}")
        self.AD2TCC = Subscriptor(self, "AD2TCC{}")

class SA_HRTIM_Common_DLLCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DLLCR", "DLL Control Register")
        self.CALRTE = BitField(self, 0x0000000C, "CALRTE", "DLL Calibration rate")
        self.CALEN = BitField(self, 0x00000002, "CALEN", "DLL Calibration Enable")
        self.CAL = BitField(self, 0x00000001, "CAL", "DLL Calibration Start")

class SA_HRTIM_Common_FLTINR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTINR1", "HRTIM Fault Input Register 1")
        self.FLT4LCK = BitField(self, 0x80000000, "FLT4LCK", "FLT4LCK")
        self.FLT4F = BitField(self, 0x78000000, "FLT4F", "FLT4F")
        self.FLT4SRC = BitField(self, 0x04000000, "FLT4SRC", "FLT4SRC")
        self.FLT4P = BitField(self, 0x02000000, "FLT4P", "FLT4P")
        self.FLT4E = BitField(self, 0x01000000, "FLT4E", "FLT4E")
        self.FLT3LCK = BitField(self, 0x00800000, "FLT3LCK", "FLT3LCK")
        self.FLT3F = BitField(self, 0x00780000, "FLT3F", "FLT3F")
        self.FLT3SRC = BitField(self, 0x00040000, "FLT3SRC", "FLT3SRC")
        self.FLT3P = BitField(self, 0x00020000, "FLT3P", "FLT3P")
        self.FLT3E = BitField(self, 0x00010000, "FLT3E", "FLT3E")
        self.FLT2LCK = BitField(self, 0x00008000, "FLT2LCK", "FLT2LCK")
        self.FLT2F = BitField(self, 0x00007800, "FLT2F", "FLT2F")
        self.FLT2SRC = BitField(self, 0x00000400, "FLT2SRC", "FLT2SRC")
        self.FLT2P = BitField(self, 0x00000200, "FLT2P", "FLT2P")
        self.FLT2E = BitField(self, 0x00000100, "FLT2E", "FLT2E")
        self.FLT1LCK = BitField(self, 0x00000080, "FLT1LCK", "FLT1LCK")
        self.FLT1F = BitField(self, 0x00000078, "FLT1F", "FLT1F")
        self.FLT1SRC = BitField(self, 0x00000004, "FLT1SRC", "FLT1SRC")
        self.FLT1P = BitField(self, 0x00000002, "FLT1P", "FLT1P")
        self.FLT1E = BitField(self, 0x00000001, "FLT1E", "FLT1E")
        self.FLTP = Subscriptor(self, "FLT{}P")
        self.FLTF = Subscriptor(self, "FLT{}F")
        self.FLTSRC = Subscriptor(self, "FLT{}SRC")
        self.FLTE = Subscriptor(self, "FLT{}E")
        self.FLTLCK = Subscriptor(self, "FLT{}LCK")

class SA_HRTIM_Common_FLTINR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTINR2", "HRTIM Fault Input Register 2")
        self.FLTSD = BitField(self, 0x03000000, "FLTSD", "FLTSD")
        self.FLT6SRC_1 = BitField(self, 0x00200000, "FLT6SRC_1", "FLT6SRC")
        self.FLT4SRC_1 = BitField(self, 0x00080000, "FLT4SRC_1", "FLT4SRC_1")
        self.FLT3SRC_1 = BitField(self, 0x00040000, "FLT3SRC_1", "FLT3SRC_1")
        self.FLT2SRC_1 = BitField(self, 0x00020000, "FLT2SRC_1", "FLT2SRC_1")
        self.FLT1SRC_1 = BitField(self, 0x00010000, "FLT1SRC_1", "FLT1SRC_1")
        self.FLT6LCK = BitField(self, 0x00008000, "FLT6LCK", "FLT6LCK")
        self.FLT6F = BitField(self, 0x00007800, "FLT6F", "FLT6F")
        self.FLT6SRC_0 = BitField(self, 0x00000400, "FLT6SRC_0", "FLT6F")
        self.FLT6P = BitField(self, 0x00000200, "FLT6P", "FLT6P")
        self.FLT6E = BitField(self, 0x00000100, "FLT6E", "FLT6E")
        self.FLT5LCK = BitField(self, 0x00000080, "FLT5LCK", "FLT5LCK")
        self.FLT5F = BitField(self, 0x00000078, "FLT5F", "FLT5F")
        self.FLT5SRC = BitField(self, 0x00100004, "FLT5SRC", "FLT5SRC")
        self.FLT5P = BitField(self, 0x00000002, "FLT5P", "FLT5P")
        self.FLT5E = BitField(self, 0x00000001, "FLT5E", "FLT5E")
        self.FLT6SRC_ = Subscriptor(self, "FLT6SRC_{}")
        self.FLTP = Subscriptor(self, "FLT{}P")
        self.FLTF = Subscriptor(self, "FLT{}F")
        self.FLTE = Subscriptor(self, "FLT{}E")
        self.FLTLCK = Subscriptor(self, "FLT{}LCK")

class SA_HRTIM_Common_BDMUPDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDMUPDR", "BDMUPDR")
        self.MCMP4 = BitField(self, 0x00000200, "MCMP4", "MCMP4")
        self.MCMP3 = BitField(self, 0x00000100, "MCMP3", "MCMP3")
        self.MCMP2 = BitField(self, 0x00000080, "MCMP2", "MCMP2")
        self.MCMP1 = BitField(self, 0x00000040, "MCMP1", "MCMP1")
        self.MREP = BitField(self, 0x00000020, "MREP", "MREP")
        self.MPER = BitField(self, 0x00000010, "MPER", "MPER")
        self.MCNT = BitField(self, 0x00000008, "MCNT", "MCNT")
        self.MDIER = BitField(self, 0x00000004, "MDIER", "MDIER")
        self.MICR = BitField(self, 0x00000002, "MICR", "MICR")
        self.MCR = BitField(self, 0x00000001, "MCR", "MCR")
        self.MCMP = Subscriptor(self, "MCMP{}")

class SA_HRTIM_Common_BDTAUPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTAUPR", "Burst DMA Timerx update Register")
        self.TIMxEEFR3 = BitField(self, 0x00400000, "TIMxEEFR3", "TIMxEEFR3")
        self.TIMxCR2 = BitField(self, 0x00200000, "TIMxCR2", "TIMxCR2")
        self.TIMxFLTR = BitField(self, 0x00100000, "TIMxFLTR", "HRTIM_FLTxR register update enable")
        self.TIMxOUTR = BitField(self, 0x00080000, "TIMxOUTR", "HRTIM_OUTxR register update enable")
        self.TIMxCHPR = BitField(self, 0x00040000, "TIMxCHPR", "HRTIM_CHPxR register update enable")
        self.TIMxRSTR = BitField(self, 0x00020000, "TIMxRSTR", "HRTIM_RSTxR register update enable")
        self.TIMxEEFR2 = BitField(self, 0x00010000, "TIMxEEFR2", "HRTIM_EEFxR2 register update enable")
        self.TIMxEEFR1 = BitField(self, 0x00008000, "TIMxEEFR1", "HRTIM_EEFxR1 register update enable")
        self.TIMxRST2R = BitField(self, 0x00004000, "TIMxRST2R", "HRTIM_RST2xR register update enable")
        self.TIMxSET2R = BitField(self, 0x00002000, "TIMxSET2R", "HRTIM_SET2xR register update enable")
        self.TIMxRST1R = BitField(self, 0x00001000, "TIMxRST1R", "HRTIM_RST1xR register update enable")
        self.TIMxSET1R = BitField(self, 0x00000800, "TIMxSET1R", "HRTIM_SET1xR register update enable")
        self.TIMx_DTxR = BitField(self, 0x00000400, "TIMx_DTxR", "HRTIM_DTxR register update enable")
        self.TIMxCMP4 = BitField(self, 0x00000200, "TIMxCMP4", "HRTIM_CMP4xR register update enable")
        self.TIMxCMP3 = BitField(self, 0x00000100, "TIMxCMP3", "HRTIM_CMP3xR register update enable")
        self.TIMxCMP2 = BitField(self, 0x00000080, "TIMxCMP2", "HRTIM_CMP2xR register update enable")
        self.TIMxCMP1 = BitField(self, 0x00000040, "TIMxCMP1", "HRTIM_CMP1xR register update enable")
        self.TIMxREP = BitField(self, 0x00000020, "TIMxREP", "HRTIM_REPxR register update enable")
        self.TIMxPER = BitField(self, 0x00000010, "TIMxPER", "HRTIM_PERxR register update enable")
        self.TIMxCNT = BitField(self, 0x00000008, "TIMxCNT", "HRTIM_CNTxR register update enable")
        self.TIMxDIER = BitField(self, 0x00000004, "TIMxDIER", "HRTIM_TIMxDIER register update enable")
        self.TIMxICR = BitField(self, 0x00000002, "TIMxICR", "HRTIM_TIMxICR register update enable")
        self.TIMxCR = BitField(self, 0x00000001, "TIMxCR", "HRTIM_TIMxCR register update enable")
        self.TIMxSETR = Subscriptor(self, "TIMxSET{}R")
        self.TIMxCMP = Subscriptor(self, "TIMxCMP{}")
        self.TIMxEEFR = Subscriptor(self, "TIMxEEFR{}")

class SA_HRTIM_Common_BDTBUPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTBUPR", "Burst DMA Timerx update Register")
        self.TIMxEEFR3 = BitField(self, 0x00400000, "TIMxEEFR3", "TIMxEEFR3")
        self.TIMxCR2 = BitField(self, 0x00200000, "TIMxCR2", "TIMxCR2")
        self.TIMxFLTR = BitField(self, 0x00100000, "TIMxFLTR", "HRTIM_FLTxR register update enable")
        self.TIMxOUTR = BitField(self, 0x00080000, "TIMxOUTR", "HRTIM_OUTxR register update enable")
        self.TIMxCHPR = BitField(self, 0x00040000, "TIMxCHPR", "HRTIM_CHPxR register update enable")
        self.TIMxRSTR = BitField(self, 0x00020000, "TIMxRSTR", "HRTIM_RSTxR register update enable")
        self.TIMxEEFR2 = BitField(self, 0x00010000, "TIMxEEFR2", "HRTIM_EEFxR2 register update enable")
        self.TIMxEEFR1 = BitField(self, 0x00008000, "TIMxEEFR1", "HRTIM_EEFxR1 register update enable")
        self.TIMxRST2R = BitField(self, 0x00004000, "TIMxRST2R", "HRTIM_RST2xR register update enable")
        self.TIMxSET2R = BitField(self, 0x00002000, "TIMxSET2R", "HRTIM_SET2xR register update enable")
        self.TIMxRST1R = BitField(self, 0x00001000, "TIMxRST1R", "HRTIM_RST1xR register update enable")
        self.TIMxSET1R = BitField(self, 0x00000800, "TIMxSET1R", "HRTIM_SET1xR register update enable")
        self.TIMx_DTxR = BitField(self, 0x00000400, "TIMx_DTxR", "HRTIM_DTxR register update enable")
        self.TIMxCMP4 = BitField(self, 0x00000200, "TIMxCMP4", "HRTIM_CMP4xR register update enable")
        self.TIMxCMP3 = BitField(self, 0x00000100, "TIMxCMP3", "HRTIM_CMP3xR register update enable")
        self.TIMxCMP2 = BitField(self, 0x00000080, "TIMxCMP2", "HRTIM_CMP2xR register update enable")
        self.TIMxCMP1 = BitField(self, 0x00000040, "TIMxCMP1", "HRTIM_CMP1xR register update enable")
        self.TIMxREP = BitField(self, 0x00000020, "TIMxREP", "HRTIM_REPxR register update enable")
        self.TIMxPER = BitField(self, 0x00000010, "TIMxPER", "HRTIM_PERxR register update enable")
        self.TIMxCNT = BitField(self, 0x00000008, "TIMxCNT", "HRTIM_CNTxR register update enable")
        self.TIMxDIER = BitField(self, 0x00000004, "TIMxDIER", "HRTIM_TIMxDIER register update enable")
        self.TIMxICR = BitField(self, 0x00000002, "TIMxICR", "HRTIM_TIMxICR register update enable")
        self.TIMxCR = BitField(self, 0x00000001, "TIMxCR", "HRTIM_TIMxCR register update enable")
        self.TIMxSETR = Subscriptor(self, "TIMxSET{}R")
        self.TIMxCMP = Subscriptor(self, "TIMxCMP{}")
        self.TIMxEEFR = Subscriptor(self, "TIMxEEFR{}")

class SA_HRTIM_Common_BDTCUPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTCUPR", "Burst DMA Timerx update Register")
        self.TIMxEEFR3 = BitField(self, 0x00400000, "TIMxEEFR3", "TIMxEEFR3")
        self.TIMxCR2 = BitField(self, 0x00200000, "TIMxCR2", "TIMxCR2")
        self.TIMxFLTR = BitField(self, 0x00100000, "TIMxFLTR", "HRTIM_FLTxR register update enable")
        self.TIMxOUTR = BitField(self, 0x00080000, "TIMxOUTR", "HRTIM_OUTxR register update enable")
        self.TIMxCHPR = BitField(self, 0x00040000, "TIMxCHPR", "HRTIM_CHPxR register update enable")
        self.TIMxRSTR = BitField(self, 0x00020000, "TIMxRSTR", "HRTIM_RSTxR register update enable")
        self.TIMxEEFR2 = BitField(self, 0x00010000, "TIMxEEFR2", "HRTIM_EEFxR2 register update enable")
        self.TIMxEEFR1 = BitField(self, 0x00008000, "TIMxEEFR1", "HRTIM_EEFxR1 register update enable")
        self.TIMxRST2R = BitField(self, 0x00004000, "TIMxRST2R", "HRTIM_RST2xR register update enable")
        self.TIMxSET2R = BitField(self, 0x00002000, "TIMxSET2R", "HRTIM_SET2xR register update enable")
        self.TIMxRST1R = BitField(self, 0x00001000, "TIMxRST1R", "HRTIM_RST1xR register update enable")
        self.TIMxSET1R = BitField(self, 0x00000800, "TIMxSET1R", "HRTIM_SET1xR register update enable")
        self.TIMx_DTxR = BitField(self, 0x00000400, "TIMx_DTxR", "HRTIM_DTxR register update enable")
        self.TIMxCMP4 = BitField(self, 0x00000200, "TIMxCMP4", "HRTIM_CMP4xR register update enable")
        self.TIMxCMP3 = BitField(self, 0x00000100, "TIMxCMP3", "HRTIM_CMP3xR register update enable")
        self.TIMxCMP2 = BitField(self, 0x00000080, "TIMxCMP2", "HRTIM_CMP2xR register update enable")
        self.TIMxCMP1 = BitField(self, 0x00000040, "TIMxCMP1", "HRTIM_CMP1xR register update enable")
        self.TIMxREP = BitField(self, 0x00000020, "TIMxREP", "HRTIM_REPxR register update enable")
        self.TIMxPER = BitField(self, 0x00000010, "TIMxPER", "HRTIM_PERxR register update enable")
        self.TIMxCNT = BitField(self, 0x00000008, "TIMxCNT", "HRTIM_CNTxR register update enable")
        self.TIMxDIER = BitField(self, 0x00000004, "TIMxDIER", "HRTIM_TIMxDIER register update enable")
        self.TIMxICR = BitField(self, 0x00000002, "TIMxICR", "HRTIM_TIMxICR register update enable")
        self.TIMxCR = BitField(self, 0x00000001, "TIMxCR", "HRTIM_TIMxCR register update enable")
        self.TIMxSETR = Subscriptor(self, "TIMxSET{}R")
        self.TIMxCMP = Subscriptor(self, "TIMxCMP{}")
        self.TIMxEEFR = Subscriptor(self, "TIMxEEFR{}")

class SA_HRTIM_Common_BDTDUPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTDUPR", "Burst DMA Timerx update Register")
        self.TIMxEEFR3 = BitField(self, 0x00400000, "TIMxEEFR3", "TIMxEEFR3")
        self.TIMxCR2 = BitField(self, 0x00200000, "TIMxCR2", "TIMxCR2")
        self.TIMxFLTR = BitField(self, 0x00100000, "TIMxFLTR", "HRTIM_FLTxR register update enable")
        self.TIMxOUTR = BitField(self, 0x00080000, "TIMxOUTR", "HRTIM_OUTxR register update enable")
        self.TIMxCHPR = BitField(self, 0x00040000, "TIMxCHPR", "HRTIM_CHPxR register update enable")
        self.TIMxRSTR = BitField(self, 0x00020000, "TIMxRSTR", "HRTIM_RSTxR register update enable")
        self.TIMxEEFR2 = BitField(self, 0x00010000, "TIMxEEFR2", "HRTIM_EEFxR2 register update enable")
        self.TIMxEEFR1 = BitField(self, 0x00008000, "TIMxEEFR1", "HRTIM_EEFxR1 register update enable")
        self.TIMxRST2R = BitField(self, 0x00004000, "TIMxRST2R", "HRTIM_RST2xR register update enable")
        self.TIMxSET2R = BitField(self, 0x00002000, "TIMxSET2R", "HRTIM_SET2xR register update enable")
        self.TIMxRST1R = BitField(self, 0x00001000, "TIMxRST1R", "HRTIM_RST1xR register update enable")
        self.TIMxSET1R = BitField(self, 0x00000800, "TIMxSET1R", "HRTIM_SET1xR register update enable")
        self.TIMx_DTxR = BitField(self, 0x00000400, "TIMx_DTxR", "HRTIM_DTxR register update enable")
        self.TIMxCMP4 = BitField(self, 0x00000200, "TIMxCMP4", "HRTIM_CMP4xR register update enable")
        self.TIMxCMP3 = BitField(self, 0x00000100, "TIMxCMP3", "HRTIM_CMP3xR register update enable")
        self.TIMxCMP2 = BitField(self, 0x00000080, "TIMxCMP2", "HRTIM_CMP2xR register update enable")
        self.TIMxCMP1 = BitField(self, 0x00000040, "TIMxCMP1", "HRTIM_CMP1xR register update enable")
        self.TIMxREP = BitField(self, 0x00000020, "TIMxREP", "HRTIM_REPxR register update enable")
        self.TIMxPER = BitField(self, 0x00000010, "TIMxPER", "HRTIM_PERxR register update enable")
        self.TIMxCNT = BitField(self, 0x00000008, "TIMxCNT", "HRTIM_CNTxR register update enable")
        self.TIMxDIER = BitField(self, 0x00000004, "TIMxDIER", "HRTIM_TIMxDIER register update enable")
        self.TIMxICR = BitField(self, 0x00000002, "TIMxICR", "HRTIM_TIMxICR register update enable")
        self.TIMxCR = BitField(self, 0x00000001, "TIMxCR", "HRTIM_TIMxCR register update enable")
        self.TIMxSETR = Subscriptor(self, "TIMxSET{}R")
        self.TIMxCMP = Subscriptor(self, "TIMxCMP{}")
        self.TIMxEEFR = Subscriptor(self, "TIMxEEFR{}")

class SA_HRTIM_Common_BDTEUPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTEUPR", "Burst DMA Timerx update Register")
        self.TIMxEEFR3 = BitField(self, 0x00400000, "TIMxEEFR3", "TIMxEEFR3")
        self.TIMxCR2 = BitField(self, 0x00200000, "TIMxCR2", "TIMxCR2")
        self.TIMxFLTR = BitField(self, 0x00100000, "TIMxFLTR", "HRTIM_FLTxR register update enable")
        self.TIMxOUTR = BitField(self, 0x00080000, "TIMxOUTR", "HRTIM_OUTxR register update enable")
        self.TIMxCHPR = BitField(self, 0x00040000, "TIMxCHPR", "HRTIM_CHPxR register update enable")
        self.TIMxRSTR = BitField(self, 0x00020000, "TIMxRSTR", "HRTIM_RSTxR register update enable")
        self.TIMxEEFR2 = BitField(self, 0x00010000, "TIMxEEFR2", "HRTIM_EEFxR2 register update enable")
        self.TIMxEEFR1 = BitField(self, 0x00008000, "TIMxEEFR1", "HRTIM_EEFxR1 register update enable")
        self.TIMxRST2R = BitField(self, 0x00004000, "TIMxRST2R", "HRTIM_RST2xR register update enable")
        self.TIMxSET2R = BitField(self, 0x00002000, "TIMxSET2R", "HRTIM_SET2xR register update enable")
        self.TIMxRST1R = BitField(self, 0x00001000, "TIMxRST1R", "HRTIM_RST1xR register update enable")
        self.TIMxSET1R = BitField(self, 0x00000800, "TIMxSET1R", "HRTIM_SET1xR register update enable")
        self.TIMx_DTxR = BitField(self, 0x00000400, "TIMx_DTxR", "HRTIM_DTxR register update enable")
        self.TIMxCMP4 = BitField(self, 0x00000200, "TIMxCMP4", "HRTIM_CMP4xR register update enable")
        self.TIMxCMP3 = BitField(self, 0x00000100, "TIMxCMP3", "HRTIM_CMP3xR register update enable")
        self.TIMxCMP2 = BitField(self, 0x00000080, "TIMxCMP2", "HRTIM_CMP2xR register update enable")
        self.TIMxCMP1 = BitField(self, 0x00000040, "TIMxCMP1", "HRTIM_CMP1xR register update enable")
        self.TIMxREP = BitField(self, 0x00000020, "TIMxREP", "HRTIM_REPxR register update enable")
        self.TIMxPER = BitField(self, 0x00000010, "TIMxPER", "HRTIM_PERxR register update enable")
        self.TIMxCNT = BitField(self, 0x00000008, "TIMxCNT", "HRTIM_CNTxR register update enable")
        self.TIMxDIER = BitField(self, 0x00000004, "TIMxDIER", "HRTIM_TIMxDIER register update enable")
        self.TIMxICR = BitField(self, 0x00000002, "TIMxICR", "HRTIM_TIMxICR register update enable")
        self.TIMxCR = BitField(self, 0x00000001, "TIMxCR", "HRTIM_TIMxCR register update enable")
        self.TIMxSETR = Subscriptor(self, "TIMxSET{}R")
        self.TIMxCMP = Subscriptor(self, "TIMxCMP{}")
        self.TIMxEEFR = Subscriptor(self, "TIMxEEFR{}")

class SA_HRTIM_Common_BDTFUPR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDTFUPR", "Burst DMA Timerx update Register")
        self.TIMxEEFR3 = BitField(self, 0x00400000, "TIMxEEFR3", "TIMxEEFR3")
        self.TIMxCR2 = BitField(self, 0x00200000, "TIMxCR2", "TIMxCR2")
        self.TIMxFLTR = BitField(self, 0x00100000, "TIMxFLTR", "HRTIM_FLTxR register update enable")
        self.TIMxOUTR = BitField(self, 0x00080000, "TIMxOUTR", "HRTIM_OUTxR register update enable")
        self.TIMxCHPR = BitField(self, 0x00040000, "TIMxCHPR", "HRTIM_CHPxR register update enable")
        self.TIMxRSTR = BitField(self, 0x00020000, "TIMxRSTR", "HRTIM_RSTxR register update enable")
        self.TIMxEEFR2 = BitField(self, 0x00010000, "TIMxEEFR2", "HRTIM_EEFxR2 register update enable")
        self.TIMxEEFR1 = BitField(self, 0x00008000, "TIMxEEFR1", "HRTIM_EEFxR1 register update enable")
        self.TIMxRST2R = BitField(self, 0x00004000, "TIMxRST2R", "HRTIM_RST2xR register update enable")
        self.TIMxSET2R = BitField(self, 0x00002000, "TIMxSET2R", "HRTIM_SET2xR register update enable")
        self.TIMxRST1R = BitField(self, 0x00001000, "TIMxRST1R", "HRTIM_RST1xR register update enable")
        self.TIMxSET1R = BitField(self, 0x00000800, "TIMxSET1R", "HRTIM_SET1xR register update enable")
        self.TIMx_DTxR = BitField(self, 0x00000400, "TIMx_DTxR", "HRTIM_DTxR register update enable")
        self.TIMxCMP4 = BitField(self, 0x00000200, "TIMxCMP4", "HRTIM_CMP4xR register update enable")
        self.TIMxCMP3 = BitField(self, 0x00000100, "TIMxCMP3", "HRTIM_CMP3xR register update enable")
        self.TIMxCMP2 = BitField(self, 0x00000080, "TIMxCMP2", "HRTIM_CMP2xR register update enable")
        self.TIMxCMP1 = BitField(self, 0x00000040, "TIMxCMP1", "HRTIM_CMP1xR register update enable")
        self.TIMxREP = BitField(self, 0x00000020, "TIMxREP", "HRTIM_REPxR register update enable")
        self.TIMxPER = BitField(self, 0x00000010, "TIMxPER", "HRTIM_PERxR register update enable")
        self.TIMxCNT = BitField(self, 0x00000008, "TIMxCNT", "HRTIM_CNTxR register update enable")
        self.TIMxDIER = BitField(self, 0x00000004, "TIMxDIER", "HRTIM_TIMxDIER register update enable")
        self.TIMxICR = BitField(self, 0x00000002, "TIMxICR", "HRTIM_TIMxICR register update enable")
        self.TIMxCR = BitField(self, 0x00000001, "TIMxCR", "HRTIM_TIMxCR register update enable")
        self.TIMxSETR = Subscriptor(self, "TIMxSET{}R")
        self.TIMxCMP = Subscriptor(self, "TIMxCMP{}")
        self.TIMxEEFR = Subscriptor(self, "TIMxEEFR{}")

class SA_HRTIM_Common_BDMADR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDMADR", "Burst DMA Data Register")
        self.BDMADR = BitField(self, 0xFFFFFFFF, "BDMADR", "Burst DMA Data register")

class SA_HRTIM_Common_ADCER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADCER", "HRTIM ADC Extended Trigger Register")
        self.ADC10TRG = BitField(self, 0x7C000000, "ADC10TRG", "ADC10TRG")
        self.ADC9TRG = BitField(self, 0x03E00000, "ADC9TRG", "ADC9TRG")
        self.ADC8TRG = BitField(self, 0x001F0000, "ADC8TRG", "ADC8TRG")
        self.ADC7TRG = BitField(self, 0x00007C00, "ADC7TRG", "ADC7TRG")
        self.ADC6TRG = BitField(self, 0x000003E0, "ADC6TRG", "ADC6TRG")
        self.ADC5TRG = BitField(self, 0x0000001F, "ADC5TRG", "ADC5TRG")
        self.ADCTRG = Subscriptor(self, "ADC{}TRG")

class SA_HRTIM_Common_ADCUR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADCUR", "HRTIM ADC Trigger Update Register")
        self.AD10USRC = BitField(self, 0x00700000, "AD10USRC", "AD10USRC")
        self.AD9USRC = BitField(self, 0x00070000, "AD9USRC", "AD9USRC")
        self.AD8USRC = BitField(self, 0x00007000, "AD8USRC", "AD8USRC")
        self.AD7USRC = BitField(self, 0x00000700, "AD7USRC", "AD7USRC")
        self.AD6USRC = BitField(self, 0x00000070, "AD6USRC", "AD6USRC")
        self.AD5USRC = BitField(self, 0x00000007, "AD5USRC", "AD5USRC")
        self.ADUSRC = Subscriptor(self, "AD{}USRC")

class SA_HRTIM_Common_ADCPS1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADCPS1", "HRTIM ADC Post Scaler Register 1")
        self.ADC5PSC = BitField(self, 0x1F000000, "ADC5PSC", "ADC5PSC")
        self.ADC4PSC = BitField(self, 0x007C0000, "ADC4PSC", "ADC4PSC")
        self.ADC3PSC = BitField(self, 0x0001F000, "ADC3PSC", "ADC3PSC")
        self.ADC2PSC = BitField(self, 0x000007C0, "ADC2PSC", "ADC2PSC")
        self.ADC1PSC = BitField(self, 0x0000001F, "ADC1PSC", "ADC1PSC")
        self.ADCPSC = Subscriptor(self, "ADC{}PSC")

class SA_HRTIM_Common_ADCPS2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADCPS2", "HRTIM ADC Post Scaler Register 2")
        self.ADC10PSC = BitField(self, 0x1F000000, "ADC10PSC", "ADC10PSC")
        self.ADC9PSC = BitField(self, 0x007C0000, "ADC9PSC", "ADC9PSC")
        self.ADC8PSC = BitField(self, 0x0001F000, "ADC8PSC", "ADC8PSC")
        self.ADC7PSC = BitField(self, 0x000007C0, "ADC7PSC", "ADC7PSC")
        self.ADC6PSC = BitField(self, 0x0000001F, "ADC6PSC", "ADC6PSC")
        self.ADCPSC = Subscriptor(self, "ADC{}PSC")

class SA_HRTIM_Common_FLTINR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTINR3", "HRTIM Fault Input Register 3")
        self.FLT4RSTM = BitField(self, 0x80000000, "FLT4RSTM", "FLT4RSTM")
        self.FLT4CRES = BitField(self, 0x40000000, "FLT4CRES", "FLT4CRES")
        self.FLT4CNT = BitField(self, 0x3C000000, "FLT4CNT", "FLT4CNT")
        self.FLT4BLKS = BitField(self, 0x02000000, "FLT4BLKS", "FLT4BLKS")
        self.FLT4BLKE = BitField(self, 0x01000000, "FLT4BLKE", "FLT4BLKE")
        self.FLT3RSTM = BitField(self, 0x00800000, "FLT3RSTM", "FLT3RSTM")
        self.FLT3CRES = BitField(self, 0x00400000, "FLT3CRES", "FLT3CRES")
        self.FLT3CNT = BitField(self, 0x003C0000, "FLT3CNT", "FLT3CNT")
        self.FLT3BLKS = BitField(self, 0x00020000, "FLT3BLKS", "FLT3BLKS")
        self.FLT3BLKE = BitField(self, 0x00010000, "FLT3BLKE", "FLT3BLKE")
        self.FLT2RSTM = BitField(self, 0x00008000, "FLT2RSTM", "FLT2RSTM")
        self.FLT2CRES = BitField(self, 0x00004000, "FLT2CRES", "FLT2CRES")
        self.FLT2CNT = BitField(self, 0x00003C00, "FLT2CNT", "FLT2CNT")
        self.FLT2BLKS = BitField(self, 0x00000200, "FLT2BLKS", "FLT2BLKS")
        self.FLT2BLKE = BitField(self, 0x00000100, "FLT2BLKE", "FLT2BLKE")
        self.FLT1RSTM = BitField(self, 0x00000080, "FLT1RSTM", "FLT1RSTM")
        self.FLT1CRES = BitField(self, 0x00000040, "FLT1CRES", "FLT1CRES")
        self.FLT1CNT = BitField(self, 0x0000003C, "FLT1CNT", "FLT1CNT")
        self.FLT1BLKS = BitField(self, 0x00000002, "FLT1BLKS", "FLT1BLKS")
        self.FLT1BLKE = BitField(self, 0x00000001, "FLT1BLKE", "FLT1BLKE")
        self.FLTBLKS = Subscriptor(self, "FLT{}BLKS")
        self.FLTBLKE = Subscriptor(self, "FLT{}BLKE")
        self.FLTCNT = Subscriptor(self, "FLT{}CNT")
        self.FLTCRES = Subscriptor(self, "FLT{}CRES")
        self.FLTRSTM = Subscriptor(self, "FLT{}RSTM")

class SA_HRTIM_Common_FLTINR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTINR4", "HRTIM Fault Input Register 4")
        self.FLT6RSTM = BitField(self, 0x00008000, "FLT6RSTM", "FLT6RSTM")
        self.FLT6CRES = BitField(self, 0x00004000, "FLT6CRES", "FLT6CRES")
        self.FLT6CNT = BitField(self, 0x00003C00, "FLT6CNT", "FLT6CNT")
        self.FLT6BLKS = BitField(self, 0x00000200, "FLT6BLKS", "FLT6BLKS")
        self.FLT6BLKE = BitField(self, 0x00000100, "FLT6BLKE", "FLT6BLKE")
        self.FLT5RSTM = BitField(self, 0x00000080, "FLT5RSTM", "FLT5RSTM")
        self.FLT5CRES = BitField(self, 0x00000040, "FLT5CRES", "FLT5CRES")
        self.FLT5CNT = BitField(self, 0x0000003C, "FLT5CNT", "FLT5CNT")
        self.FLT5BLKS = BitField(self, 0x00000002, "FLT5BLKS", "FLT5BLKS")
        self.FLT5BLKE = BitField(self, 0x00000001, "FLT5BLKE", "FLT5BLKE")
        self.FLTBLKS = Subscriptor(self, "FLT{}BLKS")
        self.FLTBLKE = Subscriptor(self, "FLT{}BLKE")
        self.FLTCNT = Subscriptor(self, "FLT{}CNT")
        self.FLTCRES = Subscriptor(self, "FLT{}CRES")
        self.FLTRSTM = Subscriptor(self, "FLT{}RSTM")

class SA_HRTIM_Common(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "High Resolution Timer: Common functions")
        self.CR1 = SA_HRTIM_Common_CR1(self, 0x0)
        self.CR2 = SA_HRTIM_Common_CR2(self, 0x4)
        self.ISR = SA_HRTIM_Common_ISR(self, 0x8)
        self.ICR = SA_HRTIM_Common_ICR(self, 0xC)
        self.IER = SA_HRTIM_Common_IER(self, 0x10)
        self.OENR = SA_HRTIM_Common_OENR(self, 0x14)
        self.ODISR = SA_HRTIM_Common_ODISR(self, 0x18)
        self.ODSR = SA_HRTIM_Common_ODSR(self, 0x1C)
        self.BMCR = SA_HRTIM_Common_BMCR(self, 0x20)
        self.BMTRG = SA_HRTIM_Common_BMTRG(self, 0x24)
        self.BMCMPR = SA_HRTIM_Common_BMCMPR(self, 0x28)
        self.BMPER = SA_HRTIM_Common_BMPER(self, 0x2C)
        self.EECR1 = SA_HRTIM_Common_EECR1(self, 0x30)
        self.EECR2 = SA_HRTIM_Common_EECR2(self, 0x34)
        self.EECR3 = SA_HRTIM_Common_EECR3(self, 0x38)
        self.ADC1R = SA_HRTIM_Common_ADC1R(self, 0x3C)
        self.ADC2R = SA_HRTIM_Common_ADC2R(self, 0x40)
        self.ADC3R = SA_HRTIM_Common_ADC3R(self, 0x44)
        self.ADC4R = SA_HRTIM_Common_ADC4R(self, 0x48)
        self.DLLCR = SA_HRTIM_Common_DLLCR(self, 0x4C)
        self.FLTINR1 = SA_HRTIM_Common_FLTINR1(self, 0x50)
        self.FLTINR2 = SA_HRTIM_Common_FLTINR2(self, 0x54)
        self.BDMUPDR = SA_HRTIM_Common_BDMUPDR(self, 0x58)
        self.BDTAUPR = SA_HRTIM_Common_BDTAUPR(self, 0x5C)
        self.BDTBUPR = SA_HRTIM_Common_BDTBUPR(self, 0x60)
        self.BDTCUPR = SA_HRTIM_Common_BDTCUPR(self, 0x64)
        self.BDTDUPR = SA_HRTIM_Common_BDTDUPR(self, 0x68)
        self.BDTEUPR = SA_HRTIM_Common_BDTEUPR(self, 0x6C)
        self.BDTFUPR = SA_HRTIM_Common_BDTFUPR(self, 0x74)
        self.BDMADR = SA_HRTIM_Common_BDMADR(self, 0x70)
        self.ADCER = SA_HRTIM_Common_ADCER(self, 0x78)
        self.ADCUR = SA_HRTIM_Common_ADCUR(self, 0x7C)
        self.ADCPS1 = SA_HRTIM_Common_ADCPS1(self, 0x80)
        self.ADCPS2 = SA_HRTIM_Common_ADCPS2(self, 0x84)
        self.FLTINR3 = SA_HRTIM_Common_FLTINR3(self, 0x88)
        self.FLTINR4 = SA_HRTIM_Common_FLTINR4(self, 0x8C)
        self.ADCR = Subscriptor(self, "ADC{}R")
        self.FLTINR = Subscriptor(self, "FLTINR{}")
        self.EECR = Subscriptor(self, "EECR{}")
        self.ADCPS = Subscriptor(self, "ADCPS{}")

HRTIM_Common = SA_HRTIM_Common(0x40016B80, "HRTIM_Common")

class SA_QUADSPI_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "control register")
        self.PRESCALER = BitField(self, 0xFF000000, "PRESCALER", "Clock prescaler")
        self.PMM = BitField(self, 0x00800000, "PMM", "Polling match mode")
        self.APMS = BitField(self, 0x00400000, "APMS", "Automatic poll mode stop")
        self.TOIE = BitField(self, 0x00100000, "TOIE", "TimeOut interrupt enable")
        self.SMIE = BitField(self, 0x00080000, "SMIE", "Status match interrupt enable")
        self.FTIE = BitField(self, 0x00040000, "FTIE", "FIFO threshold interrupt enable")
        self.TCIE = BitField(self, 0x00020000, "TCIE", "Transfer complete interrupt enable")
        self.TEIE = BitField(self, 0x00010000, "TEIE", "Transfer error interrupt enable")
        self.FTHRES = BitField(self, 0x00001F00, "FTHRES", "IFO threshold level")
        self.FSEL = BitField(self, 0x00000080, "FSEL", "FSEL")
        self.DFM = BitField(self, 0x00000040, "DFM", "DFM")
        self.SSHIFT = BitField(self, 0x00000010, "SSHIFT", "Sample shift")
        self.TCEN = BitField(self, 0x00000008, "TCEN", "Timeout counter enable")
        self.DMAEN = BitField(self, 0x00000004, "DMAEN", "DMA enable")
        self.ABORT = BitField(self, 0x00000002, "ABORT", "Abort request")
        self.EN = BitField(self, 0x00000001, "EN", "Enable")

class SA_QUADSPI_DCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DCR", "device configuration register")
        self.FSIZE = BitField(self, 0x001F0000, "FSIZE", "FLASH memory size")
        self.CSHT = BitField(self, 0x00000700, "CSHT", "Chip select high time")
        self.CKMODE = BitField(self, 0x00000001, "CKMODE", "Mode 0 / mode 3")

class SA_QUADSPI_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "status register")
        self.FLEVEL = BitField(self, 0x00001F00, "FLEVEL", "FIFO level")
        self.BUSY = BitField(self, 0x00000020, "BUSY", "Busy")
        self.TOF = BitField(self, 0x00000010, "TOF", "Timeout flag")
        self.SMF = BitField(self, 0x00000008, "SMF", "Status match flag")
        self.FTF = BitField(self, 0x00000004, "FTF", "FIFO threshold flag")
        self.TCF = BitField(self, 0x00000002, "TCF", "Transfer complete flag")
        self.TEF = BitField(self, 0x00000001, "TEF", "Transfer error flag")

class SA_QUADSPI_FCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FCR", "flag clear register")
        self.CTOF = BitField(self, 0x00000010, "CTOF", "Clear timeout flag")
        self.CSMF = BitField(self, 0x00000008, "CSMF", "Clear status match flag")
        self.CTCF = BitField(self, 0x00000002, "CTCF", "Clear transfer complete flag")
        self.CTEF = BitField(self, 0x00000001, "CTEF", "Clear transfer error flag")

class SA_QUADSPI_DLR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DLR", "data length register")
        self.DL = BitField(self, 0xFFFFFFFF, "DL", "Data length")

class SA_QUADSPI_CCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR", "communication configuration register")
        self.DDRM = BitField(self, 0x80000000, "DDRM", "Double data rate mode")
        self.SIOO = BitField(self, 0x10000000, "SIOO", "Send instruction only once mode")
        self.FMODE = BitField(self, 0x0C000000, "FMODE", "Functional mode")
        self.DMODE = BitField(self, 0x03000000, "DMODE", "Data mode")
        self.DCYC = BitField(self, 0x007C0000, "DCYC", "Number of dummy cycles")
        self.ABSIZE = BitField(self, 0x00030000, "ABSIZE", "Alternate bytes size")
        self.ABMODE = BitField(self, 0x0000C000, "ABMODE", "Alternate bytes mode")
        self.ADSIZE = BitField(self, 0x00003000, "ADSIZE", "Address size")
        self.ADMODE = BitField(self, 0x00000C00, "ADMODE", "Address mode")
        self.IMODE = BitField(self, 0x00000300, "IMODE", "Instruction mode")
        self.INSTRUCTION = BitField(self, 0x000000FF, "INSTRUCTION", "Instruction")

class SA_QUADSPI_AR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AR", "address register")
        self.ADDRESS = BitField(self, 0xFFFFFFFF, "ADDRESS", "Address")

class SA_QUADSPI_ABR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ABR", "ABR")
        self.ALTERNATE = BitField(self, 0xFFFFFFFF, "ALTERNATE", "ALTERNATE")

class SA_QUADSPI_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DR", "data register")
        self.DATA = BitField(self, 0xFFFFFFFF, "DATA", "Data")

class SA_QUADSPI_PSMKR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PSMKR", "polling status mask register")
        self.MASK = BitField(self, 0xFFFFFFFF, "MASK", "Status mask")

class SA_QUADSPI_PSMAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PSMAR", "polling status match register")
        self.MATCH = BitField(self, 0xFFFFFFFF, "MATCH", "Status match")

class SA_QUADSPI_PIR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PIR", "polling interval register")
        self.INTERVAL = BitField(self, 0x0000FFFF, "INTERVAL", "Polling interval")

class SA_QUADSPI_LPTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "LPTR", "low-power timeout register")
        self.TIMEOUT = BitField(self, 0x0000FFFF, "TIMEOUT", "Timeout period")

class SA_QUADSPI(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "QuadSPI interface")
        self.CR = SA_QUADSPI_CR(self, 0x0)
        self.DCR = SA_QUADSPI_DCR(self, 0x4)
        self.SR = SA_QUADSPI_SR(self, 0x8)
        self.FCR = SA_QUADSPI_FCR(self, 0xC)
        self.DLR = SA_QUADSPI_DLR(self, 0x10)
        self.CCR = SA_QUADSPI_CCR(self, 0x14)
        self.AR = SA_QUADSPI_AR(self, 0x18)
        self.ABR = SA_QUADSPI_ABR(self, 0x1C)
        self.DR = SA_QUADSPI_DR(self, 0x20)
        self.PSMKR = SA_QUADSPI_PSMKR(self, 0x24)
        self.PSMAR = SA_QUADSPI_PSMAR(self, 0x28)
        self.PIR = SA_QUADSPI_PIR(self, 0x2C)
        self.LPTR = SA_QUADSPI_LPTR(self, 0x30)

QUADSPI = SA_QUADSPI(0xA0001000, "QUADSPI")

class SA_DAC1_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "DAC control register")
        self.EN1 = BitField(self, 0x00000001, "EN1", "DAC channel1 enable This bit is set and cleared by software to enable/disable DAC channel1.")
        self.TEN1 = BitField(self, 0x00000002, "TEN1", "DAC channel1 trigger enable")
        self.TSEL1 = BitField(self, 0x0000003C, "TSEL1", "DAC channel1 trigger selection These bits select the external event used to trigger DAC channel1. Note: Only used if bit TEN1 = 1 (DAC channel1 trigger enabled).")
        self.WAVE1 = BitField(self, 0x000000C0, "WAVE1", "DAC channel1 noise/triangle wave generation enable These bits are set and cleared by software. Note: Only used if bit TEN1 = 1 (DAC channel1 trigger enabled).")
        self.MAMP1 = BitField(self, 0x00000F00, "MAMP1", "DAC channel1 mask/amplitude selector These bits are written by software to select mask in wave generation mode or amplitude in triangle generation mode. = 1011: Unmask bits[11:0] of LFSR/ triangle amplitude equal to 4095")
        self.DMAEN1 = BitField(self, 0x00001000, "DMAEN1", "DAC channel1 DMA enable This bit is set and cleared by software.")
        self.DMAUDRIE1 = BitField(self, 0x00002000, "DMAUDRIE1", "DAC channel1 DMA Underrun Interrupt enable This bit is set and cleared by software.")
        self.CEN1 = BitField(self, 0x00004000, "CEN1", "DAC Channel 1 calibration enable This bit is set and cleared by software to enable/disable DAC channel 1 calibration, it can be written only if bit EN1=0 into DAC_CR (the calibration mode can be entered/exit only when the DAC channel is disabled) Otherwise, the write operation is ignored.")
        self.EN2 = BitField(self, 0x00010000, "EN2", "DAC channel2 enable This bit is set and cleared by software to enable/disable DAC channel2.")
        self.TEN2 = BitField(self, 0x00020000, "TEN2", "DAC channel2 trigger enable")
        self.TSEL2 = BitField(self, 0x003C0000, "TSEL2", "DAC channel2 trigger selection These bits select the external event used to trigger DAC channel2 Note: Only used if bit TEN2 = 1 (DAC channel2 trigger enabled).")
        self.WAVE2 = BitField(self, 0x00C00000, "WAVE2", "DAC channel2 noise/triangle wave generation enable These bits are set/reset by software. 1x: Triangle wave generation enabled Note: Only used if bit TEN2 = 1 (DAC channel2 trigger enabled)")
        self.MAMP2 = BitField(self, 0x0F000000, "MAMP2", "DAC channel2 mask/amplitude selector These bits are written by software to select mask in wave generation mode or amplitude in triangle generation mode. = 1011: Unmask bits[11:0] of LFSR/ triangle amplitude equal to 4095")
        self.DMAEN2 = BitField(self, 0x10000000, "DMAEN2", "DAC channel2 DMA enable This bit is set and cleared by software.")
        self.DMAUDRIE2 = BitField(self, 0x20000000, "DMAUDRIE2", "DAC channel2 DMA underrun interrupt enable This bit is set and cleared by software.")
        self.CEN2 = BitField(self, 0x40000000, "CEN2", "DAC Channel 2 calibration enable This bit is set and cleared by software to enable/disable DAC channel 2 calibration, it can be written only if bit EN2=0 into DAC_CR (the calibration mode can be entered/exit only when the DAC channel is disabled) Otherwise, the write operation is ignored.")
        self.DMAEN = Subscriptor(self, "DMAEN{}")
        self.TSEL = Subscriptor(self, "TSEL{}")
        self.MAMP = Subscriptor(self, "MAMP{}")
        self.DMAUDRIE = Subscriptor(self, "DMAUDRIE{}")
        self.TEN = Subscriptor(self, "TEN{}")
        self.WAVE = Subscriptor(self, "WAVE{}")
        self.EN = Subscriptor(self, "EN{}")
        self.CEN = Subscriptor(self, "CEN{}")

class SA_DAC1_SWTRGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SWTRGR", "DAC software trigger register")
        self.SWTRIG1 = BitField(self, 0x00000001, "SWTRIG1", "DAC channel1 software trigger This bit is set by software to trigger the DAC in software trigger mode. Note: This bit is cleared by hardware (one APB1 clock cycle later) once the DAC_DHR1 register value has been loaded into the DAC_DOR1 register.")
        self.SWTRIG2 = BitField(self, 0x00000002, "SWTRIG2", "DAC channel2 software trigger This bit is set by software to trigger the DAC in software trigger mode. Note: This bit is cleared by hardware (one APB1 clock cycle later) once the DAC_DHR2 register value has been loaded into the DAC_DOR2 register.")
        self.SWTRIGB1 = BitField(self, 0x00010000, "SWTRIGB1", "DAC channel1 software trigger B")
        self.SWTRIGB2 = BitField(self, 0x00020000, "SWTRIGB2", "DAC channel2 software trigger B")
        self.SWTRIG = Subscriptor(self, "SWTRIG{}")
        self.SWTRIGB = Subscriptor(self, "SWTRIGB{}")

class SA_DAC1_DHR12R1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR12R1", "DAC channel1 12-bit right-aligned data holding register")
        self.DACC1DHR = BitField(self, 0x00000FFF, "DACC1DHR", "DAC channel1 12-bit right-aligned data These bits are written by software which specifies 12-bit data for DAC channel1.")
        self.DACC1DHRB = BitField(self, 0x0FFF0000, "DACC1DHRB", "DAC channel1 12-bit right-aligned data B")

class SA_DAC1_DHR12L1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR12L1", "DAC channel1 12-bit left aligned data holding register")
        self.DACC1DHR = BitField(self, 0x0000FFF0, "DACC1DHR", "DAC channel1 12-bit left-aligned data These bits are written by software which specifies 12-bit data for DAC channel1.")
        self.DACC1DHRB = BitField(self, 0xFFF00000, "DACC1DHRB", "DAC channel1 12-bit left-aligned data B")

class SA_DAC1_DHR8R1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR8R1", "DAC channel1 8-bit right aligned data holding register")
        self.DACC1DHR = BitField(self, 0x000000FF, "DACC1DHR", "DAC channel1 8-bit right-aligned data These bits are written by software which specifies 8-bit data for DAC channel1.")
        self.DACC1DHRB = BitField(self, 0x0000FF00, "DACC1DHRB", "DAC channel1 8-bit right-aligned data")

class SA_DAC1_DHR12R2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR12R2", "DAC channel2 12-bit right aligned data holding register")
        self.DACC2DHR = BitField(self, 0x00000FFF, "DACC2DHR", "DAC channel2 12-bit right-aligned data These bits are written by software which specifies 12-bit data for DAC channel2.")
        self.DACC2DHRB = BitField(self, 0x0FFF0000, "DACC2DHRB", "DAC channel2 12-bit right-aligned data")

class SA_DAC1_DHR12L2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR12L2", "DAC channel2 12-bit left aligned data holding register")
        self.DACC2DHR = BitField(self, 0x0000FFF0, "DACC2DHR", "DAC channel2 12-bit left-aligned data These bits are written by software which specify 12-bit data for DAC channel2.")
        self.DACC2DHRB = BitField(self, 0xFFF00000, "DACC2DHRB", "DAC channel2 12-bit left-aligned data B")

class SA_DAC1_DHR8R2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR8R2", "DAC channel2 8-bit right-aligned data holding register")
        self.DACC2DHR = BitField(self, 0x000000FF, "DACC2DHR", "DAC channel2 8-bit right-aligned data These bits are written by software which specifies 8-bit data for DAC channel2.")
        self.DACC2DHRB = BitField(self, 0x0000FF00, "DACC2DHRB", "DAC channel2 8-bit right-aligned data")

class SA_DAC1_DHR12RD(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR12RD", "Dual DAC 12-bit right-aligned data holding register")
        self.DACC1DHR = BitField(self, 0x00000FFF, "DACC1DHR", "DAC channel1 12-bit right-aligned data These bits are written by software which specifies 12-bit data for DAC channel1.")
        self.DACC2DHR = BitField(self, 0x0FFF0000, "DACC2DHR", "DAC channel2 12-bit right-aligned data These bits are written by software which specifies 12-bit data for DAC channel2.")
        self.DACCDHR = Subscriptor(self, "DACC{}DHR")

class SA_DAC1_DHR12LD(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR12LD", "DUAL DAC 12-bit left aligned data holding register")
        self.DACC1DHR = BitField(self, 0x0000FFF0, "DACC1DHR", "DAC channel1 12-bit left-aligned data These bits are written by software which specifies 12-bit data for DAC channel1.")
        self.DACC2DHR = BitField(self, 0xFFF00000, "DACC2DHR", "DAC channel2 12-bit left-aligned data These bits are written by software which specifies 12-bit data for DAC channel2.")
        self.DACCDHR = Subscriptor(self, "DACC{}DHR")

class SA_DAC1_DHR8RD(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DHR8RD", "DUAL DAC 8-bit right aligned data holding register")
        self.DACC1DHR = BitField(self, 0x000000FF, "DACC1DHR", "DAC channel1 8-bit right-aligned data These bits are written by software which specifies 8-bit data for DAC channel1.")
        self.DACC2DHR = BitField(self, 0x0000FF00, "DACC2DHR", "DAC channel2 8-bit right-aligned data These bits are written by software which specifies 8-bit data for DAC channel2.")
        self.DACCDHR = Subscriptor(self, "DACC{}DHR")

class SA_DAC1_DOR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DOR1", "DAC channel1 data output register")
        self.DACC1DOR = BitField(self, 0x00000FFF, "DACC1DOR", "DAC channel1 data output These bits are read-only, they contain data output for DAC channel1.")
        self.DACC1DORB = BitField(self, 0x0FFF0000, "DACC1DORB", "DAC channel1 data output")

class SA_DAC1_DOR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DOR2", "DAC channel2 data output register")
        self.DACC2DOR = BitField(self, 0x00000FFF, "DACC2DOR", "DAC channel2 data output These bits are read-only, they contain data output for DAC channel2.")
        self.DACC2DORB = BitField(self, 0x0FFF0000, "DACC2DORB", "DAC channel2 data output")

class SA_DAC1_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "DAC status register")
        self.DAC1RDY = BitField(self, 0x00000800, "DAC1RDY", "DAC channel1 ready status bit")
        self.DORSTAT1 = BitField(self, 0x00001000, "DORSTAT1", "DAC channel1 output register status bit")
        self.DMAUDR1 = BitField(self, 0x00002000, "DMAUDR1", "DAC channel1 DMA underrun flag This bit is set by hardware and cleared by software (by writing it to 1).")
        self.CAL_FLAG1 = BitField(self, 0x00004000, "CAL_FLAG1", "DAC Channel 1 calibration offset status This bit is set and cleared by hardware")
        self.BWST1 = BitField(self, 0x00008000, "BWST1", "DAC Channel 1 busy writing sample time flag This bit is systematically set just after Sample & Hold mode enable and is set each time the software writes the register DAC_SHSR1, It is cleared by hardware when the write operation of DAC_SHSR1 is complete. (It takes about 3LSI periods of synchronization).")
        self.DAC2RDY = BitField(self, 0x08000000, "DAC2RDY", "DAC channel 2 ready status bit")
        self.DORSTAT2 = BitField(self, 0x10000000, "DORSTAT2", "DAC channel 2 output register status bit")
        self.DMAUDR2 = BitField(self, 0x20000000, "DMAUDR2", "DAC channel2 DMA underrun flag This bit is set by hardware and cleared by software (by writing it to 1).")
        self.CAL_FLAG2 = BitField(self, 0x40000000, "CAL_FLAG2", "DAC Channel 2 calibration offset status This bit is set and cleared by hardware")
        self.BWST2 = BitField(self, 0x80000000, "BWST2", "DAC Channel 2 busy writing sample time flag This bit is systematically set just after Sample & Hold mode enable and is set each time the software writes the register DAC_SHSR2, It is cleared by hardware when the write operation of DAC_SHSR2 is complete. (It takes about 3 LSI periods of synchronization).")
        self.DORSTAT = Subscriptor(self, "DORSTAT{}")
        self.CAL_FLAG = Subscriptor(self, "CAL_FLAG{}")
        self.BWST = Subscriptor(self, "BWST{}")
        self.DACRDY = Subscriptor(self, "DAC{}RDY")
        self.DMAUDR = Subscriptor(self, "DMAUDR{}")

class SA_DAC1_CCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR", "DAC calibration control register")
        self.OTRIM1 = BitField(self, 0x0000001F, "OTRIM1", "DAC Channel 1 offset trimming value")
        self.OTRIM2 = BitField(self, 0x001F0000, "OTRIM2", "DAC Channel 2 offset trimming value")
        self.OTRIM = Subscriptor(self, "OTRIM{}")

class SA_DAC1_MCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MCR", "DAC mode control register")
        self.MODE1 = BitField(self, 0x00000007, "MODE1", "DAC Channel 1 mode These bits can be written only when the DAC is disabled and not in the calibration mode (when bit EN1=0 and bit CEN1 =0 in the DAC_CR register). If EN1=1 or CEN1 =1 the write operation is ignored. They can be set and cleared by software to select the DAC Channel 1 mode: DAC Channel 1 in normal Mode DAC Channel 1 in sample &amp; hold mode")
        self.DMADOUBLE1 = BitField(self, 0x00000100, "DMADOUBLE1", "DAC Channel1 DMA double data mode")
        self.SINFORMAT1 = BitField(self, 0x00000200, "SINFORMAT1", "Enable signed format for DAC channel1")
        self.HFSEL = BitField(self, 0x0000C000, "HFSEL", "High frequency interface mode selection")
        self.MODE2 = BitField(self, 0x00070000, "MODE2", "DAC Channel 2 mode These bits can be written only when the DAC is disabled and not in the calibration mode (when bit EN2=0 and bit CEN2 =0 in the DAC_CR register). If EN2=1 or CEN2 =1 the write operation is ignored. They can be set and cleared by software to select the DAC Channel 2 mode: DAC Channel 2 in normal Mode DAC Channel 2 in sample &amp; hold mode")
        self.DMADOUBLE2 = BitField(self, 0x01000000, "DMADOUBLE2", "DAC Channel2 DMA double data mode")
        self.SINFORMAT2 = BitField(self, 0x02000000, "SINFORMAT2", "Enable signed format for DAC channel2")
        self.MODE = Subscriptor(self, "MODE{}")
        self.DMADOUBLE = Subscriptor(self, "DMADOUBLE{}")
        self.SINFORMAT = Subscriptor(self, "SINFORMAT{}")

class SA_DAC1_SHSR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SHSR1", "DAC Sample and Hold sample time register 1")
        self.TSAMPLE1 = BitField(self, 0x000003FF, "TSAMPLE1", "DAC Channel 1 sample Time (only valid in sample &amp; hold mode) These bits can be written when the DAC channel1 is disabled or also during normal operation. in the latter case, the write can be done only when BWSTx of DAC_SR register is low, If BWSTx=1, the write operation is ignored.")

class SA_DAC1_SHSR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SHSR2", "DAC Sample and Hold sample time register 2")
        self.TSAMPLE2 = BitField(self, 0x000003FF, "TSAMPLE2", "DAC Channel 2 sample Time (only valid in sample &amp; hold mode) These bits can be written when the DAC channel2 is disabled or also during normal operation. in the latter case, the write can be done only when BWSTx of DAC_SR register is low, if BWSTx=1, the write operation is ignored.")

class SA_DAC1_SHHR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x10001, "SHHR", "DAC Sample and Hold hold time register")
        self.THOLD1 = BitField(self, 0x000003FF, "THOLD1", "DAC Channel 1 hold Time (only valid in sample &amp; hold mode) Hold time= (THOLD[9:0]) x T LSI")
        self.THOLD2 = BitField(self, 0x03FF0000, "THOLD2", "DAC Channel 2 hold time (only valid in sample &amp; hold mode). Hold time= (THOLD[9:0]) x T LSI")
        self.THOLD = Subscriptor(self, "THOLD{}")

class SA_DAC1_SHRR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x10001, "SHRR", "DAC Sample and Hold refresh time register")
        self.TREFRESH1 = BitField(self, 0x000000FF, "TREFRESH1", "DAC Channel 1 refresh Time (only valid in sample &amp; hold mode) Refresh time= (TREFRESH[7:0]) x T LSI")
        self.TREFRESH2 = BitField(self, 0x00FF0000, "TREFRESH2", "DAC Channel 2 refresh Time (only valid in sample &amp; hold mode) Refresh time= (TREFRESH[7:0]) x T LSI")
        self.TREFRESH = Subscriptor(self, "TREFRESH{}")

class SA_DAC1_STR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "STR1", "Sawtooth register")
        self.STRSTDATA1 = BitField(self, 0x00000FFF, "STRSTDATA1", "DAC Channel 1 Sawtooth reset value")
        self.STDIR1 = BitField(self, 0x00001000, "STDIR1", "DAC Channel1 Sawtooth direction setting")
        self.STINCDATA1 = BitField(self, 0xFFFF0000, "STINCDATA1", "DAC CH1 Sawtooth increment value (12.4 bit format)")

class SA_DAC1_STR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "STR2", "Sawtooth register")
        self.STRSTDATA2 = BitField(self, 0x00000FFF, "STRSTDATA2", "DAC Channel 2 Sawtooth reset value")
        self.STDIR2 = BitField(self, 0x00001000, "STDIR2", "DAC Channel2 Sawtooth direction setting")
        self.STINCDATA2 = BitField(self, 0xFFFF0000, "STINCDATA2", "DAC CH2 Sawtooth increment value (12.4 bit format)")

class SA_DAC1_STMODR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "STMODR", "Sawtooth Mode register")
        self.STRSTTRIGSEL1 = BitField(self, 0x0000000F, "STRSTTRIGSEL1", "DAC Channel 1 Sawtooth Reset trigger selection")
        self.STINCTRIGSEL1 = BitField(self, 0x00000F00, "STINCTRIGSEL1", "DAC Channel 1 Sawtooth Increment trigger selection")
        self.STRSTTRIGSEL2 = BitField(self, 0x000F0000, "STRSTTRIGSEL2", "DAC Channel 1 Sawtooth Reset trigger selection")
        self.STINCTRIGSEL2 = BitField(self, 0x0F000000, "STINCTRIGSEL2", "DAC Channel 2 Sawtooth Increment trigger selection")
        self.STRSTTRIGSEL = Subscriptor(self, "STRSTTRIGSEL{}")
        self.STINCTRIGSEL = Subscriptor(self, "STINCTRIGSEL{}")

class SA_DAC1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Digital-to-analog converter")
        self.CR = SA_DAC1_CR(self, 0x0)
        self.SWTRGR = SA_DAC1_SWTRGR(self, 0x4)
        self.DHR12R1 = SA_DAC1_DHR12R1(self, 0x8)
        self.DHR12L1 = SA_DAC1_DHR12L1(self, 0xC)
        self.DHR8R1 = SA_DAC1_DHR8R1(self, 0x10)
        self.DHR12R2 = SA_DAC1_DHR12R2(self, 0x14)
        self.DHR12L2 = SA_DAC1_DHR12L2(self, 0x18)
        self.DHR8R2 = SA_DAC1_DHR8R2(self, 0x1C)
        self.DHR12RD = SA_DAC1_DHR12RD(self, 0x20)
        self.DHR12LD = SA_DAC1_DHR12LD(self, 0x24)
        self.DHR8RD = SA_DAC1_DHR8RD(self, 0x28)
        self.DOR1 = SA_DAC1_DOR1(self, 0x2C)
        self.DOR2 = SA_DAC1_DOR2(self, 0x30)
        self.SR = SA_DAC1_SR(self, 0x34)
        self.CCR = SA_DAC1_CCR(self, 0x38)
        self.MCR = SA_DAC1_MCR(self, 0x3C)
        self.SHSR1 = SA_DAC1_SHSR1(self, 0x40)
        self.SHSR2 = SA_DAC1_SHSR2(self, 0x44)
        self.SHHR = SA_DAC1_SHHR(self, 0x48)
        self.SHRR = SA_DAC1_SHRR(self, 0x4C)
        self.STR1 = SA_DAC1_STR1(self, 0x58)
        self.STR2 = SA_DAC1_STR2(self, 0x5C)
        self.STMODR = SA_DAC1_STMODR(self, 0x60)
        self.DHR12L = Subscriptor(self, "DHR12L{}")
        self.DHR12R = Subscriptor(self, "DHR12R{}")
        self.SHSR = Subscriptor(self, "SHSR{}")
        self.STR = Subscriptor(self, "STR{}")
        self.DOR = Subscriptor(self, "DOR{}")
        self.DHR8R = Subscriptor(self, "DHR8R{}")

DAC1 = SA_DAC1(0x50000800, "DAC1")
DAC2 = SA_DAC1(0x50000C00, "DAC2")
DAC3 = SA_DAC1(0x50001000, "DAC3")
DAC4 = SA_DAC1(0x50001400, "DAC4")

class SA_ADC1_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISR", "interrupt and status register")
        self.JQOVF = BitField(self, 0x00000400, "JQOVF", "JQOVF")
        self.AWD3 = BitField(self, 0x00000200, "AWD3", "AWD3")
        self.AWD2 = BitField(self, 0x00000100, "AWD2", "AWD2")
        self.AWD1 = BitField(self, 0x00000080, "AWD1", "AWD1")
        self.JEOS = BitField(self, 0x00000040, "JEOS", "JEOS")
        self.JEOC = BitField(self, 0x00000020, "JEOC", "JEOC")
        self.OVR = BitField(self, 0x00000010, "OVR", "OVR")
        self.EOS = BitField(self, 0x00000008, "EOS", "EOS")
        self.EOC = BitField(self, 0x00000004, "EOC", "EOC")
        self.EOSMP = BitField(self, 0x00000002, "EOSMP", "EOSMP")
        self.ADRDY = BitField(self, 0x00000001, "ADRDY", "ADRDY")
        self.AWD = Subscriptor(self, "AWD{}")

class SA_ADC1_IER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IER", "interrupt enable register")
        self.JQOVFIE = BitField(self, 0x00000400, "JQOVFIE", "JQOVFIE")
        self.AWD3IE = BitField(self, 0x00000200, "AWD3IE", "AWD3IE")
        self.AWD2IE = BitField(self, 0x00000100, "AWD2IE", "AWD2IE")
        self.AWD1IE = BitField(self, 0x00000080, "AWD1IE", "AWD1IE")
        self.JEOSIE = BitField(self, 0x00000040, "JEOSIE", "JEOSIE")
        self.JEOCIE = BitField(self, 0x00000020, "JEOCIE", "JEOCIE")
        self.OVRIE = BitField(self, 0x00000010, "OVRIE", "OVRIE")
        self.EOSIE = BitField(self, 0x00000008, "EOSIE", "EOSIE")
        self.EOCIE = BitField(self, 0x00000004, "EOCIE", "EOCIE")
        self.EOSMPIE = BitField(self, 0x00000002, "EOSMPIE", "EOSMPIE")
        self.ADRDYIE = BitField(self, 0x00000001, "ADRDYIE", "ADRDYIE")
        self.AWDIE = Subscriptor(self, "AWD{}IE")

class SA_ADC1_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x20000000, "CR", "control register")
        self.ADCAL = BitField(self, 0x80000000, "ADCAL", "ADCAL")
        self.ADCALDIF = BitField(self, 0x40000000, "ADCALDIF", "ADCALDIF")
        self.DEEPPWD = BitField(self, 0x20000000, "DEEPPWD", "DEEPPWD")
        self.ADVREGEN = BitField(self, 0x10000000, "ADVREGEN", "ADVREGEN")
        self.JADSTP = BitField(self, 0x00000020, "JADSTP", "JADSTP")
        self.ADSTP = BitField(self, 0x00000010, "ADSTP", "ADSTP")
        self.JADSTART = BitField(self, 0x00000008, "JADSTART", "JADSTART")
        self.ADSTART = BitField(self, 0x00000004, "ADSTART", "ADSTART")
        self.ADDIS = BitField(self, 0x00000002, "ADDIS", "ADDIS")
        self.ADEN = BitField(self, 0x00000001, "ADEN", "ADEN")

class SA_ADC1_CFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x80000000, "CFGR", "configuration register")
        self.JQDIS = BitField(self, 0x80000000, "JQDIS", "Injected Queue disable")
        self.AWD1CH = BitField(self, 0x7C000000, "AWD1CH", "Analog watchdog 1 channel selection")
        self.JAUTO = BitField(self, 0x02000000, "JAUTO", "JAUTO")
        self.JAWD1EN = BitField(self, 0x01000000, "JAWD1EN", "JAWD1EN")
        self.AWD1EN = BitField(self, 0x00800000, "AWD1EN", "AWD1EN")
        self.AWD1SGL = BitField(self, 0x00400000, "AWD1SGL", "AWD1SGL")
        self.JQM = BitField(self, 0x00200000, "JQM", "JQM")
        self.JDISCEN = BitField(self, 0x00100000, "JDISCEN", "JDISCEN")
        self.DISCNUM = BitField(self, 0x000E0000, "DISCNUM", "DISCNUM")
        self.DISCEN = BitField(self, 0x00010000, "DISCEN", "DISCEN")
        self.ALIGN = BitField(self, 0x00008000, "ALIGN", "ALIGN")
        self.AUTDLY = BitField(self, 0x00004000, "AUTDLY", "AUTDLY")
        self.CONT = BitField(self, 0x00002000, "CONT", "CONT")
        self.OVRMOD = BitField(self, 0x00001000, "OVRMOD", "OVRMOD")
        self.EXTEN = BitField(self, 0x00000C00, "EXTEN", "EXTEN")
        self.EXTSEL = BitField(self, 0x000003E0, "EXTSEL", "External trigger selection for regular group")
        self.RES = BitField(self, 0x00000018, "RES", "RES")
        self.DMACFG = BitField(self, 0x00000002, "DMACFG", "DMACFG")
        self.DMAEN = BitField(self, 0x00000001, "DMAEN", "DMAEN")

class SA_ADC1_CFGR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CFGR2", "configuration register")
        self.SMPTRIG = BitField(self, 0x08000000, "SMPTRIG", "SMPTRIG")
        self.BULB = BitField(self, 0x04000000, "BULB", "BULB")
        self.SWTRIG = BitField(self, 0x02000000, "SWTRIG", "SWTRIG")
        self.GCOMP = BitField(self, 0x00010000, "GCOMP", "GCOMP")
        self.ROVSM = BitField(self, 0x00000400, "ROVSM", "EXTEN")
        self.TROVS = BitField(self, 0x00000200, "TROVS", "Triggered Regular Oversampling")
        self.OVSS = BitField(self, 0x000001E0, "OVSS", "ALIGN")
        self.OVSR = BitField(self, 0x0000001C, "OVSR", "RES")
        self.JOVSE = BitField(self, 0x00000002, "JOVSE", "DMACFG")
        self.ROVSE = BitField(self, 0x00000001, "ROVSE", "DMAEN")

class SA_ADC1_SMPR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SMPR1", "sample time register 1")
        self.SMP9 = BitField(self, 0x38000000, "SMP9", "SMP9")
        self.SMP8 = BitField(self, 0x07000000, "SMP8", "SMP8")
        self.SMP7 = BitField(self, 0x00E00000, "SMP7", "SMP7")
        self.SMP6 = BitField(self, 0x001C0000, "SMP6", "SMP6")
        self.SMP5 = BitField(self, 0x00038000, "SMP5", "SMP5")
        self.SMP4 = BitField(self, 0x00007000, "SMP4", "SMP4")
        self.SMP3 = BitField(self, 0x00000E00, "SMP3", "SMP3")
        self.SMP2 = BitField(self, 0x000001C0, "SMP2", "SMP2")
        self.SMP1 = BitField(self, 0x00000038, "SMP1", "SMP1")
        self.SMPPLUS = BitField(self, 0x80000000, "SMPPLUS", "Addition of one clock cycle to the sampling time")
        self.SMP0 = BitField(self, 0x00000007, "SMP0", "SMP0")
        self.SMP = Subscriptor(self, "SMP{}")

class SA_ADC1_SMPR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SMPR2", "sample time register 2")
        self.SMP18 = BitField(self, 0x07000000, "SMP18", "SMP18")
        self.SMP17 = BitField(self, 0x00E00000, "SMP17", "SMP17")
        self.SMP16 = BitField(self, 0x001C0000, "SMP16", "SMP16")
        self.SMP15 = BitField(self, 0x00038000, "SMP15", "SMP15")
        self.SMP14 = BitField(self, 0x00007000, "SMP14", "SMP14")
        self.SMP13 = BitField(self, 0x00000E00, "SMP13", "SMP13")
        self.SMP12 = BitField(self, 0x000001C0, "SMP12", "SMP12")
        self.SMP11 = BitField(self, 0x00000038, "SMP11", "SMP11")
        self.SMP10 = BitField(self, 0x00000007, "SMP10", "SMP10")
        self.SMP = Subscriptor(self, "SMP{}")

class SA_ADC1_TR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFF0000, "TR1", "watchdog threshold register 1")
        self.HT1 = BitField(self, 0x0FFF0000, "HT1", "HT1")
        self.AWDFILT = BitField(self, 0x00007000, "AWDFILT", "AWDFILT")
        self.LT1 = BitField(self, 0x00000FFF, "LT1", "LT1")

class SA_ADC1_TR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFF0000, "TR2", "watchdog threshold register")
        self.HT2 = BitField(self, 0x00FF0000, "HT2", "HT2")
        self.LT2 = BitField(self, 0x000000FF, "LT2", "LT2")

class SA_ADC1_TR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFF0000, "TR3", "watchdog threshold register 3")
        self.HT3 = BitField(self, 0x00FF0000, "HT3", "HT3")
        self.LT3 = BitField(self, 0x000000FF, "LT3", "LT3")

class SA_ADC1_SQR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR1", "regular sequence register 1")
        self.SQ4 = BitField(self, 0x1F000000, "SQ4", "SQ4")
        self.SQ3 = BitField(self, 0x007C0000, "SQ3", "SQ3")
        self.SQ2 = BitField(self, 0x0001F000, "SQ2", "SQ2")
        self.SQ1 = BitField(self, 0x000007C0, "SQ1", "SQ1")
        self.L = BitField(self, 0x0000000F, "L", "Regular channel sequence length")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC1_SQR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR2", "regular sequence register 2")
        self.SQ9 = BitField(self, 0x1F000000, "SQ9", "SQ9")
        self.SQ8 = BitField(self, 0x007C0000, "SQ8", "SQ8")
        self.SQ7 = BitField(self, 0x0001F000, "SQ7", "SQ7")
        self.SQ6 = BitField(self, 0x000007C0, "SQ6", "SQ6")
        self.SQ5 = BitField(self, 0x0000001F, "SQ5", "SQ5")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC1_SQR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR3", "regular sequence register 3")
        self.SQ14 = BitField(self, 0x1F000000, "SQ14", "SQ14")
        self.SQ13 = BitField(self, 0x007C0000, "SQ13", "SQ13")
        self.SQ12 = BitField(self, 0x0001F000, "SQ12", "SQ12")
        self.SQ11 = BitField(self, 0x000007C0, "SQ11", "SQ11")
        self.SQ10 = BitField(self, 0x0000001F, "SQ10", "SQ10")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC1_SQR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR4", "regular sequence register 4")
        self.SQ16 = BitField(self, 0x000007C0, "SQ16", "SQ16")
        self.SQ15 = BitField(self, 0x0000001F, "SQ15", "SQ15")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC1_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DR", "regular Data Register")
        self.RDATA = BitField(self, 0x0000FFFF, "RDATA", "Regular Data converted")

class SA_ADC1_JSQR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JSQR", "injected sequence register")
        self.JSQ4 = BitField(self, 0xF8000000, "JSQ4", "JSQ4")
        self.JSQ3 = BitField(self, 0x03E00000, "JSQ3", "JSQ3")
        self.JSQ2 = BitField(self, 0x000F8000, "JSQ2", "JSQ2")
        self.JSQ1 = BitField(self, 0x00003E00, "JSQ1", "JSQ1")
        self.JEXTEN = BitField(self, 0x00000180, "JEXTEN", "JEXTEN")
        self.JEXTSEL = BitField(self, 0x0000007C, "JEXTSEL", "JEXTSEL")
        self.JL = BitField(self, 0x00000003, "JL", "JL")
        self.JSQ = Subscriptor(self, "JSQ{}")

class SA_ADC1_OFR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR1", "offset register 1")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC1_OFR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR2", "offset register 2")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC1_OFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR3", "offset register 3")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC1_OFR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR4", "offset register 4")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC1_JDR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR1", "injected data register 1")
        self.JDATA1 = BitField(self, 0x0000FFFF, "JDATA1", "JDATA1")

class SA_ADC1_JDR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR2", "injected data register 2")
        self.JDATA2 = BitField(self, 0x0000FFFF, "JDATA2", "JDATA2")

class SA_ADC1_JDR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR3", "injected data register 3")
        self.JDATA3 = BitField(self, 0x0000FFFF, "JDATA3", "JDATA3")

class SA_ADC1_JDR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR4", "injected data register 4")
        self.JDATA4 = BitField(self, 0x0000FFFF, "JDATA4", "JDATA4")

class SA_ADC1_AWD2CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AWD2CR", "Analog Watchdog 2 Configuration Register")
        self.AWD2CH = BitField(self, 0x0007FFFF, "AWD2CH", "AWD2CH")

class SA_ADC1_AWD3CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AWD3CR", "Analog Watchdog 3 Configuration Register")
        self.AWD3CH = BitField(self, 0x0007FFFF, "AWD3CH", "AWD3CH")

class SA_ADC1_DIFSEL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DIFSEL", "Differential Mode Selection Register 2")
        self.DIFSEL_0 = BitField(self, 0x00000001, "DIFSEL_0", "Differential mode for channels 0")
        self.DIFSEL_1_18 = BitField(self, 0x0007FFFE, "DIFSEL_1_18", "Differential mode for channels 15 to 1")

class SA_ADC1_CALFACT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CALFACT", "Calibration Factors")
        self.CALFACT_D = BitField(self, 0x007F0000, "CALFACT_D", "CALFACT_D")
        self.CALFACT_S = BitField(self, 0x0000007F, "CALFACT_S", "CALFACT_S")

class SA_ADC1_GCOMP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "GCOMP", "Gain compensation Register")
        self.GCOMPCOEFF = BitField(self, 0x00003FFF, "GCOMPCOEFF", "GCOMPCOEFF")

class SA_ADC1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Analog-to-Digital Converter")
        self.ISR = SA_ADC1_ISR(self, 0x0)
        self.IER = SA_ADC1_IER(self, 0x4)
        self.CR = SA_ADC1_CR(self, 0x8)
        self.CFGR = SA_ADC1_CFGR(self, 0xC)
        self.CFGR2 = SA_ADC1_CFGR2(self, 0x10)
        self.SMPR1 = SA_ADC1_SMPR1(self, 0x14)
        self.SMPR2 = SA_ADC1_SMPR2(self, 0x18)
        self.TR1 = SA_ADC1_TR1(self, 0x20)
        self.TR2 = SA_ADC1_TR2(self, 0x24)
        self.TR3 = SA_ADC1_TR3(self, 0x28)
        self.SQR1 = SA_ADC1_SQR1(self, 0x30)
        self.SQR2 = SA_ADC1_SQR2(self, 0x34)
        self.SQR3 = SA_ADC1_SQR3(self, 0x38)
        self.SQR4 = SA_ADC1_SQR4(self, 0x3C)
        self.DR = SA_ADC1_DR(self, 0x40)
        self.JSQR = SA_ADC1_JSQR(self, 0x4C)
        self.OFR1 = SA_ADC1_OFR1(self, 0x60)
        self.OFR2 = SA_ADC1_OFR2(self, 0x64)
        self.OFR3 = SA_ADC1_OFR3(self, 0x68)
        self.OFR4 = SA_ADC1_OFR4(self, 0x6C)
        self.JDR1 = SA_ADC1_JDR1(self, 0x80)
        self.JDR2 = SA_ADC1_JDR2(self, 0x84)
        self.JDR3 = SA_ADC1_JDR3(self, 0x88)
        self.JDR4 = SA_ADC1_JDR4(self, 0x8C)
        self.AWD2CR = SA_ADC1_AWD2CR(self, 0xA0)
        self.AWD3CR = SA_ADC1_AWD3CR(self, 0xA4)
        self.DIFSEL = SA_ADC1_DIFSEL(self, 0xB0)
        self.CALFACT = SA_ADC1_CALFACT(self, 0xB4)
        self.GCOMP = SA_ADC1_GCOMP(self, 0xC0)
        self.AWDCR = Subscriptor(self, "AWD{}CR")
        self.TR = Subscriptor(self, "TR{}")
        self.OFR = Subscriptor(self, "OFR{}")
        self.JDR = Subscriptor(self, "JDR{}")
        self.SMPR = Subscriptor(self, "SMPR{}")
        self.SQR = Subscriptor(self, "SQR{}")

ADC1 = SA_ADC1(0x50000000, "ADC1")
ADC2 = SA_ADC1(0x50000100, "ADC2")

class SA_ADC3_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISR", "interrupt and status register")
        self.JQOVF = BitField(self, 0x00000400, "JQOVF", "JQOVF")
        self.AWD3 = BitField(self, 0x00000200, "AWD3", "AWD3")
        self.AWD2 = BitField(self, 0x00000100, "AWD2", "AWD2")
        self.AWD1 = BitField(self, 0x00000080, "AWD1", "AWD1")
        self.JEOS = BitField(self, 0x00000040, "JEOS", "JEOS")
        self.JEOC = BitField(self, 0x00000020, "JEOC", "JEOC")
        self.OVR = BitField(self, 0x00000010, "OVR", "OVR")
        self.EOS = BitField(self, 0x00000008, "EOS", "EOS")
        self.EOC = BitField(self, 0x00000004, "EOC", "EOC")
        self.EOSMP = BitField(self, 0x00000002, "EOSMP", "EOSMP")
        self.ADRDY = BitField(self, 0x00000001, "ADRDY", "ADRDY")
        self.AWD = Subscriptor(self, "AWD{}")

class SA_ADC3_IER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IER", "interrupt enable register")
        self.JQOVFIE = BitField(self, 0x00000400, "JQOVFIE", "JQOVFIE")
        self.AWD3IE = BitField(self, 0x00000200, "AWD3IE", "AWD3IE")
        self.AWD2IE = BitField(self, 0x00000100, "AWD2IE", "AWD2IE")
        self.AWD1IE = BitField(self, 0x00000080, "AWD1IE", "AWD1IE")
        self.JEOSIE = BitField(self, 0x00000040, "JEOSIE", "JEOSIE")
        self.JEOCIE = BitField(self, 0x00000020, "JEOCIE", "JEOCIE")
        self.OVRIE = BitField(self, 0x00000010, "OVRIE", "OVRIE")
        self.EOSIE = BitField(self, 0x00000008, "EOSIE", "EOSIE")
        self.EOCIE = BitField(self, 0x00000004, "EOCIE", "EOCIE")
        self.EOSMPIE = BitField(self, 0x00000002, "EOSMPIE", "EOSMPIE")
        self.ADRDYIE = BitField(self, 0x00000001, "ADRDYIE", "ADRDYIE")
        self.AWDIE = Subscriptor(self, "AWD{}IE")

class SA_ADC3_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x20002000, "CR", "control register")
        self.ADCAL = BitField(self, 0x80000000, "ADCAL", "ADCAL")
        self.ADCALDIF = BitField(self, 0x40000000, "ADCALDIF", "ADCALDIF")
        self.DEEPPWD = BitField(self, 0x20000000, "DEEPPWD", "DEEPPWD")
        self.ADVREGEN = BitField(self, 0x10000000, "ADVREGEN", "ADVREGEN")
        self.JADSTP = BitField(self, 0x00000020, "JADSTP", "JADSTP")
        self.ADSTP = BitField(self, 0x00000010, "ADSTP", "ADSTP")
        self.JADSTART = BitField(self, 0x00000008, "JADSTART", "JADSTART")
        self.ADSTART = BitField(self, 0x00000004, "ADSTART", "ADSTART")
        self.ADDIS = BitField(self, 0x00000002, "ADDIS", "ADDIS")
        self.ADEN = BitField(self, 0x00000001, "ADEN", "ADEN")

class SA_ADC3_CFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x80000000, "CFGR", "configuration register")
        self.JQDIS = BitField(self, 0x80000000, "JQDIS", "Injected Queue disable")
        self.AWDCH1CH = BitField(self, 0x7C000000, "AWDCH1CH", "AWDCH1CH")
        self.JAUTO = BitField(self, 0x02000000, "JAUTO", "JAUTO")
        self.JAWD1EN = BitField(self, 0x01000000, "JAWD1EN", "JAWD1EN")
        self.AWD1EN = BitField(self, 0x00800000, "AWD1EN", "AWD1EN")
        self.AWD1SGL = BitField(self, 0x00400000, "AWD1SGL", "AWD1SGL")
        self.JQM = BitField(self, 0x00200000, "JQM", "JQM")
        self.JDISCEN = BitField(self, 0x00100000, "JDISCEN", "JDISCEN")
        self.DISCNUM = BitField(self, 0x000E0000, "DISCNUM", "DISCNUM")
        self.DISCEN = BitField(self, 0x00010000, "DISCEN", "DISCEN")
        self.ALIGN = BitField(self, 0x00008000, "ALIGN", "ALIGN")
        self.AUTDLY = BitField(self, 0x00004000, "AUTDLY", "AUTDLY")
        self.CONT = BitField(self, 0x00002000, "CONT", "CONT")
        self.OVRMOD = BitField(self, 0x00001000, "OVRMOD", "OVRMOD")
        self.EXTEN = BitField(self, 0x00000C00, "EXTEN", "EXTEN")
        self.EXTSEL = BitField(self, 0x000003E0, "EXTSEL", "EXTSEL")
        self.RES = BitField(self, 0x00000018, "RES", "RES")
        self.DMACFG = BitField(self, 0x00000002, "DMACFG", "DMACFG")
        self.DMAEN = BitField(self, 0x00000001, "DMAEN", "DMAEN")

class SA_ADC3_CFGR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CFGR2", "configuration register")
        self.SMPTRIG = BitField(self, 0x08000000, "SMPTRIG", "SMPTRIG")
        self.BULB = BitField(self, 0x04000000, "BULB", "BULB")
        self.SWTRIG = BitField(self, 0x02000000, "SWTRIG", "SWTRIG")
        self.GCOMP = BitField(self, 0x00010000, "GCOMP", "GCOMP")
        self.ROVSM = BitField(self, 0x00000400, "ROVSM", "EXTEN")
        self.TROVS = BitField(self, 0x00000200, "TROVS", "Triggered Regular Oversampling")
        self.OVSS = BitField(self, 0x000001E0, "OVSS", "ALIGN")
        self.OVSR = BitField(self, 0x0000001C, "OVSR", "RES")
        self.JOVSE = BitField(self, 0x00000002, "JOVSE", "DMACFG")
        self.ROVSE = BitField(self, 0x00000001, "ROVSE", "DMAEN")

class SA_ADC3_SMPR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SMPR1", "sample time register 1")
        self.SMP9 = BitField(self, 0x38000000, "SMP9", "SMP9")
        self.SMP8 = BitField(self, 0x07000000, "SMP8", "SMP8")
        self.SMP7 = BitField(self, 0x00E00000, "SMP7", "SMP7")
        self.SMP6 = BitField(self, 0x001C0000, "SMP6", "SMP6")
        self.SMP5 = BitField(self, 0x00038000, "SMP5", "SMP5")
        self.SMP4 = BitField(self, 0x00007000, "SMP4", "SMP4")
        self.SMP3 = BitField(self, 0x00000E00, "SMP3", "SMP3")
        self.SMP2 = BitField(self, 0x000001C0, "SMP2", "SMP2")
        self.SMP1 = BitField(self, 0x00000038, "SMP1", "SMP1")
        self.SMPPLUS = BitField(self, 0x80000000, "SMPPLUS", "Addition of one clock cycle to the sampling time")
        self.SMP0 = BitField(self, 0x00000007, "SMP0", "SMP0")
        self.SMP = Subscriptor(self, "SMP{}")

class SA_ADC3_SMPR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SMPR2", "sample time register 2")
        self.SMP18 = BitField(self, 0x07000000, "SMP18", "SMP18")
        self.SMP17 = BitField(self, 0x00E00000, "SMP17", "SMP17")
        self.SMP16 = BitField(self, 0x001C0000, "SMP16", "SMP16")
        self.SMP15 = BitField(self, 0x00038000, "SMP15", "SMP15")
        self.SMP14 = BitField(self, 0x00007000, "SMP14", "SMP14")
        self.SMP13 = BitField(self, 0x00000E00, "SMP13", "SMP13")
        self.SMP12 = BitField(self, 0x000001C0, "SMP12", "SMP12")
        self.SMP11 = BitField(self, 0x00000038, "SMP11", "SMP11")
        self.SMP10 = BitField(self, 0x00000007, "SMP10", "SMP10")
        self.SMP = Subscriptor(self, "SMP{}")

class SA_ADC3_TR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFF0000, "TR1", "watchdog threshold register 1")
        self.HT1 = BitField(self, 0x0FFF0000, "HT1", "HT1")
        self.AWDFILT = BitField(self, 0x00007000, "AWDFILT", "AWDFILT")
        self.LT1 = BitField(self, 0x00000FFF, "LT1", "LT1")

class SA_ADC3_TR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFF0000, "TR2", "watchdog threshold register")
        self.HT2 = BitField(self, 0x00FF0000, "HT2", "HT2")
        self.LT2 = BitField(self, 0x000000FF, "LT2", "LT2")

class SA_ADC3_TR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFF0000, "TR3", "watchdog threshold register 3")
        self.HT3 = BitField(self, 0x00FF0000, "HT3", "HT3")
        self.LT3 = BitField(self, 0x000000FF, "LT3", "LT3")

class SA_ADC3_SQR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR1", "regular sequence register 1")
        self.SQ4 = BitField(self, 0x1F000000, "SQ4", "SQ4")
        self.SQ3 = BitField(self, 0x007C0000, "SQ3", "SQ3")
        self.SQ2 = BitField(self, 0x0001F000, "SQ2", "SQ2")
        self.SQ1 = BitField(self, 0x000007C0, "SQ1", "SQ1")
        self.L = BitField(self, 0x0000000F, "L", "Regular channel sequence length")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC3_SQR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR2", "regular sequence register 2")
        self.SQ9 = BitField(self, 0x1F000000, "SQ9", "SQ9")
        self.SQ8 = BitField(self, 0x007C0000, "SQ8", "SQ8")
        self.SQ7 = BitField(self, 0x0001F000, "SQ7", "SQ7")
        self.SQ6 = BitField(self, 0x000007C0, "SQ6", "SQ6")
        self.SQ5 = BitField(self, 0x0000001F, "SQ5", "SQ5")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC3_SQR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR3", "regular sequence register 3")
        self.SQ14 = BitField(self, 0x1F000000, "SQ14", "SQ14")
        self.SQ13 = BitField(self, 0x007C0000, "SQ13", "SQ13")
        self.SQ12 = BitField(self, 0x0001F000, "SQ12", "SQ12")
        self.SQ11 = BitField(self, 0x000007C0, "SQ11", "SQ11")
        self.SQ10 = BitField(self, 0x0000001F, "SQ10", "SQ10")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC3_SQR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SQR4", "regular sequence register 4")
        self.SQ16 = BitField(self, 0x000007C0, "SQ16", "SQ16")
        self.SQ15 = BitField(self, 0x0000001F, "SQ15", "SQ15")
        self.SQ = Subscriptor(self, "SQ{}")

class SA_ADC3_DR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DR", "regular Data Register")
        self.RDATA = BitField(self, 0x0000FFFF, "RDATA", "Regular Data converted")

class SA_ADC3_JSQR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JSQR", "injected sequence register")
        self.JSQ4 = BitField(self, 0xF8000000, "JSQ4", "JSQ4")
        self.JSQ3 = BitField(self, 0x03E00000, "JSQ3", "JSQ3")
        self.JSQ2 = BitField(self, 0x000F8000, "JSQ2", "JSQ2")
        self.JSQ1 = BitField(self, 0x00003E00, "JSQ1", "JSQ1")
        self.JEXTEN = BitField(self, 0x00000180, "JEXTEN", "JEXTEN")
        self.JEXTSEL = BitField(self, 0x0000007C, "JEXTSEL", "JEXTSEL")
        self.JL = BitField(self, 0x00000003, "JL", "JL")
        self.JSQ = Subscriptor(self, "JSQ{}")

class SA_ADC3_OFR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR1", "offset register 1")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC3_OFR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR2", "offset register 2")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC3_OFR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR3", "offset register 3")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC3_OFR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "OFR4", "offset register 4")
        self.OFFSET1_EN = BitField(self, 0x80000000, "OFFSET1_EN", "OFFSET1_EN")
        self.OFFSET1_CH = BitField(self, 0x7C000000, "OFFSET1_CH", "OFFSET1_CH")
        self.SATEN = BitField(self, 0x02000000, "SATEN", "SATEN")
        self.OFFSETPOS = BitField(self, 0x01000000, "OFFSETPOS", "OFFSETPOS")
        self.OFFSET1 = BitField(self, 0x00000FFF, "OFFSET1", "OFFSET1")

class SA_ADC3_JDR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR1", "injected data register 1")
        self.JDATA1 = BitField(self, 0x0000FFFF, "JDATA1", "JDATA1")

class SA_ADC3_JDR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR2", "injected data register 2")
        self.JDATA2 = BitField(self, 0x0000FFFF, "JDATA2", "JDATA2")

class SA_ADC3_JDR3(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR3", "injected data register 3")
        self.JDATA3 = BitField(self, 0x0000FFFF, "JDATA3", "JDATA3")

class SA_ADC3_JDR4(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "JDR4", "injected data register 4")
        self.JDATA4 = BitField(self, 0x0000FFFF, "JDATA4", "JDATA4")

class SA_ADC3_AWD2CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AWD2CR", "Analog Watchdog 2 Configuration Register")
        self.AWD2CH = BitField(self, 0x0007FFFF, "AWD2CH", "AWD2CH")

class SA_ADC3_AWD3CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AWD3CR", "Analog Watchdog 3 Configuration Register")
        self.AWD3CH = BitField(self, 0x0007FFFF, "AWD3CH", "AWD3CH")

class SA_ADC3_DIFSEL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DIFSEL", "Differential Mode Selection Register 2")
        self.DIFSEL_0 = BitField(self, 0x00000001, "DIFSEL_0", "Differential mode for channels 0")
        self.DIFSEL_1_18 = BitField(self, 0x0007FFFE, "DIFSEL_1_18", "Differential mode for channels 15 to 1")

class SA_ADC3_CALFACT(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CALFACT", "Calibration Factors")
        self.CALFACT_D = BitField(self, 0x007F0000, "CALFACT_D", "CALFACT_D")
        self.CALFACT_S = BitField(self, 0x0000007F, "CALFACT_S", "CALFACT_S")

class SA_ADC3_GCOMP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "GCOMP", "Gain compensation Register")
        self.GCOMPCOEFF = BitField(self, 0x00003FFF, "GCOMPCOEFF", "GCOMPCOEFF")

class SA_ADC3(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Analog-to-Digital Converter")
        self.ISR = SA_ADC3_ISR(self, 0x0)
        self.IER = SA_ADC3_IER(self, 0x4)
        self.CR = SA_ADC3_CR(self, 0x8)
        self.CFGR = SA_ADC3_CFGR(self, 0xC)
        self.CFGR2 = SA_ADC3_CFGR2(self, 0x10)
        self.SMPR1 = SA_ADC3_SMPR1(self, 0x14)
        self.SMPR2 = SA_ADC3_SMPR2(self, 0x18)
        self.TR1 = SA_ADC3_TR1(self, 0x20)
        self.TR2 = SA_ADC3_TR2(self, 0x24)
        self.TR3 = SA_ADC3_TR3(self, 0x28)
        self.SQR1 = SA_ADC3_SQR1(self, 0x30)
        self.SQR2 = SA_ADC3_SQR2(self, 0x34)
        self.SQR3 = SA_ADC3_SQR3(self, 0x38)
        self.SQR4 = SA_ADC3_SQR4(self, 0x3C)
        self.DR = SA_ADC3_DR(self, 0x40)
        self.JSQR = SA_ADC3_JSQR(self, 0x4C)
        self.OFR1 = SA_ADC3_OFR1(self, 0x60)
        self.OFR2 = SA_ADC3_OFR2(self, 0x64)
        self.OFR3 = SA_ADC3_OFR3(self, 0x68)
        self.OFR4 = SA_ADC3_OFR4(self, 0x6C)
        self.JDR1 = SA_ADC3_JDR1(self, 0x80)
        self.JDR2 = SA_ADC3_JDR2(self, 0x84)
        self.JDR3 = SA_ADC3_JDR3(self, 0x88)
        self.JDR4 = SA_ADC3_JDR4(self, 0x8C)
        self.AWD2CR = SA_ADC3_AWD2CR(self, 0xA0)
        self.AWD3CR = SA_ADC3_AWD3CR(self, 0xA4)
        self.DIFSEL = SA_ADC3_DIFSEL(self, 0xB0)
        self.CALFACT = SA_ADC3_CALFACT(self, 0xB4)
        self.GCOMP = SA_ADC3_GCOMP(self, 0xC0)
        self.AWDCR = Subscriptor(self, "AWD{}CR")
        self.TR = Subscriptor(self, "TR{}")
        self.OFR = Subscriptor(self, "OFR{}")
        self.JDR = Subscriptor(self, "JDR{}")
        self.SMPR = Subscriptor(self, "SMPR{}")
        self.SQR = Subscriptor(self, "SQR{}")

ADC3 = SA_ADC3(0x50000400, "ADC3")
ADC4 = SA_ADC1(0x50000500, "ADC4")
ADC5 = SA_ADC3(0x50000600, "ADC5")

class SA_ADC12_Common_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CSR", "ADC Common status register")
        self.ADDRDY_MST = BitField(self, 0x00000001, "ADDRDY_MST", "ADDRDY_MST")
        self.EOSMP_MST = BitField(self, 0x00000002, "EOSMP_MST", "EOSMP_MST")
        self.EOC_MST = BitField(self, 0x00000004, "EOC_MST", "EOC_MST")
        self.EOS_MST = BitField(self, 0x00000008, "EOS_MST", "EOS_MST")
        self.OVR_MST = BitField(self, 0x00000010, "OVR_MST", "OVR_MST")
        self.JEOC_MST = BitField(self, 0x00000020, "JEOC_MST", "JEOC_MST")
        self.JEOS_MST = BitField(self, 0x00000040, "JEOS_MST", "JEOS_MST")
        self.AWD1_MST = BitField(self, 0x00000080, "AWD1_MST", "AWD1_MST")
        self.AWD2_MST = BitField(self, 0x00000100, "AWD2_MST", "AWD2_MST")
        self.AWD3_MST = BitField(self, 0x00000200, "AWD3_MST", "AWD3_MST")
        self.JQOVF_MST = BitField(self, 0x00000400, "JQOVF_MST", "JQOVF_MST")
        self.ADRDY_SLV = BitField(self, 0x00010000, "ADRDY_SLV", "ADRDY_SLV")
        self.EOSMP_SLV = BitField(self, 0x00020000, "EOSMP_SLV", "EOSMP_SLV")
        self.EOC_SLV = BitField(self, 0x00040000, "EOC_SLV", "End of regular conversion of the slave ADC")
        self.EOS_SLV = BitField(self, 0x00080000, "EOS_SLV", "End of regular sequence flag of the slave ADC")
        self.OVR_SLV = BitField(self, 0x00100000, "OVR_SLV", "Overrun flag of the slave ADC")
        self.JEOC_SLV = BitField(self, 0x00200000, "JEOC_SLV", "End of injected conversion flag of the slave ADC")
        self.JEOS_SLV = BitField(self, 0x00400000, "JEOS_SLV", "End of injected sequence flag of the slave ADC")
        self.AWD1_SLV = BitField(self, 0x00800000, "AWD1_SLV", "Analog watchdog 1 flag of the slave ADC")
        self.AWD2_SLV = BitField(self, 0x01000000, "AWD2_SLV", "Analog watchdog 2 flag of the slave ADC")
        self.AWD3_SLV = BitField(self, 0x02000000, "AWD3_SLV", "Analog watchdog 3 flag of the slave ADC")
        self.JQOVF_SLV = BitField(self, 0x04000000, "JQOVF_SLV", "Injected Context Queue Overflow flag of the slave ADC")
        self.AWD_MST = Subscriptor(self, "AWD{}_MST")
        self.AWD_SLV = Subscriptor(self, "AWD{}_SLV")

class SA_ADC12_Common_CCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CCR", "ADC common control register")
        self.DUAL = BitField(self, 0x0000001F, "DUAL", "Dual ADC mode selection")
        self.DELAY = BitField(self, 0x00000F00, "DELAY", "Delay between 2 sampling phases")
        self.DMACFG = BitField(self, 0x00002000, "DMACFG", "DMA configuration (for multi-ADC mode)")
        self.MDMA = BitField(self, 0x0000C000, "MDMA", "Direct memory access mode for multi ADC mode")
        self.CKMODE = BitField(self, 0x00030000, "CKMODE", "ADC clock mode")
        self.VREFEN = BitField(self, 0x00400000, "VREFEN", "VREFINT enable")
        self.VSENSESEL = BitField(self, 0x00800000, "VSENSESEL", "VTS selection")
        self.VBATSEL = BitField(self, 0x01000000, "VBATSEL", "VBAT selection")
        self.PRESC = BitField(self, 0x003C0000, "PRESC", "ADC prescaler")

class SA_ADC12_Common_CDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CDR", "ADC common regular data register for dual and triple modes")
        self.RDATA_SLV = BitField(self, 0xFFFF0000, "RDATA_SLV", "Regular data of the slave ADC")
        self.RDATA_MST = BitField(self, 0x0000FFFF, "RDATA_MST", "Regular data of the master ADC")

class SA_ADC12_Common(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Analog-to-Digital Converter")
        self.CSR = SA_ADC12_Common_CSR(self, 0x0)
        self.CCR = SA_ADC12_Common_CCR(self, 0x8)
        self.CDR = SA_ADC12_Common_CDR(self, 0xC)

ADC12_Common = SA_ADC12_Common(0x50000300, "ADC12_Common")
ADC345_Common = SA_ADC12_Common(0x50000700, "ADC345_Common")

class SA_FMAC_X1BUFCFG(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "X1BUFCFG", "FMAC X1 Buffer Configuration register")
        self.X1_BASE = BitField(self, 0x000000FF, "X1_BASE", "X1_BASE")
        self.X1_BUF_SIZE = BitField(self, 0x0000FF00, "X1_BUF_SIZE", "X1_BUF_SIZE")
        self.FULL_WM = BitField(self, 0x03000000, "FULL_WM", "FULL_WM")

class SA_FMAC_X2BUFCFG(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "X2BUFCFG", "FMAC X2 Buffer Configuration register")
        self.X2_BASE = BitField(self, 0x000000FF, "X2_BASE", "X1_BASE")
        self.X2_BUF_SIZE = BitField(self, 0x0000FF00, "X2_BUF_SIZE", "X1_BUF_SIZE")

class SA_FMAC_YBUFCFG(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "YBUFCFG", "FMAC Y Buffer Configuration register")
        self.Y_BASE = BitField(self, 0x000000FF, "Y_BASE", "X1_BASE")
        self.Y_BUF_SIZE = BitField(self, 0x0000FF00, "Y_BUF_SIZE", "X1_BUF_SIZE")
        self.EMPTY_WM = BitField(self, 0x03000000, "EMPTY_WM", "EMPTY_WM")

class SA_FMAC_PARAM(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PARAM", "FMAC Parameter register")
        self.START = BitField(self, 0x80000000, "START", "START")
        self.FUNC = BitField(self, 0x7F000000, "FUNC", "FUNC")
        self.R = BitField(self, 0x00FF0000, "R", "R")
        self.Q = BitField(self, 0x0000FF00, "Q", "Q")
        self.P = BitField(self, 0x000000FF, "P", "P")

class SA_FMAC_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "FMAC Control register")
        self.RESET = BitField(self, 0x00010000, "RESET", "RESET")
        self.CLIPEN = BitField(self, 0x00008000, "CLIPEN", "CLIPEN")
        self.DMAWEN = BitField(self, 0x00000200, "DMAWEN", "DMAWEN")
        self.DMAREN = BitField(self, 0x00000100, "DMAREN", "DMAREN")
        self.SATIEN = BitField(self, 0x00000010, "SATIEN", "SATIEN")
        self.UNFLIEN = BitField(self, 0x00000008, "UNFLIEN", "UNFLIEN")
        self.OVFLIEN = BitField(self, 0x00000004, "OVFLIEN", "OVFLIEN")
        self.WIEN = BitField(self, 0x00000002, "WIEN", "WIEN")
        self.RIEN = BitField(self, 0x00000001, "RIEN", "RIEN")

class SA_FMAC_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "FMAC Status register")
        self.YEMPTY = BitField(self, 0x00000001, "YEMPTY", "YEMPTY")
        self.X1FULL = BitField(self, 0x00000002, "X1FULL", "X1FULL")
        self.OVFL = BitField(self, 0x00000100, "OVFL", "OVFL")
        self.UNFL = BitField(self, 0x00000200, "UNFL", "UNFL")
        self.SAT = BitField(self, 0x00000400, "SAT", "SAT")

class SA_FMAC_WDATA(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "WDATA", "FMAC Write Data register")
        self.WDATA = BitField(self, 0x0000FFFF, "WDATA", "WDATA")

class SA_FMAC_RDATA(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RDATA", "FMAC Read Data register")
        self.RDATA = BitField(self, 0x0000FFFF, "RDATA", "RDATA")

class SA_FMAC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Filter Math Accelerator")
        self.X1BUFCFG = SA_FMAC_X1BUFCFG(self, 0x0)
        self.X2BUFCFG = SA_FMAC_X2BUFCFG(self, 0x4)
        self.YBUFCFG = SA_FMAC_YBUFCFG(self, 0x8)
        self.PARAM = SA_FMAC_PARAM(self, 0xC)
        self.CR = SA_FMAC_CR(self, 0x10)
        self.SR = SA_FMAC_SR(self, 0x14)
        self.WDATA = SA_FMAC_WDATA(self, 0x18)
        self.RDATA = SA_FMAC_RDATA(self, 0x1C)
        self.XBUFCFG = Subscriptor(self, "X{}BUFCFG")

FMAC = SA_FMAC(0x40021400, "FMAC")

class SA_CORDIC_CSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CSR", "CORDIC Control Status register")
        self.FUNC = BitField(self, 0x0000000F, "FUNC", "FUNC")
        self.PRECISION = BitField(self, 0x000000F0, "PRECISION", "PRECISION")
        self.SCALE = BitField(self, 0x00000700, "SCALE", "SCALE")
        self.IEN = BitField(self, 0x00010000, "IEN", "IEN")
        self.DMAREN = BitField(self, 0x00020000, "DMAREN", "DMAREN")
        self.DMAWEN = BitField(self, 0x00040000, "DMAWEN", "DMAWEN")
        self.NRES = BitField(self, 0x00080000, "NRES", "NRES")
        self.NARGS = BitField(self, 0x00100000, "NARGS", "NARGS")
        self.RESSIZE = BitField(self, 0x00200000, "RESSIZE", "RESSIZE")
        self.ARGSIZE = BitField(self, 0x00400000, "ARGSIZE", "ARGSIZE")
        self.RRDY = BitField(self, 0x80000000, "RRDY", "RRDY")

class SA_CORDIC_WDATA(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "WDATA", "FMAC Write Data register")
        self.ARG = BitField(self, 0xFFFFFFFF, "ARG", "ARG")

class SA_CORDIC_RDATA(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RDATA", "FMAC Read Data register")
        self.RES = BitField(self, 0xFFFFFFFF, "RES", "RES")

class SA_CORDIC(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "CORDIC Co-processor")
        self.CSR = SA_CORDIC_CSR(self, 0x0)
        self.WDATA = SA_CORDIC_WDATA(self, 0x4)
        self.RDATA = SA_CORDIC_RDATA(self, 0x8)

CORDIC = SA_CORDIC(0x40020C00, "CORDIC")

class SA_SAI_BCR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x40, "BCR1", "BConfiguration register 1")
        self.MCKEN = BitField(self, 0x08000000, "MCKEN", "MCKEN")
        self.OSR = BitField(self, 0x04000000, "OSR", "OSR")
        self.MCJDIV = BitField(self, 0x03F00000, "MCJDIV", "Master clock divider")
        self.NODIV = BitField(self, 0x00080000, "NODIV", "No divider")
        self.DMAEN = BitField(self, 0x00020000, "DMAEN", "DMA enable")
        self.SAIBEN = BitField(self, 0x00010000, "SAIBEN", "Audio block B enable")
        self.OutDri = BitField(self, 0x00002000, "OutDri", "Output drive")
        self.MONO = BitField(self, 0x00001000, "MONO", "Mono mode")
        self.SYNCEN = BitField(self, 0x00000C00, "SYNCEN", "Synchronization enable")
        self.CKSTR = BitField(self, 0x00000200, "CKSTR", "Clock strobing edge")
        self.LSBFIRST = BitField(self, 0x00000100, "LSBFIRST", "Least significant bit first")
        self.DS = BitField(self, 0x000000E0, "DS", "Data size")
        self.PRTCFG = BitField(self, 0x0000000C, "PRTCFG", "Protocol configuration")
        self.MODE = BitField(self, 0x00000003, "MODE", "Audio block mode")

class SA_SAI_BCR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BCR2", "BConfiguration register 2")
        self.COMP = BitField(self, 0x0000C000, "COMP", "Companding mode")
        self.CPL = BitField(self, 0x00002000, "CPL", "Complement bit")
        self.MUTECN = BitField(self, 0x00001F80, "MUTECN", "Mute counter")
        self.MUTEVAL = BitField(self, 0x00000040, "MUTEVAL", "Mute value")
        self.MUTE = BitField(self, 0x00000020, "MUTE", "Mute")
        self.TRIS = BitField(self, 0x00000010, "TRIS", "Tristate management on data line")
        self.FFLUS = BitField(self, 0x00000008, "FFLUS", "FIFO flush")
        self.FTH = BitField(self, 0x00000007, "FTH", "FIFO threshold")

class SA_SAI_BFRCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7, "BFRCR", "BFRCR")
        self.FSOFF = BitField(self, 0x00040000, "FSOFF", "Frame synchronization offset")
        self.FSPOL = BitField(self, 0x00020000, "FSPOL", "Frame synchronization polarity")
        self.FSDEF = BitField(self, 0x00010000, "FSDEF", "Frame synchronization definition")
        self.FSALL = BitField(self, 0x00007F00, "FSALL", "Frame synchronization active level length")
        self.FRL = BitField(self, 0x000000FF, "FRL", "Frame length")

class SA_SAI_BSLOTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BSLOTR", "BSlot register")
        self.SLOTEN = BitField(self, 0xFFFF0000, "SLOTEN", "Slot enable")
        self.NBSLOT = BitField(self, 0x00000F00, "NBSLOT", "Number of slots in an audio frame")
        self.SLOTSZ = BitField(self, 0x000000C0, "SLOTSZ", "Slot size")
        self.FBOFF = BitField(self, 0x0000001F, "FBOFF", "First bit offset")

class SA_SAI_BIM(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BIM", "BInterrupt mask register2")
        self.LFSDETIE = BitField(self, 0x00000040, "LFSDETIE", "Late frame synchronization detection interrupt enable")
        self.AFSDETIE = BitField(self, 0x00000020, "AFSDETIE", "Anticipated frame synchronization detection interrupt enable")
        self.CNRDYIE = BitField(self, 0x00000010, "CNRDYIE", "Codec not ready interrupt enable")
        self.FREQIE = BitField(self, 0x00000008, "FREQIE", "FIFO request interrupt enable")
        self.WCKCFG = BitField(self, 0x00000004, "WCKCFG", "Wrong clock configuration interrupt enable")
        self.MUTEDET = BitField(self, 0x00000002, "MUTEDET", "Mute detection interrupt enable")
        self.OVRUDRIE = BitField(self, 0x00000001, "OVRUDRIE", "Overrun/underrun interrupt enable")

class SA_SAI_BSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BSR", "BStatus register")
        self.FLVL = BitField(self, 0x00070000, "FLVL", "FIFO level threshold")
        self.LFSDET = BitField(self, 0x00000040, "LFSDET", "Late frame synchronization detection")
        self.AFSDET = BitField(self, 0x00000020, "AFSDET", "Anticipated frame synchronization detection")
        self.CNRDY = BitField(self, 0x00000010, "CNRDY", "Codec not ready")
        self.FREQ = BitField(self, 0x00000008, "FREQ", "FIFO request")
        self.WCKCFG = BitField(self, 0x00000004, "WCKCFG", "Wrong clock configuration flag")
        self.MUTEDET = BitField(self, 0x00000002, "MUTEDET", "Mute detection")
        self.OVRUDR = BitField(self, 0x00000001, "OVRUDR", "Overrun / underrun")

class SA_SAI_BCLRFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BCLRFR", "BClear flag register")
        self.LFSDET = BitField(self, 0x00000040, "LFSDET", "Clear late frame synchronization detection flag")
        self.CAFSDET = BitField(self, 0x00000020, "CAFSDET", "Clear anticipated frame synchronization detection flag")
        self.CNRDY = BitField(self, 0x00000010, "CNRDY", "Clear codec not ready flag")
        self.WCKCFG = BitField(self, 0x00000004, "WCKCFG", "Clear wrong clock configuration flag")
        self.MUTEDET = BitField(self, 0x00000002, "MUTEDET", "Mute detection flag")
        self.OVRUDR = BitField(self, 0x00000001, "OVRUDR", "Clear overrun / underrun")

class SA_SAI_BDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BDR", "BData register")
        self.DATA = BitField(self, 0xFFFFFFFF, "DATA", "Data")

class SA_SAI_ACR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x40, "ACR1", "AConfiguration register 1")
        self.MCKEN = BitField(self, 0x08000000, "MCKEN", "MCKEN")
        self.OSR = BitField(self, 0x04000000, "OSR", "OSR")
        self.MCJDIV = BitField(self, 0x03F00000, "MCJDIV", "Master clock divider")
        self.NODIV = BitField(self, 0x00080000, "NODIV", "No divider")
        self.DMAEN = BitField(self, 0x00020000, "DMAEN", "DMA enable")
        self.SAIAEN = BitField(self, 0x00010000, "SAIAEN", "Audio block A enable")
        self.OutDri = BitField(self, 0x00002000, "OutDri", "Output drive")
        self.MONO = BitField(self, 0x00001000, "MONO", "Mono mode")
        self.SYNCEN = BitField(self, 0x00000C00, "SYNCEN", "Synchronization enable")
        self.CKSTR = BitField(self, 0x00000200, "CKSTR", "Clock strobing edge")
        self.LSBFIRST = BitField(self, 0x00000100, "LSBFIRST", "Least significant bit first")
        self.DS = BitField(self, 0x000000E0, "DS", "Data size")
        self.PRTCFG = BitField(self, 0x0000000C, "PRTCFG", "Protocol configuration")
        self.MODE = BitField(self, 0x00000003, "MODE", "Audio block mode")

class SA_SAI_ACR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ACR2", "AConfiguration register 2")
        self.COMP = BitField(self, 0x0000C000, "COMP", "Companding mode")
        self.CPL = BitField(self, 0x00002000, "CPL", "Complement bit")
        self.MUTECN = BitField(self, 0x00001F80, "MUTECN", "Mute counter")
        self.MUTEVAL = BitField(self, 0x00000040, "MUTEVAL", "Mute value")
        self.MUTE = BitField(self, 0x00000020, "MUTE", "Mute")
        self.TRIS = BitField(self, 0x00000010, "TRIS", "Tristate management on data line")
        self.FFLUS = BitField(self, 0x00000008, "FFLUS", "FIFO flush")
        self.FTH = BitField(self, 0x00000007, "FTH", "FIFO threshold")

class SA_SAI_AFRCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x7, "AFRCR", "AFRCR")
        self.FSOFF = BitField(self, 0x00040000, "FSOFF", "Frame synchronization offset")
        self.FSPOL = BitField(self, 0x00020000, "FSPOL", "Frame synchronization polarity")
        self.FSDEF = BitField(self, 0x00010000, "FSDEF", "Frame synchronization definition")
        self.FSALL = BitField(self, 0x00007F00, "FSALL", "Frame synchronization active level length")
        self.FRL = BitField(self, 0x000000FF, "FRL", "Frame length")

class SA_SAI_ASLOTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ASLOTR", "ASlot register")
        self.SLOTEN = BitField(self, 0xFFFF0000, "SLOTEN", "Slot enable")
        self.NBSLOT = BitField(self, 0x00000F00, "NBSLOT", "Number of slots in an audio frame")
        self.SLOTSZ = BitField(self, 0x000000C0, "SLOTSZ", "Slot size")
        self.FBOFF = BitField(self, 0x0000001F, "FBOFF", "First bit offset")

class SA_SAI_AIM(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "AIM", "AInterrupt mask register2")
        self.LFSDET = BitField(self, 0x00000040, "LFSDET", "Late frame synchronization detection interrupt enable")
        self.AFSDETIE = BitField(self, 0x00000020, "AFSDETIE", "Anticipated frame synchronization detection interrupt enable")
        self.CNRDYIE = BitField(self, 0x00000010, "CNRDYIE", "Codec not ready interrupt enable")
        self.FREQIE = BitField(self, 0x00000008, "FREQIE", "FIFO request interrupt enable")
        self.WCKCFG = BitField(self, 0x00000004, "WCKCFG", "Wrong clock configuration interrupt enable")
        self.MUTEDET = BitField(self, 0x00000002, "MUTEDET", "Mute detection interrupt enable")
        self.OVRUDRIE = BitField(self, 0x00000001, "OVRUDRIE", "Overrun/underrun interrupt enable")

class SA_SAI_ASR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ASR", "AStatus register")
        self.FLVL = BitField(self, 0x00070000, "FLVL", "FIFO level threshold")
        self.LFSDET = BitField(self, 0x00000040, "LFSDET", "Late frame synchronization detection")
        self.AFSDET = BitField(self, 0x00000020, "AFSDET", "Anticipated frame synchronization detection")
        self.CNRDY = BitField(self, 0x00000010, "CNRDY", "Codec not ready")
        self.FREQ = BitField(self, 0x00000008, "FREQ", "FIFO request")
        self.WCKCFG = BitField(self, 0x00000004, "WCKCFG", "Wrong clock configuration flag. This bit is read only")
        self.MUTEDET = BitField(self, 0x00000002, "MUTEDET", "Mute detection")
        self.OVRUDR = BitField(self, 0x00000001, "OVRUDR", "Overrun / underrun")

class SA_SAI_ACLRFR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ACLRFR", "AClear flag register")
        self.LFSDET = BitField(self, 0x00000040, "LFSDET", "Clear late frame synchronization detection flag")
        self.CAFSDET = BitField(self, 0x00000020, "CAFSDET", "Clear anticipated frame synchronization detection flag")
        self.CNRDY = BitField(self, 0x00000010, "CNRDY", "Clear codec not ready flag")
        self.WCKCFG = BitField(self, 0x00000004, "WCKCFG", "Clear wrong clock configuration flag")
        self.MUTEDET = BitField(self, 0x00000002, "MUTEDET", "Mute detection flag")
        self.OVRUDR = BitField(self, 0x00000001, "OVRUDR", "Clear overrun / underrun")

class SA_SAI_ADR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ADR", "AData register")
        self.DATA = BitField(self, 0xFFFFFFFF, "DATA", "Data")

class SA_SAI_PDMCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDMCR", "PDM control register")
        self.PDMEN = BitField(self, 0x00000001, "PDMEN", "PDMEN")
        self.MICNBR = BitField(self, 0x00000030, "MICNBR", "MICNBR")
        self.CKEN1 = BitField(self, 0x00000100, "CKEN1", "CKEN1")
        self.CKEN2 = BitField(self, 0x00000200, "CKEN2", "CKEN2")
        self.CKEN3 = BitField(self, 0x00000400, "CKEN3", "CKEN3")
        self.CKEN4 = BitField(self, 0x00000800, "CKEN4", "CKEN4")
        self.CKEN = Subscriptor(self, "CKEN{}")

class SA_SAI_PDMDLY(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "PDMDLY", "PDM delay register")
        self.DLYM1L = BitField(self, 0x00000007, "DLYM1L", "DLYM1L")
        self.DLYM1R = BitField(self, 0x00000070, "DLYM1R", "DLYM1R")
        self.DLYM2L = BitField(self, 0x00000700, "DLYM2L", "DLYM2L")
        self.DLYM2R = BitField(self, 0x00007000, "DLYM2R", "DLYM2R")
        self.DLYM3L = BitField(self, 0x00070000, "DLYM3L", "DLYM3L")
        self.DLYM3R = BitField(self, 0x00700000, "DLYM3R", "DLYM3R")
        self.DLYM4L = BitField(self, 0x07000000, "DLYM4L", "DLYM4L")
        self.DLYM4R = BitField(self, 0x70000000, "DLYM4R", "DLYM4R")
        self.DLYML = Subscriptor(self, "DLYM{}L")
        self.DLYMR = Subscriptor(self, "DLYM{}R")

class SA_SAI(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Serial audio interface")
        self.BCR1 = SA_SAI_BCR1(self, 0x24)
        self.BCR2 = SA_SAI_BCR2(self, 0x28)
        self.BFRCR = SA_SAI_BFRCR(self, 0x2C)
        self.BSLOTR = SA_SAI_BSLOTR(self, 0x30)
        self.BIM = SA_SAI_BIM(self, 0x34)
        self.BSR = SA_SAI_BSR(self, 0x38)
        self.BCLRFR = SA_SAI_BCLRFR(self, 0x3C)
        self.BDR = SA_SAI_BDR(self, 0x40)
        self.ACR1 = SA_SAI_ACR1(self, 0x4)
        self.ACR2 = SA_SAI_ACR2(self, 0x8)
        self.AFRCR = SA_SAI_AFRCR(self, 0xC)
        self.ASLOTR = SA_SAI_ASLOTR(self, 0x10)
        self.AIM = SA_SAI_AIM(self, 0x14)
        self.ASR = SA_SAI_ASR(self, 0x18)
        self.ACLRFR = SA_SAI_ACLRFR(self, 0x1C)
        self.ADR = SA_SAI_ADR(self, 0x20)
        self.PDMCR = SA_SAI_PDMCR(self, 0x44)
        self.PDMDLY = SA_SAI_PDMDLY(self, 0x48)
        self.BCR = Subscriptor(self, "BCR{}")
        self.ACR = Subscriptor(self, "ACR{}")

SAI = SA_SAI(0x40015400, "SAI")

class SA_TAMP_CR1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF0000, "CR1", "control register 1")
        self.TAMP1E = BitField(self, 0x00000001, "TAMP1E", "TAMP1E")
        self.TAMP2E = BitField(self, 0x00000002, "TAMP2E", "TAMP2E")
        self.TAMP3E = BitField(self, 0x00000004, "TAMP3E", "TAMP2E")
        self.ITAMP3E = BitField(self, 0x00040000, "ITAMP3E", "ITAMP3E")
        self.ITAMP4E = BitField(self, 0x00080000, "ITAMP4E", "ITAMP4E")
        self.ITAMP5E = BitField(self, 0x00100000, "ITAMP5E", "ITAMP5E")
        self.ITAMP6E = BitField(self, 0x00200000, "ITAMP6E", "ITAMP6E")
        self.TAMPE = Subscriptor(self, "TAMP{}E")
        self.ITAMPE = Subscriptor(self, "ITAMP{}E")

class SA_TAMP_CR2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR2", "control register 2")
        self.TAMP1NOER = BitField(self, 0x00000001, "TAMP1NOER", "TAMP1NOER")
        self.TAMP2NOER = BitField(self, 0x00000002, "TAMP2NOER", "TAMP2NOER")
        self.TAMP3NOER = BitField(self, 0x00000004, "TAMP3NOER", "TAMP3NOER")
        self.TAMP1MSK = BitField(self, 0x00010000, "TAMP1MSK", "TAMP1MSK")
        self.TAMP2MSK = BitField(self, 0x00020000, "TAMP2MSK", "TAMP2MSK")
        self.TAMP3MSK = BitField(self, 0x00040000, "TAMP3MSK", "TAMP3MSK")
        self.TAMP1TRG = BitField(self, 0x01000000, "TAMP1TRG", "TAMP1TRG")
        self.TAMP2TRG = BitField(self, 0x02000000, "TAMP2TRG", "TAMP2TRG")
        self.TAMP3TRG = BitField(self, 0x04000000, "TAMP3TRG", "TAMP3TRG")
        self.TAMPTRG = Subscriptor(self, "TAMP{}TRG")
        self.TAMPNOER = Subscriptor(self, "TAMP{}NOER")
        self.TAMPMSK = Subscriptor(self, "TAMP{}MSK")

class SA_TAMP_FLTCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FLTCR", "TAMP filter control register")
        self.TAMPFREQ = BitField(self, 0x00000007, "TAMPFREQ", "TAMPFREQ")
        self.TAMPFLT = BitField(self, 0x00000018, "TAMPFLT", "TAMPFLT")
        self.TAMPPRCH = BitField(self, 0x00000060, "TAMPPRCH", "TAMPPRCH")
        self.TAMPPUDIS = BitField(self, 0x00000080, "TAMPPUDIS", "TAMPPUDIS")

class SA_TAMP_IER(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IER", "TAMP interrupt enable register")
        self.TAMP1IE = BitField(self, 0x00000001, "TAMP1IE", "TAMP1IE")
        self.TAMP2IE = BitField(self, 0x00000002, "TAMP2IE", "TAMP2IE")
        self.TAMP3IE = BitField(self, 0x00000004, "TAMP3IE", "TAMP3IE")
        self.ITAMP3IE = BitField(self, 0x00040000, "ITAMP3IE", "ITAMP3IE")
        self.ITAMP4IE = BitField(self, 0x00080000, "ITAMP4IE", "ITAMP4IE")
        self.ITAMP5IE = BitField(self, 0x00100000, "ITAMP5IE", "ITAMP5IE")
        self.ITAMP6IE = BitField(self, 0x00200000, "ITAMP6IE", "ITAMP6IE")
        self.TAMPIE = Subscriptor(self, "TAMP{}IE")
        self.ITAMPIE = Subscriptor(self, "ITAMP{}IE")

class SA_TAMP_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "TAMP status register")
        self.TAMP1F = BitField(self, 0x00000001, "TAMP1F", "TAMP1F")
        self.TAMP2F = BitField(self, 0x00000002, "TAMP2F", "TAMP2F")
        self.TAMP3F = BitField(self, 0x00000004, "TAMP3F", "TAMP3F")
        self.ITAMP3F = BitField(self, 0x00040000, "ITAMP3F", "ITAMP3F")
        self.ITAMP4F = BitField(self, 0x00080000, "ITAMP4F", "ITAMP4F")
        self.ITAMP5F = BitField(self, 0x00100000, "ITAMP5F", "ITAMP5F")
        self.ITAMP6F = BitField(self, 0x00200000, "ITAMP6F", "ITAMP6F")
        self.TAMPF = Subscriptor(self, "TAMP{}F")
        self.ITAMPF = Subscriptor(self, "ITAMP{}F")

class SA_TAMP_MISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "MISR", "TAMP masked interrupt status register")
        self.TAMP1MF = BitField(self, 0x00000001, "TAMP1MF", "TAMP1MF:")
        self.TAMP2MF = BitField(self, 0x00000002, "TAMP2MF", "TAMP2MF")
        self.TAMP3MF = BitField(self, 0x00000004, "TAMP3MF", "TAMP3MF")
        self.ITAMP3MF = BitField(self, 0x00040000, "ITAMP3MF", "ITAMP3MF")
        self.ITAMP4MF = BitField(self, 0x00080000, "ITAMP4MF", "ITAMP4MF")
        self.ITAMP5MF = BitField(self, 0x00100000, "ITAMP5MF", "ITAMP5MF")
        self.ITAMP6MF = BitField(self, 0x00200000, "ITAMP6MF", "ITAMP6MF")
        self.TAMPMF = Subscriptor(self, "TAMP{}MF")
        self.ITAMPMF = Subscriptor(self, "ITAMP{}MF")

class SA_TAMP_SCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SCR", "TAMP status clear register")
        self.CTAMP1F = BitField(self, 0x00000001, "CTAMP1F", "CTAMP1F")
        self.CTAMP2F = BitField(self, 0x00000002, "CTAMP2F", "CTAMP2F")
        self.CTAMP3F = BitField(self, 0x00000004, "CTAMP3F", "CTAMP3F")
        self.CITAMP3F = BitField(self, 0x00040000, "CITAMP3F", "CITAMP3F")
        self.CITAMP4F = BitField(self, 0x00080000, "CITAMP4F", "CITAMP4F")
        self.CITAMP5F = BitField(self, 0x00100000, "CITAMP5F", "CITAMP5F")
        self.CITAMP6F = BitField(self, 0x00200000, "CITAMP6F", "CITAMP6F")
        self.CTAMPF = Subscriptor(self, "CTAMP{}F")
        self.CITAMPF = Subscriptor(self, "CITAMP{}F")

class SA_TAMP_BKP0R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP0R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP1R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP2R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP3R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP3R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP4R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP4R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP5R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP5R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP6R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP6R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP7R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP7R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP8R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP8R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP9R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP9R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP10R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP10R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP11R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP11R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP12R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP12R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP13R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP13R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP14R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP14R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP15R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP15R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP16R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP16R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP17R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP17R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP18R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP18R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP19R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP19R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP20R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP20R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP21R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP21R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP22R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP22R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP23R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP23R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP24R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP24R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP25R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP25R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP26R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP26R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP27R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP27R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP28R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP28R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP29R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP29R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP30R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP30R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP_BKP31R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BKP31R", "TAMP backup register")
        self.BKP = BitField(self, 0xFFFFFFFF, "BKP", "BKP")

class SA_TAMP(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "Tamper and backup registers")
        self.CR1 = SA_TAMP_CR1(self, 0x0)
        self.CR2 = SA_TAMP_CR2(self, 0x4)
        self.FLTCR = SA_TAMP_FLTCR(self, 0xC)
        self.IER = SA_TAMP_IER(self, 0x2C)
        self.SR = SA_TAMP_SR(self, 0x30)
        self.MISR = SA_TAMP_MISR(self, 0x34)
        self.SCR = SA_TAMP_SCR(self, 0x3C)
        self.BKP0R = SA_TAMP_BKP0R(self, 0x100)
        self.BKP1R = SA_TAMP_BKP1R(self, 0x104)
        self.BKP2R = SA_TAMP_BKP2R(self, 0x108)
        self.BKP3R = SA_TAMP_BKP3R(self, 0x10C)
        self.BKP4R = SA_TAMP_BKP4R(self, 0x110)
        self.BKP5R = SA_TAMP_BKP5R(self, 0x114)
        self.BKP6R = SA_TAMP_BKP6R(self, 0x118)
        self.BKP7R = SA_TAMP_BKP7R(self, 0x11C)
        self.BKP8R = SA_TAMP_BKP8R(self, 0x120)
        self.BKP9R = SA_TAMP_BKP9R(self, 0x124)
        self.BKP10R = SA_TAMP_BKP10R(self, 0x128)
        self.BKP11R = SA_TAMP_BKP11R(self, 0x12C)
        self.BKP12R = SA_TAMP_BKP12R(self, 0x130)
        self.BKP13R = SA_TAMP_BKP13R(self, 0x134)
        self.BKP14R = SA_TAMP_BKP14R(self, 0x138)
        self.BKP15R = SA_TAMP_BKP15R(self, 0x13C)
        self.BKP16R = SA_TAMP_BKP16R(self, 0x140)
        self.BKP17R = SA_TAMP_BKP17R(self, 0x144)
        self.BKP18R = SA_TAMP_BKP18R(self, 0x148)
        self.BKP19R = SA_TAMP_BKP19R(self, 0x14C)
        self.BKP20R = SA_TAMP_BKP20R(self, 0x150)
        self.BKP21R = SA_TAMP_BKP21R(self, 0x154)
        self.BKP22R = SA_TAMP_BKP22R(self, 0x158)
        self.BKP23R = SA_TAMP_BKP23R(self, 0x15C)
        self.BKP24R = SA_TAMP_BKP24R(self, 0x160)
        self.BKP25R = SA_TAMP_BKP25R(self, 0x164)
        self.BKP26R = SA_TAMP_BKP26R(self, 0x168)
        self.BKP27R = SA_TAMP_BKP27R(self, 0x16C)
        self.BKP28R = SA_TAMP_BKP28R(self, 0x170)
        self.BKP29R = SA_TAMP_BKP29R(self, 0x174)
        self.BKP30R = SA_TAMP_BKP30R(self, 0x178)
        self.BKP31R = SA_TAMP_BKP31R(self, 0x17C)
        self.BKPR = Subscriptor(self, "BKP{}R")

TAMP = SA_TAMP(0x40002400, "TAMP")

class SA_FDCAN_CREL(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x32141218, "CREL", "FDCAN core release register")
        self.DAY = BitField(self, 0x000000FF, "DAY", "18")
        self.MON = BitField(self, 0x0000FF00, "MON", "12")
        self.YEAR = BitField(self, 0x000F0000, "YEAR", "4")
        self.SUBSTEP = BitField(self, 0x00F00000, "SUBSTEP", "1")
        self.STEP = BitField(self, 0x0F000000, "STEP", "2")
        self.REL = BitField(self, 0xF0000000, "REL", "3")

class SA_FDCAN_ENDN(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x87654321, "ENDN", "FDCAN endian register")
        self.ETV = BitField(self, 0xFFFFFFFF, "ETV", "Endianness test value. The endianness test value is 0x8765 4321.")

class SA_FDCAN_DBTP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xA33, "DBTP", "FDCAN data bit timing and prescaler register")
        self.DSJW = BitField(self, 0x0000000F, "DSJW", "Synchronization jump width. Must always be smaller than DTSEG2, valid values are 0 to 15. The value used by the hardware is the one programmed, incremented by 1: t<sub>SJW</sub> = (DSJW + 1) x tq.")
        self.DTSEG2 = BitField(self, 0x000000F0, "DTSEG2", "Data time segment after sample point. Valid values are 0 to 15. The value used by the hardware is the one programmed, incremented by 1, i.e. t<sub>BS2</sub> = (DTSEG2 + 1) x tq.")
        self.DTSEG1 = BitField(self, 0x00001F00, "DTSEG1", "Data time segment before sample point. Valid values are 0 to 31. The value used by the hardware is the one programmed, incremented by 1, i.e. t<sub>BS1</sub> = (DTSEG1 + 1) x tq.")
        self.DBRP = BitField(self, 0x001F0000, "DBRP", "Data bit rate prescaler. The value by which the oscillator frequency is divided to generate the bit time quanta. The bit time is built up from a multiple of this quanta. Valid values for the Baud Rate Prescaler are 0 to 31. The hardware interpreters this value as the value programmed plus 1.")
        self.TDC = BitField(self, 0x00800000, "TDC", "Transceiver delay compensation")
        self.DTSEG = Subscriptor(self, "DTSEG{}")

class SA_FDCAN_TEST(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TEST", "FDCAN test register")
        self.LBCK = BitField(self, 0x00000010, "LBCK", "Loop back mode")
        self.TX = BitField(self, 0x00000060, "TX", "Control of transmit pin")
        self.RX = BitField(self, 0x00000080, "RX", "Receive pin. Monitors the actual value of pin FDCANx_RX")

class SA_FDCAN_RWD(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RWD", "FDCAN RAM watchdog register")
        self.WDC = BitField(self, 0x000000FF, "WDC", "Watchdog configuration. Start value of the message RAM watchdog counter. With the reset value of 00, the counter is disabled. These are protected write (P) bits, write access is possible only when the bit 1 [CCE] and bit 0 [INIT] of FDCAN_CCCR register are set to 1.")
        self.WDV = BitField(self, 0x0000FF00, "WDV", "Watchdog value. Actual message RAM watchdog counter value.")

class SA_FDCAN_CCCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x1, "CCCR", "FDCAN CC control register")
        self.INIT = BitField(self, 0x00000001, "INIT", "Initialization")
        self.CCE = BitField(self, 0x00000002, "CCE", "Configuration change enable")
        self.ASM = BitField(self, 0x00000004, "ASM", "ASM restricted operation mode. The restricted operation mode is intended for applications that adapt themselves to different CAN bit rates. The application tests different bit rates and leaves the Restricted operation Mode after it has received a valid frame. In the optional Restricted operation Mode the node is able to transmit and receive data and remote frames and it gives acknowledge to valid frames, but it does not send active error frames or overload frames. In case of an error condition or overload condition, it does not send dominant bits, instead it waits for the occurrence of bus idle condition to resynchronize itself to the CAN communication. The error counters are not incremented. Bit ASM can only be set by software when both CCE and INIT are set to 1. The bit can be reset by the software at any time.")
        self.CSA = BitField(self, 0x00000008, "CSA", "Clock stop acknowledge")
        self.CSR = BitField(self, 0x00000010, "CSR", "Clock stop request")
        self.MON = BitField(self, 0x00000020, "MON", "Bus monitoring mode. Bit MON can only be set by software when both CCE and INIT are set to 1. The bit can be reset by the Host at any time.")
        self.DAR = BitField(self, 0x00000040, "DAR", "Disable automatic retransmission")
        self.TEST = BitField(self, 0x00000080, "TEST", "Test mode enable")
        self.FDOE = BitField(self, 0x00000100, "FDOE", "FD operation enable")
        self.BRSE = BitField(self, 0x00000200, "BRSE", "FDCAN bit rate switching")
        self.PXHD = BitField(self, 0x00001000, "PXHD", "Protocol exception handling disable")
        self.EFBI = BitField(self, 0x00002000, "EFBI", "Edge filtering during bus integration")
        self.TXP = BitField(self, 0x00004000, "TXP", "If this bit is set, the FDCAN pauses for two CAN bit times before starting the next transmission after successfully transmitting a frame.")
        self.NISO = BitField(self, 0x00008000, "NISO", "Non ISO operation. If this bit is set, the FDCAN uses the CAN FD frame format as specified by the Bosch CAN FD Specification V1.0.")

class SA_FDCAN_NBTP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x6000A03, "NBTP", "FDCAN nominal bit timing and prescaler register")
        self.NTSEG2 = BitField(self, 0x0000007F, "NTSEG2", "Nominal time segment after sample point. Valid values are 0 to 127. The actual interpretation by the hardware of this value is such that one more than the programmed value is used.")
        self.NTSEG1 = BitField(self, 0x0000FF00, "NTSEG1", "Nominal time segment before sample point. Valid values are 0 to 255. The actual interpretation by the hardware of this value is such that one more than the programmed value is used. These are protected write (P) bits, write access is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.NBRP = BitField(self, 0x01FF0000, "NBRP", "Bit rate prescaler. Value by which the oscillator frequency is divided for generating the bit time quanta. The bit time is built up from a multiple of this quanta. Valid values are 0 to 511. The actual interpretation by the hardware of this value is such that one more than the value programmed here is used. These are protected write (P) bits, write access is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.NSJW = BitField(self, 0xFE000000, "NSJW", "Nominal (re)synchronization jump width. Valid values are 0 to 127. The actual interpretation by the hardware of this value is such that the used value is the one programmed incremented by one. These are protected write (P) bits, write access is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.NTSEG = Subscriptor(self, "NTSEG{}")

class SA_FDCAN_TSCC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TSCC", "FDCAN timestamp counter configuration register")
        self.TSS = BitField(self, 0x00000003, "TSS", "Timestamp select. These are protected write (P) bits, write access is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.TCP = BitField(self, 0x000F0000, "TCP", "Timestamp counter prescaler")

class SA_FDCAN_TSCV(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TSCV", "FDCAN timestamp counter value register")
        self.TSC = BitField(self, 0x0000FFFF, "TSC", "Timestamp counter")

class SA_FDCAN_TOCC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF0000, "TOCC", "FDCAN timeout counter configuration register")
        self.ETOC = BitField(self, 0x00000001, "ETOC", "Timeout counter enable. This is a protected write (P) bit, write access is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.TOS = BitField(self, 0x00000006, "TOS", "Timeout select. When operating in Continuous mode, a write to TOCV presets the counter to the value configured by TOCC[TOP] and continues down-counting. When the timeout counter is controlled by one of the FIFOs, an empty FIFO presets the counter to the value configured by TOCC[TOP]. Down-counting is started when the first FIFO element is stored. These are protected write (P) bits, write access is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.TOP = BitField(self, 0xFFFF0000, "TOP", "Timeout period. Start value of the timeout counter (down-counter). Configures the timeout period.")

class SA_FDCAN_TOCV(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0xFFFF, "TOCV", "FDCAN timeout counter value register")
        self.TOC = BitField(self, 0x0000FFFF, "TOC", "Timeout counter")

class SA_FDCAN_ECR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ECR", "FDCAN error counter register")
        self.TEC = BitField(self, 0x000000FF, "TEC", "Transmit error counter. Actual state of the transmit error counter, values between 0 and 255. When CCCR.ASM is set, the CAN protocol controller does not increment TEC and REC when a CAN protocol error is detected, but CEL is still incremented.")
        self.REC = BitField(self, 0x00007F00, "REC", "Receive error counter. Actual state of the receive error counter, values between 0 and 127.")
        self.RP = BitField(self, 0x00008000, "RP", "Receive error passive")
        self.CEL = BitField(self, 0x00FF0000, "CEL", "CAN error logging. The counter is incremented each time when a CAN protocol error causes the transmit error counter or the receive error counter to be incremented. It is reset by read access to CEL. The counter stops at 0xFF; the next increment of TEC or REC sets interrupt flag IR[ELO]. Access type is RX: reset on read.")

class SA_FDCAN_PSR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x707, "PSR", "FDCAN protocol status register")
        self.LEC = BitField(self, 0x00000007, "LEC", "Last error code. The LEC indicates the type of the last error to occur on the CAN bus. This field is cleared to 0 when a message has been transferred (reception or transmission) without error. Access type is RS: set on read.")
        self.ACT = BitField(self, 0x00000018, "ACT", "Activity. Monitors the modules CAN communication state.")
        self.EP = BitField(self, 0x00000020, "EP", "Error passive")
        self.EW = BitField(self, 0x00000040, "EW", "Warning Sstatus")
        self.BO = BitField(self, 0x00000080, "BO", "Bus_Off status")
        self.DLEC = BitField(self, 0x00000700, "DLEC", "Data last error code. Type of last error that occurred in the data phase of a FDCAN format frame with its BRS flag set. Coding is the same as for LEC. This field is cleared to 0 when a FDCAN format frame with its BRS flag set has been transferred (reception or transmission) without error. Access type is RS: set on read.")
        self.RESI = BitField(self, 0x00000800, "RESI", "ESI flag of last received FDCAN message. This bit is set together with REDL, independent of acceptance filtering. Access type is RX: reset on read.")
        self.RBRS = BitField(self, 0x00001000, "RBRS", "BRS flag of last received FDCAN message. This bit is set together with REDL, independent of acceptance filtering. Access type is RX: reset on read.")
        self.REDL = BitField(self, 0x00002000, "REDL", "Received FDCAN message. This bit is set independent of acceptance filtering. Access type is RX: reset on read.")
        self.PXE = BitField(self, 0x00004000, "PXE", "Protocol exception event")
        self.TDCV = BitField(self, 0x007F0000, "TDCV", "Transmitter delay compensation value. Position of the secondary sample point, defined by the sum of the measured delay from FDCAN_TX to FDCAN_RX and TDCR.TDCO. The SSP position is, in the data phase, the number of minimum time quanta (mtq) between the start of the transmitted bit and the secondary sample point. Valid values are 0 to 127 mtq.")

class SA_FDCAN_TDCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TDCR", "FDCAN transmitter delay compensation register")
        self.TDCF = BitField(self, 0x0000007F, "TDCF", "Transmitter delay compensation filter window length. Defines the minimum value for the SSP position, dominant edges on FDCAN_RX that would result in an earlier SSP position are ignored for transmitter delay measurements. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.TDCO = BitField(self, 0x00007F00, "TDCO", "Transmitter delay compensation offset. Offset value defining the distance between the measured delay from FDCAN_TX to FDCAN_RX and the secondary sample point. Valid values are 0 to 127 mtq. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")

class SA_FDCAN_IR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IR", "FDCAN interrupt register")
        self.RF0N = BitField(self, 0x00000001, "RF0N", "Rx FIFO 0 new message")
        self.RF0F = BitField(self, 0x00000002, "RF0F", "Rx FIFO 0 full")
        self.RF0L = BitField(self, 0x00000004, "RF0L", "Rx FIFO 0 message lost")
        self.RF1N = BitField(self, 0x00000008, "RF1N", "Rx FIFO 1 new message")
        self.RF1F = BitField(self, 0x00000010, "RF1F", "Rx FIFO 1 full")
        self.RF1L = BitField(self, 0x00000020, "RF1L", "Rx FIFO 1 message lost")
        self.HPM = BitField(self, 0x00000040, "HPM", "High-priority message")
        self.TC = BitField(self, 0x00000080, "TC", "Transmission completed")
        self.TCF = BitField(self, 0x00000100, "TCF", "Transmission cancellation finished")
        self.TFE = BitField(self, 0x00000200, "TFE", "Tx FIFO empty")
        self.TEFN = BitField(self, 0x00000400, "TEFN", "Tx event FIFO New Entry")
        self.TEFF = BitField(self, 0x00000800, "TEFF", "Tx event FIFO full")
        self.TEFL = BitField(self, 0x00001000, "TEFL", "Tx event FIFO element lost")
        self.TSW = BitField(self, 0x00002000, "TSW", "Timestamp wraparound")
        self.MRAF = BitField(self, 0x00004000, "MRAF", "Message RAM access failure. The flag is set when the Rx handler: has not completed acceptance filtering or storage of an accepted message until the arbitration field of the following message has been received. In this case acceptance filtering or message storage is aborted and the Rx handler starts processing of the following message. was unable to write a message to the message RAM. In this case message storage is aborted. In both cases the FIFO put index is not updated. The partly stored message is overwritten when the next message is stored to this location. The flag is also set when the Tx Handler was not able to read a message from the Message RAM in time. In this case message transmission is aborted. In case of a Tx Handler access failure the FDCAN is switched into Restricted operation Mode (see Restricted operation mode). To leave Restricted operation Mode, the Host CPU has to reset CCCR.ASM.")
        self.TOO = BitField(self, 0x00008000, "TOO", "Timeout occurred")
        self.ELO = BitField(self, 0x00010000, "ELO", "Error logging overflow")
        self.EP = BitField(self, 0x00020000, "EP", "Error passive")
        self.EW = BitField(self, 0x00040000, "EW", "Warning status")
        self.BO = BitField(self, 0x00080000, "BO", "Bus_Off status")
        self.WDI = BitField(self, 0x00100000, "WDI", "Watchdog interrupt")
        self.PEA = BitField(self, 0x00200000, "PEA", "Protocol error in arbitration phase (nominal bit time is used)")
        self.PED = BitField(self, 0x00400000, "PED", "Protocol error in data phase (data bit time is used)")
        self.ARA = BitField(self, 0x00800000, "ARA", "Access to reserved address")
        self.RFN = Subscriptor(self, "RF{}N")
        self.RFF = Subscriptor(self, "RF{}F")
        self.RFL = Subscriptor(self, "RF{}L")

class SA_FDCAN_IE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IE", "FDCAN interrupt enable register")
        self.RF0NE = BitField(self, 0x00000001, "RF0NE", "Rx FIFO 0 new message interrupt enable")
        self.RF0FE = BitField(self, 0x00000002, "RF0FE", "Rx FIFO 0 full interrupt enable")
        self.RF0LE = BitField(self, 0x00000004, "RF0LE", "Rx FIFO 0 message lost interrupt enable")
        self.RF1NE = BitField(self, 0x00000008, "RF1NE", "Rx FIFO 1 new message interrupt enable")
        self.RF1FE = BitField(self, 0x00000010, "RF1FE", "Rx FIFO 1 full interrupt enable")
        self.RF1LE = BitField(self, 0x00000020, "RF1LE", "Rx FIFO 1 message lost interrupt enable")
        self.HPME = BitField(self, 0x00000040, "HPME", "High-priority message interrupt enable")
        self.TCE = BitField(self, 0x00000080, "TCE", "Transmission completed interrupt enable")
        self.TCFE = BitField(self, 0x00000100, "TCFE", "Transmission cancellation finished interrupt enable")
        self.TFEE = BitField(self, 0x00000200, "TFEE", "Tx FIFO empty interrupt enable")
        self.TEFNE = BitField(self, 0x00000400, "TEFNE", "Tx event FIFO new entry interrupt enable")
        self.TEFFE = BitField(self, 0x00000800, "TEFFE", "Tx event FIFO full interrupt enable")
        self.TEFLE = BitField(self, 0x00001000, "TEFLE", "Tx event FIFO element lost interrupt enable")
        self.TSWE = BitField(self, 0x00002000, "TSWE", "Timestamp wraparound interrupt enable")
        self.MRAFE = BitField(self, 0x00004000, "MRAFE", "Message RAM access failure interrupt enable")
        self.TOOE = BitField(self, 0x00008000, "TOOE", "Timeout occurred interrupt enable")
        self.ELOE = BitField(self, 0x00010000, "ELOE", "Error logging overflow interrupt enable")
        self.EPE = BitField(self, 0x00020000, "EPE", "Error passive interrupt enable")
        self.EWE = BitField(self, 0x00040000, "EWE", "Warning status interrupt enable")
        self.BOE = BitField(self, 0x00080000, "BOE", "Bus_Off status")
        self.WDIE = BitField(self, 0x00100000, "WDIE", "Watchdog interrupt enable")
        self.PEAE = BitField(self, 0x00200000, "PEAE", "Protocol error in arbitration phase enable")
        self.PEDE = BitField(self, 0x00400000, "PEDE", "Protocol error in data phase enable")
        self.ARAE = BitField(self, 0x00800000, "ARAE", "Access to reserved address enable")
        self.RFLE = Subscriptor(self, "RF{}LE")
        self.RFNE = Subscriptor(self, "RF{}NE")
        self.RFFE = Subscriptor(self, "RF{}FE")

class SA_FDCAN_ILS(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ILS", "FDCAN interrupt line select register")
        self.RXFIFO0 = BitField(self, 0x00000001, "RXFIFO0", "RX FIFO bit grouping the following interruption. RF0LL: Rx FIFO 0 message lost interrupt line RF0FL: Rx FIFO 0 full interrupt line RF0NL: Rx FIFO 0 new message interrupt line")
        self.RXFIFO1 = BitField(self, 0x00000002, "RXFIFO1", "RX FIFO bit grouping the following interruption. RF1LL: Rx FIFO 1 message lost interrupt line RF1FL: Rx FIFO 1 full interrupt line RF1NL: Rx FIFO 1 new message interrupt line")
        self.SMSG = BitField(self, 0x00000004, "SMSG", "Status message bit grouping the following interruption. TCFL: Transmission cancellation finished interrupt line TCL: Transmission completed interrupt line HPML: High-priority message interrupt line")
        self.TFERR = BitField(self, 0x00000008, "TFERR", "Tx FIFO ERROR grouping the following interruption. TEFLL: Tx event FIFO element lost interrupt line TEFFL: Tx event FIFO full interrupt line TEFNL: Tx event FIFO new entry interrupt line TFEL: Tx FIFO empty interrupt line")
        self.MISC = BitField(self, 0x00000010, "MISC", "Interrupt regrouping the following interruption. TOOL: Timeout occurred interrupt line MRAFL: Message RAM access failure interrupt line TSWL: Timestamp wraparound interrupt line")
        self.BERR = BitField(self, 0x00000020, "BERR", "Bit and line error grouping the following interruption . EPL Error passive interrupt line ELOL: Error logging overflow interrupt line")
        self.PERR = BitField(self, 0x00000040, "PERR", "Protocol error grouping the following interruption . ARAL: Access to reserved address line PEDL: Protocol error in data phase line PEAL: Protocol error in arbitration phase line WDIL: Watchdog interrupt line BOL: Bus_Off status EWL: Warning status interrupt line")
        self.RXFIFO = Subscriptor(self, "RXFIFO{}")

class SA_FDCAN_ILE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ILE", "FDCAN interrupt line enable register")
        self.EINT0 = BitField(self, 0x00000001, "EINT0", "Enable interrupt line 0")
        self.EINT1 = BitField(self, 0x00000002, "EINT1", "Enable interrupt line 1")
        self.EINT = Subscriptor(self, "EINT{}")

class SA_FDCAN_RXGFC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXGFC", "FDCAN global filter configuration register")
        self.RRFE = BitField(self, 0x00000001, "RRFE", "Reject remote frames extended. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.RRFS = BitField(self, 0x00000002, "RRFS", "Reject remote frames standard. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.ANFE = BitField(self, 0x0000000C, "ANFE", "Accept non-matching frames extended. Defines how received messages with 29-bit IDs that do not match any element of the filter list are treated. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.ANFS = BitField(self, 0x00000030, "ANFS", "Accept Non-matching frames standard. Defines how received messages with 11-bit IDs that do not match any element of the filter list are treated. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.F1OM = BitField(self, 0x00000100, "F1OM", "FIFO 1 operation mode (overwrite or blocking). This is a protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.F0OM = BitField(self, 0x00000200, "F0OM", "FIFO 0 operation mode (overwrite or blocking). This is protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.LSS = BitField(self, 0x001F0000, "LSS", "List size standard. 1 to 28: Number of standard message ID filter elements >28: Values greater than 28 are interpreted as 28. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.LSE = BitField(self, 0x0F000000, "LSE", "List size extended. 1 to 8: Number of extended message ID filter elements >8: Values greater than 8 are interpreted as 8. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")
        self.FOM = Subscriptor(self, "F{}OM")

class SA_FDCAN_XIDAM(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x1FFFFFFF, "XIDAM", "FDCAN extended ID and mask register")
        self.EIDM = BitField(self, 0x1FFFFFFF, "EIDM", "Extended ID mask. For acceptance filtering of extended frames the Extended ID AND Mask is AND-ed with the Message ID of a received frame. Intended for masking of 29-bit IDs in SAE J1939. With the reset value of all bits set to 1 the mask is not active. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")

class SA_FDCAN_HPMS(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "HPMS", "FDCAN high-priority message status register")
        self.BIDX = BitField(self, 0x00000007, "BIDX", "Buffer index. Index of Rx FIFO element to which the message was stored. Only valid when MSI[1] = 1.")
        self.MSI = BitField(self, 0x000000C0, "MSI", "Message storage indicator")
        self.FIDX = BitField(self, 0x00001F00, "FIDX", "Filter index. Index of matching filter element. Range is 0 to RXGFC[LSS] - 1 or RXGFC[LSE] - 1.")
        self.FLST = BitField(self, 0x00008000, "FLST", "Filter list. Indicates the filter list of the matching filter element.")

class SA_FDCAN_RXF0S(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXF0S", "FDCAN Rx FIFO 0 status register")
        self.F0FL = BitField(self, 0x0000000F, "F0FL", "Rx FIFO 0 fill level. Number of elements stored in Rx FIFO 0, range 0 to 3.")
        self.F0GI = BitField(self, 0x00000300, "F0GI", "Rx FIFO 0 get index. Rx FIFO 0 read index pointer, range 0 to 2.")
        self.F0PI = BitField(self, 0x00030000, "F0PI", "Rx FIFO 0 put index. Rx FIFO 0 write index pointer, range 0 to 2.")
        self.F0F = BitField(self, 0x01000000, "F0F", "Rx FIFO 0 full")
        self.RF0L = BitField(self, 0x02000000, "RF0L", "Rx FIFO 0 message lost. This bit is a copy of interrupt flag IR[RF0L]. When IR[RF0L] is reset, this bit is also reset.")

class SA_FDCAN_RXF0A(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXF0A", "CAN Rx FIFO 0 acknowledge register")
        self.F0AI = BitField(self, 0x00000007, "F0AI", "Rx FIFO 0 acknowledge index. After the Host has read a message or a sequence of messages from Rx FIFO 0 it has to write the buffer index of the last element read from Rx FIFO 0 to F0AI. This sets the Rx FIFO 0 get index RXF0S[F0GI] to F0AI + 1 and update the FIFO 0 fill level RXF0S[F0FL].")

class SA_FDCAN_RXF1S(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXF1S", "FDCAN Rx FIFO 1 status register")
        self.F1FL = BitField(self, 0x0000000F, "F1FL", "Rx FIFO 1 fill level. Number of elements stored in Rx FIFO 1, range 0 to 3.")
        self.F1GI = BitField(self, 0x00000300, "F1GI", "Rx FIFO 1 get index. Rx FIFO 1 read index pointer, range 0 to 2.")
        self.F1PI = BitField(self, 0x00030000, "F1PI", "Rx FIFO 1 put index. Rx FIFO 1 write index pointer, range 0 to 2.")
        self.F1F = BitField(self, 0x01000000, "F1F", "Rx FIFO 1 full")
        self.RF1L = BitField(self, 0x02000000, "RF1L", "Rx FIFO 1 message lost. This bit is a copy of interrupt flag IR[RF1L]. When IR[RF1L] is reset, this bit is also reset.")

class SA_FDCAN_RXF1A(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXF1A", "FDCAN Rx FIFO 1 acknowledge register")
        self.F1AI = BitField(self, 0x00000007, "F1AI", "Rx FIFO 1 acknowledge index. After the Host has read a message or a sequence of messages from Rx FIFO 1 it has to write the buffer index of the last element read from Rx FIFO 1 to F1AI. This sets the Rx FIFO 1 get index RXF1S[F1GI] to F1AI + 1 and update the FIFO 1 Fill Level RXF1S[F1FL].")

class SA_FDCAN_TXBC(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBC", "FDCAN Tx buffer configuration register")
        self.TFQM = BitField(self, 0x01000000, "TFQM", "Tx FIFO/queue mode. This is a protected write (P) bit, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")

class SA_FDCAN_TXFQS(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x3, "TXFQS", "FDCAN Tx FIFO/queue status register")
        self.TFFL = BitField(self, 0x00000007, "TFFL", "Tx FIFO free level. Number of consecutive free Tx FIFO elements starting from TFGI, range 0 to 3. Read as 0 when Tx queue operation is configured (TXBC[TFQM] = 1).")
        self.TFGI = BitField(self, 0x00000300, "TFGI", "Tx FIFO get index. Tx FIFO read index pointer, range 0 to 3. Read as 0 when Tx queue operation is configured (TXBC.TFQM = 1)")
        self.TFQPI = BitField(self, 0x00030000, "TFQPI", "Tx FIFO/queue put index. Tx FIFO/queue write index pointer, range 0 to 3")
        self.TFQF = BitField(self, 0x00200000, "TFQF", "Tx FIFO/queue full")

class SA_FDCAN_TXBRP(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBRP", "FDCAN Tx buffer request pending register")
        self.TRP = BitField(self, 0x00000007, "TRP", "Transmission request pending. Each Tx buffer has its own transmission request pending bit. The bits are set via register TXBAR. The bits are reset after a requested transmission has completed or has been canceled via register TXBCR. After a TXBRP bit has been set, a Tx scan is started to check for the pending Tx request with the highest priority (Tx buffer with lowest Message ID). A cancellation request resets the corresponding transmission request pending bit of register TXBRP. In case a transmission has already been started when a cancellation is requested, this is done at the end of the transmission, regardless whether the transmission was successful or not. The cancellation request bits are reset directly after the corresponding TXBRP bit has been reset. After a cancellation has been requested, a finished cancellation is signaled via TXBCF after successful transmission together with the corresponding TXBTO bit when the transmission has not yet been started at the point of cancellation when the transmission has been aborted due to lost arbitration when an error occurred during frame transmission In DAR mode all transmissions are automatically canceled if they are not successful. The corresponding TXBCF bit is set for all unsuccessful transmissions.")

class SA_FDCAN_TXBAR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBAR", "FDCAN Tx buffer add request register")
        self.AR = BitField(self, 0x00000007, "AR", "Add request. Each Tx buffer has its own add request bit. Writing a 1 sets the corresponding add request bit; writing a 0 has no impact. This enables the Host to set transmission requests for multiple Tx buffers with one write to TXBAR. When no Tx scan is running, the bits are reset immediately, else the bits remain set until the Tx scan process has completed.")

class SA_FDCAN_TXBCR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBCR", "FDCAN Tx buffer cancellation request register")
        self.CR = BitField(self, 0x00000007, "CR", "Cancellation request. Each Tx buffer has its own cancellation request bit. Writing a 1 sets the corresponding CR bit; writing a 0 has no impact. This enables the Host to set cancellation requests for multiple Tx buffers with one write to TXBCR. The bits remain set until the corresponding TXBRP bit is reset.")

class SA_FDCAN_TXBTO(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBTO", "FDCAN Tx buffer transmission occurred register")
        self.TO = BitField(self, 0x00000007, "TO", "Transmission occurred.. Each Tx buffer has its own TO bit. The bits are set when the corresponding TXBRP bit is cleared after a successful transmission. The bits are reset when a new transmission is requested by writing a 1 to the corresponding bit of register TXBAR.")

class SA_FDCAN_TXBCF(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBCF", "FDCAN Tx buffer cancellation finished register")
        self.CF = BitField(self, 0x00000007, "CF", "Cancellation finished. Each Tx buffer has its own CF bit. The bits are set when the corresponding TXBRP bit is cleared after a cancellation was requested via TXBCR. In case the corresponding TXBRP bit was not set at the point of cancellation, CF is set immediately. The bits are reset when a new transmission is requested by writing a 1 to the corresponding bit of register TXBAR.")

class SA_FDCAN_TXBTIE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBTIE", "FDCAN Tx buffer transmission interrupt enable register")
        self.TIE = BitField(self, 0x00000007, "TIE", "Transmission interrupt enable. Each Tx buffer has its own TIE bit.")

class SA_FDCAN_TXBCIE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXBCIE", "FDCAN Tx buffer cancellation finished interrupt enable register")
        self.CFIE = BitField(self, 0x00000007, "CFIE", "Cancellation finished interrupt enable.. Each Tx buffer has its own CFIE bit.")

class SA_FDCAN_TXEFS(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXEFS", "FDCAN Tx event FIFO status register")
        self.EFFL = BitField(self, 0x00000007, "EFFL", "Event FIFO fill level. Number of elements stored in Tx event FIFO, range 0 to 3.")
        self.EFGI = BitField(self, 0x00000300, "EFGI", "Event FIFO get index. Tx event FIFO read index pointer, range 0 to 3.")
        self.EFPI = BitField(self, 0x00030000, "EFPI", "Event FIFO put index. Tx event FIFO write index pointer, range 0 to 3.")
        self.EFF = BitField(self, 0x01000000, "EFF", "Event FIFO full")
        self.TEFL = BitField(self, 0x02000000, "TEFL", "Tx event FIFO element lost. This bit is a copy of interrupt flag IR[TEFL]. When IR[TEFL] is reset, this bit is also reset. 0 No Tx event FIFO element lost 1 Tx event FIFO element lost, also set after write attempt to Tx event FIFO of size 0.")

class SA_FDCAN_TXEFA(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXEFA", "FDCAN Tx event FIFO acknowledge register")
        self.EFAI = BitField(self, 0x00000003, "EFAI", "Event FIFO acknowledge index. After the Host has read an element or a sequence of elements from the Tx event FIFO, it has to write the index of the last element read from Tx event FIFO to EFAI. This sets the Tx event FIFO get index TXEFS[EFGI] to EFAI + 1 and updates the FIFO 0 fill level TXEFS[EFFL].")

class SA_FDCAN_CKDIV(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CKDIV", "FDCAN CFG clock divider register")
        self.PDIV = BitField(self, 0x0000000F, "PDIV", "input clock divider. The APB clock could be divided prior to be used by the CAN sub system. The rate must be computed using the divider output clock. These are protected write (P) bits, which means that write access by the bits is possible only when the bit 1 [CCE] and bit 0 [INIT] of CCCR register are set to 1.")

class SA_FDCAN(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "FDCAN")
        self.CREL = SA_FDCAN_CREL(self, 0x0)
        self.ENDN = SA_FDCAN_ENDN(self, 0x4)
        self.DBTP = SA_FDCAN_DBTP(self, 0xC)
        self.TEST = SA_FDCAN_TEST(self, 0x10)
        self.RWD = SA_FDCAN_RWD(self, 0x14)
        self.CCCR = SA_FDCAN_CCCR(self, 0x18)
        self.NBTP = SA_FDCAN_NBTP(self, 0x1C)
        self.TSCC = SA_FDCAN_TSCC(self, 0x20)
        self.TSCV = SA_FDCAN_TSCV(self, 0x24)
        self.TOCC = SA_FDCAN_TOCC(self, 0x28)
        self.TOCV = SA_FDCAN_TOCV(self, 0x2C)
        self.ECR = SA_FDCAN_ECR(self, 0x40)
        self.PSR = SA_FDCAN_PSR(self, 0x44)
        self.TDCR = SA_FDCAN_TDCR(self, 0x48)
        self.IR = SA_FDCAN_IR(self, 0x50)
        self.IE = SA_FDCAN_IE(self, 0x54)
        self.ILS = SA_FDCAN_ILS(self, 0x58)
        self.ILE = SA_FDCAN_ILE(self, 0x5C)
        self.RXGFC = SA_FDCAN_RXGFC(self, 0x80)
        self.XIDAM = SA_FDCAN_XIDAM(self, 0x84)
        self.HPMS = SA_FDCAN_HPMS(self, 0x88)
        self.RXF0S = SA_FDCAN_RXF0S(self, 0x90)
        self.RXF0A = SA_FDCAN_RXF0A(self, 0x94)
        self.RXF1S = SA_FDCAN_RXF1S(self, 0x98)
        self.RXF1A = SA_FDCAN_RXF1A(self, 0x9C)
        self.TXBC = SA_FDCAN_TXBC(self, 0xC0)
        self.TXFQS = SA_FDCAN_TXFQS(self, 0xC4)
        self.TXBRP = SA_FDCAN_TXBRP(self, 0xC8)
        self.TXBAR = SA_FDCAN_TXBAR(self, 0xCC)
        self.TXBCR = SA_FDCAN_TXBCR(self, 0xD0)
        self.TXBTO = SA_FDCAN_TXBTO(self, 0xD4)
        self.TXBCF = SA_FDCAN_TXBCF(self, 0xD8)
        self.TXBTIE = SA_FDCAN_TXBTIE(self, 0xDC)
        self.TXBCIE = SA_FDCAN_TXBCIE(self, 0xE0)
        self.TXEFS = SA_FDCAN_TXEFS(self, 0xE4)
        self.TXEFA = SA_FDCAN_TXEFA(self, 0xE8)
        self.CKDIV = SA_FDCAN_CKDIV(self, 0x100)
        self.RXFS = Subscriptor(self, "RXF{}S")
        self.RXFA = Subscriptor(self, "RXF{}A")

FDCAN = SA_FDCAN(0x4000A400, "FDCAN")
FDCAN1 = SA_FDCAN(0x40006400, "FDCAN1")
FDCAN2 = SA_FDCAN(0x40006800, "FDCAN2")
FDCAN3 = SA_FDCAN(0x40006C00, "FDCAN3")

class SA_UCPD1_CFG1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CFG1", "UCPD configuration register 1")
        self.HBITCLKDIV = BitField(self, 0x0000003F, "HBITCLKDIV", "HBITCLKDIV")
        self.IFRGAP = BitField(self, 0x000007C0, "IFRGAP", "IFRGAP")
        self.TRANSWIN = BitField(self, 0x0000F800, "TRANSWIN", "TRANSWIN")
        self.PSC_USBPDCLK = BitField(self, 0x000E0000, "PSC_USBPDCLK", "PSC_USBPDCLK")
        self.RXORDSETEN = BitField(self, 0x1FF00000, "RXORDSETEN", "RXORDSETEN")
        self.TXDMAEN = BitField(self, 0x20000000, "TXDMAEN", "TXDMAEN")
        self.RXDMAEN = BitField(self, 0x40000000, "RXDMAEN", "RXDMAEN")
        self.UCPDEN = BitField(self, 0x80000000, "UCPDEN", "UCPDEN")

class SA_UCPD1_CFG2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CFG2", "UCPD configuration register 2")
        self.RXFILTDIS = BitField(self, 0x00000001, "RXFILTDIS", "RXFILTDIS")
        self.RXFILT2N3 = BitField(self, 0x00000002, "RXFILT2N3", "RXFILT2N3")
        self.FORCECLK = BitField(self, 0x00000004, "FORCECLK", "FORCECLK")
        self.WUPEN = BitField(self, 0x00000008, "WUPEN", "WUPEN")

class SA_UCPD1_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CR", "UCPD configuration register 2")
        self.TXMODE = BitField(self, 0x00000003, "TXMODE", "TXMODE")
        self.TXSEND = BitField(self, 0x00000004, "TXSEND", "TXSEND")
        self.TXHRST = BitField(self, 0x00000008, "TXHRST", "TXHRST")
        self.RXMODE = BitField(self, 0x00000010, "RXMODE", "RXMODE")
        self.PHYRXEN = BitField(self, 0x00000020, "PHYRXEN", "PHYRXEN")
        self.PHYCCSEL = BitField(self, 0x00000040, "PHYCCSEL", "PHYCCSEL")
        self.ANASUBMODE = BitField(self, 0x00000180, "ANASUBMODE", "ANASUBMODE")
        self.ANAMODE = BitField(self, 0x00000200, "ANAMODE", "ANAMODE")
        self.CCENABLE = BitField(self, 0x00000C00, "CCENABLE", "CCENABLE")
        self.FRSRXEN = BitField(self, 0x00010000, "FRSRXEN", "FRSRXEN")
        self.FRSTX = BitField(self, 0x00020000, "FRSTX", "FRSTX")
        self.RDCH = BitField(self, 0x00040000, "RDCH", "RDCH")
        self.CC1TCDIS = BitField(self, 0x00100000, "CC1TCDIS", "CC1TCDIS")
        self.CC2TCDIS = BitField(self, 0x00200000, "CC2TCDIS", "CC2TCDIS")
        self.CCTCDIS = Subscriptor(self, "CC{}TCDIS")

class SA_UCPD1_IMR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "IMR", "UCPD Interrupt Mask Register")
        self.TXISIE = BitField(self, 0x00000001, "TXISIE", "TXISIE")
        self.TXMSGDISCIE = BitField(self, 0x00000002, "TXMSGDISCIE", "TXMSGDISCIE")
        self.TXMSGSENTIE = BitField(self, 0x00000004, "TXMSGSENTIE", "TXMSGSENTIE")
        self.TXMSGABTIE = BitField(self, 0x00000008, "TXMSGABTIE", "TXMSGABTIE")
        self.HRSTDISCIE = BitField(self, 0x00000010, "HRSTDISCIE", "HRSTDISCIE")
        self.HRSTSENTIE = BitField(self, 0x00000020, "HRSTSENTIE", "HRSTSENTIE")
        self.TXUNDIE = BitField(self, 0x00000040, "TXUNDIE", "TXUNDIE")
        self.RXNEIE = BitField(self, 0x00000100, "RXNEIE", "RXNEIE")
        self.RXORDDETIE = BitField(self, 0x00000200, "RXORDDETIE", "RXORDDETIE")
        self.RXHRSTDETIE = BitField(self, 0x00000400, "RXHRSTDETIE", "RXHRSTDETIE")
        self.RXOVRIE = BitField(self, 0x00000800, "RXOVRIE", "RXOVRIE")
        self.RXMSGENDIE = BitField(self, 0x00001000, "RXMSGENDIE", "RXMSGENDIE")
        self.TYPECEVT1IE = BitField(self, 0x00004000, "TYPECEVT1IE", "TYPECEVT1IE")
        self.TYPECEVT2IE = BitField(self, 0x00008000, "TYPECEVT2IE", "TYPECEVT2IE")
        self.FRSEVTIE = BitField(self, 0x00100000, "FRSEVTIE", "FRSEVTIE")
        self.TYPECEVTIE = Subscriptor(self, "TYPECEVT{}IE")

class SA_UCPD1_SR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "SR", "UCPD Status Register")
        self.TXIS = BitField(self, 0x00000001, "TXIS", "TXIS")
        self.TXMSGDISC = BitField(self, 0x00000002, "TXMSGDISC", "TXMSGDISC")
        self.TXMSGSENT = BitField(self, 0x00000004, "TXMSGSENT", "TXMSGSENT")
        self.TXMSGABT = BitField(self, 0x00000008, "TXMSGABT", "TXMSGABT")
        self.HRSTDISC = BitField(self, 0x00000010, "HRSTDISC", "HRSTDISC")
        self.HRSTSENT = BitField(self, 0x00000020, "HRSTSENT", "HRSTSENT")
        self.TXUND = BitField(self, 0x00000040, "TXUND", "TXUND")
        self.RXNE = BitField(self, 0x00000100, "RXNE", "RXNE")
        self.RXORDDET = BitField(self, 0x00000200, "RXORDDET", "RXORDDET")
        self.RXHRSTDET = BitField(self, 0x00000400, "RXHRSTDET", "RXHRSTDET")
        self.RXOVR = BitField(self, 0x00000800, "RXOVR", "RXOVR")
        self.RXMSGEND = BitField(self, 0x00001000, "RXMSGEND", "RXMSGEND")
        self.RXERR = BitField(self, 0x00002000, "RXERR", "RXERR")
        self.TYPECEVT1 = BitField(self, 0x00004000, "TYPECEVT1", "TYPECEVT1")
        self.TYPECEVT2 = BitField(self, 0x00008000, "TYPECEVT2", "TYPECEVT2")
        self.TYPEC_VSTATE_CC1 = BitField(self, 0x00030000, "TYPEC_VSTATE_CC1", "TYPEC_VSTATE_CC1")
        self.TYPEC_VSTATE_CC2 = BitField(self, 0x000C0000, "TYPEC_VSTATE_CC2", "TYPEC_VSTATE_CC2")
        self.FRSEVT = BitField(self, 0x00100000, "FRSEVT", "FRSEVT")
        self.TYPECEVT = Subscriptor(self, "TYPECEVT{}")
        self.TYPEC_VSTATE_CC = Subscriptor(self, "TYPEC_VSTATE_CC{}")

class SA_UCPD1_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "UCPD Interrupt Clear Register")
        self.TXMSGDISCCF = BitField(self, 0x00000002, "TXMSGDISCCF", "TXMSGDISCCF")
        self.TXMSGSENTCF = BitField(self, 0x00000004, "TXMSGSENTCF", "TXMSGSENTCF")
        self.TXMSGABTCF = BitField(self, 0x00000008, "TXMSGABTCF", "TXMSGABTCF")
        self.HRSTDISCCF = BitField(self, 0x00000010, "HRSTDISCCF", "HRSTDISCCF")
        self.HRSTSENTCF = BitField(self, 0x00000020, "HRSTSENTCF", "HRSTSENTCF")
        self.TXUNDCF = BitField(self, 0x00000040, "TXUNDCF", "TXUNDCF")
        self.RXORDDETCF = BitField(self, 0x00000200, "RXORDDETCF", "RXORDDETCF")
        self.RXHRSTDETCF = BitField(self, 0x00000400, "RXHRSTDETCF", "RXHRSTDETCF")
        self.RXOVRCF = BitField(self, 0x00000800, "RXOVRCF", "RXOVRCF")
        self.RXMSGENDCF = BitField(self, 0x00001000, "RXMSGENDCF", "RXMSGENDCF")
        self.TYPECEVT1CF = BitField(self, 0x00004000, "TYPECEVT1CF", "TYPECEVT1CF")
        self.TYPECEVT2CF = BitField(self, 0x00008000, "TYPECEVT2CF", "TYPECEVT2CF")
        self.FRSEVTCF = BitField(self, 0x00100000, "FRSEVTCF", "FRSEVTCF")
        self.TYPECEVTCF = Subscriptor(self, "TYPECEVT{}CF")

class SA_UCPD1_TX_ORDSET(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TX_ORDSET", "UCPD Tx Ordered Set Type Register")
        self.TXORDSET = BitField(self, 0x000FFFFF, "TXORDSET", "TXORDSET")

class SA_UCPD1_TX_PAYSZ(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TX_PAYSZ", "UCPD Tx Paysize Register")
        self.TXPAYSZ = BitField(self, 0x000003FF, "TXPAYSZ", "TXPAYSZ")

class SA_UCPD1_TXDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "TXDR", "UCPD Tx Data Register")
        self.TXDATA = BitField(self, 0x000000FF, "TXDATA", "TXDATA")

class SA_UCPD1_RX_ORDSET(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RX_ORDSET", "UCPD Rx Ordered Set Register")
        self.RXORDSET = BitField(self, 0x00000007, "RXORDSET", "RXORDSET")
        self.RXSOP3OF4 = BitField(self, 0x00000008, "RXSOP3OF4", "RXSOP3OF4")
        self.RXSOPKINVALID = BitField(self, 0x00000070, "RXSOPKINVALID", "RXSOPKINVALID")

class SA_UCPD1_RX_PAYSZ(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RX_PAYSZ", "UCPD Rx Paysize Register")
        self.RXPAYSZ = BitField(self, 0x000003FF, "RXPAYSZ", "RXPAYSZ")

class SA_UCPD1_RXDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RXDR", "UCPD Rx Data Register")
        self.RXDATA = BitField(self, 0x000000FF, "RXDATA", "RXDATA")

class SA_UCPD1_RX_ORDEXT1(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RX_ORDEXT1", "UCPD Rx Ordered Set Extension Register 1")
        self.RXSOPX1 = BitField(self, 0x000FFFFF, "RXSOPX1", "RXSOPX1")

class SA_UCPD1_RX_ORDEXT2(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "RX_ORDEXT2", "UCPD Rx Ordered Set Extension Register 2")
        self.RXSOPX2 = BitField(self, 0x000FFFFF, "RXSOPX2", "RXSOPX2")

class SA_UCPD1(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "UCPD1")
        self.CFG1 = SA_UCPD1_CFG1(self, 0x0)
        self.CFG2 = SA_UCPD1_CFG2(self, 0x4)
        self.CR = SA_UCPD1_CR(self, 0xC)
        self.IMR = SA_UCPD1_IMR(self, 0x10)
        self.SR = SA_UCPD1_SR(self, 0x14)
        self.ICR = SA_UCPD1_ICR(self, 0x18)
        self.TX_ORDSET = SA_UCPD1_TX_ORDSET(self, 0x1C)
        self.TX_PAYSZ = SA_UCPD1_TX_PAYSZ(self, 0x20)
        self.TXDR = SA_UCPD1_TXDR(self, 0x24)
        self.RX_ORDSET = SA_UCPD1_RX_ORDSET(self, 0x28)
        self.RX_PAYSZ = SA_UCPD1_RX_PAYSZ(self, 0x2C)
        self.RXDR = SA_UCPD1_RXDR(self, 0x30)
        self.RX_ORDEXT1 = SA_UCPD1_RX_ORDEXT1(self, 0x34)
        self.RX_ORDEXT2 = SA_UCPD1_RX_ORDEXT2(self, 0x38)
        self.RX_ORDEXT = Subscriptor(self, "RX_ORDEXT{}")
        self.CFG = Subscriptor(self, "CFG{}")

UCPD1 = SA_UCPD1(0x4000A000, "UCPD1")

class SA_USB_FS_device_EP0R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP0R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_EP1R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP1R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_EP2R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP2R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_EP3R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP3R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_EP4R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP4R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_EP5R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP5R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_EP6R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP6R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_EP7R(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "EP7R", "USB endpoint n register")
        self.EA = BitField(self, 0x0000000F, "EA", "EA")
        self.STAT_TX = BitField(self, 0x00000030, "STAT_TX", "STAT_TX")
        self.DTOG_TX = BitField(self, 0x00000040, "DTOG_TX", "DTOG_TX")
        self.CTR_TX = BitField(self, 0x00000080, "CTR_TX", "CTR_TX")
        self.EP_KIND = BitField(self, 0x00000100, "EP_KIND", "EP_KIND")
        self.EP_TYPE = BitField(self, 0x00000600, "EP_TYPE", "EP_TYPE")
        self.SETUP = BitField(self, 0x00000800, "SETUP", "SETUP")
        self.STAT_RX = BitField(self, 0x00003000, "STAT_RX", "STAT_RX")
        self.DTOG_RX = BitField(self, 0x00004000, "DTOG_RX", "DTOG_RX")
        self.CTR_RX = BitField(self, 0x00008000, "CTR_RX", "CTR_RX")

class SA_USB_FS_device_CNTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "CNTR", "USB control register")
        self.FRES = BitField(self, 0x00000001, "FRES", "FRES")
        self.PDWN = BitField(self, 0x00000002, "PDWN", "PDWN")
        self.LP_MODE = BitField(self, 0x00000004, "LP_MODE", "LP_MODE")
        self.FSUSP = BitField(self, 0x00000008, "FSUSP", "FSUSP")
        self.RESUME = BitField(self, 0x00000010, "RESUME", "RESUME")
        self.L1RESUME = BitField(self, 0x00000020, "L1RESUME", "L1RESUME")
        self.L1REQM = BitField(self, 0x00000080, "L1REQM", "L1REQM")
        self.ESOFM = BitField(self, 0x00000100, "ESOFM", "ESOFM")
        self.SOFM = BitField(self, 0x00000200, "SOFM", "SOFM")
        self.RESETM = BitField(self, 0x00000400, "RESETM", "RESETM")
        self.SUSPM = BitField(self, 0x00000800, "SUSPM", "SUSPM")
        self.WKUPM = BitField(self, 0x00001000, "WKUPM", "WKUPM")
        self.ERRM = BitField(self, 0x00002000, "ERRM", "ERRM")
        self.PMAOVRM = BitField(self, 0x00004000, "PMAOVRM", "PMAOVRM")
        self.CTRM = BitField(self, 0x00008000, "CTRM", "CTRM")

class SA_USB_FS_device_ISTR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISTR", "USB interrupt status register")
        self.EP_ID = BitField(self, 0x0000000F, "EP_ID", "EP_ID")
        self.DIR = BitField(self, 0x00000010, "DIR", "DIR")
        self.L1REQ = BitField(self, 0x00000080, "L1REQ", "L1REQ")
        self.ESOF = BitField(self, 0x00000100, "ESOF", "ESOF")
        self.SOF = BitField(self, 0x00000200, "SOF", "SOF")
        self.RESET = BitField(self, 0x00000400, "RESET", "RESET")
        self.SUSP = BitField(self, 0x00000800, "SUSP", "SUSP")
        self.WKUP = BitField(self, 0x00001000, "WKUP", "WKUP")
        self.ERR = BitField(self, 0x00002000, "ERR", "ERR")
        self.PMAOVR = BitField(self, 0x00004000, "PMAOVR", "PMAOVR")
        self.CTR = BitField(self, 0x00008000, "CTR", "CTR")

class SA_USB_FS_device_FNR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "FNR", "USB frame number register")
        self.FN = BitField(self, 0x000007FF, "FN", "FN")
        self.LSOF = BitField(self, 0x00001800, "LSOF", "LSOF")
        self.LCK = BitField(self, 0x00002000, "LCK", "LCK")
        self.RXDM = BitField(self, 0x00004000, "RXDM", "RXDM")
        self.RXDP = BitField(self, 0x00008000, "RXDP", "RXDP")

class SA_USB_FS_device_DADDR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "DADDR", "USB device address")
        self.ADD = BitField(self, 0x0000007F, "ADD", "ADD")
        self.EF = BitField(self, 0x00000080, "EF", "EF")

class SA_USB_FS_device_BTABLE(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "BTABLE", "Buffer table address")
        self.BTABLE = BitField(self, 0x0000FFF8, "BTABLE", "BTABLE")

class SA_USB_FS_device(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "USB_FS_device")
        self.EP0R = SA_USB_FS_device_EP0R(self, 0x0)
        self.EP1R = SA_USB_FS_device_EP1R(self, 0x4)
        self.EP2R = SA_USB_FS_device_EP2R(self, 0x8)
        self.EP3R = SA_USB_FS_device_EP3R(self, 0xC)
        self.EP4R = SA_USB_FS_device_EP4R(self, 0x10)
        self.EP5R = SA_USB_FS_device_EP5R(self, 0x14)
        self.EP6R = SA_USB_FS_device_EP6R(self, 0x18)
        self.EP7R = SA_USB_FS_device_EP7R(self, 0x1C)
        self.CNTR = SA_USB_FS_device_CNTR(self, 0x40)
        self.ISTR = SA_USB_FS_device_ISTR(self, 0x44)
        self.FNR = SA_USB_FS_device_FNR(self, 0x48)
        self.DADDR = SA_USB_FS_device_DADDR(self, 0x4C)
        self.BTABLE = SA_USB_FS_device_BTABLE(self, 0x50)
        self.EPR = Subscriptor(self, "EP{}R")

USB_FS_device = SA_USB_FS_device(0x40005C00, "USB_FS_device")

class SA_CRS_CR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x4000, "CR", "CRS control register")
        self.SYNCOKIE = BitField(self, 0x00000001, "SYNCOKIE", "SYNC event OK interrupt enable")
        self.SYNCWARNIE = BitField(self, 0x00000002, "SYNCWARNIE", "SYNC warning interrupt enable")
        self.ERRIE = BitField(self, 0x00000004, "ERRIE", "Synchronization or trimming error interrupt enable")
        self.ESYNCIE = BitField(self, 0x00000008, "ESYNCIE", "Expected SYNC interrupt enable")
        self.CEN = BitField(self, 0x00000020, "CEN", "Frequency error counter enable This bit enables the oscillator clock for the frequency error counter. When this bit is set, the CRS_CFGR register is write-protected and cannot be modified.")
        self.AUTOTRIMEN = BitField(self, 0x00000040, "AUTOTRIMEN", "Automatic trimming enable This bit enables the automatic hardware adjustment of TRIM bits according to the measured frequency error between two SYNC events. If this bit is set, the TRIM bits are read-only. The TRIM value can be adjusted by hardware by one or two steps at a time, depending on the measured frequency error value. Refer to Section7.3.4: Frequency error evaluation and automatic trimming for more details.")
        self.SWSYNC = BitField(self, 0x00000080, "SWSYNC", "Generate software SYNC event This bit is set by software in order to generate a software SYNC event. It is automatically cleared by hardware.")
        self.TRIM = BitField(self, 0x00007F00, "TRIM", "HSI48 oscillator smooth trimming These bits provide a user-programmable trimming value to the HSI48 oscillator. They can be programmed to adjust to variations in voltage and temperature that influence the frequency of the HSI48. The default value is 32, which corresponds to the middle of the trimming interval. The trimming step is around 67 kHz between two consecutive TRIM steps. A higher TRIM value corresponds to a higher output frequency. When the AUTOTRIMEN bit is set, this field is controlled by hardware and is read-only.")

class SA_CRS_CFGR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x2022BB7F, "CFGR", "This register can be written only when the frequency error counter is disabled (CEN bit is cleared in CRS_CR). When the counter is enabled, this register is write-protected.")
        self.RELOAD = BitField(self, 0x0000FFFF, "RELOAD", "Counter reload value RELOAD is the value to be loaded in the frequency error counter with each SYNC event. Refer to Section7.3.3: Frequency error measurement for more details about counter behavior.")
        self.FELIM = BitField(self, 0x00FF0000, "FELIM", "Frequency error limit FELIM contains the value to be used to evaluate the captured frequency error value latched in the FECAP[15:0] bits of the CRS_ISR register. Refer to Section7.3.4: Frequency error evaluation and automatic trimming for more details about FECAP evaluation.")
        self.SYNCDIV = BitField(self, 0x07000000, "SYNCDIV", "SYNC divider These bits are set and cleared by software to control the division factor of the SYNC signal.")
        self.SYNCSRC = BitField(self, 0x30000000, "SYNCSRC", "SYNC signal source selection These bits are set and cleared by software to select the SYNC signal source. Note: When using USB LPM (Link Power Management) and the device is in Sleep mode, the periodic USB SOF will not be generated by the host. No SYNC signal will therefore be provided to the CRS to calibrate the HSI48 on the run. To guarantee the required clock precision after waking up from Sleep mode, the LSE or reference clock on the GPIOs should be used as SYNC signal.")
        self.SYNCPOL = BitField(self, 0x80000000, "SYNCPOL", "SYNC polarity selection This bit is set and cleared by software to select the input polarity for the SYNC signal source.")

class SA_CRS_ISR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ISR", "CRS interrupt and status register")
        self.SYNCOKF = BitField(self, 0x00000001, "SYNCOKF", "SYNC event OK flag This flag is set by hardware when the measured frequency error is smaller than FELIM * 3. This means that either no adjustment of the TRIM value is needed or that an adjustment by one trimming step is enough to compensate the frequency error. An interrupt is generated if the SYNCOKIE bit is set in the CRS_CR register. It is cleared by software by setting the SYNCOKC bit in the CRS_ICR register.")
        self.SYNCWARNF = BitField(self, 0x00000002, "SYNCWARNF", "SYNC warning flag This flag is set by hardware when the measured frequency error is greater than or equal to FELIM * 3, but smaller than FELIM * 128. This means that to compensate the frequency error, the TRIM value must be adjusted by two steps or more. An interrupt is generated if the SYNCWARNIE bit is set in the CRS_CR register. It is cleared by software by setting the SYNCWARNC bit in the CRS_ICR register.")
        self.ERRF = BitField(self, 0x00000004, "ERRF", "Error flag This flag is set by hardware in case of any synchronization or trimming error. It is the logical OR of the TRIMOVF, SYNCMISS and SYNCERR bits. An interrupt is generated if the ERRIE bit is set in the CRS_CR register. It is cleared by software in reaction to setting the ERRC bit in the CRS_ICR register, which clears the TRIMOVF, SYNCMISS and SYNCERR bits.")
        self.ESYNCF = BitField(self, 0x00000008, "ESYNCF", "Expected SYNC flag This flag is set by hardware when the frequency error counter reached a zero value. An interrupt is generated if the ESYNCIE bit is set in the CRS_CR register. It is cleared by software by setting the ESYNCC bit in the CRS_ICR register.")
        self.SYNCERR = BitField(self, 0x00000100, "SYNCERR", "SYNC error This flag is set by hardware when the SYNC pulse arrives before the ESYNC event and the measured frequency error is greater than or equal to FELIM * 128. This means that the frequency error is too big (internal frequency too low) to be compensated by adjusting the TRIM value, and that some other action should be taken. An interrupt is generated if the ERRIE bit is set in the CRS_CR register. It is cleared by software by setting the ERRC bit in the CRS_ICR register.")
        self.SYNCMISS = BitField(self, 0x00000200, "SYNCMISS", "SYNC missed This flag is set by hardware when the frequency error counter reached value FELIM * 128 and no SYNC was detected, meaning either that a SYNC pulse was missed or that the frequency error is too big (internal frequency too high) to be compensated by adjusting the TRIM value, and that some other action should be taken. At this point, the frequency error counter is stopped (waiting for a next SYNC) and an interrupt is generated if the ERRIE bit is set in the CRS_CR register. It is cleared by software by setting the ERRC bit in the CRS_ICR register.")
        self.TRIMOVF = BitField(self, 0x00000400, "TRIMOVF", "Trimming overflow or underflow This flag is set by hardware when the automatic trimming tries to over- or under-flow the TRIM value. An interrupt is generated if the ERRIE bit is set in the CRS_CR register. It is cleared by software by setting the ERRC bit in the CRS_ICR register.")
        self.FEDIR = BitField(self, 0x00008000, "FEDIR", "Frequency error direction FEDIR is the counting direction of the frequency error counter latched in the time of the last SYNC event. It shows whether the actual frequency is below or above the target.")
        self.FECAP = BitField(self, 0xFFFF0000, "FECAP", "Frequency error capture FECAP is the frequency error counter value latched in the time ofthe last SYNC event. Refer to Section7.3.4: Frequency error evaluation and automatic trimming for more details about FECAP usage.")

class SA_CRS_ICR(RegisterBase):
    
    def __init__(self, peripheral, offset):
        super().__init__(peripheral, offset, 0x0, "ICR", "CRS interrupt flag clear register")
        self.SYNCOKC = BitField(self, 0x00000001, "SYNCOKC", "SYNC event OK clear flag Writing 1 to this bit clears the SYNCOKF flag in the CRS_ISR register.")
        self.SYNCWARNC = BitField(self, 0x00000002, "SYNCWARNC", "SYNC warning clear flag Writing 1 to this bit clears the SYNCWARNF flag in the CRS_ISR register.")
        self.ERRC = BitField(self, 0x00000004, "ERRC", "Error clear flag Writing 1 to this bit clears TRIMOVF, SYNCMISS and SYNCERR bits and consequently also the ERRF flag in the CRS_ISR register.")
        self.ESYNCC = BitField(self, 0x00000008, "ESYNCC", "Expected SYNC clear flag Writing 1 to this bit clears the ESYNCF flag in the CRS_ISR register.")

class SA_CRS(PeripheralBase):

    def __init__(self, base, name):
        super().__init__(base, name, "CRS")
        self.CR = SA_CRS_CR(self, 0x0)
        self.CFGR = SA_CRS_CFGR(self, 0x4)
        self.ISR = SA_CRS_ISR(self, 0x8)
        self.ICR = SA_CRS_ICR(self, 0xC)

CRS = SA_CRS(0x40002000, "CRS")
