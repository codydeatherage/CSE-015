def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def IF(p, q):
    return NOT(p) or q

def NOT(p):
    return not(p)

def IFF (p, q):
    return OR(AND(p,q), AND(NOT(p),NOT(q)))

print "Basic Operations Test"
print
p = True
q = False
print AND(p,q)
print OR(p,q)
print IF(p,q)
print IFF(p,q)
print NOT(p)
print NOT(q)
print 
print "*" * 40
print

def evaluate(*formula):
    if formula[0] is 'OR':
        return formula[1] or formula[2]

    if formula[0] is 'AND':
        return formula[1] and formula[2]

    if formula[0] is 'IF':
        return not(formula[1]) or formula[2])

    if formula[0] is 'NOT':
        return not(formula[1])

    if formula[0] is 'IFF':
        return OR(AND(formula[1],formula[2]), AND(not(formula[1]),not(formula[2])))
    return 

print "Simple Evaluation Function Test"
print
p = True
q = False
print "p =", p
print "q = ", q     
print
print "(p or q): ", evaluate ('OR', p, q)
print "(p and q): ", evaluate ('AND', p, q)
print "(p -> q): ", evaluate ('IF', p, q)
print "(p <-> q): ", evaluate ('IFF', p, q)
print "-p: ", evaluate ('NOT', p)
print
print "*" * 40
print