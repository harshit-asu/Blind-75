"""

Problem: 347. Top K Frequent Elements

URL: https://leetcode.com/problems/top-k-frequent-elements/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def topKFrequent(nums, k: int):
    # maintain a dictionary to count frequencies
    # sort the dict in decreasing order of frequencies
    # get the top k keys
    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = d.get(nums[i], 0) + 1
    d = dict(sorted(d.items(), key=lambda x: -x[1]))
    return list(d.keys())[:k]


# sample test cases
cases = [
    {
        "nums": [1,1,1,2,2,3],
        "k": 2
    },
    {
        "nums": [1],
        "k": 1
    }
]

for case in cases:
    print(case["nums"], case["k"], ":", topKFrequent(case["nums"], case["k"]))