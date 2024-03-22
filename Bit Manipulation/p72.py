"""

Problem: 338. Counting Bits

URL: https://leetcode.com/problems/counting-bits/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def countBits(n: int):
    result = [0]*(n+1)
    for i in range(n+1):
        t = i
        while t:
            result[i] += t%2
            t = t >> 1
    return result


# sample test cases
cases = [
    2,
    5
]

for case in cases:
    print(case, ":", countBits(case))