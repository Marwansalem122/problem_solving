s=input()
n=[int (i)for i in s]
if(n[1]==0 or n[0]%n[1]==0 or n[1]%n[0]==0):
        print("YES")
else:
      print("NO")