"""

Problem: 191. Number of 1 Bits

URL: https://leetcode.com/problems/number-of-1-bits/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def hammingWeight(n: int) -> int:
    c = 0
    while n:
        c += n%2
        n = n>>1
    return c


# sample test cases
cases = [
    11
]

for case in cases:
    print(case, ":", hammingWeight(case))