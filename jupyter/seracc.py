# version 4.0 - updated 2025/6/19

if "ser" not in globals():
    ser = None
_crc = None
_ev = False
_count = 0
SER_LEN = 1040

def serial_init(which=None):
    import serial
    global ser, _crc, _ev, _count

    if isinstance(ser, serial.Serial):
        ser.close()
        
    if which is None:
        count = 0
        port_st, desc_st, hwid_st = None, None, None
        import serial.tools.list_ports
        for port, desc, hwid in serial.tools.list_ports.comports():
            if desc.startswith("STMicroelectronics") or desc.startswith("XDS110 Class App"):
                count += 1
                port_st, desc_st, hwid_st = port, desc, hwid
        if count == 1:
            print(f"Automatically detected:\n\t{port_st}: {desc_st} [{hwid_st}]")
            which = port_st
    
    if which is None:
        print("Listing serial ports:")
        for port, desc, hwid in serial.tools.list_ports.comports():
            print(f"\t{port}: {desc} [{hwid}]")
        which = input("Which COM port? Enter 0 for evaluation mode")

    if isinstance(which, int) or which.isnumeric():
        which = f"COM{which}"
    
    if which == "COM0":
        _ev = True
        print("Entering evaluation mode")
        return

    ser = serial.Serial(which, baudrate=1000000, timeout=1)
    _count = 0
    
    from crc import Configuration, Calculator
    config = Configuration(
        width=16,
        polynomial=0x1021,
        init_value=0x0000,
        final_xor_value=0x0000,
        reverse_input=False,
        reverse_output=False,
    )
    _crc = Calculator(config)

serial_init()

