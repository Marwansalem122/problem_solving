import os.path

# First solution
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        f=strs[0]
        for i in strs[1:]:
            while i[:len(f)]!=f:
                f=f[:len(f)-1]
        return f

s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))


# Second Solution:
answer=os.path.commonprefix(["flower","flow","flight"])
print(f"Answer is: {answer}")


