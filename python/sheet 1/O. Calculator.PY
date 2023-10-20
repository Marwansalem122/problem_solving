import re 
state=input()
values=[int(i)for i in re.split(r"\+|\*|\/|\-",state)]
if "+" in state:
    print(values[0]+values[1])
elif "-" in state:
    print(values[0]-values[1])
elif "*" in state:
    print(values[0]*values[1])
else:
    print(values[0]//values[1])
