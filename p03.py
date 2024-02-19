"""

Problem: 1. Two Sum

URL: https://leetcode.com/problems/two-sum/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def twoSum(nums, target):
    # maintain a dictionary
    d = dict()
    for i in range(len(nums)):
        # find difference of target and curr number
        diff = target - nums[i]
        # if diff is in the dict, return those indices
        if diff in d:
            return [d[diff], i]
        d[nums[i]] = i
    return []


# sample test cases
cases = [
    {
        "nums": [2,7,11,15],
        "target": 9
    },
    {
        "nums": [3,2,4],
        "target": 6
    },
    {
        "nums": [3,3],
        "target": 6
    }
]

for case in cases:
    print(case["nums"], case["target"], ":", twoSum(case["nums"], case["target"]))