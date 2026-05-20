class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))

        def find(x):
            if x!=parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return True
            parent[px] = py
            return False
        
        res = []
        for u, v in edges:
            if union(u, v):
                res = [u, v]
        return res
