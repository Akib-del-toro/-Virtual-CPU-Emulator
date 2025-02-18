import sys

# Week 1: Project Planning & Setup
class Memory:
    def __init__(self, size=256):
        self.memory = [0] * size

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value

# Week 2: Instruction Set Architecture (ISA)
class Registers:
    def __init__(self):
        self.registers = {f'R{i}': 0 for i in range(4)}
        self.pc = 0
        self.ir = 0

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
        instr = self.registers.ir.split()
        if instr[0] in self.instructions:
            self.instructions[instr[0]](*instr[1:])

    # Week 5: Memory Management
    def load(self, reg, addr):
        self.registers.registers[reg] = self.memory.read(int(addr))

    def store(self, reg, addr):
        self.memory.write(int(addr), self.registers.registers[reg])

    # Week 6: I/O Operations
    def add(self, reg1, reg2):
        self.registers.registers[reg1] = ALU.execute('ADD', self.registers.registers[reg1], self.registers.registers[reg2])

    def sub(self, reg1, reg2):
        self.registers.registers[reg1] = ALU.execute('SUB', self.registers.registers[reg1], self.registers.registers[reg2])

    def jmp(self, addr):
        self.registers.pc = int(addr)

    def print_reg(self, reg):
        print(self.registers.registers[reg])

    # Week 7: Advanced Features
    def run(self, program):
        for i, instr in enumerate(program):
            self.memory.write(i, instr)
        while self.registers.pc < len(program):
            self.fetch()
            self.decode_execute()

# Week 8: Performance Optimization
if __name__ == "__main__":
    program = [
        "LOAD R0 10",  
        "LOAD R1 20",  
        "ADD R0 R1",   
        "PRINT R0"
    ]
    cpu = CPU()
    cpu.run(program)

# Week 9: Final Testing & Debugging