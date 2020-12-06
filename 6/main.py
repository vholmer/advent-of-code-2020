def get_input():
	f = open("input.txt")

	return f.readlines()

def part1(data):
	counts = []

	adict = set()

	for line in data:
		line = line.strip()

		if line == "":
			counts += [len(adict)]
			adict = set()

		for char in line:
			adict.add(char)

	return sum(counts)

def part2(data):
	counts = []

	adict = {}
	
	num_people = 0

	for line in data:
		line = line.strip()

		if line == "":
			counts += [1 for x in adict if adict[x] == num_people]
			
			adict = {}

			num_people = 0
		else:
			num_people += 1

		for char in line:
			if char not in adict:
				adict[char] = 1
			else:
				adict[char] += 1

	return sum(counts)

def main():
	data = get_input()

	print("Part 1:")
	print(part1(data))

	print("Part 2:")
	print(part2(data))

main()