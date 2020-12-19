# CSE15 Discrete Mathematics
# Lab Assignment 5

# You are required to complete this assignment on your own. This means every single line of code has to be your original work. You may talk to your fellow students about the problems, and exchange ideas, but not code. Similarly, you may research the problems on the internet, but you may not copy and paste entire implementations of functions. You can look at code posted online in order to help you understand the ideas behind the algorithm, but you have to generate your solution on your own, without looking at the code you found online. 

# Failure to adhere to the above instructions will be treated as plagiarism, and if you are suspected of plagiarism for this assignment, the UC Merced disciplinary committee will be involved in dealing with your case.

# Mathematical functions that may be of use
from math import sqrt
from math import ceil


# Exercise 1. Implement the algorithm covered in lectures (and not any other algorithm) that determines if an integer n is prime. Your function should return True, if n is prime, and False otherwise. Your algorithm has to be effective for n ~ 1,000,000,000,000. A description of the algorithm covered in class appears on page 258 of the Rosen textbook.
def isPrime(n):

    for i in range(2, int(sqrt(n)) + 1):

        if n % i == 0:

            return False

    return True



# Exercise 2. Using the isPrime function above, implement a function that takes in an integer n, and returns the smallest prime number greater than n. Your code should computer in a reasonable time for n ~ 1,000,000,000,000.


def nextPrime(n):

    nP = ceil(n)
    for i in range(2, nP + int(sqrt(n)) + 1):

        nP = nP + 1

        if(isPrime(nP) == True):

         return nP




# Exercise 3. It is sometimes necessary to find all prime numbers less than some integer n. Implement a function that takes in an integer n and returns a list of all primes that are less than or equal to n. Your algorithm should be effective for n ~ 1,000,000
def allPrimes(n):

    primesList = []

    aP = floor(n))
    for i in range(2, n+1):

       aP = 1
 
       if(isPrime(aP) == True and aP >= 2):

            primesList.append(aP)

    return primesList


# Exercsie 4. The Fundamental Theorem of Arithmetic tells us that every positive integer n, can be expressed uniquely as a product of primes in non-decreasing order. Implement the method covered in class (and not any other method), for finding prime factorizations of integers. The function below should take in an integer n, and return a list of the prime factors of n.
def factorize(n):
    # Provide a correct implementation for this function
    return []
    
    
        
# Exercise 5. The scrurity of many popular cryptographic schemes, such as RSA, rests on the fact that factorizing numbers is difficult, meaning that it takes long to factorize some numbers. Use your code from exrecise 4 to experiment with different inputs and try to figure out what makes some numbers take longer to factorize than others. Explain what you found in the string/comment below

ex5answer = """
Write your answer for exercise 5 within the triple-double quotes:




"""   



# Exercise 6. In some cryptographic applications, it is necessary to use a special kind of prime numbers called safe primes. These are primes of the form q = 2p + 1, where p is also prime. The integer p is known as a Sophie Germain prime. Write a function that takes in an integer n, and returns the first safe prime, such that p > n. Your function should output a tuple (p, q), comprising the Sophie Germain prime, and the safe prime.
def safePrime(n):
   q = 2*n + 1

   for i in range(n, q)  
    if(isPrime(q) == True):

         return (n, q)
 

