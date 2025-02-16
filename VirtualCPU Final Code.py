import struct

class VirtualCPU:
    def __init__(self, memory_size=256):
        self.registers = {f'R{i}': 0 for i in range(8)}  # 8 general-purpose registers
        self.pc = 0  # Program Counter
        self.ir = None  # Instruction Register
        self.memory = bytearray(memory_size)
        self.running = True
        self.instruction_set = {
            0x01: self.add,
            0x02: self.sub,
            0x03: self.load,
            0x04: self.store,
            0x05: self.jmp,
            0x06: self.io,
            0x07: self.branch,
            0x08: self.call,
            0x09: self.ret,
        }
        self.stack = []

    # Week 1: Setup
    def fetch(self):
        if self.pc >= len(self.memory):
            self.running = False
            return
        self.ir = self.memory[self.pc]
        self.pc += 1

    def decode_execute(self):
        if self.ir in self.instruction_set:
            self.instruction_set[self.ir]()
        else:
            self.running = False

    # Week 2: Basic Instructions
    def add(self):
        reg1, reg2, reg3 = self.memory[self.pc:self.pc+3]
        self.pc += 3
        self.registers[f'R{reg1}'] = self.registers[f'R{reg2}'] + self.registers[f'R{reg3}']

    def sub(self):
        reg1, reg2, reg3 = self.memory[self.pc:self.pc+3]
        self.pc += 3
        self.registers[f'R{reg1}'] = self.registers[f'R{reg2}'] - self.registers[f'R{reg3}']

    def load(self):
        reg, addr = self.memory[self.pc:self.pc+2]
        self.pc += 2
        self.registers[f'R{reg}'] = self.memory[addr]

    def store(self):
        reg, addr = self.memory[self.pc:self.pc+2]
        self.pc += 2
        self.memory[addr] = self.registers[f'R{reg}']

    # Week 3: Memory and Control
    def jmp(self):
        addr = self.memory[self.pc]
        self.pc = addr

    def io(self):
        reg = self.memory[self.pc]
        self.pc += 1
        print(f'Output: {self.registers[f"R{reg}"]}')

    # Week 4: Advanced Control Flow
    def branch(self):
        reg, addr = self.memory[self.pc:self.pc+2]
        self.pc += 2
        if self.registers[f'R{reg}'] != 0:
            self.pc = addr

    def call(self):
        addr = self.memory[self.pc]
        self.pc += 1
        self.stack.append(self.pc)
        self.pc = addr

    def ret(self):
        if self.stack:
            self.pc = self.stack.pop()

    # Week 5: Program Loading
    def load_program(self, program):
        self.memory[:len(program)] = program

    # Week 6-8: Execution and Optimization
    def run(self):
        while self.running:
            self.fetch()
            self.decode_execute()

# Example program (ADD R0, R1, R2, then output R0)
program = bytes([0x01, 0, 1, 2, 0x06, 0])
cpu = VirtualCPU()
cpu.registers['R1'] = 10
cpu.registers['R2'] = 20
cpu.load_program(program)
cpu.run()
