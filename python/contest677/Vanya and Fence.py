import math
st1=input()
st2=input()
values1=[int(i) for i in st1.split()]
values2=[int(i) for i in st2.split()]
c=0
for i in range(values1[0]):
    if(values2[i]/values1[1]<=1):
         c+=1
    else:
         c+=math.ceil(values2[i]/values1[1])
    
print(c)
