"""

Problem: 1143. Longest Common Subsequence

URL: https://leetcode.com/problems/longest-common-subsequence/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m = len(text1)
    n = len(text2)
    # m rows, and n cols
    dp = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


# sample test cases
cases = [
    {
        "text1": "abcde",
        "text2": "ace"
    },
    {
        "text1": "abc",
        "text2": "abc"
    },
    {
        "text1": "abc",
        "text2": "def"
    }
]

for case in cases:
    print(case, ":", longestCommonSubsequence(case["text1"], case["text2"]))