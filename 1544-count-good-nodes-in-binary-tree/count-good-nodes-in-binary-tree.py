class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, root.val)]  # Stack stores (node, max_value_so_far)
        good_nodes = 0

        while stack:
            node, max_so_far = stack.pop()

            # Check if the current node is a "good" node
            if node.val >= max_so_far:
                good_nodes += 1

            # Update max value for the path
            new_max = max(max_so_far, node.val)

            # Push right and left children into stack with updated max_so_far
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
        
        return good_nodes