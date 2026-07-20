from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums[:i]):
                if num1 > num2:dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
sol = Solution()
nums = [10,9,2,5,3,7,101,18]
print(sol.lengthOfLIS(nums))