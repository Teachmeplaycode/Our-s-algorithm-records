from typing import List
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dq = deque(nums[i] for i in range(len(nums)))
        while k>0:
            cur = dq[-1]
            dq.pop()
            dq.appendleft(cur)
            k-=1
        for i in range(len(dq)):
            nums[i] = dq[i]
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            cur = nums[-1]
            nums.pop()
            nums.insert(0, cur)
            
sol = Solution2()
nums = [1,2,3,4,5,6,7]
k = 3
sol.rotate(nums, k)
print(nums)