from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:return 0
        n = len(nums)
        dp = [0]*(n+1)
        dp[0],dp[1] = 0,nums[0]
        for k in range(2,n+1):
            dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])
        return dp[n]
sol = Solution()
nums = [2,7,9,3,1]
print(sol.rob(nums))