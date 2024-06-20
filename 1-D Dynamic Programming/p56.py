"""

Problem: 152. Maximum Product Subarray

URL: https://leetcode.com/problems/maximum-product-subarray/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def maxProduct(nums) -> int:
    prevMin, prevMax = nums[0], nums[0]
    result = float('-inf')
    for i in range(1, len(nums)):
        result = max(result, prevMax)
        temp = [prevMin * nums[i], prevMax * nums[i], nums[i]]
        prevMin, prevMax = min(temp), max(temp)
    return max(result, prevMax)


# sample test cases
cases = [
    [2,3,-2,4],
    [-2,0,-1]
]

for case in cases:
    print(case, ":", maxProduct(case))