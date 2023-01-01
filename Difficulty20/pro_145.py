# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/3 16:07
# site :
# file : pro_145.py
# solftware : PyCharm

# bruce force
# import time
# time_start = time.time()
#
# ans = 0
# lst = []
# for i in range(0, 10000001):
#     if i == 10**(len(lst)+1):
#         lst.append(ans)
#
#     if i % 1000000 == 0:
#         print(str(i) + '/' + '1000000000')
#         print('totally time cost:', time.time() - time_start)
#     if i % 10 == 0:
#         continue
#     num = int(str(i)) + int(str(i)[::-1])
#     flag = True
#     for dig in str(num):
#         if int(dig) % 2 == 0:
#             flag = False
#             break
#     ans += (1 if flag else 0)
#
# print(lst)
# for i in range(1 ,len(lst)):
#     print(lst[i] - lst[i-1])
#
# time_end = time.time()
# print('totally time cost:', time_end - time_start)

# dp
# 先忽略各数位的具体数字，只考虑逆序后各位相加的结果
# eg ： 123 + 321 = (1+3) (2+2) (3+1)
# 注意到有对称性，只考虑一半即可
# 根据 对称性，进位，奇偶 这三个约束写状态转移方程

# dp[pos][odd][car][sta] :在从中心到左边第pos位，当前位数值为偶数/奇数，是否有进位，边界类型为A/B是有几种可行方案
# 可行方案是指，除了pos位，其他位都为奇数
import numpy as np
import time
time_start = time.time()

dp = np.empty([6, 2, 2, 2], dtype='int64')

# ans是dp排除前导0的结果
ans = [0] * 20

# 初始化边界
# 考虑到对称以及奇偶
# 0：321123型边界，最中间的两位
# 无进位，中间都是奇数，有五种方案：1 3 5 7 9  ，eg:'11'
dp[0][1][0][0] = 30
# 无进位，中间都是偶数， 由于左边一位一定是偶数，无可行方案
dp[0][0][0][0] = 0
# 有进位，中间都是奇数， 无可行方案
dp[0][1][1][0] = 0
# 有进位，中间都是偶数， 进位会影响左边，有五种方案：10 12 14 16 18 ，eg:'(18)(18)' = '(19)8'
dp[0][0][1][0] = 25
ans[1] = (dp[0][1][0][0] - 10) + dp[0][1][1][0]

# 1：32123型边界，最中间一位，由于只有一位，所以只有不进位的情况都可行
dp[0][1][0][1] = 0  # 1 3 5 7 9
dp[0][0][0][1] = 5  # 0 2 4 6 8
dp[0][1][1][1] = 0  # 11 13 15 17
dp[0][0][1][1] = 5  # 10 12 14 16 18
ans[0] = 0

# 转移方程
# 关键约束: 在左边 pos 对pos-1 有进位，在右边 pos-1对pos+1有进位
# 以此为依据讨论全是奇数的情况
for pos in range(1, 6):
    for odd in range(0, 2):
        for car in range(0, 2):
            for sta in range(0, 2):
                if odd == 1:
                    if car == 1:
                        dp[pos][odd][car][sta] = (8 + 6 + 4 + 2) * dp[pos - 1][0][0][sta]
                        if sta == 1:
                            ans[2 * pos] += 20 * dp[pos - 1][0][0][sta]
                        else:
                            ans[2 * pos + 1] += 20 * dp[pos - 1][0][0][sta]
                    else:
                        dp[pos][odd][car][sta] = (2 + 4 + 6 + 8 + 10) * dp[pos - 1][1][0][sta]
                        if sta == 1:
                            ans[2 * pos] += 20 * dp[pos - 1][1][0][sta]
                        else:
                            ans[2 * pos + 1] += 20 * dp[pos - 1][1][0][sta]
                else:
                    if car == 1:
                        dp[pos][odd][car][sta] = (9 + 7 + 5 + 3 + 1) * dp[pos - 1][0][1][sta]
                    else:
                        dp[pos][odd][car][sta] = (1 + 3 + 5 + 7 + 9) * dp[pos - 1][1][1][sta]

                print(pos, odd, car, sta, dp[pos][odd][car][sta])

for i in range(0, 10):
    print(ans[i])

print(sum(ans[0:9]))

time_end = time.time()
print('totally time cost:', time_end - time_start)
# totally time cost 2: 0.001001596450805664

