# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:    
        def validate(node, low, high):
            # Base Case: An empty node is technically a valid BST
            if not node:
                return True
            
            # If the current node's value breaks the boundary rules, it's invalid
            if not (low < node.val < high):
                return False
            
            # Check subtrees:
            #   5  <- Range: (-inf, inf)
            # /   \
            # 3     7
            # Going Left: The maximum allowed value becomes the current node's value 
            # validate(node.left, -inf, 5)
            # Going Right: The minimum allowed value becomes the current node's value
            # validate(node.right, 5, inf)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Initially, the root can be any number between minus infinity and infinity
        return validate(root, float('-inf'), float('inf'))
