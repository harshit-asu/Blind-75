"""

Problem: 125. Valid Palindrome

URL: https://leetcode.com/problems/valid-palindrome/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

import re

def isPalindrome(s: str) -> bool:
    # remove all not alnums using regular expression
    s = re.sub("[^a-zA-Z0-9]", '', s).lower()
    return s == s[::-1]
    # this can be solved using two pointer method as well
    # take left and right pointers and check for equality only if current char is alnum
    # if it not alnum, perform the required increment or decrement operation.


# sample test cases
cases = [
    "A man, a plan, a canal: Panama",
    "race a car"
]

for case in cases:
    print(case, ":", isPalindrome(case))