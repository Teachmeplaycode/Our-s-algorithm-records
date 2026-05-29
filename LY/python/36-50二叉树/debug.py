class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    """以 / \ 树形打印二叉树"""
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
