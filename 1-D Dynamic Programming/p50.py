"""

Problem: 198. House Robber

URL: https://leetcode.com/problems/house-robber/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def maxRob(nums, inds, prev, dp):
    if inds == len(nums):
        return 0
    if (inds, False) not in dp:
        dp[(inds, False)] = maxRob(nums, inds+1, False, dp)
    a = dp[(inds, False)]
    if prev:
        return a
    if (inds, True) not in dp:
        dp[(inds, True)] = nums[inds] + maxRob(nums, inds+1, True, dp)
    return max(a, dp[(inds, True)])

def rob(nums) -> int:
    dp = dict()
    return maxRob(nums, 0, False, dp)

# sample test cases
cases = [
    [1,2,3,1],
    [2,7,9,3,1]
]

for case in cases:
    print(case, ":", rob(case))