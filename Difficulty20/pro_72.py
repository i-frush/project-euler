# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/2 1:05
# site :
# file : pro_72.py
# solftware : PyCharm

# 互质则为真分数，用ph(i)
import sympy

k = 10**6
print(sum( sympy.totient(i) for i in range(2 ,k+1)))
