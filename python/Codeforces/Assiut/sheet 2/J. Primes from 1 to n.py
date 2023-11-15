
def isprime(n):  #O(sqrt(n))
    if(n<2):
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return  True

def main():
    n=int(input())
    if n==2:
        print(2)
    else:
        print(2,end=" ")
        for i in range(3,n+1):
           if  isprime(i):
               print(i,end=" ")
if __name__=="__main__":
    main()
