# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = pre
            pre, curr = curr, nxt
        
        p1, p2 = head, pre
        while p2:
            nxt1, nxt2 = p1.next, p2.next
            p1.next = p2
            p2.next = nxt1
            p1, p2 = nxt1, nxt2