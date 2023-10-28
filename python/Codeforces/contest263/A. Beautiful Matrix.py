
arr=[]
c=0
x=0
for i in range(5):
    l =list (map(int, input().split()))
    
    if 1 in l:
            c=i
            x=l.index(1)
    
    arr.append(l)
    
print(abs(2-c)+abs(2-x))



