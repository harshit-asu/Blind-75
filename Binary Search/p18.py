"""

Problem: 33. Search in Rotated Sorted Array

URL: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def search(nums, target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[l]:
            if nums[mid] > target:
                if nums[l] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
        else:
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                if nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
    return -1


# sample test cases
cases = [
    {
        "nums": [4,5,6,7,0,1,2],
        "target": 0
    },
    {
        "nums": [4,5,6,7,0,1,2],
        "target": 3
    },
    {
        "nums": [1],
        "target": 0
    }
]

for case in cases:
    print(case, ":", search(case["nums"], case["target"]))