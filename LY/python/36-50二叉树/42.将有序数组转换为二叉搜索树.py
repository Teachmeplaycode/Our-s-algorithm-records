from typing import List, Optional
from debug import TreeNode, printTree

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:return None
        mid = len(nums)//2
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])
        return TreeNode(nums[mid],left,right)

sol = Solution()
printTree(sol.sortedArrayToBST([-10,-3]))