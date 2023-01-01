import sympy
import numpy as np

global stas, ans
stas = [0]*10
ans = []


def check(snum):
    for i in range(1, 8):
        for j in range(i+1, 9):
            # print(snum ,i ,j)
            a = int(snum[:i])
            b = int(snum[i:j])
            c = int(snum[j:])
            if a * b == c:
                print(a, b, c)
                ans.append(c)
                return True
    return False


def dfs(i, num, s):
    if i == 8:
        return 1 if check(s) else 0
    res = 0
    stas[num] = 1
    for n in range(1, 10):
        if stas[n] == 0:
            res += dfs(i+1, n, s+str(n))
    stas[num] = 0
    return res


for i in range(1, 10):
    dfs(0, i, str(i))
print(sum(set(ans)))
