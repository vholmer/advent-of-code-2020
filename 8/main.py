class Instruction:
	def __init__(self, opcode, value):
		self.opcode = opcode
		self.value = int(value)
		self.text = opcode + " " + str(value)

class CPU:
	def __init__(self):
		self.opcodes = {"nop", "jmp", "acc"}

		self.acc = 0
		self.pc = 0

		self.called = set()

	def execute(self, instruction):
		if instruction.opcode not in self.opcodes:
			raise Exception(f"{instruction.opcode} is not a supported operation!")

		self.called.add(self.pc)

		if instruction.opcode == "jmp":
			self.pc += instruction.value
		elif instruction.opcode == "acc":
			self.acc += instruction.value

		if instruction.opcode != "jmp":
			self.pc += 1

def get_input():
	f = open("input.txt")

	program = []

	for line in f.readlines():
		line = line.strip()

		parts = line.split(" ")

		program.append(Instruction(parts[0], parts[1]))

	return program

def part1(program):
	cpu = CPU()

	while cpu.pc < len(program):
		if cpu.pc in cpu.called:
			return cpu.acc

		cpu.execute(program[cpu.pc])

def part2(program):
	success = False

	for i, instruction in enumerate(program):
		cpu = CPU()

		if instruction.opcode == "nop":
			program_clone = program.copy()
			program_clone[i] = Instruction("jmp", instruction.value)
		elif instruction.opcode == "jmp":
			program_clone = program.copy()
			program_clone[i] = Instruction("nop", instruction.value)
		else:
			continue

		while cpu.pc < len(program_clone):
			if cpu.pc in cpu.called:
				break

			cpu.execute(program_clone[cpu.pc])

			if cpu.pc >= len(program_clone):
				success = True

		if success:
			return cpu.acc

def main():
	program = get_input()

	print("Part 1:")
	print(part1(program))

	print("Part 2:")
	print(part2(program))

main()