from typing import List, Optional
from debug import *
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        if len(preorder)==1: return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        preorder.pop(0)
        root.left = self.buildTree(preorder,inorder[:mid])
        root.right = self.buildTree(preorder,inorder[mid+1:])
        return root
sol = Solution()
printTree(sol.buildTree([3,9,20,15,7],[9,3,15,20,7]))