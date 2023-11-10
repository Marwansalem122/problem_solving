n=int(input())
even,odd,pos,neg=0,0,0,0
l=list(map(int,input().split()))
for i in range(n):
   if l[i]%2==0:
       even+=1  # 1 2 3
   else:
       odd+=1  #  1 2
   if l[i]>0:
       pos+=1  # 1
   elif l[i]<0:
       neg+=1   #  1 2 3
print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {pos}")
print(f"Negative: {neg}")