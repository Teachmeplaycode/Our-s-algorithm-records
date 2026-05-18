class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left,maxL=0,0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            maxL = max(maxL,right-left+1)
        return maxL
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         stack = []
#         max_len = 0
#         length = 0
#         for l in s:
#             if l not in stack:
#                 stack.append(l)
#                 max_len = max(max_len,len(stack))
#             else:
#                 index = stack.index(l)
#                 del stack[:index+1]
#                 stack.append(l)
#         return max_len