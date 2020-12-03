def get_input():
	f = open("input.txt")

	return f.readlines()

def solve(data, slope_x, slope_y):
	x_pos = 0
	num_trees = 0

	for y_pos, line in enumerate(data):
		if y_pos != 0 and y_pos % slope_y != 0:
			continue

		width = len(line) - 1

		if line[x_pos] == "#":
			num_trees += 1

		x_pos += slope_x
		x_pos %= width

	return num_trees

def main():
	data = get_input()

	print("Part 1:")
	print("Answer: ", solve(data, 3, 1))

	print("Part 2:")
	print("Answer: ", solve(data, 1, 1) * solve(data, 3, 1) * solve(data, 5, 1) * solve(data, 7, 1) * solve(data, 1, 2))

main()