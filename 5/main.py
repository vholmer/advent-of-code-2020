import numpy as np

def get_input():
	f = open("input.txt")

	return f.readlines()

def get_seat_id(boardingpass, lower = 0, upper = 127):
	# First do the front / back partitioning
	rows = list(range(lower, upper + 1))

	for partition in boardingpass[:7]:
		if partition == "F":
			rows = rows[0:len(rows) // 2]
		elif partition == "B":
			rows = rows[len(rows) - (len(rows) // 2):]

	row = rows[0]

	# Then do the left / right partitioning
	cols = list(range(0, 8))

	for partition in boardingpass[7:]:
		if partition == "L":
			cols = cols[0:len(cols) // 2]
		elif partition == "R":
			cols = cols[len(cols) - (len(cols) // 2):]

	col = cols[0]

	return row * 8 + col

def part1(data):
	sums = []

	numbers = [int(x.translate(str.maketrans({"B": "1", "F": "0", "L": "0", "R": "1"})), 2) for x in data]

	return get_seat_id(data[np.argmax(numbers)])

def part2(data):
	"""
	For part 2 I realized what we're looking for is two boarding passes with the second last bit flipped to each other,
	with one number empty between them, which can happen in two ways:

	10 and 00 meaning our binary boarding pass is the first 8 bits + 01
	11 and 01 meaning our binary boarding pass is the first 8 bits + 10

	Make a dict using the first 8 bits for all binary converted passes as the key
	Then check if we can fullfil any of those two cases for the last two bits (the dict values)
	If yes we found our seat and then convert back to alphabetical boarding pass and calculate the seat id
	"""

	binaries = [x.translate(str.maketrans({"B": "1", "F": "0", "L": "0", "R": "1"})) for x in data]

	binary_dict = {}

	for binary in binaries:
		if binary[:8] not in binary_dict:
			binary_dict[binary[:8]] = [binary[8:-1]]
		else:
			binary_dict[binary[:8]] += [binary[8:-1]]

	for binary in binaries:
		key = binary[:8]

		seats = binary_dict[key]

		if len(seats) < 2:
			continue

		if "11" in seats and "01" in seats and "10" not in seats:
			my_seat = key + "10"
			break

		if "10" in seats and "00" in seats and "01" not in seats:
			my_seat = key + "01"
			break

	return get_seat_id(my_seat[:7].translate(str.maketrans({"0": "F", "1": "B"})) + my_seat[7:].translate(str.maketrans({"0": "L", "1": "R"})))

def main():
	data = get_input()

	print("Part 1:")
	print(part1(data))

	print("Part 2:")
	print(part2(data))

main()