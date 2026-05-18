from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for s in strs:
            k=''.join(sorted(s))
            mp[k].append(s)
        res=list(mp.values())
        return res