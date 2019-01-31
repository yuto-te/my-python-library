"""
素因数分解
約数列挙
"""


"""
e.g. 2**2 * 3**2 * 5**2 = [(2, 2), (3, 2), (5, 2)]
"""
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


"""
e.g. 900 = [1, 2, 3, ..., 450, 900]
"""
def divisionize(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    # divisors = sorted(divisors) # ソートが必要であれば
    return divisors
