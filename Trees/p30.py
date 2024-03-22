"""

Problem: 102. Binary Tree Level Order Traversal

URL: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    queue = []
    traversal = []
    queue.append((1, root))
    while len(queue):
        level, node = queue.pop(0)
        if len(traversal) < level:
            traversal.append([node.val])
        else:
            traversal[level-1].append(node.val)
        if node.left:
            queue.append((level+1, node.left))
        if node.right:
            queue.append((level+1, node.right))
    return traversal