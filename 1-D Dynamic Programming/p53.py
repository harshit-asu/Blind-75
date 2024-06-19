"""

Problem: 647. Palindromic Substrings

URL: https://leetcode.com/problems/palindromic-substrings/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def countSubstrings(s: str) -> int:
    palindromes = {}
    for length in range(1, len(s)+1):
        for i in range(len(s)-length+1):
            if (
                length == 1 or
                (length == 2 and s[i] == s[i+length-1]) or
                (s[i] == s[i+length-1] and (i+1, i+length-2) in palindromes)
            ):
                palindromes[(i, i+length-1)] = True
    return len(palindromes)

# sample test cases
cases = [
    "abc",
    "aaa"
]

for case in cases:
    print(case, ":", countSubstrings(case))