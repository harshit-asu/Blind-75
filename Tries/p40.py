"""

Problem: 39. Combination Sum

URL: https://leetcode.com/problems/combination-sum/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def combinationSum(candidates, target):
    path = []
    result = set()

    def dfs(start, curr):
        if start >= len(candidates) or curr > target:
            return
        if curr == target:
            res = []
            for ind in path:
                res.append(candidates[ind])
            result.add(tuple(res))
            return
        path.append(start)
        dfs(start, curr+candidates[start])
        path.pop()
        dfs(start+1, curr)

    dfs(0,0)

    return list(result)

# sample test cases
cases = [
    {
        "candidates": [2,3,6,7],
        "target": 7
    },
    {
        "candidates": [2,3,5],
        "target": 8
    },
    {
        "candidates": [2],
        "target": 1
    }
]

for case in cases:
    print(case, ":", combinationSum(case["candidates"], case["target"]))