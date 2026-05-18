from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        ori_h = height[:]
        l, r = 0, len(height) - 1
        c = 0
        lm, rm = 0, 0
        while l < r:
            if ori_h[l] < ori_h[r]:
                if ori_h[l] >= lm:
                    lm = ori_h[l]
                else:
                    c += lm - ori_h[l]
                l += 1
            else:
                if ori_h[r] >= rm:
                    rm = ori_h[r]
                else:
                    c += rm - ori_h[r]
                r -= 1
        return c
# h = [5,6,8,0,8,0,1,0,6,8,6]
# ori_h = h[:]

# l, r = 0, len(h) - 1
# c = 0
# lm, rm = 0, 0

# while l < r:
#     if ori_h[l] < ori_h[r]:
#         if ori_h[l] >= lm:
#             lm = ori_h[l]
#         else:
#             c += lm - ori_h[l]
#         l += 1
#     else:
#         if ori_h[r] >= rm:
#             rm = ori_h[r]
#         else:
#             c += rm - ori_h[r]
#         r -= 1

# print(c)
