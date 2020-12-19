
p = True
q = False

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

print AND(p,q)
print OR(p,q)
print IF(p,q)
print IFF(p,q)
print NOT(p)
print NOT(q)
print 
print "*" * 40  
print

#2
p = True
q = False

def evaluate(*formula):
    if formula[0] is 'OR':
        return formula[1] or formula[2]
    if formula[0] is 'AND':
        return formula[1] and formula[2]
    if formula[0] is 'IF':
        return not(formula[1]) or formula[2]
    if formula[0] is 'NOT':
        return not(formula[1])
    if formula[0] is 'IFF':
        return (formula[1] and formula[2]) or (not(formula[1]) and not(formula[2]))
    return 

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

#Question 3
def AND(p, q):
   if p == True and q == True:
       return True
   return False
  
def OR(p,q):
   if p == False and q == False:
       return False
   return True
  
def IF(p,q):
   if p == True and q == False:
       return False
   return True

def NOT(p):
   if p == True:
       return False
   return True
  
def IFF(p,q):
   if (p == True and q == True) or (p == False and q == False):
       return True
   return False

p = False
q = False
def evaluate_r(formula):
    
    if formula[1:]:
     evaluate_r(formula[1:])
    if formula[0] == 'AND':
     return AND(formula[1], formula[2])
    elif formula[0] == 'OR':
     return OR(formula[1], formula[2])
    elif formula[0] == 'IF':
     return IF(formula[1], formula[2])
    elif formula[0] == 'IFF':
     return IFF(formula[1], formula[2])
    elif formula[0] == 'NOT':
     return NOT(formula[1])

print "p =", p
print "q =", q

print "(p or q) or -p: ", evaluate_r(('OR', ('OR', p, q), ('NOT', p)))
print "(p or q) and -p: ", evaluate_r(('AND', ('OR', p, q), ('NOT', p)))