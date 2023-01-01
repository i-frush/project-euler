
import sys
import sympy
import numpy as np
sys.path.append("D:\Documents\codePractice\eulerProject")
import Utils.primetable as primetable

nmax = 1000000

chk = [0]*(nmax+1)
primes = primetable.get_prime_under(nmax)

here = 0
for i in primes:
    
    tmp = i // 1000
    if tmp > here:
        here = tmp
        print(here, "/", 1000)
    for j in range(0, nmax):
        tmp = i + j*j*2
        if tmp > nmax:
            break
        chk[tmp] = 1

ans = [i for i in range(1, nmax) if chk[i] == 0 and i % 2 == 1]
print(ans)