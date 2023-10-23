state=[int(i) for i in (input().split(" "))]
if(state[1]>=state[2]) and state[0]<=state[3]:
    state.sort()
    print(state[1],state[2])
else:
    print(-1)