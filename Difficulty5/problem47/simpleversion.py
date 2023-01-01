import sympy
import numpy as np

a = [[j for j in sympy.factorint(i).keys()] for i in range(2, 5)]

cnt = 1
flag = True
while flag:
    if cnt>600 and cnt<650:
        print('-', cnt, a)
        
    flag = False
    for i in range(0,3):
        if len(a[i]) != 3:
            flag = True
            break
        
    if not flag:
        if len(set(a[0]+a[1]+a[2])) != 9:
            flag = True  
    
    (a[0], a[1]) = (a[1],a[2])
    a[2] = [j for j in sympy.factorint(cnt+4).keys()]
    cnt += 1

print(cnt ,a)
