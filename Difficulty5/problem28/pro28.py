import sympy
import numpy as np

end = 1001*1001
ans = 1
n = 1
step = 2

while n < end:
    for i in range(0, 4):
        n += step
        ans += n
    step += 2

print(ans)