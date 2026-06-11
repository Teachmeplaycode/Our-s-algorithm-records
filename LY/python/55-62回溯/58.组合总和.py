from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(nums:List,idx,s):
            if idx<0 or idx>=len(candidates):return
            if s>=target:
                if s==target:res.append(nums)
                return
            dfs(nums+[candidates[idx]],idx,s+candidates[idx])
            for i in range(idx+1,len(candidates)):
                dfs(nums+[candidates[i]],i,s+candidates[i])
        for i in range(len(candidates)):
            dfs([candidates[i]],i,candidates[i])
        return res
sol = Solution()
candidates = [3,5,8]
target = 11
print(sol.combinationSum(candidates,target))