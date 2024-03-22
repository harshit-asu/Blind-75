"""

Problem: 200. Number of Islands

URL: https://leetcode.com/problems/number-of-islands/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def valid(rows, cols, r, c):
        if r >= 0 and r < rows and c >= 0 and c < cols:
            return True
        return False

def dfs(grid, r, c, visited, rows, cols):
    if valid(rows, cols, r, c) and not visited[r][c] and grid[r][c] == "1":
        visited[r][c] = True
        dfs(grid, r+1, c, visited, rows, cols)
        dfs(grid, r-1, c, visited, rows, cols)
        dfs(grid, r, c+1, visited, rows, cols)
        dfs(grid, r, c-1, visited, rows, cols)

def numIslands(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for j in range(cols)] for i in range(rows)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(grid, i, j, visited, rows, cols)
                count += 1
    return count

# sample test cases
cases = [
    [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ],
    [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
]

for case in cases:
    print(case, ":", numIslands(case))