def display_equation(left, message):
	equation = message
	for i,poly in enumerate(left):
		if i != 0 or poly.sign == False and poly.factor != 0:
			equation += "- " if poly.sign == False else "+ "
		equation += f"{poly.factor} * X^{poly.power} "
	equation += "= 0"
	print(equation)

def check_power(left, final):
	for i in range(len(final)):
		if final[i].power == left.power:
			return i
	return -1

def get_degree(final):
	best = 0
	for i in final:
		if i.power > best and i.factor != 0:
			best = i.power
	return best

def reduce(left, right, degree):
	final = []
	for poly in right:
		left.append(poly)
		left[len(left) - 1].sign = True if poly.sign == False else False
	for i in range(len(left)):
		result = check_power(left[i], final)
		if result >= 0:
			if left[i].sign == False:
				if final[result] == 0:
					final[result].factor = left[i].factor
					final[result].sign = False
				else:
					final[result].factor = final[result].factor - left[i].factor
			else :
				final[result].factor = final[result].factor + left[i].factor
		else:
			final.append(left[i])
	display_equation(final, "Reduced form: ")
	degree = get_degree(final)
	return final, degree