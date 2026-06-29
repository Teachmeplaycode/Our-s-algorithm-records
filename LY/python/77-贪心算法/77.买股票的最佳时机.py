from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit,minProfit = 0,1e9
        for p in prices:
            maxProfit = max(p - minProfit,maxProfit)
            minProfit = min(p,minProfit)
        return maxProfit
sol = Solution()
prices = [7,6,4,3,1]
print(sol.maxProfit(prices))