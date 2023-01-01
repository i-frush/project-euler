import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

import Utils.primetable

nmax = 1000000
primes = Utils.primetable.get_prime_under(nmax)

sump = [0] + [ d for d in primes ]
for i in range(1, len(sump)):
    sump[i] = sump[i] + sump[i-1]

k = len(sump)
ans = 0
anss = 0
for i in range(0, k):
    print("-", i, "/", k)
    for j in range(i+1, k):
        tmp = sump[j] - sump[i]
        if tmp > 1000000:
            break
        if sympy.isprime(tmp):
            if j - i > ans:
                ans = j - i
                anss = tmp

print(ans, anss)