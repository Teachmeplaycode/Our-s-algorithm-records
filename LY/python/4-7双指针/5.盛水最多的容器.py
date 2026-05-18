from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left,right,res=0,len(height)-1,0
#         while left<right:
#             h=min(height[left],height[right])
#             w=right-left
#             res=max(res,h*w)
#             if height[left]<height[right]:
#                 left+=1
#             else:
#                 right-=1
#         return res
# nums=[1,8,6,2,5,4,8,3,7]
# res=0
# # for i in range(len(nums)):
# #     for j in range(len(nums)-1,i,-1):
# #         h=min(nums[i],nums[j])
# #         w=j-i
# #         res=max(res,w*h)
# # print(res)
# left,right=0,0
# while left<right:
#     h=min(nums[left],nums[right])
#     w=right-left
#     res=max(res,w*h)
#     if nums[left]<nums[right]:
#         left+=1
#     else:
#         right-=1
# print(res)