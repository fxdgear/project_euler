from math import floor, log


def is_prime(n):
    import math
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def product_of(*values):
    if len(values) == 0:
        return 0
    else:
        return reduce(lambda a, b: int(a) * int(b), values)


def reverse_string(string):
    x = [x for x in string]
    x.reverse()
    return "".join(x)


def is_palindrome(string):
    reverse = reverse_string(string)
    return string == reverse


def sieve(limit):
    primes = []
    values = [x for x in xrange(2, limit + 1)]
    candidates = [x for x in xrange(2, limit + 1)]

    for i in values:
        try:
            p = candidates[0]
        except:
            break
        primes.append(p)
        c = 1
        while p * c in values:
            try:
                candidates.remove(p * c)
            except:
                pass
            c += 1

    return primes


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)


def gen_primes():
    """
    Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
