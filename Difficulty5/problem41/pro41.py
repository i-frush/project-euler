import sympy
import numpy as np

# key: dfs from the largest num(987654321)， and the first prime is ans

digchk = [0]*10

def dfs(i, n, s, limit):
    if i==limit :
        # print(s)
        if sympy.isprime(int(s)):
            print("ans: " + s)
            return True
        else:
            return False
    
    digchk[n] = 1
    for d in range(limit, 0, -1):
        if digchk[d] == 0:
            if dfs(i+1, d, s+str(d), limit):
                return True
    digchk[n] = 0
    return False

for d in range(9, 0, -1):
    dfs(1, d, str(d), d)