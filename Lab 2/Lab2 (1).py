import itertools
from itertools import product
from itertools import combinations

def cartesian_product(X,Y):
	list = []
	for i in itertools.product(X,Y):
		list.append(i)
	return list
X = [1,2]
Y = ['a', 'b', 'c', 'd']
print cartesian_product(X,Y)
print

def power_set(X):
	set = []
	for i in range(len(X) + 1):
		for y in itertolls.combinations(X,i):
		  set.append(y)
	return set
print power_set(Y)