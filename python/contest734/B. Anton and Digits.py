k2, k3, k5, k6 = map(int, input().split())

x = min(k2, k5, k6)
y = min(k2-x, k3)

sum = 256 * x + 32 * y
print(sum)
