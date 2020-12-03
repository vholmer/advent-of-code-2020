def get_input():
	f = open("input.txt")

	return f.readlines()

def part1(data):
	x_pos = 0

	num_trees = 0

	for line in data:
		width = len(line) - 1

		if line[x_pos] == "#":
			num_trees += 1
			marker = line[:x_pos] + "X" + line[x_pos + 1:]
		else:
			marker = line[:x_pos] + "O" + line[x_pos + 1:]

		x_pos += 3
		x_pos %= width

	return num_trees

def part2(data):
	# hspeed, vspeed. part 1 is 3, 1
	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

	result = 1

	for hspeed, vspeed in slopes:
		x_pos = 0
		num_trees = 0

		for y_pos, line in enumerate(data):
			if y_pos != 0 and y_pos % vspeed != 0:
				continue

			width = len(line) - 1

			if line[x_pos] == "#":
				num_trees += 1

			x_pos += hspeed
			x_pos %= width

		result *= num_trees

	return result

def main():
	data = get_input()

	print("Part 1:")
	print("Answer: ", part1(data))

	print("Part 2:")
	print("Answer: ", part2(data))

main()