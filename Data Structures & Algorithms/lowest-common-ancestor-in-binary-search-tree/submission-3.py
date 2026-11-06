# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        
        while current:
            # If both values are smaller than current, LCA is in the left branch
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both values are larger than current, LCA is in the right branch
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # If they split paths, or one matches the current node, we found our LCA!
            else:
                return current
