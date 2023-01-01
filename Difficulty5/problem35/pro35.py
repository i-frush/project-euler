import sympy
import numpy as np


def check(n):
    s = str(n)
    for i in range(0, len(s)):
        tmp = int(s[i:]+s[:i])
        if not sympy.isprime(tmp):
            return False
    return True

ans = []
for i in range(1, 1000001):
    if check(i):
        ans.append(i)
print(ans ,len(ans))