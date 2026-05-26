from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        def bfs(root):
            if not root: return
            dq = deque([root])
            while dq:
                cur = dq.popleft()
                cur.left,cur.right = cur.right,cur.left
                if cur.left: dq.append(cur.left)
                if cur.right: dq.append(cur.right)
            cur = root
            return cur
        return bfs(root)
        
            
        
sol = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
sol.invertTree(root)