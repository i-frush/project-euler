import sympy
import numpy as np

a = [[j for j in sympy.factorint(i).keys()] for i in range(2, 6)]

cnt = 1
flag = True
while flag:
    if cnt%10000 == 0:
        print(cnt, a)
        
    flag = False
    for i in range(0,4):
        if len(a[i]) != 4:
            flag = True
            break
        
    
    (a[0], a[1], a[2]) = (a[1],a[2],a[3])
    a[3] = [j for j in sympy.factorint(cnt+5).keys()]
    cnt += 1

print(cnt ,a)
    