import itertools
from itertools import product
from itertools import combinations

def cartesian_product(X,Y):
	output = []
	for x in itertools.product(X,Y):
		output.append(x)
	return output
X = [1,2]
Y = ['a', 'b', 'c', 'd']
print cartesian_product(X,Y)
print

def power_set(X):
	pset = []
	for x in range(len(X) + 1):
		for y in itertolls.combinations(X,x):
		  pset.append(y)
	return pset
print power_set(Y)