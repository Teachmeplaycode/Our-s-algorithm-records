from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 将数组中所有小于等于0或大于n的数设置为n+1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        # 使用数组本身作为哈希表
        # 如果数字x存在于[1,n]范围内，则将nums[x-1]标记为负数
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        # 找到第一个正数的索引，即为缺失的第一个正数
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        # 如果数组中都是负数，则缺失的第一个正数是n+1
        return n + 1
sol = Solution()
nums = [10,8,9,6,7,2,3,4,5,1]
print(sol.firstMissingPositive(nums))
# import sys
# file = open('./input.txt','w')
# for i in range(1,int(1e5+1)):
#     if i%10==0:file.writelines('\n')
#     file.writelines(f'{i},')
# file.close()
     