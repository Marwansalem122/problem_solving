state=input().split(" ")

if state[1]==">":
    if(int(state[0]) >int(state[2])):
        print("Right")
    else:
        print("Wrong")
elif state[1]=="<":
    if(int(state[0]) <int(state[2])):
        print("Right")
    else:
        print("Wrong")
else:
       if(int(state[0]) ==int(state[2])):
           print("Right")
       else:
          print("Wrong")