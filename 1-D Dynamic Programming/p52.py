"""

Problem: 5. Longest Palindromic Substring

URL: https://leetcode.com/problems/longest-palindromic-substring/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def longestPalindrome(s: str) -> str:
    r = s[::-1]
    n = len(s)
    for l in range(n, 1, -1):
        for i in range(n-l+1):
            s1 = s[i:i+l]
            s2 = r[n-(i+l):n-i]
            if s1 == s2:
                return s1
    return s[0]

# sample test cases
cases = [
    "babad",
    "cbbd"
]

for case in cases:
    print(case, ":", longestPalindrome(case))