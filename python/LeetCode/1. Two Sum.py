class Solution(object):
    def twoSum(self, nums, target):
          
          l,r=0,len(nums)-1
          while r>l:
               if nums[l]+nums[r]==target:
                    return [l+1,r+1]
               elif nums[l]+nums[r]<target:
                    l+=1
               else:
                    r-=1
          return []
l=list(map(int,input().split()))
t=int(input())
s=Solution().twoSum(l,t)
print(s)