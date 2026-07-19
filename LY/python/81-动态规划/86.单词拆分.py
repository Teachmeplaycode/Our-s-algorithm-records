import functools
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len,wordDict))
        words = set(wordDict)
        @functools.cache
        def dfs(i:int)->bool:
            if i==0:return True
            return any(s[j:i] in words and dfs(j)
                       for j in range(i - 1, max(i - max_len - 1, -1), -1))
        return dfs(len(s))
sol = Solution()
s = "leetcode"
wordDict = ["leet","code"]
print(sol.wordBreak(s,wordDict))