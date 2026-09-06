# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Pre(t) -> t is a binary tree, 0 <= nn(t) <= 100

        Need to return t0 s.t. Post(t0) -> t0 is a binary tree, t0
        contains the same nodes as t, and t0 is an inverted version of t
        """
        def invert(root):
            if not root:
                return 

            invert(root.left)
            invert(root.right)
            root.right, root.left = root.left, root.right


        invert(root)
        return root
        