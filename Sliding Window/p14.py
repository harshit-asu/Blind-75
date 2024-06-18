"""

Problem: 424. Longest Repeating Character Replacement

URL: https://leetcode.com/problems/longest-repeating-character-replacement/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def characterReplacement(s: str, k: int) -> int:
    count = {}
    start, end = 0, 0
    result = 0
    while end < len(s):
        count[s[end]] = count.get(s[end], 0) + 1
        length = end - start + 1
        while start <= end and length - max(count.values()) > k:
            count[s[start]] -= 1
            start += 1
            length -= 1
        result = max(result, length)
        end += 1
    return result



# sample test cases
cases = [
    {
        's': "ABAB",
        'k': 2
    },
    {
        's': "AABABBA",
        'k': 1
    },
]

for case in cases:
    print(case, ":", characterReplacement(case["s"], case["k"]))