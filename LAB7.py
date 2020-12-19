def chars_to_nums(c):
    nums = []
    for i in c:
        nums.append(ord(i)-32)
    return nums
    
def nums_to_chars(n):
    chars = ""
    for i in n:
        chars = chars + chr(i+32)
    return chars

# Exercise 1: Implement an encode procedure for the Caesar cipher.    
def caesar_encode(plaintext, key, mod):
    charNum = chars_to_nums(plaintext)
    for i in range(len(charNum)):
        charNum[i] += key
    result = nums_to_chars(charNum)
    return result
print caesar_encode("HELLO", 3, 95)

# Exercise 2: Implement the decode procedure for the Caesar cipher.
def caesar_decode(ciphertext, key, mod):
    charNum = chars_to_nums(ciphertext)
    for i in range(len(charNum)):
        charNum[i] -= key
    result = nums_to_chars(charNum)
    return result
print caesar_decode("KHOOR",3, 95)

# Exercise 3:
ex_5_plaintext = "SUPERSECRET"

# Exercise 4: Implement the encode function for the Affine cipher.
def affine_encode(plaintext, a, b, m):
    charNum = chars_to_nums(plaintext)
    for i in range(len(charNum)):
        charNum[i] = (a * charNum[i] + b) % m
    result = nums_to_chars(charNum)
    return result
print affine_encode("HELLO", 7, 23, 95)

# Exercise 5: Implement the decode function for the Affine cipher.
def affine_decode(ciphertext, a, b, m):

    result = ""

    charNum = chars_to_nums(ciphertext)

    for i in range(0, m):

        newA = (a * i) % m

        if(newA == 1):

            modInv = i

    for i in range(len(charNum)):

        charNum[i] = (modInv * (charNum[i]- b)) % m

    result = nums_to_chars(charNum)

    return result

print affine_decode("2|NNc", 7, 23, 95)
