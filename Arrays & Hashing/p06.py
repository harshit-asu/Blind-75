"""

Problem: 238. Product of Array Except Self

URL: https://leetcode.com/problems/product-of-array-except-self/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def productExceptSelf(nums):
    # get prefix product and suffix product
    # get product of both at each index and return
    prefix = [1 for i in range(len(nums))]
    suffix = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        prefix[i] = nums[i-1] * prefix[i-1]
    for i in range(len(nums)-2, -1, -1):
        suffix[i] = nums[i+1] * suffix[i+1]
    result = []
    for i in range(len(nums)):
        result.append(prefix[i]*suffix[i])
    return result 


# sample test cases
cases = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]

for case in cases:
    print(case, ":", productExceptSelf(case))