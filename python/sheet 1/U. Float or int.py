
import math
num=float(input())
n=(len(str(num).split('.')[1]))
print(f"int {int(num)}")if num==math.ceil(num)else print(f"float {int(num)} {(num-int(num)):.{n}f}")
