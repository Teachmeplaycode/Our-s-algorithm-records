from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 2)
        def dfs(i: int) -> int:
            if i > n:return 0
            if i == n:return 1
            if memo[i] != -1:return memo[i]
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)
sol = Solution()
print(sol.climbStairs(2))