import copy
def cartesian_product(X, Y):
    output = []
    for i in X:
        for j in Y:
            output.append((i,j))
    return output
X = [1, 2]
Y = ['a', 'b', 'c', 'd']

print cartesian_product(X, Y)

def power_set(X):
    if len(X) == 0:
        return [[]]
    else:
        head = X[0]
        tail = X[1:] 
        result = power_set(tail)
        output = copy.deepcopy(result)
        for i in result:
            tempCopy = copy.deepcopy(i)
            copy.insert(0, head)
            output.append(tempCopy)
        return output
P = cartesian_product(X,Y)      
print power_set(P)
