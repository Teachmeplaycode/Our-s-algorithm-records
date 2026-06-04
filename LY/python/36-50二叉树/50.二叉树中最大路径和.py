from typing import Optional
from debug import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 70%
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0
#         ans = float('-inf')
#         def bfs(root):
#             nonlocal ans
#             if not root: return
#             queue = [root]
#             while queue:
#                 for _ in range(len(queue)):
#                     node = queue.pop(0)
#                     ans = max(ans,dfs(node,0),node.val)
#                     if node.left:queue.append(node.left)
#                     if node.right:queue.append(node.right)
#         def dfs(root,s):
#             if not root: return 0
#             l = dfs(root.left,s)
#             r = dfs(root.right,s)
#             return max(root.val,root.val+l,root.val+r,root.val+l+r)
#         bfs(root)
#         return ans    
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = float('-inf')            
        def bfs(root):
            if not root: return
            queue = [root]
            roots = []
            lefts = []
            rights = []
            while queue:
                node = queue.pop(0)
                roots.append(node.val)
                if node.left:
                    queue.append(node.left)
                    lefts.append(len(roots)+len(queue)-1) #我去！神之一手！
                else:lefts.append(float('-inf'))
                if node.right:
                    queue.append(node.right)
                    rights.append(len(roots)+len(queue)-1)
                else:rights.append(float('-inf'))
            def dfs(i):
                nonlocal ans
                # 获取左孩子能提供的最大向下和
                left_max = 0
                # 判断左孩子是否存在
                if lefts[i] != float('-inf'):
                    left_idx = lefts[i]
                    left_max = max(0, dfs(left_idx))
                # 获取右孩子能提供的最大向下和
                right_max = 0
                if rights[i] != float('-inf'):
                    right_idx = rights[i]
                    right_max = max(0, dfs(right_idx))
                # 当前节点 i 处产生拐点，汇合左右两边
                current_path_sum = roots[i] + left_max + right_max
                ans = max(ans, current_path_sum)
                # 向上汇报
                return roots[i] + max(left_max, right_max)                     
            dfs(0)
        bfs(root)
        return ans       
sol = Solution()
root = createTree([5,4,8,11,None,13,4,7,2,None,None,None,1])
printTree(root)
print(sol.maxPathSum(root))