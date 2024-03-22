"""

Problem: 124. Binary Tree Maximum Path Sum

URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, allMax):
        if not node:
            return 0
        l = self.dfs(node.left, allMax)
        r = self.dfs(node.right, allMax)
        vals = [
            node.val,
            node.val + l,
            node.val + r
        ]
        allMax.append(max(node.val + l + r, max(vals)))
        return max(vals)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        allMax = []

        retVal = self.dfs(root, allMax)

        return max(allMax)