# from cmath import log
from math import log
state=[int(i)for i in input().split()]
a,b,c,d=state
if (log(b)*log(a)) > (log(d*log(c))):
    print("YES")
else:
 print("NO")
