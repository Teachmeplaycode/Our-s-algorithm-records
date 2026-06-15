from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        col,dg,bdg = [0]*n,[0]*2*n,[0]*2*n
        def trackback(row):
            if row == n:
                s = [''.join(row) for row in board]
                ans.append(s)
                return
            for i in range(n):
                if col[i] or dg[row+i] or bdg[row-i+n-1]:continue
                board[row][i] = 'Q'
                col[i] = dg[row+i] = bdg[row-i+n-1] = 1
                trackback(row+1)
                board[row][i] = '.'
                col[i] = dg[row+i] = bdg[row-i+n-1] = 0
        trackback(0)
        return ans

sol = Solution()
n = 4
res = sol.solveNQueens(n)
for i in res:
    for j in i:
        print(j)
    print()