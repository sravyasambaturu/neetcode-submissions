# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return head.right

# 1. The Theory: What are Preorder and Inorder?
# • Preorder ([Root -> Left -> Right]): Tells you the exact sequence nodes were created. The first element is always the root.
# • Inorder ([Left -> Root -> Right]): Tells you the left-to-right positioning.
# 	• If you look at an item in inorder, everything to its left belongs to its left subtree, and everything to its right belongs to its right subtree.
# 	• The first item in inorder is always the absolute farthest-left leaf node of the entire tree.
# 2. The Logic: How This Specific Code Works
# Instead of using a standard programming array (a stack) to remember parent nodes as it climbs up and down, this code uses a temporary bridge trick:
# 1. Diving Left: As the code processes preorder and builds nodes going down-left, it intentionally wires the new child's .right pointer back up to its parent.
# 2. The "Stop" Sign: It keeps building left until the node it just made matches inorder[j]. This match is a signal that says: "Stop! You have reached the absolute bottom-left corner of this section."
# 3. Climbing Back Up: Once it hits that stop sign, it reads those temporary .right pointers to easily climb back up to the parent, deletes the temporary bridge to clean up the tree, and moves to the right.
# 3. Step-by-Step Walkthrough Example
# Let's build this simple tree using the code:
# • preorder = [3, 9, 20]
# • inorder  = [9, 3, 20]
# python
# # Initial Setup
# head = TreeNode(None) # Dummy starter node
# curr = head
# i, j = 0, 0           # i tracks preorder, j tracks inorder
# Use code with caution.
# Round 1: Creating the True Root
# • Line: curr.right = TreeNode(preorder[i]) \(\rightarrow \) Creates Node 3 and links it to head.right.
# • curr moves to Node 3.
# • i increments to 1.
#   head (None)
#      \
#       3 (curr) <-- (i=1)
# Round 2: Diving Left
# • Check the loop: while i < n and curr.val != inorder[j]:
# 	• curr.val is 3, inorder[j] is inorder[0] which is 9.
# 	• Since 3 != 9, we enter the loop!
# • Line: curr.left = TreeNode(preorder[i], right=curr)
# 	• Creates Node 9 (from preorder[1]).
# 	• The Trick: Node 9's .left pointer is empty, but its .right pointer is wired back up to Node 3 (curr).
# • curr moves down to Node 9.
# • i increments to 2.
#      head (None)
#         \
#          3  <----\
#         /          | (Temporary bridge)
#   (curr) 9 --------/
# Round 3: Hitting the Stop Sign & Climbing Up
# • Check the loop again: curr.val is 9, inorder[j] is 9.
# 	• Since 9 == 9, the while loop stops! We reached the bottom-left corner.
# • Line: j += 1 \(\rightarrow \) j becomes 1 (looking for 3 now).
# • Line: while curr.right and curr.right.val == inorder[j]:
# 	• curr.right is Node 3. Its value is 3. inorder[1] is 3. They match!
# 	• This means we are completely done with Node 3's left side.
# • Inside the climb-up loop:
# 	• prev = curr.right (remembers Node 3)
# 	• curr.right = None (Erases the temporary bridge so Node 9's right becomes clean/empty).
# 	• curr = prev (curr safely climbs back up to Node 3).
# 	• j += 1 \(\rightarrow \) j becomes 2 (looking for 20 now).
# Our tree now looks perfectly normal again:
#      head (None)
#         \
#          3 (curr)
#         /
#        9 
# Round 4: Moving Right
# • The outer loop continues because i < 3 and j < 3.
# • Line: curr.right = TreeNode(preorder[i]) \(\rightarrow \) Creates Node 20 (from preorder[2]) and attaches it to Node 3's right side.
# • curr moves to Node 20.
# • i increments to 3.
#      head (None)
#         \
#          3 
#         / \
#        9   20 (curr)
# • The inner loops are all skipped now because i has reached the end of the array (3).
# • The main loop finishes, and the code executes: return head.right.
# Final Output Tree:
#      3 
#     / \
#    9   20
