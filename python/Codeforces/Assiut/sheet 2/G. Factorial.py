
def factor(n):
   if n==0:
       return 1
   else :
       return n*factor(n-1)
def main():
    n=int(input())
    for i in range(n):
        f=int(input())
        print(factor(f))
if __name__ =="__main__":
    main()