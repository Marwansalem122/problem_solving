char=input()
if char.isdigit():
    print("IS DIGIT")
else:
    if(90>=ord(char)>=64):
        print("ALPHA")
        print("IS CAPITAL")
    else:
        print("ALPHA")
        print("IS SMALL")
# print(char.isdigit())
