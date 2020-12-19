def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)   
print gcd(128, 60)

def groupLikeTerms(exp):

    termTable = {}

    result = []

    for tuple in exp:

        num, term = tuple

        if term in termTable:

            termTable[term] += num

        else:

            termTable[term] = num

    for i in termTable:

        var = i
        num = termTable[var]

        result.append((num, var))

    result.sort()

    return result

print groupLikeTerms([(5, "x"), (5, "y"), (-3, "x")])

def extended_euclid(a, b):

    a0 = a

    b0 = b

    list = []

    xp, x = 1, 0

    yp, y = 0, 1

    while b:

        quot, rem = divmod(a,b)

        x, xp = xp - quot*x, x

        y, yp = yp - quot*y, y

        a, b = b, rem

    list.append(a)

    if xp > yp:

        list.append([(xp,a0),(yp,b0)])

    else:

        list.append([(yp,b0),(xp,a0)])

    return list

print extended_euclid(101,23)


def inverse(n, m):

    if gcd(n,m) == 1 and m > 1:

        [gcdValue, [(s,a),(t,b)]] = extended_euclid(n,m)

        return s

    else:

        return "Does not exist"
print inverse(23, 101)






























