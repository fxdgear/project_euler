# Project Euler: Problem 1
#
# If we list all the natural numbers below 10 that are multiples of
# 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

import itertools

CONST = 1000
c = CONST +1

# create list of all multiples of 3 that are less than 1000
m3 = [x*3 for x in range(0, (c/3 + 1))]

# create list of all multiples of 5 that are less than 1000
m5 = [x*5 for x in range(0, (c/5))]

# combine lists and remove duplicates
multiples = set(list(itertools.chain(*[m3, m5])))
# compute sum of all multiples of 3 or 5 below 1000.
value = sum(list(multiples))

print value



