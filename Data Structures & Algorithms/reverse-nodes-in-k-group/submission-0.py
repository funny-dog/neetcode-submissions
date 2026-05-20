# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(-1, head)
        pre_tail = dummy
        while True:
            p = pre_tail
            for _ in range(k):
                p = p.next
                if not p:
                    return dummy.next
            curr_tail, next_head = pre_tail.next, p.next
            pre, curr = next_head, pre_tail.next
            for _ in range(k):
                nxt = curr.next
                curr.next = pre
                pre, curr = curr, nxt
            
            pre_tail.next = pre
            pre_tail = curr_tail
            
        return dummy.next