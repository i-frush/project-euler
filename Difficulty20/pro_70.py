# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/1 23:30
# site :
# file : pro_70.py
# solftware : PyCharm
# 应该是想让求φ的表达式
import sympy
import time

time_start = time.time()

tmp = 87109/79180
ans = 87109
for i in range(2, 10**7):
    phi = sympy.totient(i)
    if sorted(str(phi)) ==  sorted(str(i)):
        print(i ,phi)
        if i/phi < tmp:
            tmp = i/phi
            ans = i

print(ans)

time_end = time.time()
print('totally time cost:', time_end - time_start)