import math
x,y,z=map(int,input().split())
result=(x*y)/z
if result!=math.floor(result):
    print("double")
else:
    if  -2**31 <=result<= 2**31-1:
        print("int")
    else:
        print("long long")


