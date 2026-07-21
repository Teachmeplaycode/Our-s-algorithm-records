import functools
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = mi = ans = nums[0]
        for num in nums[1:]:
            cb = (num, mx*num, mi*num)
            mx = max(cb)
            mi = min(cb)
            ans = max(ans, mx)
        return ans
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         ans = -inf 
#         f_max = f_min = 1
#         for x in nums:
#             f_max, f_min = max(f_max * x, f_min * x, x), \
#                            min(f_max * x, f_min * x, x)
#             ans = max(ans, f_max)
#         return ans
sol = Solution()
nums = [2,3,-2,4]
print(sol.maxProduct(nums))