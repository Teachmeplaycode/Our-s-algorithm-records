from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        for left in range(len(nums)):
            if nums[left] == target:return left
            if left+1 > right:return -1
            if nums[left+1] < nums[left]:
                left = left+1
                break
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:return mid
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
        return -1
sol = Solution()
nums = [1,3]
target = 3
print(sol.search(nums,target))