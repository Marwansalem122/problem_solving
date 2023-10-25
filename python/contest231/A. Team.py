n=int(input())
c=0
t=tuple()
while n>0:
    n-=1
    x,y,z=map(int,input().split())
    t=x,y,z
    if t.count(1)>=2 :
        c+=1
print(c)
