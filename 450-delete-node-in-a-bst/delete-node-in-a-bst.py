# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                successor=self.findmin(root.right)
                root.val=successor.val
                root.right=self.deleteNode(root.right,successor.val)
        return root   
    # To find in-order successor
    def findmin(self, node:Optional[TreeNode]) -> Optional[TreeNode]:
            while node.left:
                node=node.left
            return node