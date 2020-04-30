import matplotlib.pyplot as plt

def display_graph(left):
	a=[]
	b=[]
	for x in range(-50,50,1):
		y = 0
		for i in left:
			sign = 1 if i.sign == True else -1
			if i.x == True:
				result = sign * i.factor * x**i.power
			else :
				result = sign * i.factor
			y += result
		a.append(x)
		b.append(y)
	fig= plt.figure()
	axes=fig.add_subplot(111)
	axes.plot(a,b)
	axes.set_ylabel("y")
	axes.set_xlabel("x")
	axes.set_title("Computorv1")
	plt.show()