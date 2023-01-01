# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/8 2:40
# site :
# file : pro_754.py
# solftware : PyCharm

# G(n) = n! without factor of n
from eulerutils import calcu
import sympy
from eulerutils import calcu
import functools

# at first ,i try to find a formula using arithmetical function ,but i falsed
# then i try to print table to find the regular of the prime factors' distribution.
# and i find it:
# vi = n-i - [(n-i)/i]*sum[(n-1)/pn] - sum[((n-i)%i)/pn]
n = 10
mod = 10 ** 9 + 7

prime_lst = sympy.primerange(2, n - 1)
ans = 1
for i in range(2, n):
    print(i)
    tmp_lst = [p for p in sympy.primefactors(i) ]
    # vi = n - i - (n - i) // i * (sum([(i - 1 )// p for p in tmp_lst]) +1)- sum([((n - i) % i) // p for p in tmp_lst])
    # print( (sum([(i - 1 )// p for p in tmp_lst]) +1) )
    tmp = (n) % i
    print(tmp)
    for p in tmp_lst:
        tmp = tmp - tmp//p
    print((n - i) // i * sympy.totient(i) ,tmp)
    vi = (n - i) // i * sympy.totient(i) + tmp
    print(vi)
    ans = ans * calcu.quick_powmod(i ,vi ,mod)
    print('here')

print(ans)
