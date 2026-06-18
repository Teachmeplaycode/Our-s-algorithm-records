from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = 0,n-1
        k = 1
        for left in range(n):
            if left+1 > right:
                break
            if nums[left+1]<nums[left]:
                k += 1
                move = nums.pop()
                nums.insert(0,move)
        return nums[0]
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] < nums[-1]:return nums[0]
        res = nums[0]
        left,right = 0,n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[0] <= nums[mid]:
                left = mid + 1
            else: 
                res = nums[mid]
                right = mid - 1
        return res

sol = Solution2()
nums = [11,13,15,17,1,2,3,4,5]
print(sol.findMin(nums))