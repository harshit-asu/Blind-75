"""

Problem: 133. Clone Graph

URL: https://leetcode.com/problems/clone-graph/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = Node(val=node.val)
        q = deque([(node, clone)])
        explored = set()
        created_node = {
            node: clone
        }
        while q:
            curr_node, cloned_node = q.popleft()
            if curr_node not in explored:
                for neighbor in curr_node.neighbors:
                    if neighbor not in created_node:
                        created_node[neighbor] = Node(val=neighbor.val)
                    q.append((neighbor, created_node[neighbor]))
                    cloned_node.neighbors.append(created_node[neighbor])
                explored.add(curr_node)
        return clone