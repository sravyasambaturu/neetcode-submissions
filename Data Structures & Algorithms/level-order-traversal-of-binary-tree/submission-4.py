# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


#     3 (Level 0)
#    / \
#   9  20 (Level 1)
# Step 1: Start at the Root (Node 3, depth = 0)
# • res is empty ([]). len(res) is 0.
# • Because len(res) == depth (0 == 0), it appends an empty list: res = [[]].
# • It appends the value 3 into index 0: res = [[3]].
# • It calls dfs(node.left, 1) to visit Node 9.
# Step 2: Move to Left Child (Node 9, depth = 1)
# • len(res) is 1. Our current depth is 1.
# • Because len(res) == depth (1 == 1), it adds a new level basket: res = [[3], []].
# • It appends the value 9 into index 1: res = [[3], [9]].
# • Node 9 has no children, so both of its child calls return None back up to the root.
# Step 3: Move to Right Child (Node 20, depth = 1)
# • We backtracked up to Node 3 and now dive right into Node 20.
# • Our current depth is 1.
# • Check the condition: len(res) is 2, but depth is 1. Since 2 ≠ 1, it skips creating a new list (the basket for level 1 already exists!).
# • It appends the value 20 into the existing index 1 basket: res = [[3], [9, 20]].
# Step 4: Finish
# • Node 20 has no children. The recursive stack clears out, and res is returned.
# • Final Output: [[3], [9, 20]]