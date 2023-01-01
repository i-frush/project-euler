# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/5 0:08
# site :
# file : pro_315.py
# solftware : PyCharm

# 模拟
import math

import sympy

num_dic = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1],
           [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0]]


def cal_root_lst(num):
    lst = [num]
    while num >= 10:
        num = sum( int(i) for i in str(num))
        lst.append(num)
    return lst

def cal_diff_digit(num1, num2):
    dig1 = num_dic[num1]
    dig2 = num_dic[num2]
    ret = sum((dig1[i] ^ dig2[i]) for i in range(0, 7))
    return ret


def cal_diff_num(num1, num2):
    # num1 -> num2
    s_num1 = (str(num1))[::-1]
    s_num2 = (str(num2))[::-1]
    if len(s_num1) > len(s_num2):
        tmp = s_num1
        s_num1 = s_num2
        s_num2 = tmp

    ret = 0
    for i in range(0, len(s_num1)):
        ret += cal_diff_digit(int(s_num1[i]), int(s_num2[i]))
    for i in range(len(s_num1), len(s_num2)):
        ret += cal_diff_digit(int(s_num2[i]), 10)
    return ret


import time

time_start = time.time()

ans = 0
prime_lst = [*sympy.primerange(10 ** 7, 2 * 10 ** 7)]
# prime_lst = [137]

for i in range(0, len(prime_lst)):
    if i % 10000 == 0:
        print(str(i) + '/' + str(len(prime_lst)))
        time_end = time.time()
        print('totally time cost:', time_end - time_start)
    root_lst = cal_root_lst(prime_lst[i])
    for j in range(0, len(root_lst)-1):
        ans += (cal_diff_num(root_lst[j], '') + cal_diff_num('', root_lst[j + 1])) \
            - cal_diff_num(root_lst[j], root_lst[j + 1])
print(ans)

time_end = time.time()
print('totally time cost:', time_end - time_start)
