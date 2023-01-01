import sympy
import numpy as np

a = sympy.factorial(100)
ans = sum( int(i) for i in str(a))
print(ans)
