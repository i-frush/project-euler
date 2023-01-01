# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/5 11:26
# site :
# file : pro_772.py
# solftware : PyCharm

# 构造
# 思路： N = 2m
# 考虑k划分：全是m-1，m-2...2
# 2,3...m-1|m -> lcm[2,3...m-1]|m
# 考虑棘手的情况：折断
# lcm[2,3...m-1]保证了不会出现折断

# 构造均分划分:
# m = m = lcm[2,3...m-1] ，考虑k为划分中的最大元素， 证明m一定是k划分
# 1.若划分中k的个数>=m/k
# 则 m = m/k 个 k相加，均等划分
# 2.若划分中k的个数<m/k
# 则将k全放置于等号右边，等号左边的最大元素l
# 将l放在与k等同的位置，使用同样的思路使用m是一个l划分，直到l=1
# m一定是一个1划分，所以m一定是2->3->...k划分
# m所有划分中可能出现的最大元素是m-1，故m是m-1划分
# 故 N = 2*m 是均等的m划分，即 f(k) = 2*lcm[2,3...k-1]
import sympy
import numpy as np
import time

time_start = time.time()
mod = 10 ** 9 + 7

# def write_anslist(lst, a, b):
#     # lst: [( k ,P(k))]
#     f_name = 'ans' + str(a) + '_' + str(b) + '.txt'
#     fp = open('problem_772/' + f_name, 'w')
#     for line in lst:
#         fp.write(str(line[0]) + ' ' + str(line[1]) + '\n')
#     fp.close()
#
#
# def read_anslist(lst, a, b):
#     f_name = 'ans' + str(a) + '_' + str(b) + '.txt'
#     fp = open('euler_project_file/diff_20/problem_772/' + f_name, 'r')
#     lines = fp.writelines()
#     lst = [0] * 10 ** 8
#     for line in lines:
#         s = line.split(' ')
#         lst[s[0]] = s[1]
#     fp.close()
#     return lst
#
#
def quick_pow(a, b, mod):
    a = a % mod
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % mod
        b >>= 1
        a = (a * a) % mod
    return ans
#
#
# factors_lst = np.zeros([10 ** 8], dtype=int)
# for i in range(2, 5*10**7):
#     if i % 100000 == 0:
#         print('{0}/{1}'.format(i, 10 ** 8))
#         time_end = time.time()
#         print('totally time cost:', time_end - time_start)
#     fac_dic = sympy.factorint(i)
#     for item in fac_dic.items():
#         if factors_lst[item[0]] < item[1]:
#             factors_lst[item[0]] = item[1]
#
# ans = 1
# ans_lst = []
# for i in range(2, 10 ** 8):
#     if factors_lst[i] != 0:
#         ans_lst.append((i, factors_lst[i]))
#         ans = ans * quick_pow(i, factors_lst[i], mod) % mod


# LCM(1,...,n)有O(nloglogn)的公式
# lcm(1,2,3,⋯,n)=∏pp⌊logpn⌋.
# 大致思路是考虑lcm的唯一分解式中某素数p的次方m最大，则该p^m<lcm，且不存在有p^k(k>m)在lcm的分解中
# 还有一个使用Mangoldt function的公式
# 数列见：https://oeis.org/A014963
# lcm(1,2,3,⋯,n)=expψ(n).
# 详见 https://math.stackexchange.com/questions/302278/mathrmlcm1-2-3-ldots-n

def bin_search(p ,k ,l ,r):
    # 二分查找最大的p^m < k
    while l < r:
        mid = (l + r +1) // 2
        if p**mid <= k:
            l = mid
        else:
            r = mid-1
    return l

lcm_dic = {}
prime_lst = [*sympy.primerange(2,10**8+1)]


fac1 = 0
for p in prime_lst:
    print( p )
    m = bin_search(p ,10**8 ,1 ,100)
    if m == 1:
        fac1 = p
        break
    print(p, m)
    lcm_dic[p] = m

ans = 1
for p in prime_lst:
    print( p )
    if p < fac1:
        ans = ans*quick_pow(p ,lcm_dic[p] ,mod)%mod
    else:
        ans = ans * p % mod

print(ans*2%mod)
time_end = time.time()
print('totally time cost:', time_end - time_start)
