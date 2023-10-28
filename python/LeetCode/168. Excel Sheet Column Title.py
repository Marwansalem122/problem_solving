class Solution:
    def convertToTitle(self, n: int) -> str:
        sb = []
        while n != 0:
            sb.append(chr(((n - 1) % 26)+65))
            n = (n - 1) // 26
        return ''.join(sb[::-1])

num=int(input())

s=Solution().convertToTitle(num)
print(s)