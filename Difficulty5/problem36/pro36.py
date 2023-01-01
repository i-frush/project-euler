import sympy
import numpy as np

def check(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

ans = [i for i in range(0, 1000000) \
    if (check(str(i)) and check(format(i, 'b')))]    
print(ans ,sum(ans))
