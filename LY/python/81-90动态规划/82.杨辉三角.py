from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(1,numRows+1):
            ls = []
            for _ in range(i):ls.append(1)
            dp.append(ls)
        if numRows <= 2: return dp
        for i in range(2,len(dp)):
            for j in range(1,len(dp[i])-1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp
sol = Solution()
numRows = 5
print(sol.generate(numRows))