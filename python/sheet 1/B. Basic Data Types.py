word=input()
listvalue=word.split()
number=int(listvalue[0])
numberlong=int(listvalue[1])
char=listvalue[2]
floatnumber=float(listvalue[3])
doublenumber=float(listvalue[4])

print(number)
print(numberlong)
print(char)
print(floatnumber)
print(f"{doublenumber:0.1f}")