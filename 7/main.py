import numpy as np

class Node:
	def __init__(self, color):
		self.color = color
		self.edges = []
		self.parents = []

	def add_edge(self, to_node, weight):
		to_node.parents += [self]
		self.edges += [Edge(self, to_node, weight)]

class Edge:
	def __init__(self, from_node, to_node, weight):
		self.from_node = from_node
		self.to_node = to_node
		self.weight = weight

class Tree:
	def __init__(self):
		self.nodes = set()

	def add_node(self, color):
		new_node = Node(color)

		self.nodes.add(new_node)

	def add_edge(self, from_color, to_color, weight):
		for node in self.nodes:
			if node.color == to_color:
				to_node = node

		for node in self.nodes:
			if node.color == from_color:
				node.add_edge(to_node, weight)

def get_input():
	f = open("input.txt")
	lines = f.readlines()

	bag_tree = Tree()

	# Add nodes
	for line in lines:
		line = line.strip()

		adjective = line.split(" ")[0]
		bag_color = adjective + " " + line.split(" ")[1]

		bag_tree.add_node(bag_color)

	# Add edges
	for line in lines:
		line = line.strip()

		adjective = line.split(" ")[0]
		bag_color = adjective + " " + line.split(" ")[1]

		contained = line.split("contain")[-1].strip()
		contained = contained.replace(".", "")
		contained_bags = contained.split(", ")

		for contained_bag in contained_bags:
			quantity = contained_bag[0].strip()

			if quantity == "n": # No other bags
				quantity = 0
			else:
				quantity = int(quantity)

			contained_color = contained_bag[1:].replace("bags", "").replace("bag", "").replace("o other", "").strip()

			if contained_color != "":
				bag_tree.add_edge(bag_color, contained_color, quantity)

	return bag_tree

def traverse(nodes, solution_set = set()):
	for node in nodes:
		if node.color != "shiny gold":
			solution_set.add(node.color)

		solution_set.union(traverse(node.parents, solution_set))

	return solution_set

def traverse_weight(nodes, total = 0):
	for node in nodes:
		if len([edge for edge in node.edges]) == 0:
			return total

		if total == 0:
			total += np.sum([traverse_weight([edge.to_node], edge.weight) for edge in node.edges])
		else:
			total += total * np.sum([traverse_weight([edge.to_node], edge.weight) for edge in node.edges])

	return total

def part1(tree):
	# Find shiny gold
	shiny_gold = [node for node in tree.nodes if node.color == "shiny gold"]

	# Traverse roots until we find shiny gold bag
	return len(traverse(shiny_gold))

def part2(tree):
	# Find shiny gold
	shiny_gold = [node for node in tree.nodes if node.color == "shiny gold"]

	return traverse_weight(shiny_gold)

def main():
	tree = get_input()

	print("Part 1:")
	print(part1(tree))

	print("Part 2:")
	print(part2(tree))

main()