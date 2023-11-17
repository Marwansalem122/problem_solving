
x,y=map(int,input().split())
v=False

for i in range(x,y+1):
    c=False
    n=i
    while(n!=0):
        dig=n%10
        n//=10
        if dig!=7 and dig!=4:
            c=True
    if c==False:
        print(i,end=" ")
        v=True
if v==False:
    print(-1)

if c==False:
    print(-1)