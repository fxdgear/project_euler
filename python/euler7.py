"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from utils import gen_primes

LIMIT = 10001

prime_gen = gen_primes()
c = 0
while c != LIMIT:
    prime = prime_gen.next()
    c += 1
print prime
