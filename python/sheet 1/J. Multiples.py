state=input()
values=state.split()
x=int(values[0])
y=int(values[1])
print("Multiples" if (x%y==0 or y%x==0) else "No Multiples")