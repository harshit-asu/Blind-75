"""

Problem: 190. Reverse Bits

URL: https://leetcode.com/problems/reverse-bits/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def reverseBits(n: int) -> int:
    reverse = 0
    total = 32
    while total:
        reverse *= 2
        if n:
            reverse += n%2
            n = n >> 1
        total -= 1
    return reverse


# sample test cases
cases = [
    43261596,
    4294967293
]

for case in cases:
    print(case, ":", reverseBits(case))