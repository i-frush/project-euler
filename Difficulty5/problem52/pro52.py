import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

def check(a ,b):
    return set(str(a)) == set(str(b))

n = 1
flag = False
while not flag:
    flag = True
    for i in range(2, 7):
        flag = flag and check(n, i*n)
    if flag:
        print(n)
    n += 1