# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # fast slow
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next #once 
            fast = fast.next.next #twice

        # reverse second half
        prev = None
        curr = slow.next
        slow.next = None # cutting

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge two halves alternating
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

