
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# left=0
# a=[]
# res=[]
# for right in range(len(nums)):
#     while right-left+1>k:
#         a.remove(nums[left])
#         left+=1
#     a.append(nums[right])
#     if right-left+1==k:
#         res.append(max(a))
# print(res)
from collections import deque
nums = [1,3,-1,-3,5,3,6,7]
k = 3
dq=deque()
res=[]
for i,num in enumerate(nums):
    while dq and dq[0]<=i-k:
        dq.popleft()
    while dq and nums[dq[-1]]<=num:
        dq.pop()
    dq.append(i)
    if i>=k-1:
        res.append(nums[dq[0]])
print(res)