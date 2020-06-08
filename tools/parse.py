import re
from tools.utils import lookup_index, atof, print_error, format_check
from tools.Polynom import Polynom

charset = "0123456789+-*=X^. "
sign = "+-"

def set_polynom_list(side, degree):
	error = False
	side_list = []
	separator = re.split('[0-9X^.* ]+', side)[:-1]
	polynomList = re.split('[\-+=]', side)
	if not separator:
		print_error(0,0,0,0)
	if separator[0] == "-":
		polynomList = re.split('[\-+=]', side)[1:]
	for i in range(len(separator)):
		power = -1
		sign = True if (separator[i] == '' or separator[i] == '+') else False
		try :
			index = polynomList[i][polynomList[i].index("X^") + 2:]
			if len(index) == 0 or not index[0].isdigit() :
				error = True
				raise Exception()
			power = re.findall(r'\d+', index)
			if len(power) == 0:
				error = True
				raise Exception()
			power = int(power[0])
			if power > degree:
				degree = power
			nums = re.findall(r'\d+.\d+|\d+', polynomList[i])
			if len(nums) == 1:
				nums.append(1)
			factor = float(nums[0]) if nums.index(str(power)) == 1 else float(nums[1])
		except :
			if error == False:
				power = 0
				factor = re.findall(r'\d+.\d+|\d+', polynomList[i])
				x_index = lookup_index(polynomList[i], 'X')
				if len(factor) > 0:
					factor = atof(factor[0])
				else:
					factor = 1
				if x_index != -1:
					format_check(polynomList[i], x_index)
					power = 1
				else:
					power = 0
		if error == True:
			print_error(polynomList[i], 0, 0, 2)
		new_term = Polynom(sign, polynomList[i].strip(), power, factor)
		new_term.check()
		side_list.append(new_term)
	return side_list, degree

def parse(eq, verbose, degree) :
	if "=" not in eq:
		print_error(0, 0, 0, 0)
	eq = re.sub(r"\s+", ' ', eq)
	eq = re.sub(r"(\s\^\s)", '^', eq)
	eq = eq.replace("x", "X")
	for i, letter in enumerate(eq):
		if letter not in charset:
			print_error(0, letter, i, 1)
	left, degree = set_polynom_list(eq[:eq.index("=")].strip(), degree)
	right, degree = set_polynom_list(eq[eq.index("=") + 1:].strip(), degree)
	return left, right, degree
