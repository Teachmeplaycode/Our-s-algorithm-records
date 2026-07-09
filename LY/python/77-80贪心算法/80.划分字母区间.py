from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        last = {c:i for i,c in enumerate(s)}
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                ans.append(end - start + 1)
                start = end + 1
        return ans        
sol = Solution()
s = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(s))