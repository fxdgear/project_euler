#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
#

from math import sqrt, floor

n = 13195

def eratosthenes(max):
    #Takes in a number, and returns all primes between 2 and that number

    #Start with all of the numbers
    primes = range(2,max+1)
    #Start running through each number
    for i in primes:
        #Start with double the number, and
        j = 2
        #remove all multiples
        while i * j <= primes[-1]:
            #As long as the current multiple of the number
            #is less than than the last element in the list
            #If the multiple is in the list, take it out
            if i * j in primes:
                primes.remove(i*j)
            j += 1
    return primes



primes = eratosthenes(n)
factors = []
for p in primes:
    if (float(n)/p)-floor(float(n)/p) == 0:
        factors.append(p)

print factors


