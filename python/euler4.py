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
# that means the total number of palindromic numbers is 1999
#
#
#

from utils import is_palindrome


def main():
    print is_palindrome(str(2202))

if __name__ == "__main__":
    main()
