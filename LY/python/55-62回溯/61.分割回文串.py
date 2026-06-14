from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1: return [[s]]
        res,path = [],[]
        def isPalindrome(sub)-> bool:return sub == sub[::-1]
        def trace(start:int):
            if start == len(s):
                res.append(path[:])
                return
            for i in range(start+1,len(s)+1):
                sub = s[start:i]
                if isPalindrome(sub):
                    path.append(sub)
                    trace(i)
                    path.pop()
        trace(0)
        return res
sol = Solution()
s = "aab"
print(sol.partition(s))