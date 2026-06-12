from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:return False
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(-1,0),(1,0),(0, -1),(0,1)]
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word) - 1:return board[r][c] == word[idx]
            if board[r][c] != word[idx]:return False
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    if dfs(nr, nc, idx + 1):return True
            visited[r][c] = False
            return False
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):return True 
        return False
sol = Solution()
board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"
print(sol.exist(board,word))