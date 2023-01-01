import sympy
import numpy as np

# nmax = 10000
nmax = 10000

ans = []
for i in range(1, nmax):
    s = ""
    j = 1
    while len(s) <= 9:        
        if len(set(s)) == 9 and  ('0' not in set(s)):
            ans.append(s)
        s = s + str(i*j)
        j += 1
        
print(ans)