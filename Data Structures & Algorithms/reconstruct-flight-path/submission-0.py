class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)
        
        route = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            route.append(start)
        dfs("JFK")
        return route[::-1]