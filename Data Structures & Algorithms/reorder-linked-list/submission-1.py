# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        

        



# You cannot easily read a singly linked list backward from the tail. To solve this efficiently in O(n) time and O(1) space, we break the problem down into three smaller steps:
# Find the middle of the list (using the Fast and Slow pointer trick).
# Reverse the second half of the list (using the Reverse Linked List trick).
# Merge the two halves by alternating nodes (using a variation of the Merge trick).
