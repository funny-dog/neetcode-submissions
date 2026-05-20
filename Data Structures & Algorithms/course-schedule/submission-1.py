from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque()
        for course, cnt in enumerate(indegree):
            if cnt == 0:
                q.append(course)
        cnt = 0
        while q:
            course = q.popleft()
            cnt += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        return cnt == numCourses
        