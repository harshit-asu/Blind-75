"""

Problem: 70. Climbing Stairs

URL: https://leetcode.com/problems/climbing-stairs/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

dp = [-1 for i in range(46)]

def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    if dp[n] >= 0:
        return dp[n]
    dp[n] = climbStairs(n-1) + climbStairs(n-2)
    return dp[n]


# sample test cases
cases = [
    2,
    3,
    40
]

for case in cases:
    print(case, ":", climbStairs(case))