# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        step = 0
        p1, p2 = l1, l2
        while p1 and p2:
            sum += (p1.val + p2.val) * (10 ** step)
            p1, p2 = p1.next, p2.next
            step += 1
        while p1:
            sum += p1.val * (10 ** step)
            p1 = p1.next
            step += 1
        while p2:
            sum += p2.val * (10 ** step)
            p2 = p2.next
            step += 1
        if sum == 0:
            return ListNode(0)
        dummy = ListNode(-1)
        p = dummy
        while sum:
            p.next = ListNode(sum % 10)
            p = p.next
            sum //= 10
        return dummy.next