import re
from collections import Counter
from tools.utils import print_error, lookup_index

class Polynom:
	def __init__(self, sign, definition, power, factor):
		self.sign = sign
		self.definition = definition
		self.power = power
		self.x = False
		self.factor = factor

	def check(self):
		count = Counter(self.definition)
		numbers = len(re.findall('[^X\^ *]+', self.definition))
		if count['X'] > 1 or count['*'] > 1 or count['^'] > 1:
			print_error(self.definition, 0, 0, 2)

		self.x = True if count['X'] == 1 else False
		if self.x == True :
			if count['*'] == 0 and count['^'] == 1 and numbers > 2:
				print_error(self.definition, 0, 0, 2)
			if count['*'] == 1 and count['^'] == 0 and numbers > 1:
				print_error(self.definition, 0, 0, 2)
			if count['*'] == 0 and count['^'] == 0 and numbers > 1:
				print_error(self.definition, 0, 0, 2)
			index = lookup_index(self.definition, '^')
			index2 = lookup_index(self.definition, 'X')
			if index > 0 and (index2 == -1 or index2 != index - 1):
				print_error(self.definition, 0, 0, 2)
		else:
			if count['^'] > 0 or count['*'] > 0 or numbers > 1:
				print_error(self.definition, 0, 0, 2)

	def display(self):
		print(f"sign : {self.sign}\npower : {self.power}\nx : {self.x}\nfactor : {self.factor}\n")
