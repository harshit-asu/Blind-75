"""

Problem: 54. Spiral Matrix

URL: https://leetcode.com/problems/spiral-matrix/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def matrixSpiralTraversal(matrix, flip: bool):
    if len(matrix) == 0:
        return []
    if len(matrix) == 1:
        if flip:
            return matrix[0][::-1]
        return matrix[0]
    if len(matrix[0]) == 1:
        newMatrix = []
        for i in range(len(matrix)):
            newMatrix += matrix[i]
        if flip:
            newMatrix = newMatrix[::-1]
        return newMatrix
    border = []
    newMatrix = []
    if flip:
        for j in range(len(matrix[0])-1, -1, -1):
            border.append(matrix[-1][j])
        for i in range(len(matrix)-2, -1, -1):
            border.append(matrix[i][0])
        for i in range(len(matrix)-1):
            newMatrix.append(matrix[i][1:])
    else:
        for j in range(len(matrix[0])):
            border.append(matrix[0][j])
        for i in range(1, len(matrix)):
            border.append(matrix[i][-1])
        for i in range(1, len(matrix)):
            newMatrix.append(matrix[i][:-1])
    return border + matrixSpiralTraversal(newMatrix, not flip)

def spiralOrder(matrix):
    return matrixSpiralTraversal(matrix, False)

# sample test cases
cases = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
]

for case in cases:
    print(case, ":", spiralOrder(case))