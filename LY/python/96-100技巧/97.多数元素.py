from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = hp = 0
        for x in nums:
            if hp == 0:
                ans, hp = x, 1
            else:
                hp += 1 if x == ans else -1
        return ans
sol = Solution()
nums = [2,2,4,4,4,4,2]
print(sol.majorityElement(nums))