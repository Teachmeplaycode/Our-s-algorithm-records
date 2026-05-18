from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        result = []
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        while top <= bottom and left <= right:
            # 从左到右遍历上边
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # 从上到下遍历右边
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # 从右到左遍历下边（如果还有行）
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # 从下到上遍历左边（如果还有列）
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result
matrix = [[1,2,3,4],
          [5,6,7,8],
          [8,9,10,11],
          [12,13,14,15]]
matrix2 = [[1,2,3,4,5,6],
          [7,8,9,10,11,12],
          [13,14,15,16,17,18],
          [19,20,21,22,23,24]]
sol = Solution()
print(sol.spiralOrder(matrix))