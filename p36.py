"""

Problem: 208. Implement Trie (Prefix Tree)

URL: https://leetcode.com/problems/implement-trie-prefix-tree/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


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
            if word[i] in currNode.children:
                currNode = currNode.children[word[i]]
            else:
                newNode = TrieNode()
                currNode.children[word[i]] = newNode
                currNode = newNode
        currNode.isWord = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for i in range(len(word)):
            if word[i] in currNode.children:
                if i == len(word)-1:
                    return currNode.children[word[i]].isWord
                else:
                    currNode = currNode.children[word[i]]
            else:
                return False
        return False
        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i in range(len(prefix)):
            if prefix[i] in currNode.children:
                if i == len(prefix) - 1:
                    return True
                else:
                    currNode = currNode.children[prefix[i]]
            else:
                return False
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)