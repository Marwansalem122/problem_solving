
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            st=str(x)
            st=st[::-1]
            r=int(st)
            if x==r:
             return True
            else:
             return False
