INSTRUCTION_SET = {
    "LOAD": "0001",
    "STORE": "0010",
    "ADD": "0011",
    "SUB": "0100",
    "MUL": "0101",
    "DIV": "0110",
    "JUMP": "0111",
    "JZ": "1000",
    "JNZ": "1001",
    "HALT": "1111",
}

REGISTERS = {
    "R0": "0000",
    "R1": "0001",
    "R2": "0010",
    "R3": "0011",
    "R4": "0100",
    "R5": "0101",
    "R6": "0110",
    "R7": "0111",
}

def convert_to_binary(value, mapping=None, bits=8):
    if mapping:
        return mapping.get(value, "00000000")
    else:
        return f"{int(value):0{bits}b}"

def get_opcode(instruction):
    return convert_to_binary(instruction, INSTRUCTION_SET, bits=8)

def get_register(register):
    return convert_to_binary(register, REGISTERS, bits=4)

def get_address_or_immediate(value, bits=16):
    return convert_to_binary(value, bits=bits)

def assemble_instruction_general(parsed_line):
    opcode = get_opcode(parsed_line[0])
    operands = []
    for i in range(1, len(parsed_line)):
        operand = parsed_line[i]
        if operand in REGISTERS:
            operands.append(get_register(operand))
        else:
            operands.append(get_address_or_immediate(operand))
    while len(operands) < 3:
        operands.append("00000000")
    return opcode + "".join(operands)
