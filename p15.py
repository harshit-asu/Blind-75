"""

Problem: 76. Minimum Window Substring

URL: https://leetcode.com/problems/minimum-window-substring/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def getDiffDict(dt, ds):
    d = dict()
    for k, v in dt.items():
        if k not in ds:
            d[k] = v
        else:
            if v - ds[k] > 0:
                d[k] = v-ds[k]
    return d

# first find t frequencies
# then find the first possible substring in s with atleast all t frequencies
# then slide the window satisfying the condition that each substring contains all chars freq in t
def minWindow(s: str, t: str) -> str:
    m = len(s)
    n = len(t)
    if m < n:
        return ""
    dt = dict()
    for i in range(len(t)):
        dt[t[i]] = dt.get(t[i], 0) + 1
    ds = dict()
    for i in range(n):
        if s[i] in dt:
            ds[s[i]] = ds.get(s[i], 0) + 1
    left, right = 0, n-1
    minLength = m+1
    result = ""
    while right < m:
        diff = getDiffDict(dt, ds)
        while len(diff):
            right += 1
            if right < m and s[right] in dt:
                ds[s[right]] = ds.get(s[right], 0) + 1
                if s[right] in diff:
                    diff[s[right]] -= 1
                    if diff[s[right]] == 0:
                        del diff[s[right]]
            if right == m:
                break
        while left < m:
            if s[left] not in dt:
                left += 1
            else:
                if ds[s[left]] > dt[s[left]]:
                    ds[s[left]] -= 1
                    left += 1
                else:
                    break
        if left == m or right == m:
            break
        if right - left + 1 < minLength:
            minLength = right - left + 1
            result = s[left:right+1]
        ds[s[left]] -= 1
        left += 1
    return result


# sample test cases
cases = [
    {
        "s": "ADOBECODEBANC",
        "t": "ABC"
    },
    {
        "s": "a",
        "t": "a"
    },
    {
        "s": "a",
        "t": "aa"
    }
]

for case in cases:
    print(case["s"], case["t"], ":", minWindow(case["s"], case["t"]))