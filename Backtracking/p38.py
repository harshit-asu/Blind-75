"""

Problem: 212. Word Search II

URL: https://leetcode.com/problems/word-search-ii/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on leetcode

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for i in range(len(word)):
            if word[i] not in currNode.children:
                newNode = TrieNode()
                currNode.children[word[i]] = newNode
            currNode = currNode.children[word[i]]
        currNode.isWord = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for i in range(len(word)):
            if word[i] in currNode.children:
                currNode = currNode.children[word[i]]
            else:
                return False
        return currNode.isWord

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i in range(len(prefix)):
            if prefix[i] in currNode.children:
                currNode = currNode.children[prefix[i]]
            else:
                return False
        return True
    
class Solution:
    def valid(self, i, j, board):
        return (i >=0 and i < len(board)) and (j>=0 and j < len(board[0]))

    def allWords(self, board, i, j, word, visited, trie, result, maxLen):
        if not self.valid(i, j, board) or visited[i][j]:
            return
        word += board[i][j]
        if word[-1] in trie.children:
            trie = trie.children[word[-1]]
            if trie.isWord:
                result.add(word)
            if len(word) == maxLen:
                return
            visited[i][j] = True
            updates = [[1,0], [-1,0], [0, 1], [0, -1]]
            for update in updates:
                self.allWords(board, i+update[0], j+update[1], word, visited, trie, result, maxLen)
            visited[i][j] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        maxLen = 0
        for word in words:
            trie.insert(word)
            maxLen = max(maxLen, len(word))
        result = set()
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.allWords(board, i, j, "", visited, trie.root, result, maxLen)
        return list(result)