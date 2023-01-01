import sympy
import numpy as np
d = [ sum(sympy.divisors(i))-i  for i in range( 0, 100001 )]

abd = [ i for i in range( 1,50001 ) if d[i] > i ]

check = [1]*28124
check[0] = 0

for i in abd:
    for j in abd:
        if i + j > 28123:
            break
        check[i+j]=0

ans = sum( [ i for i in range( 1, 28124) if check[i] == 1] )
print( ans )