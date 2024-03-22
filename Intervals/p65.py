"""

Problem: 435. Non-overlapping Intervals

URL: https://leetcode.com/problems/non-overlapping-intervals/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def eraseOverlapIntervals(intervals) -> int:
    intervals = sorted(intervals, key=lambda x: x[1])
    prev = intervals[0][1]
    result = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev:
            result += 1
        else:
            prev = intervals[i][1]
    return result


cases = [
    [[1,2],[2,3],[3,4],[1,3]],
    [[1,2],[1,2],[1,2]],
    [[1,2],[2,3]]
]

for case in cases:
    print(case, ":", eraseOverlapIntervals(case))