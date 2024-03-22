"""

Problem: 128. Longest Consecutive Sequence

URL: https://leetcode.com/problems/longest-consecutive-sequence/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def longestConsecutive(nums) -> int:
    # get all elements into dict
    # check if current element is the start of a consec seq
    # by checking if curr_ele-1 is in dict or not
    # if it is the start, find the length
    maxLen = 0
    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = d.get(nums[i], 0) + 1
    for k, v in d.items():
        if k-1 not in d:
            next_ele = k+1
            while next_ele in d:
                next_ele += 1
            maxLen = max(maxLen, next_ele-k)
    return maxLen


# sample test cases
cases = [
    [100,4,200,1,3,2],
    [0,3,7,2,5,8,4,6,0,1]
]

for case in cases:
    print(case, ":", longestConsecutive(case))