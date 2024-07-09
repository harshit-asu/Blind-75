"""

Problem: 269. Alien Dictionary

URL: https://leetcode.com/problems/alien-dictionary/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def foreignDictionary(words) -> str:
    n = len(words)
    adj = {letter:set() for word in words for letter in word}
    for i in range(n-1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    
    visited = {}
    result = list()

    def dfs(letter):
        if letter in visited:
            return visited[letter]
        visited[letter] = True
        for neighbor in adj[letter]:
            if dfs(neighbor):
                return True
        visited[letter] = False
        result.append(letter)

    for letter in adj:
        if dfs(letter):
            return ""

    return "".join(result[::-1])


# sample test cases
cases = [
    ["z","o"],
    ["hrn","hrf","er","enn","rfnn"]
]

for case in cases:
    print(case, ":", foreignDictionary(case))