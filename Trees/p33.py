"""

Problem: 105. Construct Binary Tree from Preorder and Inorder Traversal

URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


# run this on Leetcode, because TreeNode is not implemented here.
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(inorder) == 0:
        return None
    ind = inorder.index(preorder[0])
    return TreeNode(preorder[0], left=self.buildTree(preorder[1:ind+1], inorder[:ind]), right=self.buildTree(preorder[ind+1:], inorder[ind+1:]))