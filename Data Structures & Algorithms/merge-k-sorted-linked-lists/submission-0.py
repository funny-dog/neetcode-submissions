# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        dummy = ListNode(-1)
        head = dummy
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(q, (node.val, i, node))
        while q:
            val, i, node = heapq.heappop(q)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))
        return dummy.next
