class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        sq = [i*i for i in range(1, int(n**0.5) + 1)]
        for i in range(1,n+1):
            for q in sq:
                if q > i:break
                dp[i] = min(dp[i],dp[i-q] + 1)
        return dp[n]
sol = Solution()
n = 13
print(sol.numSquares(n))