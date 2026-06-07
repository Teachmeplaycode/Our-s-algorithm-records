from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prev,course in prerequisites:
            graph[course].append(prev)
        visited = [0]*numCourses
        def dfs(i):
            if visited[i]==1:return False
            if visited[i]==2:return True
            visited[i] = 1
            for prev in graph[i]:
                if not dfs(prev):return False
            visited[i] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True
s = Solution()
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(s.canFinish(numCourses, prerequisites))