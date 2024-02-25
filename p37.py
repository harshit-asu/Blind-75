"""

Problem: 211. Design Add and Search Words Data Structure

URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for letter in word:
            if letter in currNode.children:
                currNode = currNode.children[letter]
            else:
                newNode = Node()
                currNode.children[letter] = newNode
                currNode = newNode
        currNode.isWord = True

    def searchWord(self, node: Node, word: str) -> bool:
        if len(word) == 0:
            return node.isWord
        if word[0] == ".":
            for child in node.children:
                if self.searchWord(node.children[child], word[1:]):
                    return True
            return False
        if word[0] in node.children:
            return self.searchWord(node.children[word[0]], word[1:])
        return False

    def search(self, word: str) -> bool:
        return self.searchWord(self.root, word)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)