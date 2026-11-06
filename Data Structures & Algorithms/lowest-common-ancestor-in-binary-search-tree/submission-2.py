# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start at the top of the tree
        current = root
        
        while current:
            # Case 1: Both targets are greater than current node -> Go Right
            if p.val > current.val and q.val > current.val:
                current = current.right
                
            # Case 2: Both targets are smaller than current node -> Go Left
            elif p.val < current.val and q.val < current.val:
                current = current.left
                
            # Case 3: Split point found! One is on the left, one is on the right
            else:
                return current

        