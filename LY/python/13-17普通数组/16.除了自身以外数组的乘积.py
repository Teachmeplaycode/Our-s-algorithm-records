from typing import List
from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]
        right=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        return ans
sol = Solution()
nums=[1,2,3,4]
nums = sol.productExceptSelf(nums)
print(nums)