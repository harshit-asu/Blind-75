"""

Problem: 261. Graph Valid Tree

URL: https://leetcode.com/problems/graph-valid-tree/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

from collections import deque

def validTree(n: int, edges) -> bool:
    if n == 1 and len(edges) == 0:
        return True
    if len(edges) != n-1:
        return False
    # BFS should cover all vertices
    edgesDict = {}
    for a, b in edges:
        if a not in edgesDict:
            edgesDict[a] = []
        if b not in edgesDict:
            edgesDict[b] = []
        edgesDict[a].append(b)
        edgesDict[b].append(a)

    visited = [False]*n
    queue = deque([visited.index(False)])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            visited[node] = True
            for adj in edgesDict[node]:
                if not visited[adj]: queue.append(adj)
    return not (False in visited)


# sample test cases
cases = [
    {
        "n": 5,
        "edges": [[0, 1], [0, 2], [0, 3], [1, 4]]
    },
    {
        "n": 5,
        "edges": [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    }
]

for case in cases:
    print(case, ":", validTree(case["n"], case["edges"]))