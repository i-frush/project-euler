# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/2 22:35
# site :
# file : pro_601.py
# solftware : PyCharm
import sympy


def streak(n):
    tmp = 0
    while (n + tmp) % (tmp + 1) == 0:
        tmp += 1
    return tmp


def num_of_streak(k, M):
    # k+1 |/ n+k -> k+1 |/ n-1
    # 1,2...k | n-1
    # 构造 n-1 = lcm(1,2...k)*[ a*(k+1) + d ]
    # 其中d为 1,2...k 中保证 k+1 |/ n-1 的数值
    # 求a的最大取值即可
    ans = 0
    M = M
    m = sympy.ilcm( 1, *range(1, k + 1))
    # print(m)
    for i in range(1, k+1):
        if m * i % (k + 1) == 0:
            continue
        # print( m ,i)
        ans += ((M//m) - i)//(k+1)+1
    return ans

# 打表
# 1.偶数都是1: (n+1)是奇数，不能被2整除
# 2. n+k|k+1 -> n-1|k+1

print( num_of_streak(1 ,4))
print( sum( [num_of_streak(i ,4**i) for i in range(2,32) ]) )



# 更简单的方法:
#P(N,k) = (N-2)/lcm(1,...,k) - (N-2)/lcm(1,...,k+1)
# 省略了我讨论lcm(1,...,k)*(a*(k+1) + d)是否能被k+1整除的这一步