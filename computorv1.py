import argparse
from tools.parse import parse
from tools.compute import compute
from tools.reduce import reduce
from tools.graph import display_graph

def resolve(eq, verbose, graph) :
	degree = 0
	left, right, degree = parse(eq, verbose, degree)
	left, degree = reduce(left, right, degree)
	print("Polynomial degree:", degree)
	if degree > 2:
		print("The polynomial degree is stricly greater than 2, I can't solve.")
		exit()
	compute(left, verbose, degree)
	if graph == True:
		display_graph(left)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("equation", type=str, help="Equation to resolve")
	parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose")
	parser.add_argument("-g", "--graph", action="store_true", help="Enable graph visualisation")
	args = parser.parse_args()
	resolve(args.equation.strip(), args.verbose, args.graph)
