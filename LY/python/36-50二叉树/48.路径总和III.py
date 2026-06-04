from typing import Optional
from debug import *
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        res = 0
        queue = [root]
        # path = []
        def dfs(root,S):
            nonlocal res
            if not root: return
            S+=root.val
            # path.append(root.val)
            if S == targetSum: 
                # print(path)
                res+=1
            dfs(root.left,S)
            dfs(root.right,S)
            S-=root.val  
            # path.pop()
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                dfs(node,0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res

from collections import defaultdict
class Solution2():
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        cnt = defaultdict(int)
        cnt[0] = 1
        res = 0
        def dfs(node,s):
            if node is None: return
            nonlocal res
            s+=node.val
            res+=cnt[s-targetSum]
            cnt[s]+=1
            dfs(node.left,s)
            dfs(node.right,s)
            cnt[s]-=1
        dfs(root,0)
        return res
sol = Solution2()
# root = TreeNode(10,TreeNode(5,TreeNode(3,TreeNode(3),TreeNode(-2)),TreeNode(2,None,TreeNode(1))),TreeNode(-3,None,TreeNode(11)))
# root = TreeNode(5,TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)),None),TreeNode(8,TreeNode(13,None,None),TreeNode(4,TreeNode(5),TreeNode(1))))
root = TreeNode(1,None,TreeNode(2,None,TreeNode(3,None,TreeNode(4,None,TreeNode(5)))))
printTree(root)
print(sol.pathSum(root,3))