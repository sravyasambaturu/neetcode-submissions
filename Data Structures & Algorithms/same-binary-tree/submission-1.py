# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. If both nodes are empty, they match.
        if not p and not q:
            return True
        
        # 2. If only one is empty, or their values don't match, they don't match.
        if not p or not q or p.val != q.val:
            return False
        
        # 3. Recursively check if left matches left AND right matches right.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        