"""

Problem: 235. Lowest Common Ancestor of a Binary Search Tree

URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
        return root
    elif root.val > p.val and root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    return self.lowestCommonAncestor(root.right, p, q)