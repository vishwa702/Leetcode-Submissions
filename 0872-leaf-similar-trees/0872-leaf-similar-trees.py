# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf_sequence(root):
            # Iterative Pre-order traversal
            if not root:
                return []
            
            stack, result = [root], []
            
            while stack:
                node = stack.pop()
                
                if not node.left and not node.right:
                    result.append(node.val)
                
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            if True: 
                print(result)
            
            return result

        
        return get_leaf_sequence(root1) == get_leaf_sequence(root2)
