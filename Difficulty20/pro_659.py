# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/1/29 21:55
# site :
# file : pro_659.py
# solftware : PyCharm

# NO.659
# 1.观察发现an = n^2 + 3 时有循环节
# 1 1 1 1 1 13 1 1 1 1 1 13
# 猜测都有循环节
# 找循环节需要两个循环
# 2.打表发现，对于 n^2+k^2 ,当n = 2*k^2 时有最大质因数

# 捏麻麻地
# 今天我才算学习到了python的内存泄漏问题
# 如果内存线性增长一般就是泄露了
# 先使用tracemalloc查看是哪一部分对象一直在泄露内存
# 比如这个程序里就是nmmd sympy在分解质因子的时候一直使用cache不释放
# 搜索 发现github上有这个issue，是因为cache和irucache的问题
# 解决方案：升级sympy到最新版
import gc
import math
import tracemalloc

import sympy
import bisect
import utils

def write_anslist(lst):
    # lst: [( k ,P(k))]
    f_name = 'pans' + str(lst[0][0]) + '_' + str(lst[len(lst) - 1][0]) + '.txt'
    fp = open('euler_project_file/problem_659/' + f_name, 'w')
    for line in lst:
        fp.write(str(line[0]) + ' ' + str(line[1]) + '\n')
    fp.close()


def read_anslist(l, r):
    lst = []
    f_name = 'pans' + str(l) + '_' + str(r) + '.txt'
    fp = open('euler_project_file/problem_659/' + f_name, 'r')
    lines = fp.readlines()
    for line in lines:
        s = line.split(' ')
        lst.append(int(s[1]))
    return lst

def check_anslist(l ,r):
    lst = []
    f_name = 'ans' + str(l) + '_' + str(r) + '.txt'
    fp = open('euler_project_file/problem_659/' + f_name, 'r')
    lines = fp.readlines()
    for line in lines:
        s = line.split(' ')
        lst.append(int(s[1]))

    plst = read_anslist(l ,r)
    for i in range(0,len(lst)):
        if lst[i] != plst[i]:
            print( l+i ,'wrong:', lst[i] ,'right', plst[i])


def get_write_anslist(l, r):
    f_name = 'ans' + str(l) + '_' + str(r) + '.txt'
    for i in range(l, r + 1):
        write_to_file(f_name, i)


def write_to_file(f_name, i):
    # python大循环内存过高
    # 修改为 循环体为函可破数
    fp = open('euler_project_file/problem_659' + f_name, 'a')
    # temp_dic = sympy.factorint(4 * i * i + 1)
    # temp_keys = temp_dic.keys()
    # temp_list = [*temp_keys]
    # temp = temp_list[-1]
    # fp.write(str(i) + ' ' + str(temp) + '\n')
    # del temp_dic
    # del temp_keys
    # del temp_list
    # del temp

    # fp.write(str(i) + ' ' + str([*sympy.factorint(4 * i * i + 1).keys()][-1]) + '\n')
    fp.write(str(i) + ' ' + str(sympy.primefactors(4 * i * i + 1)[-1]) + '\n')

    # fp.write(str(i) + ' ' + str(1) + '\n')
    # print(gc.isenabled())
    fp.close()
    if i % 10000 == 0:
        # 防止内存占用过高
        # （为什么内存占用会这么高？）
        if i % 10000 == 0:
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')

            print("[ Top 10 ]")
            for stat in top_stats[:10]:
                print(stat)
            # gc.collect()
            print(f_name, i)
            sympy.cacheit
    # for x in locals().keys():
    #     del locals()[x]


def get_anslist(l, r):
    lst = []
    for i in range(l, r + 1):
        lst.append((i, sympy.primefactors(4 * i * i + 1)[-1]))
        # lst.append((i, [*sympy.factorint(4 * i * i + 1).keys()][-1]))
        if i % 10000 == 0:
            print('l r prc ', l, r, i)
    return lst

#
# eulerutils.write_primesfile(2*k)
# print(lst)
# 1181979 242862875272160687
# tracemalloc.start()

# for i in range(0,5):
#     lst = get_anslist(i * 10**6 +1 ,(i+1) * 10**6 )
#     write_anslist(lst)


# ans = 0
# for i in range(0, 10):
#     lst = read_anslist(i * 1000000 + 1, (i + 1) * 1000000)
#     ans += sum(lst)
# print(ans)
# print(ans%10**18)

# 检测第一种方法哪里错了
# for i in range(0, 10):
#     check_anslist(i*10**6 + 1 , (i+1)*10**6 )

# 验证两种不同
print( sympy.primefactors(9999998**2*4+1) )
print( sympy.factorint(9999998**2*4+1) )
print( [*sympy.factorint(9999998**2*4+1).keys()])
# ans = 0
# for i in range(0, 10):
#     lst = read_anslist(i * 1000000 + 1, (i + 1) * 1000000)
#     ans = (ans + sum(lst)%10**18)%10**18
# print(ans)

