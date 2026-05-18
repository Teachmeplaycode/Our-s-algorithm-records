# num=[1,2,3]
# k=6
# ans=0
# prefix = [0]
# for i in range(len(num)):
#     prefix.append(prefix[i]+num[i])
# # print(len(prefix))
# # print(prefix)
# # for i in range(len(prefix)):
# #     for j in range(i+1,len(prefix)):
# #         print(f'{prefix[j]}-{prefix[i]}={prefix[j]-prefix[i]}')
# #         if prefix[j]-prefix[i]==k:
# #             ans+=1
# # print(ans)
# left=0
# for right in range(len(prefix)):
#     while prefix[right]-prefix[left]>k:
#         left+=1
#     if prefix[right]-prefix[left]==k:
#         ans+=1
# print(ans)
nums=[1,2,3]
k=3
ans=0
count = {0:1}
prefix=0
for num in nums:
    prefix += num
    if count.get(prefix - k):
        ans += count[prefix - k]
    count[prefix] = count.get(prefix, 0) + 1
print(ans)