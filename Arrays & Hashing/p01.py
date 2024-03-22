"""

Problem: Contains Duplicate

URL: https://leetcode.com/problems/contains-duplicate/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def containsDuplicate(nums):
    # create a set using nums elements
    # this set's length will be <= length of nums
    # if nums has duplicates it'll definitely be less
    return len(set(nums)) < len(nums)


# sample test cases
cases = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2]
]

for case in cases:
    print(case, ":", containsDuplicate(case))