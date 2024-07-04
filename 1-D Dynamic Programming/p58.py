"""

Problem: 300. Longest Increasing Subsequence

URL: https://leetcode.com/problems/longest-increasing-subsequence/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


def lengthOfLIS(nums) -> int:
    n = len(nums)
    dp = [1]*n
    for i in range(n-1, -1, -1):
        maxLen = 0
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                maxLen = max(maxLen, dp[j])
        dp[i] += maxLen
    return max(dp)


# sample test cases
cases = [
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [7,7,7,7,7,7,7]
]

for case in cases:
    print(case, ":", lengthOfLIS(case))