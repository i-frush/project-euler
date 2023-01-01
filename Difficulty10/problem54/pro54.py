import sympy
import numpy as np
import sys
sys.path.append("D:\Documents\codePractice\eulerProject")

# J=11 Q=12 K=13 A=14
# deck: (value, kind)

global val
val = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def initdeck(s):
    l = s.split(' ')
    decka = [(val[l[i][0]], l[i][1]) for i in range(0, 5)]
    deckb = [(val[l[i][0]], l[i][1]) for i in range(5, 10)]
    return (decka, deckb)
        
def check(i ,decks ,comb):
    if i == 1:
        comb.extend(decks)
        return True
    elif i == 2:
        for i in range(0, 5):
            for j in range(i+1, 5):
                if decks[i][0] == decks[j][0]:
                    comb.extend([decks[i],decks[j]])
                    return True
        return False
    elif i == 3:
        for i in range(0, 5):
            for j in range(i+1, 5):
                if decks[i][0] == decks[j][0]:
                    if comb == []:
                        comb.extend([decks[i],decks[j]])
                    else:
                        comb.append(decks[i])
                        comb.append(decks[j])
        return len(comb) == 4
    elif i == 4:
        for i in range(0, 5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    if decks[i][0] == decks[j][0] and decks[i][0] == decks[k][0]:
                        comb.extend([decks[i], decks[j], decks[k]])
                        return True
        return False
    elif i == 5:
        tmp = list(set([decks[i][0] for i in range(0,5)]))
        if len(tmp) < 5:
            return False
        if tmp == [14, 2 ,3 ,4 ,5]:
            comb.extend(decks)
            return True
        for i in range(0,4):
            if tmp[i+1] != tmp[i]+1:
                return False
        comb.extend(decks)
        return True
    elif i == 6:
        tmp = set([decks[i][1] for i in range(0,5)])
        if len(tmp) == 1:
            comb.extend(decks)
            return True
        return False
    elif i == 7:
        tmp = list(set([decks[i][0] for i in range(0,5)]))
        tmpcomb = []
        if check(4, decks, tmpcomb) and len(tmp) == 2:
            comb.extend(tmpcomb)
            return True
        return False
    elif i == 8:
        for i in range(0, 5):
            for j in range(i+1, 5):
                for k in range(j+1, 5):
                    for l in range(k+1, 5):
                        if decks[i][0] == decks[j][0] and \
                            decks[i][0] == decks[k][0] and \
                            decks[i][0] == decks[l][0]:
                            comb.extend([decks[i], decks[j], decks[k], decks[l]])
                            return True
        return False
    elif i == 9:
        tmpcomb = []
        if check(6, decks, tmpcomb) and check(5, decks, tmpcomb):
            comb.extend(decks)
            return True
        return False
    elif i == 10:
        tmpcomb = []
        if check(9, decks, tmpcomb):
            tmp = list(set(a[0] for a in decks))
            if tmp == [10 ,11 ,12 ,13 ,14]:
                comb.extend(decks)
                return True
        return False
    
def getpoint(decks ,combs):
    res = []
    for i in range(9, 0, -1):
        tmp = []
        if check(i, decks, tmp):
            if i == 5:
                print(tmp)
            res.append(i)
            combs.append(tmp)
    return res

def comparerank(ranka, rankb):
    # l = max(len(ranka), len(rankb))
    # for i in range(0, l):
    #     if i >= len(rankb) and i < len(ranka):
    #         return 1
    #     if i >= len(ranka) and i < len(rankb):
    #         return -1
    #     if ranka[i] > rankb[i]:
    #         return 1
    #     if ranka[i] < rankb[i]:
    #         return -1
    if ranka[0] > rankb[0]:
        return 1
    if ranka[0] < rankb[0]:
        return -1
    return 0

def samecompare(combas, decka, combbs, deckb):
    print("ab", combas, combbs)
    
    for i in range(0, len(combas)):
        ca = [combas[i][j][0] for j in range(0,len(combas[i]))]
        cb = [combbs[i][j][0] for j in range(0,len(combbs[i]))]
        ca.sort(reverse=True)
        cb.sort(reverse=True)
        print("cab", ca, cb)
        for j in range(0, len(ca)):
            if ca[j] > cb[j]:
                return True
            if ca[j] < cb[j]:
                return False
        
    # for i in range(0, len(da)):
    #     if da[i] > db[i]:
    #         return True
    #     if da[i] < db[i]:
    #         return False
    return True

def compare(decka, deckb):
    combas = []
    combbs = []
    ranka = getpoint(decka, combas)
    rankb = getpoint(deckb, combbs)
    # print("ranka", ranka)
    # print("rankb", rankb)
    flag = comparerank(ranka, rankb)
    if flag == 1:
        return True
    if flag == -1:
        return False
    if flag == 0:
        if ranka[0]>1:
            print(decka, deckb)
            print("ranka", ranka)
            print("rankb", rankb)
            print(samecompare([combas[0],decka], decka, [combbs[0],deckb], deckb))
        return samecompare([combas[0],decka], decka, [combbs[0],deckb], deckb)
    
ans = 0
with open("D:\Documents\codePractice\eulerProject\Difficulty10\problem54\p054_poker.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        d = initdeck(line)
        decka = d[0]
        deckb = d[1]
        ans += 1 if compare(decka, deckb) else 0
print(ans)

# d = initdeck("6D 7S 5H 5H 3C 5D JD 2H 5D 3S")
# decka = d[0]
# deckb = d[1]
# print(decka, deckb)
# print(compare(decka, deckb))
    
    