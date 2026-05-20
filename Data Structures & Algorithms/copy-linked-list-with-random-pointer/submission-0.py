"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        p = head
        while p:
            old_to_new[p] = Node(p.val)
            p = p.next
        p = head
        while p:
            node = old_to_new[p]
            node.next, node.random = old_to_new.get(p.next), old_to_new.get(p.random)
            p = p.next
        return old_to_new[head]