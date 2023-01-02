import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")


n = sympy.Rational(1, 1)
n.denominator
ans = 0
for i in range(0, 1000):
    n = 1/(n+1)
    n = 1 + n
    if len(str(n.numerator)) > len(str(n.denominator)):
        ans += 1
print(ans)