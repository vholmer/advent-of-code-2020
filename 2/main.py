import re
import numpy as np

def get_input(filePath):
	f = open(filePath)

	data = []

	for line in f.readlines():
		(policy, password) = line.split(":")
		
		(lower, upper) = re.findall(r"\d+", policy)
		lower, upper = int(lower), int(upper)

		letter = policy[-1]

		data = data + [(lower, upper, letter, password.strip())]

	return data

def part1(data):
	num_correct_passwords = 0
	
	for lower, upper, letter, password in data:
		letter_count = np.sum([1 for x in password if x == letter])

		if letter_count >= lower and letter_count <= upper:
			num_correct_passwords += 1

	return num_correct_passwords

def part2(data):
	num_correct_passwords = 0
	
	for lower, upper, letter, password in data:
		# Subtract one for zero-indexing
		lower -= 1
		upper -= 1
		if password[lower] == letter and password[upper] != letter:
			num_correct_passwords +=1
			continue
		if password[upper] == letter and password[lower] != letter:
			num_correct_passwords +=1

	return num_correct_passwords

def main():
	data = get_input("input.txt")

	print("Part 1:")
	print(part1(data))

	print("Part 2:")
	print(part2(data))

main()