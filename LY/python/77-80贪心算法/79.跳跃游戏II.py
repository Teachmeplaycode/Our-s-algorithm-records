from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        l = dp[0] = 0
        for i in range(1, len(nums)):
            while nums[l] < i - l:l += 1
            dp[i] = dp[l] + 1
        return dp[-1]
sol = Solution()
nums = [2,1,0]
print(sol.jump(nums))