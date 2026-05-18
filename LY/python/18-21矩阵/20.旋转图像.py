from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_queue=[]
        for col in range(n):
            lst=[]
            for row in range(n):
                lst.append(matrix[row][col])
            lst.reverse()
            new_queue.append(lst)
        matrix[:]=new_queue
        print(matrix)
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        
        for i in range(len(matrix)):
            matrix[i].reverse()
        

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol = Solution()
sol.rotate(matrix)      