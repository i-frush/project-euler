def checkCycle(dived ,div):
    remainders_check = [0]*(div+1)
    cnt = 0
    while True:        
        quo = dived // div
        # print(dived, div, quo ,'q')
        cnt += 1
        if dived < div:
            dived *= 10
            continue
        
        rem = dived % div
        # print(dived, div, rem ,'r')
        if rem == 0 :
            return 0
        if remainders_check[rem] > 0:
            return cnt - remainders_check[rem]
        dived = rem*10
        remainders_check[rem] = cnt
        

lst = [0]*1005
for i in range(1, 1000):
    lst[i] = checkCycle(1, i) 
ans = lst.index(max(lst))
print(ans)
