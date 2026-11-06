# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:   
#     def isSubtree(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
#         if not t: return True
#         if not s: return False
        
#         if self.sameTree(s, t):
#             return True
#         return (self.sameTree(s.left, t) and self.sameTree(s.right, t))

#     def sameTree(self, s, t):
#         if not s and not t:
#             return True
#         if s and t and s.val == t.val:
#             return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
#         return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False


        