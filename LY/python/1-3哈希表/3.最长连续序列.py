from typing import List
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        nums = sorted(set(nums))
        diff=[0]
        diff.extend([nums[i]-nums[i-1] for i in range(1,len(nums))])
        max_l,cur_l=0,0
        for i in range(len(diff)):
            if diff[i]==0 or diff[i]==1:
                cur_l+=1
            else:
                max_l = max(cur_l,max_l)
                cur_l = 1
        return max(cur_l,max_l)

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        max_l = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_l = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_l += 1
                max_l = max(max_l, current_l)
        return max_l

class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        max_len = 1
        current_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:  
                current_len += 1
            else:  
                max_len = max(max_len, current_len)
                current_len = 1
        return max(max_len, current_len)  
# 最优解↓
class Solution4:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        for num in st:
            if num-1 in st:continue
            nxt = num+1
            while nxt in st:nxt+=1
        ans=max(ans,nxt-num)
        return ans