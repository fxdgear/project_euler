#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
#

import random
import fractions
from utils import is_prime, product_of

FACTORS = []

VALUE = 600851475143


def f(x, a, n):
    return (x ^ 2 + a) % n


def rho(f, n, limit=100):
    a = random.randint(1, (n - 3))
    b = random.randint(1, (n - 1))
    c = a
    d = b
    g = 1
    i = 0
    while g == 1 and i <= limit:
        i += 1
        c = f(c, a, n)
        d = f(d, a, n)
        g = fractions.gcd(abs(c - d), n)

    if g == 1:
        return None
    else:
        return g


def find_factor(n, f):
    factor = rho(f, n)
    i = 0
    # If we didn't find a factor, keep trying for 10000 times
    while factor is None and i <= 1000:
        factor = rho(f, n)
        i += 1

    # we found a factor, is it prime? return it, else, factor the factor.
    if factor:
        if is_prime(factor):
            return factor
        else:
            return find_factor(factor, f)
    # We didn't find a factor, try again.
    else:
        return find_factor(n, f)


def main():
    n = VALUE
    while product_of(FACTORS) != VALUE:
        factor = find_factor(n, f)
        FACTORS.append(factor)
        n = n / factor
    FACTORS.sort()
    print "Largest Prime factor is: %s" % FACTORS[-1]

if __name__ == "__main__":
    main()
