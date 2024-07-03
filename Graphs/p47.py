"""

Problem: 323. Number of Connected Components in an Undirected Graph

URL: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

from collections import deque

def countComponents(n: int, edges) -> int:
    edgesDict = {}
    for a, b in edges:
        if a not in edgesDict:
            edgesDict[a] = []
        if b not in edgesDict:
            edgesDict[b] = []
        edgesDict[a].append(b)
        edgesDict[b].append(a)

    visited = [False]*n
    numConnectedComponents = 0
    while False in visited:
        node = visited.index(False)
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            visited[currNode] = True
            if currNode in edgesDict:
                for adj in edgesDict[currNode]:
                    if not visited[adj]: queue.append(adj)
        numConnectedComponents += 1
    return numConnectedComponents


# sample test cases
cases = [
    {
        "n": 3,
        "edges": [[0,1], [0,2]]
    },
    {
        "n": 6,
        "edges": [[0,1], [1,2], [2,3], [4,5]]
    }
]

for case in cases:
    print(case, ":", countComponents(case["n"], case["edges"]))