from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def createTree(*args):
    """
    根据层序遍历序列创建二叉树
    支持传入列表或逐个传入元素，例如:
    createTree([1, 2, 3, None, 4]) 或 createTree(1, 2, 3, None, 4)
    """
    # 兼容传入列表或可变参数
    if len(args) == 1 and isinstance(args[0], list):
        vals = args[0]
    else:
        vals = list(args)
        
    if not vals or vals[0] is None:
        return None
        
    # 初始化根节点和队列
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    
    # 层序遍历构建二叉树
    while queue and i < len(vals):
        node = queue.popleft()
        
        # 构建左子节点
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
            
        # 构建右子节点
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
            
    return root

def printTree(root):
    def build(node):
        if not node:
            return [], 0, 0
        val_str = str(node.val)
        val_len = len(val_str)
        if not node.left and not node.right:
            return [val_str], val_len, val_len // 2

        left_lines, left_w, left_root = build(node.left)
        right_lines, right_w, right_root = build(node.right)
        gap = 2

        total_width = left_w + val_len + gap + right_w
        root_pos = left_w + val_len // 2

        # 根节点行
        line1 = " " * left_w + val_str + " " * (gap + right_w)

        # 斜线行
        line2_chars = [" "] * total_width
        if node.left:
            left_slash = left_root
            line2_chars[left_slash] = '/'
        if node.right:
            right_slash = left_w + val_len + gap + right_root
            line2_chars[right_slash] = '\\'
        line2 = "".join(line2_chars)

        # 后续行合并
        other_lines = []
        max_depth = max(len(left_lines), len(right_lines))
        for i in range(max_depth):
            left_part = left_lines[i] if i < len(left_lines) else " " * left_w
            right_part = right_lines[i] if i < len(right_lines) else " " * right_w
            other_lines.append(left_part + " " * gap + right_part)

        lines = [line1, line2] + other_lines
        # 填充右侧空格，使所有行等宽
        for i in range(len(lines)):
            if len(lines[i]) < total_width:
                lines[i] = lines[i].ljust(total_width)

        return lines, total_width, root_pos

    lines, _, _ = build(root)
    if lines:
        print("\n".join(lines))
