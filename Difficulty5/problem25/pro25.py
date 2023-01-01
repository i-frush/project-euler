import sympy
import numpy as np

fib1 = 1
fib2 = 1
cnt = 2

while len(str(fib2)) < 1000:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    cnt += 1
print(cnt)
