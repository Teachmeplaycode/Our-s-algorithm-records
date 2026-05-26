from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        def dfs(root:Optional[TreeNode],length):
            if root is None:return max(length,0)
            else:return max(dfs(root.left,length+1),
                            dfs(root.right,length+1))
        return dfs(root,0)
root = TreeNode(3)
root.left = TreeNode(9)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
sol.maxDepth(root)