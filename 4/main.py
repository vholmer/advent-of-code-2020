import re

def get_input():
	f = open("input.txt")
	lines = f.readlines()
	num_lines = len(lines)

	data = []

	passport = {}

	for i, line in enumerate(lines):
		line = line.strip()

		if line == "":
			data.append(passport)
			passport = {}
			continue

		parts = line.split(" ")

		for part in parts:
			key, value = part.split(":")

			passport[key] = value

		if i == num_lines - 1:
			data.append(passport)
			passport = {}

	return data

def part1(data):
	required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

	num_valid = 0

	for passport in data:
		passport_valid = True

		for required_key in required_keys:
			if required_key not in passport.keys():
				passport_valid = False

		if passport_valid:
			num_valid += 1

	return num_valid

def part2(data):
	required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

	num_valid = 0

	for passport in data:
		print(f"Checking passport: {passport}")

		missing_required = False
		
		for required_key in required_keys:
			if required_key not in passport.keys():
				print(f"Missing required key: {required_key}")
				missing_required = True

		if missing_required:
			continue

		if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
			print(f"Length is < 1920 or > 2002: {passport['byr']}")
			continue

		if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
			print(f"Issue year < 2010 or > 2020: {passport['iyr']}")
			continue

		if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
			print(f"Expiration year < 2020 or > 2030: {passport['eyr']}")
			continue

		if "in" in passport["hgt"]:
			inches = int(passport["hgt"].split("in")[0])

			if inches < 59 or inches > 76:
				print(f"Inches < 59 or > 76: {inches}")
				continue
		elif "cm" in passport["hgt"]:
			centimeters = int(passport["hgt"].split("cm")[0])

			if centimeters < 150 or centimeters > 193:
				print(f"Centimeters < 150 or > 193: {centimeters}")
				continue
		else:
			print(f"Unknown if height is cm or in: {passport['hgt']}")
			continue

		if len(re.findall(r"^#[0-9a-f]{6}$", passport["hcl"])) <= 0:
			print(f"Invalid hair color: {passport['hcl']}")
			continue

		if len(re.findall(r"^(amb|blu|brn|gry|grn|hzl|oth){1}$", passport["ecl"])) <= 0:
			print(f"Invalid eye color: {passport['ecl']}")
			continue

		if len(re.findall(r"^\d{9}$", passport["pid"])) <= 0:
			print(f"Invalid passport ID: {passport['pid']}")
			continue

		print("Congratulations, your passport is valid!")

		num_valid += 1

	return num_valid

def main():
	data = get_input()

	print("Part 1:")
	print(part1(data))

	print("Part 2:")
	print(part2(data))

main()