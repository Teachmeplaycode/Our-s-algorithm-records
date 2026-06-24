from typing import List
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0 for _ in range(len(temperatures))]
#         for i in range(len(answer)):
#             for j in range(i+1, len(temperatures)):
#                 if temperatures[j] <= temperatures[i]:continue
#                 else:
#                     answer[i] += j-i
#                     break
#         return answer
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre = stack.pop()
                answer[pre] = i - pre
            stack.append(i) 
        return answer
sol = Solution()
temperatures = [71,76,71,76,71,76,71,76,71,71]
# temperatures = [30,40,50,60]
# temperatures = [30,60,90]
# temperatures = [10,12,11,3,4,5,6,7,8,9,10,14,15,16,11]
print(sol.dailyTemperatures(temperatures))