"""

Problem: 3. Longest Substring Without Repeating Characters

URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def lengthOfLongestSubstring(s: str) -> int:
    maxLen = 0
    unique = set()
    for i in range(len(s)):
        initial_len = len(unique)
        unique.add(s[i])
        final_len = len(unique)
        if final_len == initial_len:
            maxLen = max(final_len, maxLen)
            del unique
            unique = set()
            unique.add(s[i])
            j = i-1
            while s[j] != s[i]:
                unique.add(s[j])
                j -= 1
    return max(maxLen, len(unique))


# sample test cases
cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]

for case in cases:
    print(case, ":", lengthOfLongestSubstring(case))