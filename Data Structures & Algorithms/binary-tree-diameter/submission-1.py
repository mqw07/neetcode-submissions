# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Pre(root) -> root is the root of a binary tree, 1 <= nn(root) <= 100

        Return integer l s.t. Post(l) -> l is the max path length between two nodes
        Strategy: Find the diameter of any subtree, add them up.
        """
        self.res = 0

        def height(root):
            if not root:
                return 0
            h1 = height(root.left)
            h2 = height(root.right)
            
            self.res = max(self.res, h1 + h2)
            return 1 + max(h1, h2)
        
        height(root)
        return self.res
        
        

        

