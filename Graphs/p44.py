"""

Problem: 417. Pacific Atlantic Water Flow

URL: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r, c, visited, prevHeight):
        if ((r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
            return
        visited.add((r, c))
        dfs(r+1, c, visited, heights[r][c])
        dfs(r-1, c, visited, heights[r][c])
        dfs(r, c+1, visited, heights[r][c])
        dfs(r, c-1, visited, heights[r][c])
    
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows-1, c, atlantic, heights[rows-1][c])
    
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols-1, atlantic, heights[r][cols-1])

    result = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append([r, c])

    return result


# sample test cases
cases = [
    [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
    [[1]]
]

for case in cases:
    print(case, ":", pacificAtlantic(case))