"""

Problem: 268. Missing Number

URL: https://leetcode.com/problems/missing-number/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def missingNumber(nums) -> int:
    # this only works for small values of n
    # n = len(nums)
    # return (n*(n+1))//2 - sum(nums)
    result = 0
    for i in range(len(nums)):
        result ^= nums[i]
        result ^= (i+1)
    return result


# sample test cases
cases = [
    [3,0,1],
    [0,1],
    [9,6,4,2,3,5,7,0,1]
]

for case in cases:
    print(case, ":", missingNumber(case))