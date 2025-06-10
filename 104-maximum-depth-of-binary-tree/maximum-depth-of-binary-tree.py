# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth_helper(root, 0)

    def depth_helper(self, root, depth):
        if root is None:
            return depth
        l_depth = self.depth_helper(root.right, depth)
        r_depth = self.depth_helper(root.left, depth)
        depth = max(l_depth, r_depth)+1
        return depth
