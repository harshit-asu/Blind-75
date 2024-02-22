"""

Problem: 98. Validate Binary Search Tree

URL: https://leetcode.com/problems/validate-binary-search-tree/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def traverse(self, root, inorder):
    if root:
        self.traverse(root.left, inorder)
        inorder.append(root.val)
        self.traverse(root.right, inorder)

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    inorder = []
    self.traverse(root, inorder)
    return len(inorder) == len(set(inorder)) and inorder == sorted(inorder)