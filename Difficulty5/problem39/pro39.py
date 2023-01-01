import sympy
import numpy as np

cnt = [0]*1005

for a in range(1, 1000):
    for b in range(a, 1000):
        if a+b > 1000:
                break
        for c in range(b, 1000):
            if a+b+c > 1000:
                break
            if c**2 == a**2 + b**2:
                cnt[a+b+c] += 1
                
print(cnt.index(max(cnt)))
    