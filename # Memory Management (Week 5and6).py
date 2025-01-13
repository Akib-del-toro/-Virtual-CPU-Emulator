# Memory Management (Week 5)
MEMORY_SIZE = 1024
memory = [0] * MEMORY_SIZE

def read_memory(address):
    if 0 <= address < MEMORY_SIZE:
        return memory[address]
    else:
        raise ValueError("Invalid memory address")

def write_memory(address, data):
    if 0 <= address < MEMORY_SIZE:
        memory[address] = data
    else:
        raise ValueError("Invalid memory address")

segments = {
    "code": {"base": 0, "limit": 256},
    "data": {"base": 256, "limit": 512},
    "stack": {"base": 512, "limit": 1024},
}

def get_physical_address(segment, logical_address):
    if segment in segments:
        base = segments[segment]["base"]
        limit = segments[segment]["limit"]
        if 0 <= logical_address < (limit - base):
            return base + logical_address
        else:
            raise ValueError("Address out of segment bounds")
    else:
        raise ValueError("Invalid segment")

# I/O Operations (Week 6)
io_devices = {
    "keyboard": [],
    "display": []
}

def io_write(device, data):
    if device in io_devices:
        io_devices[device].append(data)
    else:
        raise ValueError("Invalid I/O device")

def io_read(device):
    if device in io_devices:
        if io_devices[device]:
            return io_devices[device].pop(0)
        else:
            return None
    else:
        raise ValueError("Invalid I/O device")

def execute_io_instruction(instruction, device, data=None):
    if instruction == "write":
        io_write(device, data)
    elif instruction == "read":
        return io_read(device)
    else:
        raise ValueError("Invalid I/O instruction")

# Testing Example
write_memory(get_physical_address("data", 10), 42)
print(read_memory(get_physical_address("data", 10)))

execute_io_instruction("write", "keyboard", "Input from user")
print(execute_io_instruction("read", "keyboard"))
execute_io_instruction("write", "display", "Hello, World!")
print(io_devices["display"])
