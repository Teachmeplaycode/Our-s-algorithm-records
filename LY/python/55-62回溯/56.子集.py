from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        res=[]
        def dfs(path,nums):
            if not nums:
                res.append(path)
                return
            dfs(path+[nums[0]],nums[1:])
            dfs(path,nums[1:])
        dfs([],nums)
        return res
sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))