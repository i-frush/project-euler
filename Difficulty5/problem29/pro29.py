import sympy
import numpy as np
from pprint import pprint

amax = 100
bmax = 100

# divide a^b into simplest format:
# a^b = (min_fac)^(b2)
# eg: 27^100 = 3^300 and 81^75 = 3^300
# let (min_fac,b2) as the key of (a,b)
# dedup the elemt by the key

keylist = []
notsimplest_check = [0]*(amax+1)

for a in range(2, amax+1):
    if notsimplest_check[a] == 1:
        continue
    for b in range(2, bmax+1):
        keylist.append((a, b))
        if a**b <= amax:
            notsimplest_check[a**b] = 1
            for b2 in range(2, bmax+1):
                keylist.append((a, b*b2))

dedup = set(keylist)
print(len(dedup))