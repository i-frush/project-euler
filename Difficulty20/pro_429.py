# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/7 14:32
# site :
# file : pro_429.py
# solftware : PyCharm

# v2(n!) = [n/k] + ... + [n/k^p]
# sum of mul of any number of ai = (1+a0)(1+a1)...(1+an)
import math
import eulerutils.calcu as cal

import sympy

mod = 10 ** 9 + 9
k = 10 ** 8
prime_dic = {}
prime_list = sympy.primerange(2, k)


def v_factor(k, p):
    ret = 0
    tmp = k
    while tmp:
        ret += tmp // p
        tmp //= p
    return ret


for p in prime_list:
    prime_dic[p] = v_factor(k, p)

ans = 1
for p in prime_dic:
    print(p, prime_dic[p])
    tmp = int(cal.quick_powmod(p, prime_dic[p], mod))
    ans = ans * (1 + tmp * tmp) % mod

print(ans)
