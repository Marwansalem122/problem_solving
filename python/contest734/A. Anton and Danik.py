
num=int(input())
state=list(input())
values=tuple(state)
a=values.count("A")
b=values.count("D")
if a>b:
    print("Anton")
elif b>a:
    print("Danik")
else:
    print("Friendship")