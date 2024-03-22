"""

Problem: 20. Valid Parentheses

URL: https://leetcode.com/problems/valid-parentheses/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def isValid(s: str) -> bool:
    # use a stack
    # if open bracket, push into stack
    # else, check if stack top is the corresponding closing bracket
    stack = []
    braces = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for i in range(len(s)):
        if s[i] in braces:
            if len(stack) > 0 and stack[-1] == braces[s[i]]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s[i])
    return len(stack) == 0


# sample test cases
cases = [
    "()",
    "()[]{}",
    "(]"
]

for case in cases:
    print(case, ":", isValid(case))