"""

Problem: 55. Jump Game

URL: https://leetcode.com/problems/maximum-subarray/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def isJumpToLastPossible(nums, curr_index, visited):
    # print(visited)
    if curr_index == len(nums)-1:
        return True
    if visited[curr_index] != -1:
        return visited[curr_index]
    if nums[curr_index] == 0:
        visited[curr_index] = False
        return False
    # isPossible = False
    start = min(len(nums)-1, nums[curr_index]+curr_index)
    for i in range(start, curr_index, -1):
        if visited[i] == -1:
            visited[i] = isJumpToLastPossible(nums, i, visited)
        if visited[i]:
            visited[curr_index] = True
            break
    if visited[curr_index] == -1:
        visited[curr_index] = False
    return visited[curr_index]

def canJump(nums) -> bool:
    visited = [-1 for i in range(len(nums))]
    return isJumpToLastPossible(nums, 0, visited)

# sample test cases
cases = [
    [2,3,1,1,4],
    [3,2,1,0,4]
]

for case in cases:
    print(case, ":", canJump(case))