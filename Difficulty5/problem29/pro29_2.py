import sympy
import numpy as np

amax = 100
bmax = 100

lst = []
for a in range(2 ,amax+1):
    for b in range(2, bmax+1):
        lst.append(a**b)

slst = set(lst)
print(len(slst))
