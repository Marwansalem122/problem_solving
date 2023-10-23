state=input().split(" ")
if state[1]=="+":
    if(int(state[0]) + int(state[2])==int(state[4])):
        print("Yes")
    else:
        print(int(state[0]) +int(state[2]))
elif state[1]=="-":
    if(int(state[0]) - int(state[2])==int(state[4])):
        print("Yes")
    else:
         print(int(state[0])-int(state[2]))
else:
       if(int(state[0]) * int(state[2])==int(state[4])):
           print("Yes")
       else:
          print(int(state[0]) * int(state[2]))
