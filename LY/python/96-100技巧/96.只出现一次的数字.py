from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {nums[i]:0 for i in range(len(nums))}
        for i in range(len(nums)):
            mp[nums[i]] += 1
        for i in range(len(nums)):
            if mp[nums[i]] == 1:return nums[i]
from functools import reduce
from operator import xor
class Solution2():
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
sol = Solution()
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))