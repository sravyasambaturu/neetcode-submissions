# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head 
        count = 0
        while node and count < k:
            count = count + 1
            node = node.next
        
        if count < k:
            return head 
        
        prev = None 
        curr = head 
        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseKGroup(curr, k)
        return prev
        