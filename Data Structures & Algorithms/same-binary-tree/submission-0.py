# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Pre(p, q) -> p, q and binary trees
        Post(b) -> b iff p and q are the same trees

        Strategy:
        bfs through p, q at same time, while checking all nodes are the same in both
        """
        
        def bfs(root1, root2):
            if not root1 and not root2:
                return True
            
            if (root1 and not root2) or (not root1 and root2):
                return False
            
            right = bfs(root1.right, root2.right)
            # Propogate wrong answer up
            if not right:
                return False
            
            left = bfs(root1.left, root2.left)
            if not left:
                return False
            
            return root1.val == root2.val

        return bfs(p, q)



        

        