import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

n = 1
pnum = 0
dnum = 1
num = 1

while True:
    n += 2
    d = n-1
    dnum += 4
    for i in range(0, 4):
        num += d
        pnum += 1 if sympy.isprime(num) else 0
    
    if pnum*10 < dnum:
        print(n)
        break