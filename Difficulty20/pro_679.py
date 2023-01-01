# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/5 17:25
# site :
# file : pro_679.py
# solftware : PyCharm
import numpy as np
import time
time_start = time.time()

A = 0
E = 1
F = 2
R = 3
FREE = 1
FARE = 1 << 1
AREA = 1 << 2
REEF = 1 << 3

dp = np.zeros((35, 4, 4, 4, 16), dtype='int64')

for j in range(0, 4):
    for k in range(0, 4):
        for l in range(0, 4):
            dp[3][j][k][l][0] = 1

for i in range(4, 35):
    for j in range(0, 4):
        for k in range(0, 4):
            for l in range(0, 4):
                for sta in range(0, 16):

                    if (j, k, l) == (R, E, E):
                        dp[i][R][E][E][sta] += \
                            dp[i - 1][F][R][E][sta - FREE] if sta & FREE else 0
                        dp[i][j][k][l][sta] += \
                            sum([dp[i - 1][m][j][k][sta] for m in range(0, 4)
                                 if m != F])

                    elif (j, k, l) == (A, R, E):
                        dp[i][A][R][E][sta] += \
                            dp[i - 1][F][A][R][sta - FARE] if sta & FARE else 0
                        dp[i][j][k][l][sta] += \
                            sum([dp[i - 1][m][j][k][sta] for m in range(0, 4)
                                 if m != F])

                    elif (j, k, l) == (R, E, A):
                        dp[i][R][E][A][sta] += \
                            dp[i - 1][A][R][E][sta - AREA] if sta & AREA else 0
                        dp[i][j][k][l][sta] += \
                            sum([dp[i - 1][m][j][k][sta] for m in range(0, 4)
                                 if m != A])

                    elif (j, k, l) == (E, E, F):
                        dp[i][E][E][F][sta] += \
                            dp[i - 1][R][E][E][sta - REEF] if sta & REEF else 0
                        dp[i][j][k][l][sta] += \
                            sum([dp[i - 1][m][j][k][sta] for m in range(0, 4)
                                 if m != R])

                    else:
                        dp[i][j][k][l][sta] += sum([dp[i - 1][m][j][k][sta] for m in range(0, 4)])

print( sum( dp[9][i][j][k][ (1<<4) - 1] \
            for i in range(0,4) for j in range(0,4) for k in range(0,4)) )
print( sum( dp[15][i][j][k][ (1<<4) - 1] \
            for i in range(0,4) for j in range(0,4) for k in range(0,4)) )
print( sum( dp[30][i][j][k][ (1<<4) - 1] \
            for i in range(0,4) for j in range(0,4) for k in range(0,4)) )

time_end = time.time()
print('totally time cost:', time_end - time_start)
