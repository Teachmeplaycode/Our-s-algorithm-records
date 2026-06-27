from typing import List
class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     ans = 0
    #     sign_min,sign_max = 0,0
    #     for i in range(len(heights)):
    #         ans = max(heights[i],ans)
    #         if heights[i] <= heights[sign_min]:sign_min = i
    #         if heights[i] >= heights[sign_max]:sign_max = i
    #     for i in range(len(heights)):
    #         if i <= sign_min: 
    #             h = heights[sign_min]
    #             l = len(heights) - i
    #             s = l * h
    #             ans = max(s,ans)
    #         h = heights[sign_max]
    #         for j in range(i+1,len(heights)):
    #             h = min(heights[j],heights[i],h)
    #             l = j - i + 1
    #             s = l * h
    #             ans = max(s,ans)
    #     return ans
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        ans = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                w = i - left -1
                ans = max(ans,h*w)
            stack.append(i)
        heights.pop()
        return ans     
sol = Solution()
heights = [2,2,5,6,2,2]
print(sol.largestRectangleArea(heights))