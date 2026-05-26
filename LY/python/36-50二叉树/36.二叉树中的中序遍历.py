from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def dfs(root:Optional[TreeNode]):        
            if root is None: 
                return None
            dfs(root.left)
            if root.val is not None: 
                lst.append(root.val)
            dfs(root.right)
        dfs(root)
        return lst
        