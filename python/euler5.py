"""
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by
    all of the numbers from 1 to 20?
"""

from utils import is_prime, product_of

values = xrange(1, 21)
primes = [x for x in values if is_prime(x)]


def check(value):
    """
    Check that value is evenly divisiable by all values
    """
    for x in values:
        y = value / x
        if y * x != value:
            return False
    return True


def main():
    value = p = product_of(primes)
    # check product of primes, if it doesn't work
    # iterate by product of primes and try again
    while not check(value):
        value += p
    return value


if __name__ == "__main__":
    print main()
