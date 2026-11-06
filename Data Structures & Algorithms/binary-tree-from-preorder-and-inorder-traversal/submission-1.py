# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}

        preorder_map = iter(preorder)

        def helper(left_inorder_idx, right_inorder_idx):
            if left_inorder_idx > right_inorder_idx:
                return None

            root_val = next(preorder_map)
            root = TreeNode(root_val)

            root_inorder_idx = inorder_map[root_val]

            root.left = helper(left_inorder_idx, root_inorder_idx-1)
            root.right = helper(root_inorder_idx + 1, right_inorder_idx)

            return root

        return helper(0, len(inorder)-1)


























# preorder = [3, 9, 20]inorder = [9, 3, 20]We call helper(0, 2) because the whole inorder list has indices 0, 1, 2.next(preorder_iter) gives us 3. We make 3 our root node.We look up 3 in our inorder map. Its index is 1 (root_inorder_idx = 1).Left Child Call: helper(0, 1 - 1) \(\rightarrow \) helper(0, 0).Inside this call, next() gives us 9. We make 9 a node.9 is at index 0 in inorder.Its left call will be helper(0, -1), which hits the stop sign and returns None.Its right call will be helper(1, 0), which also hits the stop sign and returns None.Node 9 is finished and attaches to the left of 3.Right Child Call: helper(1 + 1, 2) \(\rightarrow \) helper(2, 2).Inside this call, next() gives us 20. We make 20 a node.Following the same logic, it attaches to the right of 3.Finally, the function returns the completed root node 3, which now holds the entire tree structure.