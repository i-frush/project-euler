
def checkPermutation(s):
    for i in range(0, len(s) - 1):
        if s[i] < s[i+1]:
            return False
    return True

def next_permutation(s):
    if len(s) == 1:
        return s
    if checkPermutation(s):
        return s[::-1]
    a = s[0]
    sub = s[1:]
    
    if checkPermutation(sub):
        b = min( [i for i in sub if i>a] )
        sub[sub.index(b)] = a
        #基于sub已经满序，置换a，b后的下一次递归会发生什么?
        return [b, *next_permutation(sub)]
    else:
        return [a, *next_permutation(sub)]
    
lst = [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]
for i in range( 0, 1000000 ):
    lst = next_permutation( lst )
print( lst )
