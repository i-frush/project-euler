import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

import Utils.primetable
import sympy
import numpy as np




primes = Utils.primetable.get_prime_under(9999)


a = [i for i in primes if i > 999]
ans = []

for i in range(0, len(a)):
    print(a[i])
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i]+a[k] == 2*a[j]:
                for d in range(1, 5):
                    if len(set(str(a[i]))) == d and len(set(str(a[j]))) == d and len(set(str(a[k]))) == d:
                        s = str(a[i]) + str(a[j]) + str(a[k])
                        if len(set(s)) == d:
                            ans.append((a[i], a[j], a[k]))

print(ans)
