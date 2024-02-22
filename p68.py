"""

Problem: 48. Rotate Image

URL: https://leetcode.com/problems/rotate-image/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for k in range(n):
        matrix[k] = matrix[k][::-1]


# sample test cases
cases = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
]

for case in cases:
    print(case, ":", end=" ")
    rotate(case)
    print(case)