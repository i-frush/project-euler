# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/6 23:47
# site :
# file : pro_704.py
# solftware : PyCharm

# Is this diff 20%? It's too hard too me...
# the formula there used：

# 1. the number of n!'s factor k
# v2(n!) = [n/k] + ... + [n/k^p]

# 2. legendre's formula(corollary of 1)
# detail:http://www.cut-the-knot.org/blue/LegendresTheorem.shtml
# vp(n!) = n-Sp(n)/(p-1) ，Sp is the digit-sum in base p
# * Particular：in binary ,v2(n!)is the 1's number in expansion of n

# 3. kummer's formula
# vp((n ,m)) = the number of m + (n-m) 's carries in base p
# detail:https://planetmath.org/KummersTheorem


# * as learing algebra ,you can learn the formular above 1 -> 2 -> 3
# and now, with the theorem 3, the question is :how to construct most carries when patitioning the m into a + b?

# *it easy to find that the the carries can only crated in the '0' digit of m
# so the greatest number of carries is no greater the the number of '0' digit of m
# First ,we should consider the easy case as m is even
# let construct a is all of 1 except the first digit ,eg: m = 1001000 ,a = 0111111
# and b as a form just right making a create most carries:
# except the first and last digit ,it has the same digit as m  ,eg: b =0001001
# we can find that in this case the number of carries is equal to the '0' digit of m
# so this is the most carries' construction
# When m is odd ,we can right shift m until it becoming a even

# *let's return to the theorem 2
# In our construction we can find the number of 1 in a and b is equal the length of m when m is even
# when m is odd ,just minus the number of 1 in the last of m


# now ,the question is :the sum formula of:1.(length - 1)
# 2. the length of last 1's number of odd binary number
# with the help of OEIS ,we ca find proper formula
# 1.A061168
# 2.A005187
# because in all 1 case, it will minus 1 more
# so we should plus int(log2(k)) to ans as compensation

from math import log2

def A061168(n):
    s, i, z = -n , n, 1
    while 0 <= i: s += i; i -= z; z += z
    return s

def A005187(n):
    return 2*n-bin(n).count('1')

k = 10**16
ans = A061168(k) - A005187((k)//2) + int(log2(k+1))
print( ans )
