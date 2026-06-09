from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:return []
        res = []
        def dfs(i,ls):
            if i<0 or i>=len(nums):return
            if len(ls) == len(nums):return res.append(ls[:])
            for i in range(len(nums)):
                if nums[i] in ls:continue
                ls.append(nums[i])
                dfs(i,ls)
                ls.pop()
        dfs(0,[])
        return res
nums=[1,2,3]
sol = Solution()
sol.permute(nums)    