"""

Problem: 207. Course Schedule

URL: https://leetcode.com/problems/course-schedule/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""


def canFinish(numCourses: int, prerequisites) -> bool:
    courseDict = {}
    for course, prereq in prerequisites:
        if course not in courseDict:
            courseDict[course] = []
        courseDict[course].append(prereq)

    def dfs(course, visited):
        if course not in courseDict:
            return True
        if course in visited:
            return False
        visited.add(course)
        for prereq in courseDict[course]:
            if not dfs(prereq, visited):
                return False
        visited.remove(course)
        del courseDict[course]
        return True
    
    for course in range(numCourses):
        if not dfs(course, set()):
            return False
    return True


# sample test cases
cases = [
    {
        "numCourses": 2,
        "prerequisites": [[1,0]]
    },
    {
        "numCourses": 2,
        "prerequisites": [[1,0], [0, 1]]
    },
]

for case in cases:
    print(case, ":", canFinish(case["numCourses"], case["prerequisites"]))