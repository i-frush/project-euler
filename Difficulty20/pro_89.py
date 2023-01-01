# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/1 19:57
# site :
# file : pro_89.py
# solftware : PyCharm

# 罗马数字
'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''
# 规则1: 降序
# 规则2: 若能进位必须进位
# 规则3: D,L,V只能出现一次
# 减法缩写规则
'''
IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900
'''

# 解析: 匹配
# 构造：尽量用大的

dic1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


def read_to_lst():
    fp = open('problem_89/roman.txt')
    lst = []
    lines = fp.readlines()
    for line in lines:
        # strip去除空字符 \n
        lst.append(line.strip())
    return lst

def word_to_num(str):
    pos = 0
    num = 0
    while pos < len(str):
        if pos + 1 < len(str) and str[pos:pos + 2] in dic2:
            num += dic2[str[pos:pos + 2]]
            pos += 2
        else:
            num += dic1[str[pos]]
            pos += 1
    return num


def num_to_wordlen(num):
    flag_D = False
    flag_L = False
    flag_V = False

    ans = 0
    tmp = num
    n_1000 = tmp // 1000
    tmp -= n_1000 * 1000
    n_100 = tmp // 100
    tmp -= n_100 * 100
    n_10 = tmp // 10
    tmp -= n_10 * 10
    n_1 = tmp

    ans += n_1000
    if n_100 < 5:
        if n_100 == 4:
            ans += 2
        else:
            ans += n_100
    elif n_100 == 9:
        ans += 2
    else:
        ans += (n_100 - 4)

    if n_10 < 5:
        if n_10 == 4:
            ans += 2
        else:
            ans += n_10
    elif n_10 == 9:
        ans += 2
    else:
        ans += (n_10 - 4)

    if n_1 < 5:
        if n_1 == 4:
            ans += 2
        else:
            ans += n_1
    elif n_1 == 9:
        ans += 2
    else:
        ans += (n_1 - 4)
    return ans

# print(word_to_num('MMMMDCLXXII'))
# print(num_to_wordlen(4672))
str_lst = read_to_lst()
ans = sum( num_to_wordlen( word_to_num(word)) - len(word) for word in str_lst)
print(ans)