class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        cnt = n
        def union(x, y):
            nonlocal cnt
            px, py = find(x), find(y)
            if px != py:
                cnt -= 1
                parent[px] = py

        for u, v in edges:
            union(u, v)
        return cnt