"""

Problem: 57. Insert Interval

URL: https://leetcode.com/problems/insert-interval/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


class Solution:
    def isOverlapping(self, i1, i2):
        if (i1[0] >= i2[0] and i1[0] <= i2[1] or
            i1[1] >= i2[0] and i1[1] <= i2[1] or
            i2[0] >= i1[0] and i2[0] <= i1[1] or
            i2[1] >= i1[0] and i2[1] <= i1[1]):
            return True
        return False

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        result = []
        flag = False
        while i < len(intervals):
            if self.isOverlapping(intervals[i], newInterval):
                flag = True
                j = i
                while j < len(intervals) and self.isOverlapping(intervals[j], newInterval):
                    j += 1
                result.append([min(intervals[i][0], newInterval[0]), max(intervals[j-1][1], newInterval[1])])
                i = j-1
            else:
                result.append(intervals[i])
            if flag:
                result += intervals[i+1:]
                break
            i += 1
        if not flag:
            result.append(newInterval)
            result = sorted(result)
        return result