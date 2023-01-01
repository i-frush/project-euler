# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/7 20:21
# site :
# file : pro_60.py
# solftware : PyCharm

import sympy
import numpy as np
import functools


def check(a, b):
    return sympy.isprime(int(str(a) + str(b))) and sympy.isprime(int(str(b) + str(a)))


# find a feasible solution as the upper-limit of the answer

# while True:
#     flag = functools.reduce( lambda x,y: x and y ,[check(tmp,i) for i in lst])
#     if flag:
#         print(tmp)
#         break
#     print(tmp)
#     tmp = sympy.nextprime(tmp)

# lst = [3 ,7 ,111 ,109 ,93187]
# the upper-limit 93417

# search

ans = 26033
prime_lst = [*sympy.primerange(3, 26033)]
check_lst = np.ones((len(prime_lst), len(prime_lst)), dtype=bool)
tmp_lst = [-1] * 5

for i in range(0, len(prime_lst)):
    print('{0}/{1}'.format(i, len(prime_lst)))
    for j in range(i + 1, len(prime_lst)):
        check_lst[i][j] = check_lst[j][i] = check(prime_lst[i], prime_lst[j])


def dfs(pos, depth, tmp_sum):
    global ans
    print(pos, depth ,tmp_sum)
    if tmp_sum > ans or pos >= len(prime_lst):
        return
    if depth == 4:
        print([prime_lst[i] for i in tmp_lst])
        ans = min(ans, tmp_sum)
        return
    tmp_lst[depth] = pos
    # print([prime_lst[i] for i in tmp_lst])
    for i in range(pos + 1, len(prime_lst)):
        flag = functools.reduce(lambda x, y: x and y,
                                [check_lst[i][j] for j in tmp_lst[0:depth + 1]])
        if flag:
            dfs(i, depth + 1, tmp_sum + prime_lst[i])
    return


for i in range(0, len(prime_lst)):
    # print(i, prime_lst[i])
    dfs(i, 0, prime_lst[i])

print(ans)
