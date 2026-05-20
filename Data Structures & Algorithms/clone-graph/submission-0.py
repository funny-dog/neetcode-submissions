"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        def dfs(node):
            if node in visited:
                 return visited[node]
            new_node = Node(node.val, None)
            visited[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)
            

