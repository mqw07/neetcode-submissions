# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Pre(root) -> 0 <= nn(root) <= 1000
        Need to return bool b s.t. Post(b) -> b iff root is balanced

        Strategy:
        Find height of each individual subtree, return true iff height of left and right differ
        no more than 1

        """

        self.bools = set()
        
        def height(root) -> int:
            if not root:
                self.bools.add(True)
                return 0
            lh = height(root.left)
            rh = height(root.right)
            self.bools.add(abs(lh - rh) <= 1)
            return 1 + max(lh, rh)
        
        height(root)
        return all(self.bools)

        