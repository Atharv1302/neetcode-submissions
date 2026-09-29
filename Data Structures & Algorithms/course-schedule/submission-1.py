from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseMap = defaultdict(list)

        for main, prereq in prerequisites:
            courseMap[main].append(prereq)

        visited = set()

        def dfs(mainCourse):

            if mainCourse in visited:
                return False

            visited.add(mainCourse)

            for prereq in courseMap[mainCourse]:
                if not dfs(prereq):
                    return False


            visited.remove(mainCourse)
            courseMap[mainCourse] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True


        