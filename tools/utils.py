def atof(s):
	try:
		return float(s)
	except:
		if not s:
			return False
		return atof(s[:-1])

def lookup_index(string, char):
	for i in range(len(string)):
		if string[i] == char:
			return i
	return -1

def print_error(polynom, letter, index, code):
	error_message = {
	0:"Syntax error: string is not an equation ('=' is missing)",
	1:f"Syntax error: forbidden character, at index {index} -> '{letter}'",
	2:f"Syntax error: term '{polynom}' not proprely formated. (Expected 'a [* X^p])'"
	}
	print(error_message.get(code))
	exit()

def format_check(polynom, index):
	string = polynom[index:]
	substring2 = polynom[:index]
	for i in range(len(string)):
		if i == 0 or string[i] == ' ':
			continue
		if string[i].isdigit():
			print_error(polynom, 0, 0, 2)
		if string[i] == '*':
			substring = string[i:]
			for j in range(len(substring)):
				if j == 0 or substring[j] == ' ':
					continue
				if substring[j].isdigit():
					for k in range(len(substring2)):
						if substring2[k].isdigit() or substring2[k] == '*':
							print_error(polynom, 0, 0, 2)
					return True
			print_error(polynom, 0, 0, 2)
		else:
			print_error(polynom, 0, 0, 2)
	found = False
	for l in range(len(substring2)):
		if substring2[l] == ' ':
			continue
		if substring2[l] == '*':
			found = True
		if substring2[l].isdigit() and found == True:
			print_error(polynom, 0, 0, 2)
	return True
