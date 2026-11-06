# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1



        
# This code implements Morris In-Order Traversal to find the k-th smallest element in a Binary Search Tree (BST).
# What makes this solution incredible is its space efficiency. While normal tree traversals use recursion or a stack which takes O(H) memory (where H is the tree height), Morris Traversal uses O(1) auxiliary space (no recursion stack, no extra array). It achieves this by temporarily modifying the tree structure to create "threads" (pointers) back to parent nodes, cleaning up after itself as it goes.
# The Core Concept: The "Predecessor Link"
# In a sorted (in-order) traversal, the node you visit right before curr is called its in-order predecessor.
# • The predecessor is found by going to curr.left, and then traveling as far right as possible.
# • Normally, once you finish a left subtree, you need a stack to remember how to get back up to curr.
# • Morris Traversal says: Let's find the predecessor ahead of time, make its right pointer point to curr, and use that temporary bridge to walk back up!
# Code Logic Step-by-Step
# The code runs a while curr: loop and handles two main scenarios at each node:
# Scenario A: No Left Child (if not curr.left:)
# If there is no left subtree, curr is the smallest available node right now.
# 1. We "visit" it by decrementing k (k -= 1).
# 2. If k == 0, we found our answer and return curr.val.
# 3. Otherwise, we move to the right child (curr = curr.right).
# Scenario B: Left Child Exists (else:)
# We must explore the left side first, but we need a way back. We find the predecessor (pred) by going left once, then all the way right.
# • Case 1: Bridge doesn't exist yet (if not pred.right:)
# We create a temporary bridge from the predecessor back to our current node: pred.right = curr. Then, we safely move into our left subtree: curr = curr.left.
# • Case 2: Bridge already exists (else:)
# If pred.right == curr, it means we have already fully explored the left subtree and used the bridge to come back up! To restore the original tree, we break the bridge: pred.right = None. Since the left side is done, we "visit" curr (k -= 1), check if it's the k-th element, and move right (curr = curr.right).
# Beginner Walkthrough Example
# Let's find the k = 2 (2nd smallest) element in this BST:
#     3
#    / \
#   1   4
#    \
#     2
# Step 1: curr starts at 3
# • It has a left child (1), so it finds the predecessor of 3.
# • Go left to 1, then as far right as possible → Node 2.
# • pred.right is None, so it creates a bridge: Node 2's right pointer now points to 3.
# • Move left: curr becomes 1.
#    [3] <----\
#    / \       | (temporary bridge)
#   1   4      |
#    \         |
#     2 -------/
# Step 2: curr is now 1
# • It has no left child!
# • Decrement k: k drops from 2 to 1. (Not zero yet).
# • Move right: curr becomes 2.
# Step 3: curr is now 2
# • It has no left child!
# • Decrement k: k drops from 1 to 0.
# • Match Found! k == 0 triggers, and the function returns curr.val, which is 2.
# (Note: If k was larger, the code would keep going, follow the bridge back up to 3, realize pred.right == curr, delete the bridge to restore the tree, and check node 3).