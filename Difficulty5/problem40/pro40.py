import sympy
import numpy as np

i = 1
n = 1
s = "0"
while len(s) <= 1000000:
    s += str(n)
    n += 1
    
ans = 1
while i <= 1000000:
    ans *= int(s[i])
    print(s[i])
    i *= 10
print(ans)