from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True