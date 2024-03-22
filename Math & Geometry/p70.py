"""

Problem: 73. Set Matrix Zeroes

URL: https://leetcode.com/problems/set-matrix-zeroes/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def setZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = []
    cols = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    for i in rows:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
    for j in cols:
        for i in range(len(matrix)):
            matrix[i][j] = 0


# sample test cases
cases = [
    [[1,1,1],[1,0,1],[1,1,1]],
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
]

for case in cases:
    print(case, ":", end=" ")
    setZeroes(case)
    print(case)