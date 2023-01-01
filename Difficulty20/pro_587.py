# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/8 0:16
# site :
# file : pro_587.py
# solftware : PyCharm

import math

r = 1
n = 5000


def cal_S2(n, r):
    q = r - 1 / n * r
    a = math.atan(1 / n)
    b = math.asin(q / r * math.cos(a))
    print( q ,a ,b )
    return 0.5*((r-q)*r + r*q*math.sin(math.pi/2-a-b) - r*r*(math.pi/2-a-b))


S1 = r * r * (1 - math.pi / 4)
print( S1 )
print( cal_S2(n,r)/S1 )

for i in range(1 ,10000):
    if cal_S2(i ,r)/S1 < 0.001:
        print(i)
        break