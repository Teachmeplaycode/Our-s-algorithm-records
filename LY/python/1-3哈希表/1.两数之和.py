'''
https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            if target - num in mp:
                return [mp[target - num], i]
            mp[num] = i
        return []
'''
思路：
1. 创建一个字典mp,用于存储数组中的元素和对应的索引。
2. 遍历数组中的每一个元素num和索引i。
3. 计算目标值target - num,并判断该值是否在mp中。
4. 如果在mp中,则返回mp[target - num]和i。
5. 如果不在mp中,则将num和i添加到mp中。

什么时候我们会想到哈希表呢？
1. 当问题需要快速查找某个元素是否存在时。
2. 当问题需要快速查找某个元素对应的索引时。
3. 当问题需要快速查找某个元素对应的值时。
总之就是需要快速查找某个元素，那么哈希表就适合
'''
