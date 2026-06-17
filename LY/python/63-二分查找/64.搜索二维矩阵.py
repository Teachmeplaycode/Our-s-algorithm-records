from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            left,right = 0,n-1
            while left<=right:
                mid = (left+right)//2
                if matrix[i][mid] == target: 
                    return True
                elif matrix[i][mid] < target: 
                    left = mid + 1
                else:right = mid - 1
        return False
sol = Solution()
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
print(sol.searchMatrix(matrix,13))