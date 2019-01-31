"""
最大公約数
最小公倍数
"""
import math
from functools import reduce


def gcd(a, b):
    return math.gcd(a, b)


def lcm(a, b):
    return (a*b) // math.gcd(a, b)


"""
e.g. gcd_list([27, 18, 9, 3]) = 3
"""
def gcd_list(numbers):
    return reduce(math.gcd, numbers)


"""
e.g. lcm_list([27, 9, 3]) = 27
"""
def lcm_list(numbers):
    return reduce(lcm, numbers, 1)