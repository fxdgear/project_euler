#
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
#
# According to http://en.wikipedia.org/wiki/Palindromic_number
# There are 1999 palindromic numbers under 10^6
#
# According to our requriements the largest number which is the product of 2 3digit
# numbers is less than 10^6
#
# that means the total number of palindromic numbers is 1999
# Also note that there are 113 palindromic prime numbers
#
# Therefore there are (1999 - 113) = 1886 palindrome numbers
#
# Therefore the largest palindromic number which is a product two 3 digit numbers
# is between 9009 and 1000000
#
# To further reduce the number of candidates we're looking for the product of two
# 3 digit numbers, which would max at 999 * 999 = 998001
#
# The lower bound of our numbers would be 100 * 100 = 10000
#
# now to reiterate we are looking for the largest Palindrome which is a
# product of 2 3-digit numbers. These palindromes are contained within the set
# 10000 < x < 998001

from math import floor
from utils import is_palindrome, is_prime
from decimal import Decimal


def non_primes(lst):
    return [x for x in lst if not is_prime(x)]


def find_products(p):
    x = Decimal(999)
    p = Decimal(p)
    y = p / x

    # Keep decrementing x till we get a value for y that is 3 digits
    # if x gets below 3 digits stop and return none.
    while len(str(y)) != 3 and x > 101:
        x -= 1
        y = p / x

    # y and x are both 3 digits, return x and y
    if y == floor(y) and len(str(y)) == 3:
        return x, y
    else:
        return None, None


def main():
    # create list of Palindromes between 10000 and 998001
    palindromes = [x for x in xrange(10000, 998001) if is_palindrome(str(x))]

    # remove prime palindromes, to reduce the number of options to try
    palindromes = non_primes(palindromes)

    # reverse list to start with the highest palindromes first.
    # find products, once we find a palindrome that meets the problem requirements
    # return the palindrome and the values used to produce it.
    palindromes.reverse()
    for p in palindromes:
        x, y = find_products(p)
        if x and y:
            return p, x, y


if __name__ == "__main__":
    p, x, y = main()
    print "%s = %s X %s" % (p, x, y)
