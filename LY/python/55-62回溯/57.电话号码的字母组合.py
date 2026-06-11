from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        op = [dic[digits[i]] for i in range(len(digits))]
        comblen = len(digits)
        res = []
        def trace(comb,use):
            if len(comb) == comblen:
                res.append("".join(comb))
                return
            for i in range(len(use)):
                for j in range(len(use[i])):
                    comb.append(use[i][j])
                    trace(comb,use[i+1:])
                    comb.pop()
        trace([],op)
        return res
        
digits="2345"
sol = Solution()
print(sol.letterCombinations(digits))