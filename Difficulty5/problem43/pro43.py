import sympy
import numpy as np

global ans
ans = []
chk = [0]*10
div = [2, 3, 5, 7, 11, 13 ,17]

def dfs(i, s, n):
    if s == "140":
        print(i, s, n)
    if i >= 4:
        if s == "1406357289":
            print(s[i-3:]) 
        tmp = s[i-3:]
        # print(tmp)
        if int(tmp) % div[i-4] != 0:
            return False
    
    if i == 10:
        ans.append(int(s))
        return True
    
    chk[n] = 1
    for d in range(0, 10):
        if chk[d] == 1:
            continue
        dfs(i+1, s+str(d), d)
    chk[n] = 0
    return False

for i in range(0, 10):
    dfs(1, str(i), i)

# dfs(1, str(1), 1)
print(ans, sum(ans))
