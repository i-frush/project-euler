# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/1 22:45
# site :
# file : pro_491.py
# solftware : PyCharm
# 性质：一个数奇数位上的数字和与偶数位上的数字和的差能被11整除,那么这个数就能被11整除
# 偶数位有10位,剩下的是奇数位
# 总和是90 ，奇数和 = 总和-偶数和
# 共有C(20,10)种情况，根据选择的数位判断排列情况

import itertools

ans = 0
lst = list(set([*itertools.combinations('00112233445566778899', 10)]))
for evens in lst:
    evensum = sum([int(i) for i in evens])
    if (90 - 2 * evensum) % 11 != 0:
        continue
    # 麻烦的地方
    # 奇数：10！/(2)^m
    # 偶数：10！/(2)^m - 前导0的情况
    num_dic = [0 for i in range(0, 10)]
    for i in evens:
        num_dic[int(i)] += 1
    e_tmp = 3628800
    o_tmp = 3628800

    for i in range(0, 10):
        if num_dic[i] == 2:
            e_tmp //= 2
        elif num_dic[i] == 0:
            o_tmp //= 2

    if num_dic[0] != 0:
        e0_tmp = 362880
        num_dic[0] -= 1
        for i in range(0, 10):
            if num_dic[i] == 2:
                e0_tmp //= 2
        e_tmp -= e0_tmp

    ans += e_tmp*o_tmp

print(ans)

