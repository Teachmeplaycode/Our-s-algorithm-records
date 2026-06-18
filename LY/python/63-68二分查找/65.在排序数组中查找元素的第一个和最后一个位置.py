from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        min_index,max_index = float('inf'),float('-inf')
        def search(l,r):
            nonlocal min_index,max_index
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid+1
                elif nums[mid]>target:
                    r = mid-1
                elif nums[mid]==target:
                    min_index, max_index = min(min_index,mid), max(max_index,mid)
                    search(l,mid-1)
                    search(mid+1,r)
                    break
        search(left,right)
        if min_index!=float('inf') and max_index!=float('-inf'): return [min_index,max_index]
        return [-1,-1]
sol = Solution()
nums = [5,7,7,8,8,10,10]
target = 10
print(sol.searchRange(nums,target))