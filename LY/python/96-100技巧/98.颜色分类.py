from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i]>=nums[j]:
        #             nums[i],nums[j] = nums[j], nums[i]
        # print(nums)
        p0 = p1 = 0
        for i, x in enumerate(nums):
            nums[i] = 2
            if x <= 1:
                nums[p1] = 1
                p1 += 1
            if x == 0:
                nums[p0] = 0
                p0 += 1
                
sol = Solution()
nums = [1,0,0,2,2,1,1]
sol.sortColors(nums)
            
        