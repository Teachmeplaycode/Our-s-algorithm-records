from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i>=coin: dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
sol = Solution()
coins = [1,2,5]
amount = 11
print(sol.coinChange(coins,amount))
# def dfs(i,s,cnt):
#     if s > amount: return 
#     if s == amount:
#         print(cnt)
#     for coin in coins:
#         dfs(coin,s+coin,cnt+1)
# for i in coins:dfs(i,0,0)