from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            left,right=0,len(matrix[0])
            while left<right:
                mid = (left+right)//2
                if matrix[i][mid]==target:
                    return True
                if matrix[i][mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            if left<len(matrix[0]) and matrix[i][left]==target:
                return True
        return False
matrix =[[1,4,7,11,15],
         [2,5,8,12,19],
         [3,6,9,16,22],
         [10,13,14,17,24],
         [18,21,23,26,30]]
target = 20
sol = Solution()
print(sol.searchMatrix(matrix, target))