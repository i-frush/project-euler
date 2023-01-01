# Author : ifrush
# -*- coding: utf-8 -*-
# author : Administrator
# date : 2022/2/8 0:58
# site :
# file : pro_61.py
# solftware : PyCharm


import networkx as nx
import time

time_start = time.time()

num_dic = {}


def cal_poly_num(i, n):
    return n * ((i - 2) * n - (i - 4)) // 2


for i in range(0, 6):
    lst = []
    tmp = 1
    while True:
        cal = cal_poly_num(i + 3, tmp)
        if cal >= 10000:
            break
        if cal >= 1000:
            if cal in num_dic:
                num_dic[cal].append(i)
            else:
                num_dic[cal] = [i]
        tmp += 1

G = nx.DiGraph()
G.add_nodes_from(num_dic.keys())
for u in num_dic.keys():
    for v in num_dic.keys():
        if u // 100 == v % 100:
            G.add_edge(v, u)

vis = [False] * 10005
tmp_lst = [False] * 6
ans_lst = [-1] * 6


def dfs(u, depth):
    ans_lst[depth] = u
    if depth == 5:
        if G.has_edge(u, ans_lst[0]):
            print('ans: ', ans_lst, sum(ans_lst))
            print([num_dic[i] for i in ans_lst])
        return

    for v in G[u]:
        if vis[v]:
            continue
        for col in num_dic[v]:
            if not tmp_lst[col]:
                vis[v] = True
                tmp_lst[col] = True
                dfs(v, depth + 1)
                tmp_lst[col] = False
                vis[v] = False
    return


nodes = list(G.nodes)
print(nodes[0])
for i in range(0, len(nodes)):
    v = nodes[i]
    print("{0}/{1}".format(i + 1, len(nodes)))
    for col in num_dic[v]:
        vis[v] = True
        tmp_lst[col] = True
        dfs(v, 0)
        tmp_lst[col] = False
        vis[v] = False

time_end = time.time()
print('totally time cost:', time_end - time_start)
