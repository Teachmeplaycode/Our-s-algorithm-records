from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == []: return 0
        ans = 0
        queue = []
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 and not vis[i][j]:
                    vis[i][j] = True
                    queue.append([i,j])
        while queue:
            size = len(queue)
            rotted = False
            for _ in range(size):
                x,y = queue.pop(0)
                for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not vis[nx][ny] and grid[nx][ny] == 1:
                        rotted = True
                        vis[nx][ny] = True
                        queue.append([nx,ny])
                        grid[nx][ny] = 2
            if rotted: ans += 1
        for i in range(len(grid)):
            if 1 in grid[i]: return -1
        return ans
s = Solution()
grid = [
    [1,2]
]
print(s.orangesRotting(grid))