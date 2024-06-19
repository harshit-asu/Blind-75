"""

Problem: 91. Decode Ways

URL: https://leetcode.com/problems/decode-ways/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

dp = {}
def numDecodings(s: str) -> int:
    if len(s) == 0:
        return 1
    if s[0] == '0':
        return 0
    if s not in dp:
        a = numDecodings(s[1:])
        b = 0
        if len(s) >= 2 and int(s[:2]) <= 26:
            b = numDecodings(s[2:])
        dp[s] = a + b
    return dp[s]

# sample test cases
cases = [
    "12",
    "226",
    "06"
]

for case in cases:
    print(case, ":", numDecodings(case))