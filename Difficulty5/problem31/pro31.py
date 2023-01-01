import sympy
import numpy as np

global mny
mny = [200, 100, 50, 20, 10, 5, 2, 1]


def check(n, i):
    res = []
    tmp = n//i
    while tmp >= 0:
        res.append((tmp, n-tmp*i))
        tmp -= 1
    return res


def dfs(n, i):
    if i == 7:
        return 1

    # print(i)
    stas = check(n, mny[i])
    return sum([dfs(a[1], i+1) for a in stas])


print(dfs(200, 0))
