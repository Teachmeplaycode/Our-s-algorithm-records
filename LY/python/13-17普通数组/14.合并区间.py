from typing import List
class Solution:
    def __init__(self):
        self.res = []
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        print(f'按第一个数字升序排序:{intervals}')
        # 初始化结果数组，放入第一个区间
        self.res = [intervals[0].copy()]
        # 处理剩余区间
        for i in range(1, len(intervals)):
            current = intervals[i]
            last = self.res[-1]
            # 如果当前区间的开始 <= 上一个区间的结束，说明有重叠
            if current[0] <= last[1]:
                # 合并：更新上一个区间的结束为两者结束的最大值
                last[1] = max(last[1], current[1])
            else:
                self.res.append(current.copy())
        print(f'合并后的结果:{self.res}')
        return self.res
intervals =  [[1,4],[5,6]]
sol = Solution()
sol.merge(intervals)

            