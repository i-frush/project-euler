import sympy
import numpy as np

ans_a = 0
ans_b = 0
maxn = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while sympy.isprime(n*n + a*n + b):
            n += 1
        # print(n)
        maxn = max(maxn, n)
        (ans_a,ans_b) = (a,b) if maxn == n else (ans_a,ans_b)
    
print(ans_a, ans_b, ans_a*ans_b)
    