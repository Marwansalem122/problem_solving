##################
# first solution #
##################
# x,y,z=map(int,input().split())
# if x==0 or x==1:
#     print(x)
# else:
#     m=min(x,y,z)
#     x-=m
#     y-=m
#     z-=m
#     if x!=0 and z!=0:
#         if x//2<=z:
#            m+=x//2
#         else: 
#             m+=z
#     print(m)
##################
# Second solution #
##################

x,y,z=map(int,input().split())
if x==0 or x==1:
    print(x)
else:
    m=min(x,y,z)
    x-=m
    y-=m
    z-=m
    m+=min(x//2,z)
       
    print(m)