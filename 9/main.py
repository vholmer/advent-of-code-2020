import numpy as np

def get_input():
	f = open("input.txt")

	data = []

	for line in f.readlines():
		data += [int(line)]

	return data

def part1(data, preamble_length = 25):
	preamb_start = 0
	preamb_end = preamble_length

	while preamb_end + 1 < len(data):
		preambles = data[preamb_start : preamb_end]
		value = data[preamb_end]
		
		sums = set()

		for i, preamble in enumerate(preambles):
			while i < len(preambles) - 1:
				sums.add(preamble + preambles[i + 1])
				i += 1

		if value not in sums:
			return value

		preamb_start += 1
		preamb_end += 1

def part2(value, data, preamble_length = 25):
	contig_set_length = 2

	while contig_set_length < len(data):
		contig_set_start = 0
		contig_set_end = contig_set_length

		while contig_set_end < len(data):
			contig_set = data[contig_set_start : contig_set_end]

			if np.sum(contig_set) == value:
				return np.min(contig_set) + np.max(contig_set)

			contig_set_start += 1
			contig_set_end += 1

		contig_set_length += 1

def main():
	data = get_input()

	print("Part 1:")
	value = part1(data)
	print(value)

	print("Part 2:")
	print(part2(value, data))

main()