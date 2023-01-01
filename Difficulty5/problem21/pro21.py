import sympy
import numpy as np
d = [ sum(sympy.divisors(i))-i  for i in range( 0, 100001 )]

ans = 0
for i in range( 1, 10001 ):
    if i == d[d[i]] and i!=d[i]:
        ans += i
print( ans )
