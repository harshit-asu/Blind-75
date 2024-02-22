"""

Problem: 104. Maximum Depth of Binary Tree

URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))