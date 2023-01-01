import sympy
import numpy as np

def check(s):
    for i in range(1, len(s)):
        l = int(s[:i])
        r = int(s[len(s)-i:])
        # print( l, r )
        if not (sympy.isprime(l) and sympy.isprime(r)):
            return False
    return True

cnt = 0
ans = []
n = 7
while cnt <11:
    n = sympy.nextprime(n)
    if check(str(n)):
        cnt += 1
        ans.append(n)

print(ans ,sum(ans))