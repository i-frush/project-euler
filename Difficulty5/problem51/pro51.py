import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")


def replacen(n, d):
    res = []
    s = str(n)
    for i in range(0, 10):
        res.append(int(s.replace(str(d), str(i))))
    return res


def check(l, n):
    return sum(1 for i in l if sympy.isprime(i)) == n\
        if len(str(l[0])) != len(str(l[1])) else\
           sum(1 for i in range(1, 10) if sympy.isprime(l[i])) == n


n = 10
flag = True
while flag:
    if n % 10000 == 0:
        print('-', n)
    for i in range(0, 10):
        l = replacen(n, i)
        if check(l, 6):
            print(n, l)
            flag = False
            break
    n += 1
