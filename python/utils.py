

def is_prime(n):
    import math
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def product_of(factors):
    if len(factors) == 0:
        return 0
    else:
        return reduce(lambda a, b: a * b, factors)
