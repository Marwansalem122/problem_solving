state=[int(i)for i in input().split()]
sum=1
for i in range(len(state)):
     sum*=state[i]
print(str(sum)[-2:])