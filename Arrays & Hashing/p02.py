"""

Problem: 242. Valid Anagram

URL: https://leetcode.com/problems/valid-anagram/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def isAnagram(s, t):
    # count occurrences of each char
    ds, dt = dict(), dict()
    for i in range(len(s)):
        ds[s[i]] = ds.get(s[i], 0) + 1
    for i in range(len(t)):
        dt[t[i]] = dt.get(t[i], 0) + 1
    # return False if not same number of unique chars
    if len(ds) != len(dt):
        return False
    for k, v in ds.items():
        if k not in dt or dt[k] != v:
            return False
    return True


# sample test cases
cases = [
    {
        "s": "anagram",
        "t": "nagaram"
    },
    {
        "s": "rat",
        "t": "car"
    }
]

for case in cases:
    print(case["s"], case["t"], ":", isAnagram(case["s"], case["t"]))