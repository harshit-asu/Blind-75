"""

Problem: 297. Serialize and Deserialize Binary Tree

URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return "(.)"
    return f"({str(root.val)}" + self.serialize(root.left) + self.serialize(root.right) + ")"
    

def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    if data == "(.)":
        return None
    i = 1
    while data[i] != "(":
        i += 1
    num = int(data[1:i])
    root = TreeNode(num)
    start = i + 1
    end = start + 1
    stack = ["("]
    while len(stack):
        if data[end] == ")":
            stack.pop()
        elif data[end] == '(':
            stack.append("(")
        end += 1
    root.left = self.deserialize(data[start-1:end])
    root.right = self.deserialize(data[end:-1])
    return root