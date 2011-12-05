"""
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^(2) + b^(2) = c^(2)

    For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    From Euclid's formula:

    for m > n and m,n are Natural numbers
    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2

    from the constraints of our problem a + b + c = 1000

    substituting the previous equations and solving for n we get:

    n = (500/m) - m

    using Euclids equations we can genarate Pythagorean Triples.
    iterating over m and solving for various n's
    we can gernate Pythagorean Triples.

    The number of triples genrated this way are FAR less than by brute forcing them.
    And it is much faster to solve.
"""
from utils import product_of
m = 1


def generate_triple(m, n, k=1):
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return (k * a, k * b, k * c)


def n(m):
    return (500/m) - m

for m in xrange(1, 1000):
    if n(m) > 0 and m > n(m):
        triple = generate_triple(m, n(m))
        if sum(triple) == 1000:
            break

print product_of(*triple)
