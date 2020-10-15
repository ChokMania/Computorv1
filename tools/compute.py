def second_degree(a, b, c, verbose):
	d = b**2 - (4 * a * c)
	if verbose == True:
		print(f"\na = {a}\nb = {b}\nc = {c}\nΔ = {d}\n")
	if d > 0:
		print("Discriminant is strictly positive, so this equation got 2 solutions:")
		if verbose == True:
			print(f"\nx' = (-b - √Δ) / 2a \nx' = ({-b} - {d ** 0.5}) / 2 * {a}\nx' = ", end ="")
		print(f"{(-b - (d ** 0.5)) / (2 * a)}")
		if verbose == True:
			print(f"\nx\" = (-b + √Δ) / 2a \nx\" = ({-b} + {d ** 0.5}) / 2 * {a}\nx\" = ", end ="")
		print(f"{(-b + (d ** 0.5)) / (2 * a)}")
		if verbose == True:
			print("")
	elif d == 0:
		print("Discriminant is equal to zero, so this equation got only 1 solution:")
		if verbose == True:
			print(f"\nx = −b / 2a\nx = {-b} / 2 * {a}\nx = ", end="")
		print(f"{-b / (2 * a)}")
		if verbose == True:
			print("")
	elif d < 0:
		print("Discriminant is strictly negative, so this equation got 2 complexes solutions:")
		if verbose == True:
			print(f"\nz1 = (-b - i√|Δ|) / 2a\nz1 = (-1 - i√|{-d}|) / 2 * {a}\nz1 = ", end="")
		print(f"({-b} - i√{abs(d)}) / {2 *a}")
		if verbose == True:
			print(f"\nz2 = (-b + i√|Δ|) / 2a\nz2 = ({-b} - i√|{-d}|) / 2 * {a}\nz1 = ", end="")
		print(f"({-b} + i√{abs(d)}) / {2 *a}")
		if verbose == True:
			print("")

def first_degree(b, c,verbose):
	if verbose == True:
		print(f"\na = {b}\nb = {c}\n")
	print("The solution is:")
	if verbose == True:
		print(f"\nx = -b/a\nx = {-c}/{b}\nx = ", end="")
	print (f"{-c/b}")
	if verbose == True:
		print("")

def compute(left, verbose, degree):
	a, b, c = 0, 0, 0
	for i in left:
		sign = 1 if i.sign == True else -1
		if i.power == 2:
			a = i.factor * sign
		elif i.power == 1:
			b = i.factor * sign
		elif i.power == 0:
			c = i.factor * sign
	if degree == 2:
		second_degree(a, b, c, verbose)
	elif degree == 1:
		first_degree(b, c, verbose)
	elif degree == 0:
		if c == 0:
			print ("Every real are solution")
		else:
			print("There is no solution for this equation")
		exit()