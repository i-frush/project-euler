import sympy
import numpy as np
from functools import reduce

# 快速幂
# a^n%mod
def fast_pow(a, n ,mod):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = res * a % mod
        a = a * a % mod
        n //= 2
    return res % mod

mod = 10**10
lst = [fast_pow( i, i ,mod) for i in range( 1, 1001 )]
print( lst )
ans = reduce( lambda x, y: (x + y)%mod , lst )
print( ans%mod )