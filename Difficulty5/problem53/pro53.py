import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

ans = 0
for n in range(1, 101):
    for r in range(1, n):
        ans += 1 if sympy.binomial(n, r) > 1000000 else 0 
        
print(ans)