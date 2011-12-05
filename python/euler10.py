"""
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

"""
from utils import gen_primes

limit = 2000000
prime_gen = gen_primes()
p = prime_gen.next()
value = 0
while p < limit:
    value += p
    p = prime_gen.next()

print value