from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:mp[num] += 1
        bk = [[] for _ in range(len(nums) + 1)]
        for val,key in mp.items():bk[key].append(val)
        res = []
        for i in range(len(bk) - 1, 0, -1):
            for num in bk[i]:
                res.append(num)
                if len(res) == k:return res
sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums,k))
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = [x for x in arr[1:] if x <= pivot]
#     right = [x for x in arr[1:] if x > pivot]
#     return quicksort(left) + [pivot] + quicksort(right)