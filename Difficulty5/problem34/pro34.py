import sympy
import numpy as np

# nmax = 999999
ans = []
for i in range(3, 1000000):
    tmp = sum([sympy.factorial(int(d)) for d in str(i)])
    if tmp == i:
        ans.append(i)
print(ans ,sum(ans))
