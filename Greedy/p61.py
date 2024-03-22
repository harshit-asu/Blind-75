"""

Problem: 53. Maximum Subarray

URL: https://leetcode.com/problems/maximum-subarray/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def maxSubArray(nums) -> int:
    # Kadane's algorithm
    globalMax = -10**4 - 1
    localMax = 0
    for i in range(len(nums)):
        localMax += nums[i]
        globalMax = max(globalMax, localMax)
        if localMax < 0:
            localMax = 0
    return globalMax

# sample test cases
cases = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8]
]

for case in cases:
    print(case, ":", maxSubArray(case))