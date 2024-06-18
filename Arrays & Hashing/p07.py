"""

Problem: 271. Encode and Decode Strings

URL: https://leetcode.com/problems/encode-and-decode-strings/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def encode(strs) -> str:
    resultStr = ""
    for i in range(len(strs)):
        resultStr += f'{len(strs[i])}#{strs[i]}'
    return resultStr

def decode(s: str):
    strs = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] != '#':
            j += 1
        length = int(s[i:j])
        strs.append(s[j+1:j+1+length])
        i = j + 1 + length
    return strs


# sample test cases
cases = [
    ["leet","code","love","you"],
    ["we","say",":","yes"]
]

for case in cases:
    print(case, ":", decode(encode(case)))