from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==[]: return 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = []
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==True or grid[i][j]=='0': continue
                visited[i][j] = True
                queue.append([i,j])
                while queue:
                    cur = queue.pop(0)
                    for dir in directions:
                        x = cur[0]+dir[0]
                        y = cur[1]+dir[1]
                        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]): continue
                        if visited[x][y]==True: continue
                        if grid[x][y]=='0': continue
                        visited[x][y] = True
                        queue.append([x,y])
                ans += 1
        return ans
grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','0','0','0','0'],
  ['0','0','0','0','0']
]
sol = Solution()
print(sol.numIslands(grid))