class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque([a for a in range(numCourses) if indegree[a] == 0])
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        return res if len(res) == numCourses else []