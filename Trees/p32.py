"""

Problem: 230. Kth Smallest Element in a BST

URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def traverse(self, root, inorder):
    if root:
        self.traverse(root.left, inorder)
        inorder.append(root.val)
        self.traverse(root.right, inorder)

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    inorder = []
    self.traverse(root, inorder)
    return inorder[k-1]