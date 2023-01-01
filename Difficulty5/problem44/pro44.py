import sympy
import numpy as np

# key:
# 1.from P1 to find the first any solution D1
# 2.then we can decide the upper limit of Pn
# because min|P_n-P_i|(n>i) for P_n is P_n-P_n-1=3n-2
# so if 3n-2 > D1,n is upper limit

P = [i*(3*i-1)//2 for i in range(0, 10000000)]
chk = set(P)

Dmin = 99999999
n = 2
while Dmin >= 3*n-2:
    for i in range(n-1, 0, -1):
        if P[n] - P[i] > Dmin:
            break
        
        if (P[n] - P[i]) in chk and (P[n] + P[i]) in chk:
            Dmin = min(P[n] - P[i], Dmin)
            print(n ,i)
            print(Dmin)
    n += 1
    

print(Dmin)
