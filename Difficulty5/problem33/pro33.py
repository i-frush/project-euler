import sympy
import numpy as np

ans = 1
for a in range(10, 100):
    for b in range(a+1, 100):
        if a % 10 == 0 and b % 10 == 0:
            continue
        
        x = sympy.Rational(a, b)
        a1 = a//10
        a2 = a % 10
        b1 = b//10
        b2 = b % 10
        if a1 == a2 and b1 == b2:
            continue
        
        if a1 == b1:
            y = sympy.Rational(a2, b2)
        elif a1 == b2:
            y = sympy.Rational(a2, b1)
        elif a2 == b1:
            y = sympy.Rational(a1, b2)
        elif a2 == b2:
            y = sympy.Rational(a1, b1)
        else:
            y = 1
        if x==y:
            print(a ,b ,x ,y)
            ans *= x
print( ans )
