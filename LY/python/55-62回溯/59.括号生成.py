from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(left,right,path):
            if left==0 and right==0:
                res.append("".join(path))
                return
            if left>0:
                path.append("(")
                generate(left-1,right,path)
                path.pop()
            if right>left:
                path.append(")")
                generate(left,right-1,path)
                path.pop()
        generate(n,n,[])
        return res
sol = Solution()               
n = 1
print(sol.generateParenthesis(n))