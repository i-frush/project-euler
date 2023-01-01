import sympy
import numpy as np

# the upper limit: 999999

nmax = 999999
lst = []
for i in range(2, nmax):
    if sum([int(d)**5 for d in str(i)]) == i:
        print(i)
        lst.append(i)
        
print(sum(lst)) 
