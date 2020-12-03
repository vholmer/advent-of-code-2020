import numpy as np

def get_input(filePath):
	f = open(filePath)

	integer_list = []

	for line in f.readlines():
		integer_list = integer_list + [int(line)]

	return integer_list

# Returns (result, first, second)
def part1_slow(data):
	return [(x * (2020 - x), x, 2020 - x) for x in data if (2020 - x) in data][0]

# Returns (result, first, second)
def part1_fast(data):
	seen = set()

	for x in data:
		if 2020 - x > 0 and 2020 - x in seen:
			return (x * (2020 - x), x, 2020 - x)

		seen.add(x)

# Returns (result, first, second, third)
def part2(data):
	seen = set()

	for i, x in enumerate(data):
		for y in data[i:]:
			if 2020 - x - y > 0 and 2020 - x - y in seen:
				return (x * y * (2020 - x - y), x, y, (2020 - x - y))
			seen.add(y)
		seen.add(x)

def main():
	data = get_input("input.txt")

	print("Part 1:")

	res = part1_slow(data)
	print(res)

	res = part1_fast(data)
	print(res)

	print("Part 2:")

	res = part2(data)
	print(res)

main()