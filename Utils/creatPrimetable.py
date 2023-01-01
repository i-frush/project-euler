import sympy
import numpy as np

with open("D:/Documents/codePractice/eulerProject/Utils/prime_10000000.txt", 'w') as f:
    n = 1
    cnt = 0
    while True:
        n = sympy.nextprime(n);
        
        if cnt > 10000000:
            break
        
        if cnt % 10000 == 0:
            print(cnt, n)
            
        f.write(str(n) + '\n')
        cnt += 1