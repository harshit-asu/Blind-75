"""

Problem: 139. Word Break

URL: https://leetcode.com/problems/word-break/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def breakWord(s, wordDict, dp):
    if len(s) == 0:
        return True
    if s not in dp:
        dp[s] = False
        for word in wordDict:
            if len(s) >= len(word) and s[:len(word)] == word:
                if breakWord(s[len(word):], wordDict, dp):
                    dp[s] = True
                    break
    return dp[s]

def wordBreak(s: str, wordDict) -> bool:
    dp = {}
    wordDict.sort()
    return breakWord(s, wordDict, dp)


# sample test cases
cases = [
    {
        "s": "leetcode",
        "wordDict": ["leet","code"]
    },
    {
        "s": "applepenapple",
        "wordDict": ["apple","pen"]
    },
    {
        "s": "catsandog",
        "wordDict": ["cats","dog","sand","and","cat"]
    }
]

for case in cases:
    print(case, ":", wordBreak(case["s"], case["wordDict"]))