def serial_transmit(bs):
    # print([hex(b) for b in bs])

    global ser, _crc, _ev, _count

    if _ev:
        return
    
    if isinstance(bs, str):
        bs = bs.encode()
    
    l = len(bs)
    data = [l % 256, l // 256]
    data += bs
    crc = _crc.checksum(bs)
    data += [crc % 256, crc // 256]

    l = len(data)
    if l >= SER_LEN:
        print("Error: packet too long")
        return
    
    if _count + l >= SER_LEN:
        serial_sync()
    _count += l

    ser.write(data)

def serial_receive(size):
    global ser, _crc, _ev, _count
    
    if _ev:
        return bytes([0] * size)

    bs = ser.read(size+4)
    
    if len(bs) == 0:
        print("No response")
        return bytes()

    if len(bs) != size+4 \
        or bs[0]+bs[1]*256 != size:
            print("Format error")
            ser.read_all()
            return bytes()
    
    crc = bs[-2] + bs[-1] * 256
    bs = bs[2:-2]
    if _crc.checksum(bs) != crc:
        print("CRC error")
        return bytes()
    
    _count = 0
    return bs

def serial_clear():
    global ser, _crc, _ev, _count
    
    if _ev:
        return
    ser.read_all()

def serial_sync():
    global ser, _crc, _ev, _count
    
    if _ev:
        return
    
    ser.write(bytes([0x55, 0xAA]))
    read = ser.read(2)
    if len(read) != 2 or read[0] != ord('O') or read[1] != ord('K'):
        print("Sync failed")

    _count = 0

def mask_shl(value, mask):
    result = 0
    j = 0
    for i in range(32):
        if mask & (1 << i):
            if value & (1 << j):
                result |= 1 << i
            j += 1
    return result

def mask_shr(value, mask):
    result = 0
    j = 0
    for i in range(32):
        if mask & (1 << i):
            if value & (1 << i):
                result |= 1 << j
            j += 1
    return result

def mask_to_pos(mask):
    pos = []
    for i in range(32):
        if 1 << i & mask:
            pos.append(i)
    return pos

def bin_repr(v, n):
    return f"0b{v:0{n}b}"

def hex_repr(v, n=32):
    return f"0x{v:0{(n+3)//4}X}"

def from_bin(s):
    if isinstance(s, BitField):
        s = s.__repr__()
    if s.startswith("0b"):
        s = s[2:]
    return int(s, base=2)

def from_hex(s):
    if isinstance(s, RegisterBase):
        s = s.__repr__()
    if s.startswith("0x"):
        s = s[2:]
    return int(s, base=16)

def simplify_access(mask, value):
    mask_toset   = mask &  value
    mask_toclear = mask & ~value
    n_toset   = bin(mask_toset  ).count("1")
    n_toclear = bin(mask_toclear).count("1")
    n_mask    = bin(mask        ).count("1")

    if mask == MASK_32B:
        return ["write-only"]
    elif n_toset == 1 and n_toclear == 0:
        return ["single-set", mask_to_pos(mask_toset)[0]]
    elif n_toset == 0 and n_toclear == 1:
        return ["single-clear", mask_to_pos(mask_toclear)[0]]
    elif n_toset == n_mask and n_toclear == 0:
        return ["set-only"]
    elif n_toset == 0 and n_toclear == n_mask:
        return ["clear-only"]
    else:
        return ["full-modify"]

_logger = None

# set filename to log into a file which you can `#include` in your code
# otherwise, it prints on the console
# note that the logging feature does not record branch or loop statements within the `with` block
# it only records the read and write accesses
# for write accesses, the exact masks and values are produced
class AccessLogger:
    def __init__(self, filename):
        self.filename = filename
        self.ops = [] # typ, addr, mask, value, width, comment
                      # typ=0 for write, 1 for read, 2 for barrier, 3 for wait
        self.node = None
        self.waiting = False

    def __enter__(self):
        global _logger
        _logger = self
        return self

    def __exit__(self, tp, v, tb):
        if tp is not None:
            raise tp(v).with_traceback(tb)
        
        addr, mask, value = 0, 0, 0
        temp_cmt = []
        declared = False
        commands = []
        comments = []

        def flush():
            nonlocal addr, mask, value, temp_cmt, declared, commands, comments

            if addr == 0:
                return
            
            cls = simplify_access(mask, value)
            if cls[0] == "write-only":
                cmd = f"*(volatile uint32_t*){hex_repr(addr)} = {value};"
            elif cls[0] == "single-set":
                cmd = f"*(volatile uint32_t*){hex_repr(addr)} |= 1u << {cls[1]};"
            elif cls[0] == "single-clear":
                cmd = f"*(volatile uint32_t*){hex_repr(addr)} &= ~(1u << {cls[1]});"
            elif cls[0] == "set-only":
                cmd = f"*(volatile uint32_t*){hex_repr(addr)} |= {hex_repr(mask)};"
            elif cls[0] == "clear-only":
                cmd = f"*(volatile uint32_t*){hex_repr(addr)} &= ~{hex_repr(mask)};"
            elif cls[0] == "full-modify":
                cmd = "volatile uint32_t* " if not declared else ""
                declared = True
                cmd += f"_reg = (volatile uint32_t*){hex_repr(addr)};"
                commands.append(cmd)
                comments.append("")
                cmd = f"*_reg = (*_reg & ~{hex_repr(mask)}) | {hex_repr(value)};"
            
            commands.append(cmd)
            commands += [""] * (len(temp_cmt) - 1)
            comments += temp_cmt

            addr, mask, value = 0, 0, 0
            temp_cmt = []

        for op in self.ops:
            if op[0] == 0: # write
                if op[4] in [8, 16]: # 8/16-bit write
                    flush()
                    commands.append(f"*(volatile uint{op[4]}_t*){hex_repr(op[1])} = {op[3]};")
                    comments.append(op[5])
                else:                # 32-bit write
                    if op[1] != addr:
                        flush()
                    addr = op[1]
                    value = (value & (MASK_32B-op[2])) | (op[3] & op[2])
                    mask |= op[2]
                    temp_cmt.append(op[5])
            else:
                flush()
                if op[0] == 1: # read
                    commands.append(f"(void) *(volatile uint{op[4]}_t*){hex_repr(op[1])};")
                    comments.append(op[5])
                elif op[0] == 2: # barrier
                    pass
                elif op[0] == 3: # wait
                    cmd = "volatile uint32_t* " if not declared else ""
                    declared = True
                    cmd += f"_reg = (volatile uint32_t*){hex_repr(op[1])};"
                    commands.append(cmd)
                    comments.append("")
                    cmd = f"while ((*_reg & {hex_repr(op[2])}) != {hex_repr(op[3])});"
                    commands.append(cmd)
                    comments.append(op[5])
        flush()
        
        code = ""
        width = len(max(zip(commands, comments), key=
                        lambda p: len(p[0]) if len(p[1]) > 0 else 0)
                        [0])
        for c, cmt in zip(commands, comments):
            code += c + " " * (width - len(c))
            if len(cmt) > 0:
                code += " // "
            code += cmt + "\n"

        if self.filename is None:
            print(code[:-1])
        else:
            with open(self.filename, "w") as f:
                f.write(code)

        global _logger
        _logger = None

    def barrier(self):
        self.ops.append([2])

    def set_node(self, node):
        if self.node is None:
            self.node = node

    def log_read(self, addr, width):
        if self.waiting:
            return
        comment = self.node.get_full_name()
        self.ops.append([1, addr, 0, 0, width, comment])
        self.node = None

    def log_write(self, addr, mask, value, width):
        comment = self.node.get_full_name() + " = "
        if isinstance(self.node, BitField):
            comment += bin_repr(mask_shr(value, mask), self.node.n)
        else:
            comment += f"{value}"
        self.ops.append([0, addr, mask, value, width, comment])
        self.node = None

    def log_wait(self, addr, mask, value):
        if addr == 0:
            self.waiting = True
        else:
            self.waiting = False

            comment = self.node.get_full_name() + " != "
            if isinstance(self.node, BitField):
                comment += bin_repr(value, self.node.n)
            else:
                comment += f"{value}"
            self.ops.append([3, addr, mask, mask_shl(value, mask), 32, comment])
            self.node = None

def logging(filename=None):
    return AccessLogger(filename)

# FORMAT (little-ended):
#        CMD                0-3       4     5  6-7  8-11
#  8-bit read        _SA: <addr|1>
# 16-bit read        _SA: <addr|2>
# 32-bit read        _SA: <addr  >
#  8-bit write       _SA: <addr|1> <value>
# 16-bit write       _SA: <addr  > <value   >
# 32-bit write       _SA: <addr  > <value        >
# single bit set     _SA: <addr  > <pos>
# single bit clear   _SA: <addr|2> <pos>
#   set bits         _SA: <addr|1> <mask         >
# clear bits         _SA: <addr|2> <mask         >
# modify masked bits _SA: <addr  > <mask         > <value>

# assume all registers are 32-bit
MASK_32B = 2**32 - 1

def to_4bytes(word):
    bs = [0, 0, 0, 0]
    for i in range(4):
        bs[i] = word & 0xFF
        word >>= 8
    return bytes(bs)

# mask: extract the bits where mask is 1
# direct: if True, preserve the bit positions in the word
# width: 8, 16 or 32
def read_register(addr, mask=MASK_32B, direct=False, width=32):
    bs = "_:".encode()
    bs += to_4bytes(addr)

    ored = 0
    if width == 32:
        pass
    elif width == 16:
        ored = 2
    elif width == 8:
        ored = 1
    else:
        raise NotImplementedError("Unknown access width")
    bs = bs[:4] + bytes([bs[4] | ored]) + bs[5:]

    serial_clear()
    serial_transmit(bs)
    
    bs = serial_receive(width//8)
    if len(bs) != width//8:
        raise EOFError("Reading error")
    
    if width == 32:
        value = bs[0] | bs[1]<<8 | bs[2]<<16 | bs[3]<<24
    elif width == 16:
        value = bs[0] | bs[1]<<8
    else:
        value = bs[0]
    
    if direct:
        value &= mask
    else:
        value = mask_shr(value, mask)
    
    if _logger:
        _logger.log_read(addr, width)

    return int(value)

# masked write: change bits with mask 1 only, mask only applies when width=32
# direct: if True, preserve the bit positions in the word
# width: 8, 16 or 32
def write_register(addr, value, mask=MASK_32B, direct=False, width=32):
    bs = "_:".encode()
    bs += to_4bytes(addr)
    if not direct:
        value = mask_shl(value, mask)
    ored = 0

    if width == 32:
        cls = simplify_access(mask, value)
        if cls[0] == "write-only":
            bs += to_4bytes(value)
        elif cls[0] == "single-set":
            bs += bytes([cls[1]])
        elif cls[0] == "single-clear":
            ored = 2
            bs += bytes([cls[1]])
        elif cls[0] == "set-only":
            ored = 1
            bs += to_4bytes(mask)
        elif cls[0] == "clear-only":
            ored = 2
            bs += to_4bytes(MASK_32B - mask)
        elif cls[0] == "full-modify":
            bs += to_4bytes(mask)
            bs += to_4bytes(value)

    elif width == 16:
        bs += to_4bytes(value)[:2]

    elif width == 8:
        ored = 1
        bs += to_4bytes(value)[:1]

    else:
        raise NotImplementedError("Unknown access width")

    bs = bs[:2] + bytes([bs[2] | ored]) + bs[3:]
    serial_transmit(bs)

    if _logger:
        _logger.log_write(addr, mask, value, width)
    
# the generated code does not include the timeout
def wait_until_equal(field, value, timeout=1):
    if _logger:
        _logger.log_wait(0, 0, 0)
        _logger.set_node(field)
    
    import time
    start_time = time.time()
    while field.read() != value:
        if _ev:
            break
        if time.time() > start_time + timeout:
            raise EOFError("Timeout")
    
    if _logger:
        _logger.log_wait(field.register.address, field.mask, value)


class InstanceSetter:
    def __setattr__(self, attr, value):
        try:
            at = super().__getattribute__(attr)
            at.__set__(self, value)
        except AttributeError:
            super().__setattr__(attr, value)

class BitField:
    def __init__(self, register, mask, name, desc):
        self.register = register
        self.mask = mask
        self.n = bin(mask).count("1")
        self.name = name
        self.desc = desc

    def get_full_name(self):
        return self.register.get_full_name() + "." + self.name
    
    def __repr__(self):
        return bin_repr(self.read(), self.n)
    
    def __set__(self, instance, value):
        self.write(value)
        return value
    
    def read(self):
        result = self.register.read(mask=self.mask)
        return result
    
    def write(self, value, direct=False):
        if _logger:
            _logger.set_node(self)
        self.register.write(value, mask=self.mask, direct=direct)

    def reset(self):
        self.write(self.register.reset_value, direct=True)
    
import IPython.display as ipydisp

class RegisterBase(InstanceSetter):
        
    def __init__(self, peripheral, offset, reset, name, desc):
        self.peripheral = peripheral
        self.address = peripheral.base + offset
        self.offset = offset
        self.reset_value = reset
        self.name = name
        self.desc = desc

    def get_full_name(self):
        return self.peripheral.name + "." + self.name
    
    def structure(self, value=-1):
        if value < 0:
            bits = ["N/A"] * 32
        else:
            bits = bin_repr(value, 32)[2:]
        
        html = """\
<style type="text/css">
    table.register th {
        font-weight: normal;
        text-align: center !important;
        padding: 2px;
    }
    table.register td {
        text-align: center !important;
        border: 1px solid;
        word-wrap: break-word;
        padding: 2px;
    }
    .jp-RenderedHTMLCommon tbody tr:nth-child(even) {
        background: var(--jp-layout-color0);
    }
    .jp-RenderedHTMLCommon tbody tr:hover {
        background: rgba(0, 0, 0, 0);
    }

    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
    }

    .tooltip .tooltiptext-0 {
        visibility: hidden;
        width: 120px;
        background-color: black;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        top: 150%;
        left: 50%;
        margin-left: -60px;
    }

    .tooltip .tooltiptext-0::after {
        content: "";
        position: absolute;
        bottom: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: transparent transparent black transparent;
    }

    .tooltip:hover .tooltiptext-0 {
        visibility: visible;
    }

    .tooltip .tooltiptext-16 {
        visibility: hidden;
        width: 120px;
        background-color: black;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        bottom: 150%;
        left: 50%;
        margin-left: -60px;
    }

    .tooltip .tooltiptext-16::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: black transparent transparent transparent;
    }

    .tooltip:hover .tooltiptext-16 {
        visibility: visible;
    }
</style>
"""
        
        # I cannot understand the code below after writing it,
        # but it does print a table
        # mask2 is mainly for dual-role registers like timer CCMR
        mask = [None] * 32
        mask2 = [None] * 32
        for name in dir(self):
            bf = getattr(self, name)
            if not isinstance(bf, BitField):
                continue
            pos = mask_to_pos(bf.mask)
            if all(m is None for m in [mask[p] for p in pos]):
                if bf.n == 1:
                    mask[pos[0]] = [name, -1, bf.desc]
                else:
                    for i, p in enumerate(pos):
                        mask[p] = [name, i, bf.desc]
            elif all(m is None for m in [mask2[p] for p in pos]):
                if bf.n == 1:
                    mask2[pos[0]] = [name, -1, bf.desc]
                else:
                    for i, p in enumerate(pos):
                        mask2[p] = [name, i, bf.desc]
        mask = list(reversed(mask))
        mask2 = list(reversed(mask2))
        
        html += """\
<table class="register" style="width:1000px">
"""
        
        for base in [0, 16]:
            
            html += """\
    <tr>
"""
            
            for i in range(base, base+16):
                html += f"""\
        <th>{31-i}</th>
"""
            html += """\
    </tr>
"""
            
            for mm in [mask, mask2]:
                mm = mm[base:base+16]
                if not all(m is None for m in mm):
                    html += """\
    <tr>
"""
                    i = 0
                    while i < 16:
                        if mm[i] is None:
                            html += """\
        <td></td>
"""
                            i += 1
                        elif mm[i][1] == -1:
                            html += f"""\
        <td>
            <div class="tooltip">{mm[i][0]}
                <span class="tooltiptext-{base}">{mm[i][2]}</span>
            </div>
        </td>
"""
                            i += 1
                        else:
                            j = i + 1
                            while j < 16 and mm[j] is not None and \
                                mm[j][0] == mm[j-1][0] and mm[j][1] == mm[j-1][1]-1:
                                j += 1
                            if j == i + 1:
                                html += f"""\
        <td>
            <div class="tooltip">{mm[i][0]}[{mm[i][1]}]
                <span class="tooltiptext-{base}">{mm[i][2]}</span>
            </div>
        </td>
"""
                            else:
                                html += f"""\
        <td colspan="{j-i}">
            <div class="tooltip">{mm[i][0]}[{mm[i][1]}:{mm[j-1][1]}]
                <span class="tooltiptext-{base}">{mm[i][2]}</span>
            </div>
        </td>
"""
                            i = j
                    html += """\
    </tr>
"""
            html += """\
    <tr>
"""
            for i in range(base, base+16):
                html += f"""\
        <td>{bits[i]}</td>
"""
        html += """\
    </tr>
"""
        
        ipydisp.display(ipydisp.HTML(html))

    def __repr__(self):
        return self.get_repr()
    
    def __set__(self, instance, value):
        self.write(value)
        return value
        
    def read(self, mask=MASK_32B, direct=False):
        if _logger:
            _logger.set_node(self)
        result = read_register(self.address, mask, direct)
        return result
    
    def read8(self):
        if _logger:
            _logger.set_node(self)
        return read_register(self.address, width=8)
    
    def read16(self):
        if _logger:
            _logger.set_node(self)
        return read_register(self.address, width=16)
    
    # warning: value is always right-aligned
    # e.g. to write high 4 bits to 0b0100, set value=0b0100 and mask=0xF0000000
    # set direct=True to bypass the shifting
    def write(self, value, mask=MASK_32B, direct=False):
        if _logger:
            _logger.set_node(self)
        write_register(self.address, value, mask, direct)

    def write8(self, value):
        if _logger:
            _logger.set_node(self)
        write_register(self.address, value, width=8)

    def write16(self, value):
        if _logger:
            _logger.set_node(self)
        write_register(self.address, value, width=16)

    def reset(self):
        self.write(self.reset_value)
    
    def get_repr(self, show=True):
        value = self.read()
        info = f"DEC: {value}, HEX: {hex_repr(value)}"
        
        if show:
            self.structure(value)
        
        return info
    
class PeripheralBase(InstanceSetter):
        
    def __init__(self, base, name, desc):
        self.base = base
        self.name = name
        self.desc = desc

    def __repr__(self):
        return self.get_repr()
    
    def get_repr(self, regnames=None, show=True):
        if regnames is None:
            names = []
            offsets = []
            for attr in dir(self):
                if isinstance(getattr(self, attr), RegisterBase) and\
                    not attr.endswith("_Input") and not attr.endswith("_Output"):
                    names.append(attr)
                    reg = getattr(self, attr)
                    offsets.append(reg.offset)
            
            sort = sorted(zip(names, offsets), key=lambda x: x[1])
            names = [p[0] for p in sort]
            n_offset = len(f"{max(offsets):b}")
        else:
            names = regnames
            n_offset = max([len(f"{getattr(self, attr).offset:b}") for attr in names])
        
        html = """\
<style type="text/css">
    table.peripheral th {
        font-weight: normal;
        text-align: center !important;
        padding: 2px;
    }
    table.peripheral td {
        border: 1px solid;
        word-wrap: break-word;
        padding: 2px;
        position: relative;
    }
    .jp-RenderedHTMLCommon tbody tr:nth-child(even) {
        background: var(--jp-layout-color0);
    }
    .jp-RenderedHTMLCommon tbody tr:hover {
        background: rgba(0, 0, 0, 0);
    }

    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 400px;
        background-color: black;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        top: -5px;
        left: 110%;
    }

    .tooltip .tooltiptext::after {
        content: " ";
        position: absolute;
        top: 50%;
        right: 100%;
        margin-top: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: transparent black transparent transparent;
    }
</style>

<table class="peripheral" style="width:800px">
    <tr>
        <th style="width:100px">Offset</th>
        <th style="width:100px">Register</th>
        <th>Content</th>
    </tr>
"""

        for name in names:
            reg = getattr(self, name)
            html += f"""\
    <tr>
        <td align="center" style='font-family:"Courier New"'>{hex_repr(reg.offset, n_offset)}</td>
        <td align="center">
            <div class="tooltip">{name}
                <span class="tooltiptext">{reg.desc}</span>
            </div>
        </td>
        <td align="right" style='font-family:"Courier New"'>{reg.get_repr(False)}</td>
	</tr>
"""
        
        html += """\
</table>
"""

        if show:
            ipydisp.display(ipydisp.HTML(html))
        
        return f"{self.desc}"
    
    def find(self, query):

        def tokenize(s):
            import re
            tokens = set(re.split(r":|;|,|\.| ", s.lower()))
            tokens.discard('')
            return tokens

        keywords = tokenize(query)
        if len(keywords) == 0:
            return
        
        def match(desc):
            import re
            count = 0
            desc_tokens = tokenize(desc)
            for word in keywords:
                if word in desc_tokens:
                    count += 1
                elif word.isnumeric() and desc.find(word) >= 0:
                    idx = desc.find(word)
                    if idx+len(word) == len(desc) or not desc[idx+len(word)].isdigit():
                        count += 1
            if len(keywords) >= 2 and count <= len(keywords) / 2:
                return False

            result = True
            has_name = False
            for name in re.findall(r"[A-Z][A-Z\d]+", query):
                has_name = True
                idx = desc.find(name)
                if idx < 0:
                    result = False
                    break
                if name[0].isalpha() and idx > 0 and desc[idx-1].isalpha():
                    result = False
                    break
                if name[-1].isdigit() and idx+len(name) < len(desc) and desc[idx+len(name)].isdigit():
                # if name.lower() not in desc_tokens:
                    result = False
                    break
            if len(keywords) == 1 and count == 0 and not has_name:
                return False
            return result
        
        for attr in dir(self):
            if not isinstance(getattr(self, attr), RegisterBase) or\
                attr.endswith("_Input") or attr.endswith("_Output"):
                continue
            reg = getattr(self, attr)
            desc = reg.get_full_name() + ": " + reg.desc
            if match(desc):
                print(desc)
            
            for att in dir(reg):
                if not isinstance(getattr(reg, att), BitField):
                    continue
                field = getattr(reg, att)
                if match(field.desc):
                    print(field.get_full_name() + ": " + field.desc)
    
class Subscriptor():
    
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __getitem__(self, idx):
        return getattr(self.parent, self.name.format(idx))
    
    def __setitem__(self, idx, value):
        return setattr(self.parent, self.name.format(idx), value)
    
    def __repr__(self):
        if isinstance(self.parent, PeripheralBase):
            names = []
            for idx in range(32):
                attr = self.name.format(idx)
                if hasattr(self.parent, attr):
                    names.append(attr)
            self.parent.get_repr(names, True)

        else:
            html = """\
<style type="text/css">
    table.peripheral th {
        font-weight: normal;
        text-align: center !important;
        padding: 2px;
    }
    table.peripheral td {
        border: 1px solid;
        word-wrap: break-word;
        padding: 2px;
        position: relative;
    }
    .jp-RenderedHTMLCommon tbody tr:nth-child(even) {
        background: var(--jp-layout-color0);
    }
    .jp-RenderedHTMLCommon tbody tr:hover {
        background: rgba(0, 0, 0, 0);
    }

    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted black;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 400px;
        background-color: black;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px 0;
        position: absolute;
        z-index: 1;
        top: -5px;
        left: 110%;
    }

    .tooltip .tooltiptext::after {
        content: " ";
        position: absolute;
        top: 50%;
        right: 100%;
        margin-top: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: transparent black transparent transparent;
    }
</style>

<table class="peripheral" style="width:800px">
    <tr>
        <th style="width:100px">Mask</th>
        <th style="width:100px">Field</th>
        <th>Content</th>
    </tr>
"""

            for idx in range(32):
                attr = self.name.format(idx)
                if hasattr(self.parent, attr):
                    bf = getattr(self.parent, attr)
                    html += f"""\
    <tr>
        <td align="center" style='font-family:"Courier New"'>{hex_repr(bf.mask)}</td>
        <td align="center">
            <div class="tooltip">{attr}
                <span class="tooltiptext">{bf.desc}</span>
            </div>
        </td>
        <td align="right" style='font-family:"Courier New"'>{repr(bf)}</td>
    </tr>
"""
        
            html += """\
</table>
"""

            ipydisp.display(ipydisp.HTML(html))
            
        return ""
    
    def __set__(self, instance, value):
        raise NotImplementedError(f"Please specify the index: {self.name.format('')}[n]")
    
