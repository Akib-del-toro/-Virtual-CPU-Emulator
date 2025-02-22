import sys

# Week 1: Project Planning & Setup
class Memory:
    def __init__(self, size=256):
        self.memory = [""] * size  

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):  
        self.memory[address] = value

# Week 2: Instruction Set Architecture (ISA)
class Registers:
    def __init__(self):
        self.registers = {f'R{i}': 0 for i in range(4)}
        self.pc = 0
        self.ir = ""

# Week 3: Basic CPU Components
class ALU:
    @staticmethod
    def execute(op, operand1, operand2):
        if op == 'ADD':
            return operand1 + operand2
        elif op == 'SUB':
            return operand1 - operand2
        return 0

# Week 4: Instruction Execution
class CPU:
    def __init__(self):
        self.memory = Memory()
        self.registers = Registers()
        self.instructions = {
            'LOAD': self.load,
            'STORE': self.store,
            'ADD': self.add,
            'SUB': self.sub,
            'JMP': self.jmp,
            'PRINT': self.print_reg
        }

    def fetch(self):
        self.registers.ir = self.memory.read(self.registers.pc)
        self.registers.pc += 1

    def decode_execute(self):
        if not self.registers.ir:
            return  
        instr = self.registers.ir.split()
        if instr[0] in self.instructions:
            if len(instr) == 3:
                self.instructions[instr[0]](instr[1], instr[2])
            elif len(instr) == 2:
                self.instructions[instr[0]](instr[1])
            else:
                print(f"Invalid instruction format: {self.registers.ir}")

    # Week 5: Memory Management
    def load(self, reg, addr):
        addr = int(addr)
        if 0 <= addr < len(self.memory.memory):
            binary_value = self.memory.read(addr)
            self.registers.registers[reg] = int(binary_value, 2) if binary_value else 0  
        else:
            print(f"Memory address out of bounds: {addr}")

    def store(self, reg, addr):
        addr = int(addr)
        if 0 <= addr < len(self.memory.memory):
            binary_value = bin(self.registers.registers[reg])[2:]  
            self.memory.write(addr, binary_value)  
        else:
            print(f"Memory address out of bounds: {addr}")

    # Week 6: I/O Operations (Modified to Print in Binary)
    def add(self, reg1, reg2):
        self.registers.registers[reg1] = ALU.execute('ADD', self.registers.registers[reg1], self.registers.registers[reg2])

    def sub(self, reg1, reg2):
        self.registers.registers[reg1] = ALU.execute('SUB', self.registers.registers[reg1], self.registers.registers[reg2])

    def jmp(self, addr):
        self.registers.pc = int(addr)

    def print_reg(self, reg):
        binary_output = bin(self.registers.registers[reg])[2:] 
        print(binary_output)

    # Week 7: Advanced Features
    def run(self, program):
        for i, instr in enumerate(program):
            self.memory.write(i, instr) 
        while self.registers.pc < len(program):
            self.fetch()
            self.decode_execute()

# Week 8: Performance Optimization
if __name__ == "__main__":
    memory_values = {10: bin(10)[2:], 20: bin(20)[2:]}  

    program = [
        "LOAD R0 10",  
        "LOAD R1 20",  
        "ADD R0 R1",   
        "PRINT R0"
    ]
    
    cpu = CPU()

    for addr, val in memory_values.items():
        cpu.memory.write(addr, val)

    cpu.run(program)
