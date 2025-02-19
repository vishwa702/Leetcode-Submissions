# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        def get_successor(curr):
            if (not curr) or (not curr.right):
                return curr

            curr = curr.right
            while curr and curr.left:
                curr = curr.left
            return curr


        if root is None: 
            return root
        
        print(f'Called deleteNode({root.val}, {key})')

        if key < root.val:
            if root.left: root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            if root.right: root.right = self.deleteNode(root.right, key)
            return root
        else:
            
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left


            # find smallest in the right subtree (in-order successor)
            successor = get_successor(root)
            
            # bring the successor node to the current place
            root.val = successor.val

            # remove the successor
            root.right = self.deleteNode(root.right, successor.val)

        return root
        