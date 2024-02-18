"""

Problem: 11. Container With Most Water

URL: https://leetcode.com/problems/container-with-most-water/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def maxArea(height) -> int:
    i, j = 0, len(height)-1
    area = 0
    while i < j:
        a = min(height[i], height[j])*(j-i)
        if a > area:
            area = a
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return area


# sample test cases
cases = [
    [1,8,6,2,5,4,8,3,7],
    [1,1]
]

for case in cases:
    print(case, ":", maxArea(case))