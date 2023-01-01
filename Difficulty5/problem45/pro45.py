import sympy
import numpy as np

T = [i*(i+1)//2 for i in range(0, 100000)]
P = [i*(3*i-1)//2 for i in range(0, 100000)]
H = [i*(2*i-1) for i in range(0, 100000)]

cnt = {}

for i in T:
    if i in cnt.keys():
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in P:
    if i in cnt.keys():
        cnt[i] += 1
    else:
        cnt[i] = 1
        
for i in H:
    if i in cnt.keys():
        cnt[i] += 1
    else:
        cnt[i] = 1

ans = [i for i in cnt.keys() if cnt[i] == 3]
print(ans)