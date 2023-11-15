def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def main():
    x, y = map(int, input().split())
    print(gcd(x,y))

if __name__=="__main__":
    main()