
n = int(input())
l = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    

    
    if x > 1:
        l[x-2] += y-1
    if x < n:
        l[x] += l[x-1] - y
    l[x-1] = 0
    

for i in l:
    print(i)

