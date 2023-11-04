def solve(x,y,z):

    if x>y:
        return x
    else:
        if abs(x-y)<=z:
            return max(x,y)
        else:
            return max(x,y)+(abs(x-y)-z)
def main():
    t = int(input())
    while t>0:
        t-=1
        x,y,z=map(int,input().split())
        print(solve(x,y,z))
if __name__ == "__main__":
     main()