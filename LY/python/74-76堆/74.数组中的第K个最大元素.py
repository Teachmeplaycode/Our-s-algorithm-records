from typing import List
from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = PriorityQueue()
        for i in nums:pq.put(i)
        cnt = 0
        while not pq.empty():
            cur = pq.get()
            cnt += 1
            if cnt == len(nums)+1-k:return cur
        return -1
            
        
sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(sol.findKthLargest(nums,k))