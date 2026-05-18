from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        req,res,left=len(p),[],0
        if len(p)>len(s):return []
        count={}
        for c in p:
            count[c]=count.get(c,0)+1
        for right in range(len(s)):
            if s[right] in count:
                if count[s[right]]>0:
                    req-=1
                count[s[right]]-=1
            if right-left+1>len(p):
                if s[left] in count:
                    if count[s[left]]>=0:
                        req+=1
                    count[s[left]]+=1
                left+=1
            if req==0 and right-left+1==len(p):
                res.append(left)
        return res
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         res,ans,left=[],[],0
#         if len(p)==1:
#             for i in range(len(s)): 
#                 if s[i]==p: 
#                     ans.append(i)
#         else:
#             for right in range(len(s)):
#                 while len(res)==len(p):
#                     res.remove(s[left])
#                     left+=1
#                 res.append(s[right])
#                 if sorted(res)==sorted(p):
#                     idx = s.find(''.join(res))
#                     while idx in ans:
#                         idx = s.find(''.join(res), idx+1)
#                     ans.append(idx)
#         return ans
# s = "abab"
# p = "ab"
# left,ans,res=0,[],""
# for right in range(len(s)):
#     while right-left+1>len(p):
#         res=s[left:right]
#         str_lst = sorted(res)
#         if str_lst==sorted(p) and left not in ans:
#             ans.append(left)
#         left+=1
#     if right-left+1==len(p):
#         res=s[left:right+1]
#         str_lst = sorted(res)
#         if str_lst==sorted(p) and left not in ans:
#             ans.append(left)
# print(ans)
# s = "abab"
# p = "ab"
# req,res,left=len(p),[],0
# if len(p)>len(s): ans=[]
# count={}
# for c in p:
#     count[c]=count.get(c,0)+1
# for right in range(len(s)):
#     if s[right] in count:
#         if count[s[right]]>0:
#             req-=1
#         count[s[right]]-=1
#     if right-left+1>len(p):
#         if s[left] in count:
#             if count[s[left]]>=0:
#                 req+=1
#             count[s[left]]+=1
#         left+=1
#     if req==0 and right-left+1==len(p):
#         res.append(left)
# print(res)
