from typing import Optional
from debug import TreeNode,printTree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,max_val,min_val):
            if not root: return True
            if root.val >= max_val or root.val <= min_val: return False
            return dfs(root.left,root.val,min_val) and dfs(root.right,max_val,root.val)
        return dfs(root,float('inf'),float('-inf'))
sol = Solution()
root = TreeNode(2,TreeNode(1),TreeNode(3))
printTree(root)
print(sol.isValidBST(root))