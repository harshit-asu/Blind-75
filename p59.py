"""

Problem: 62. Unique Paths

URL: https://leetcode.com/problems/unique-paths/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def uniquePaths(m: int, n: int) -> int:
    dp = [
        [0 for i in range(n)] for j in range(m)
    ]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


# sample test cases
cases = [
    {
        "m": 3,
        "n": 7
    },
    {
        "m": 3,
        "n": 2
    }
]

for case in cases:
    print(case, ":", uniquePaths(case["m"], case["n"]))