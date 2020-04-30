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
