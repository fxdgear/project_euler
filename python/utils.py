

def is_prime(n):
    import math
    n = abs(n)
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def product_of(values):
    if len(values) == 0:
        return 0
    else:
        return reduce(lambda a, b: a * b, values)


def reverse_string(string):
    x = [x for x in string]
    x.reverse()
    return "".join(x)


def is_palindrome(string):
    reverse = reverse_string(string)
    return string == reverse
