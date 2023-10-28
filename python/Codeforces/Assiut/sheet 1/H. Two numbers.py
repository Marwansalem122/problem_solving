import math

state=input()
values=state.split()
x=int(values[0])
y=int(values[1])
print(f"floor {x} / {y} = {math.floor(x/y)}")
print(f"ceil {x} / {y} = {math.ceil(x/y)}")
print(f"round {x} / {y} = {int(x/y)+1 if((x/y)-int(x/y))>=0.5 else int(x/y)}")

