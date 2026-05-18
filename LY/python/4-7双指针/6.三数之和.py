# def threeSum(nums):
#     nums.sort()
#     res = []
#     def dfs(start, path, target):
#         if len(path) == 3:
#             if target == 0:
#                 res.append(path[:])
#             return
#         if len(path) > 3:
#             return           
#         for i in range(start, len(nums)):
#             if i > start and nums[i] == nums[i-1]:
#                 continue
#             path.append(nums[i])
#             dfs(i + 1, path, target - nums[i])  
#             path.pop()
    
#     dfs(0, [], 0)
#     return res
# nums=[-1,0,1,2,-1,-4]
# print(threeSum(nums))
# nums = [-1,0,1,2,-1,-4]
# nums.sort()
# res_dict = {}
# res = []
# for i in range(len(nums)):
#     num1 = nums[i]
#     left = i+1
#     right = len(nums)-1
#     while left < right:
#         num2 = nums[left]
#         num3 = nums[right]
#         if num1 + num2 + num3 == 0:
#             key = (num1, num2, num3) 
#             if key not in res_dict:
#                 res_dict[key] = [num1, num2, num3]
#             left += 1
#             right -= 1
#         elif num1 + num2 + num3 > 0:
#             right -= 1
#         elif num1 + num2 + num3 < 0:
#             left += 1
# res = list(res_dict.values()) 
# print(res)
def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:  # 跳过重复
            continue
            
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                # 跳过重复元素
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return res