"""

Problem: 79. Word Search

URL: https://leetcode.com/problems/word-search/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def wordStart(board, i, j, word, visited):
    if len(word) == 0:
        return True
    if not (i >= 0 and i < len(board)) or not (j >= 0 and j < len(board[0])) or visited[i][j] or board[i][j] != word[0]:
        return False
    visited[i][j] = True
    updates = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]
    for update in updates:
        if wordStart(board, i+update[0], j+update[1], word[1:], visited):
            return True
    visited[i][j] = False
    return False

def exist(board, word: str) -> bool:
    visited = [[False for j in range(len(board[i]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and wordStart(board, i, j, word, visited):
                return True
    return False

# sample test cases
cases = [
    {
        "board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        "word": "ABCCED"
    },
    {
        "board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        "word": "SEE"
    },
    {
        "board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
        "word": "ABCB"
    }
]

for case in cases:
    print(case, ":", exist(case["board"], case["word"]))