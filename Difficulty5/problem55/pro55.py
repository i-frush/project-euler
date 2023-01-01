import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

def check(n):
    for i in range(0, 50):
        tmp = str(n)[::-1]
        n = n + int(tmp)
        
        tmp = str(n)[::-1]
        if str(n) == tmp:
            return True
    return False

ans = 0
for i in range(0, 10000):
    ans += 0 if check(i) else 1
print(ans)