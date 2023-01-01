# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/1/31 18:21
# site :
# file : pro_630.py
# solftware : PyCharm

# 观察，发现数量关系与平行与共线有关
# 统计一系列直线中共线与平行的数量similar,para[]
# M = C(n,2) - similar
# S = M*(M-1) - sum(para[k]*para[k-1])
import time

time_start = time.time()
# 复杂度 O(V^4)
import sympy
import sympy.geometry as gm

n = 2500
S = [0] * (2 * n + 10)
S[0] = 290797
for i in range(1, 2 * n + 5):
    S[i] = S[i - 1] * S[i - 1] % 50515093

T = [i % 2000 - 1000 for i in S]
# print(T)

# point_set = [gm.Point(T[2 * k - 1], T[2 * k]) for k in range(1, n + 1)]
# # print(point_set)
# line_set = [gm.Line(point_set[i], point_set[j]) for i in range(0, n) for j in range(i + 1, n)]
#
# # for i in range(0, 2500):
# #     print(i)
# #     for j in range(i + 1, 2500):
# #         line_set.append(gm.Line(point_set[i], point_set[j]))
#
# print(len(line_set), line_set[0])
#
# time_end = time.time()
# print('totally time cost 1:', time_end - time_start)
#
# similar = 0
# dic_para = {}
#
# for i in range(0, len(line_set)):
#     print(str(i) + '/' + str(len(line_set)))
#     for j in range(i + 1, len(line_set)):
#         if gm.Line.is_similar(line_set[i], line_set[j]):
#             similar += 1
#         elif gm.Line.is_parallel(line_set[i], line_set[j]):
#             if line_set[i].slope not in dic_para:
#                 # 至少有两个线相互平行
#                 dic_para[line_set[i].slope] = 2
#             else:
#                 dic_para[line_set[i].slope] += 1
#
# para_lst = [*dic_para.values()]
# M = len(line_set) - similar
# S = M * (M - 1) - sum([i * (i - 1) for i in para_lst])
#
# print(M, S)
# time_end = time.time()
# print('totally time cost 2:', time_end - time_start)

# 太慢了
# 自定义直线为四元组试试
from fractions import Fraction


def line_check(l1, l2):
    # k1 = (a1-c1)/(b1-d1)
    # k2 = (a2-c2)/(b2-d2)
    # k3 = (a1-a2)/(b1-b2)
    if (l1[0] - l1[2]) * (l2[1] - l2[3]) == (l2[0] - l2[2]) * (l1[1] - l1[3]):
        if (l1[0] - l2[0]) * (l2[1] - l2[3]) == (l1[1] - l2[1]) * (l2[0] - l2[2]):
            # 共线
            return 1
        else:
            # 平行
            return 2
    return 0


def get_slope(l1):
    # 斜率最大是2000 垂直可以定义为10000
    if l1[2] == l1[0]:
        return Fraction(10000, 1)
    return Fraction(l1[3] - l1[1], l1[2] - l1[0])


# 废弃方法：直线去重
class SimiLine:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __eq__(self, other):
        return (self.b - self.d) * (other.c - other.a) == (other.b - other.d) * (self.c - self.a) and (
                self.b - other.b) * (self.a - self.c) == (self.b - self.d) * (self.a - other.a)

    def __hash__(self):
        return hash(1)


# point = (a ,b)
point_set = [(T[2 * k - 1], T[2 * k]) for k in range(1, n + 1)]
print('unset', len(point_set))
# 点集去重
point_set = list(set(point_set))
print('set', len(point_set))

# line = (a ,b ,c ,d)
line_set = [SimiLine(point_set[i][0], point_set[i][1], point_set[j][0], point_set[j][1]) for i in range(0, n) for j in
            range(i + 1, n)]
print(len(line_set), line_set[0])

time_end = time.time()
print('totally time cost 1:', time_end - time_start)

# set去重
line_dic = {}
dic_para = {}

# *直接去重时间复杂度太高
# 考虑到重复只会按照斜率出现
# 按照斜率分组
# 根据信息已有特征简化算法
for i in range(0, len(line_set)):
    print(str(i) + '/' + str(len(line_set)))
    k1 = get_slope((line_set[i].a, line_set[i].b, line_set[i].c, line_set[i].d))
    if k1 not in line_dic:
        line_dic[k1] = [ line_set[i] ]
    else:
        line_dic[k1].append( line_set[i] )

# 去重
slopes = [*line_dic.keys()]
for i in range(0 ,len(slopes)):
    print(i ,'/' ,len(slopes) ,slopes[i])
    line_dic[slopes[i]] = list(set(line_dic[slopes[i]]))

para_lst = [*dic_para.values()]
M = sum( len(lines) for lines in [*line_dic.values()])
S = M * (M - 1) - sum([len(lines) * (len(lines) - 1) for lines in [*line_dic.values()]])

print(M, S)
time_end = time.time()
print('totally time cost 2:', time_end - time_start)

'''
    3109535 9669182880384
totally time cost 2: 331.44644927978516
'''