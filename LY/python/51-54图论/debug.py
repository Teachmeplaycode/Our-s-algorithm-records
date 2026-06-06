from typing import List, Any


def print_grid(grid: List[List[Any]], sep: str = " "):
    """按行打印二维数组，每个元素用 sep 分隔"""
    for row in grid:
        print(sep.join(str(x) for x in row))


def print_grid_aligned(grid: List[List[Any]]):
    """按行打印二维数组，列对齐"""
    if not grid:
        print("[]")
        return
    # 计算每列最大宽度
    col_widths = [0] * len(grid[0])
    for row in grid:
        for j, val in enumerate(row):
            col_widths[j] = max(col_widths[j], len(str(val)))
    for row in grid:
        print("  ".join(str(val).rjust(col_widths[j]) for j, val in enumerate(row)))


# 用法示例
if __name__ == "__main__":
    grid1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    grid2 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    print("=== print_grid ===")
    print_grid(grid1)
    print()
    print_grid(grid2)

    print("\n=== print_grid_aligned ===")
    print_grid_aligned(grid1)
    print()
    print_grid_aligned(grid2)
