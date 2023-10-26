x,y=map(int,input().split())
if x==0 and y==0 or abs(x-y)>=2:
    print("NO")
else:
    print("YES")