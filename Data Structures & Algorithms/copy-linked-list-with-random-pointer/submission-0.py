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
        dicts = {None : None}
        tmp = head 
        while tmp != None:
            new_node = Node(tmp.val)
            dicts[tmp] = new_node
            tmp = tmp.next
        
        tmp = head
        while tmp != None:
            dicts[tmp].next = dicts[tmp.next]
            dicts[tmp].random = dicts[tmp.random]
            tmp = tmp.next

        return dicts[head]




            # 1 -> 3 
            # tmp  tmp.next
            #      dicts[3]
            # dicts[1].next = 


        

        

