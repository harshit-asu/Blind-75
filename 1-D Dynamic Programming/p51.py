"""

Problem: 213. House Robber II

URL: https://leetcode.com/problems/house-robber-ii/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


def maxRob(nums, inds, prev, dp, first):
    if inds == len(nums):
        return 0
    if (inds, False, first) not in dp:
        dp[(inds, False, first)] = maxRob(nums, inds+1, False, dp, first)
    a = dp[(inds, False, first)]
    if prev or (inds == len(nums)-1 and first):
        return a
    if inds == 0:
        first = True
    if (inds, True, first) not in dp:
        dp[(inds, True, first)] = nums[inds] + maxRob(nums, inds+1, True, dp, first)
    return max(a, dp[(inds, True, first)])

def rob(nums) -> int:
    dp = dict()
    return maxRob(nums, 0, False, dp, False)


# sample test cases
cases = [
    [2,3,2],
    [1,2,3,1],
    [1,2,3]
]

for case in cases:
    print(case, ":", rob(case))