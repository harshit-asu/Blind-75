"""

Problem: 56. Merge Intervals

URL: https://leetcode.com/problems/merge-intervals/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

class Solution:
    def isOverlapping(self, i1, i2):
        if i1[1] < i2[0] or i2[1] < i1[0]:
            return False
        return True

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        # stack = []
        # for interval in intervals:
        #     temp = interval
        #     while len(stack) and self.isOverlapping(temp, stack[-1]):
        #         temp = [min(temp[0], stack[-1][0]), max(temp[1], stack[-1][1])]
        #         stack.pop()
        #     stack.append(temp)
        # return stack
        result = []
        i = 0
        while i < len(intervals):
            j = i+1
            currInt = intervals[i]
            while j < len(intervals) and self.isOverlapping(currInt, intervals[j]):
                currInt[1] = max(currInt[1], intervals[j][1])
                j += 1
            i = j
            result.append(currInt)
        return result