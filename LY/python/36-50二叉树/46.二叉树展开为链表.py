from typing import List, Optional
from debug import *
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        lst = []
        def dfs(node:TreeNode):
            if not node: return None
            lst.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(lst)
        node = TreeNode(None)
        dummy = node
        for i in range(1,len(lst)):
            node.right = TreeNode(lst[i])
            node = node.right
        root.right = dummy.right
        root.left = None
        

sol = Solution()
root = TreeNode(1,TreeNode(2),None)
# root = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,None,TreeNode(6)))
# root = TreeNode(1,None,TreeNode(2,None,TreeNode(3,None,TreeNode(4,None,TreeNode(5,None,TreeNode(6))))))
printTree(root)
sol.flatten(root)
# printTree(root)