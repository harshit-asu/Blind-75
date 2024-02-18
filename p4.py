"""

Problem: 49. Group Anagrams

URL: https://leetcode.com/problems/group-anagrams/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def groupAnagrams(strs):
    # sort a string to get a key
    # anagrams give same sorted string
    # add them to dict with the obtained string as key
    d = dict()
    for i in range(len(strs)):
        s = "".join(sorted(strs[i]))
        if s not in d:
            d[s] = [strs[i]]
        else:
            d[s].append(strs[i])
    return list(d.values())


# sample test cases
cases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]

for case in cases:
    print(case, ":", groupAnagrams(case))