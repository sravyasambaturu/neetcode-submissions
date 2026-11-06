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

        # If the main tree is empty, it cannot contain subRoot
        if not root:
            return False
        
        # If the current structure matches, return True
        if self.sameTree(root, subRoot):
            return True
        
        # Otherwise, check if subRoot matches the left or right branches of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                self.sameTree(root.right, subRoot.right))
        return False

    #    Main Tree (root)                   Your SubRoot Tree
       
    #          1                                    2
    #         / \                                  / \
    #        2   3                                4   5
    #       / \                                  (No children below 4)
    #      4   5 
    #     /
    #    6   <-- This extra node 
    #            breaks the match!
