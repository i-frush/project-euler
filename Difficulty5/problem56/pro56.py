import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

ans = 0
for a in range(1, 100):
    for b in range(1, 100):
        n = a**b
        ans = max(ans, sum([int(c) for c in str(n)]))
print(ans)