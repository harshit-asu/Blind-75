"""

Problem: 572. Subtree of Another Tree

URL: https://leetcode.com/problems/subtree-of-another-tree/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p == None and q == None:
        return True
    if p != None and q == None:
        return False
    if p == None and q != None:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root:
        return False
    if self.isSameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)