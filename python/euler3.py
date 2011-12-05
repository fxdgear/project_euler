#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
#

from utils import prime_factors

VALUE = 600851475143
factors = prime_factors(VALUE)
print "Largest Prime factor is: %s" % factors[-1]
