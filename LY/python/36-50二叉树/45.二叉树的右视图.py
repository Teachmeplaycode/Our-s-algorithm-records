from typing import List, Optional
from debug import *
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = [root]
        Floor=[root.val]
        while queue:
            stack = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left: 
                    queue.append(node.left)
                    stack.append(node.left.val)
                if node.right: 
                    queue.append(node.right)
                    stack.append(node.right.val)
            Floor.append(stack[-1]) if stack else None
        return Floor
sol = Solution()
root = TreeNode(1,TreeNode(2,None,TreeNode(5)),TreeNode(3,None,TreeNode(4)))
# root2 = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(5),None),None),TreeNode(3))
printTree(root)
print(sol.rightSideView(root))