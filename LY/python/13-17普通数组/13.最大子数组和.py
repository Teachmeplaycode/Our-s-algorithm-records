from typing import List
from collections import deque
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化：第一个元素结尾的最大子数组和就是它本身
        current_sum = max_sum = nums[0]
        # 从第二个元素开始遍历
        for i in range(1, len(nums)):
            # 状态转移：当前元素单独成组 vs 与前面子数组合并
            current_sum = max(nums[i], current_sum + nums[i])
            # 更新全局最大值
            max_sum = max(max_sum, current_sum)
        
        return max_sum

t1 = [-2,1,-3,4,-1,2,1,-5,4]
t2 = [1]
t3 = [5,4,-1,7,8]
t4 = [-2,1]
nums_list=[t3]
sol = Solution()
for i in nums_list:
   print(sol.maxSubArray(i))