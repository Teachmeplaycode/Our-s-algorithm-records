from typing import Optional
from debug import *
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None: return None
        self.lst = []
        def dfs(root):
            if root is None: return
            self.lst.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        self.lst.sort()
        return self.lst[k-1]
sol = Solution()
root = TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4))
root2 = TreeNode(5,TreeNode(3,TreeNode(2,TreeNode(1),None),TreeNode(4)),TreeNode(6,None,None))
print(sol.kthSmallest(root,1))
print(sol.kthSmallest(root,3))