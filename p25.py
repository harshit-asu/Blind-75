"""

Problem: 226. Invert Binary Tree

URL: https://leetcode.com/problems/invert-binary-tree/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        # swap
        left = root.left
        root.left = root.right
        root.right = left
        # recurse
        self.invertTree(root.left)
        self.invertTree(root.right)
    return root