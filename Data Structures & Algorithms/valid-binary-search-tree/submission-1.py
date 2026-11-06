# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        def in_order(node):
            if not node:
                return True

            in_order(node.left)
            values.append(node.val)
            in_order(node.right)

        in_order(root)

        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False

        return True
        