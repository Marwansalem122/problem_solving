num=int(input())
y=0
m=0
d=0
while num>=365:
    num-=365
    y+=1
while num>=30:
    num-=30
    m+=1
d=num
print(y,"years")
print(m,"months")
print(d,"days")