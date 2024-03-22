"""

Problem: 153. Find Minimum in Rotated Sorted Array

URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def findMin(nums) -> int:
    left, right = 1, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] < nums[0]:
            right = mid - 1
        elif nums[mid] > nums[0]:
            left = mid + 1
    if left < len(nums):
        return nums[left]
    return nums[0]


# sample test cases
cases = [
    [3,4,5,1,2],
    [4,5,6,7,0,1,2],
    [11,13,15,17]
]

for case in cases:
    print(case, ":", findMin(case))