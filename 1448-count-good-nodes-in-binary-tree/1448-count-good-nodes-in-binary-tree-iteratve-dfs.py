# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, float("-inf"))]  # Stack stores (node, max_val_so_far)
        good_nodes = 0
        
        while stack:
            node, max_val = stack.pop()
            
            if node.val >= max_val:
                good_nodes += 1  # Count the node as a "good node"
            
            new_max = max(max_val, node.val)  # Update max value
            
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
        
        return good_nodes

        