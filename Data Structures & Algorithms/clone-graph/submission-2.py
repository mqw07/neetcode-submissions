"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        from collections import deque
        queue = deque([node])

        res = Node(node.val)
        seen = {node: res}

        # Within BFS, we need to connect res with traversed neighbors
        while queue:
            curr = queue.popleft()
            copy = seen[curr]

            for neighbor in curr.neighbors:
                if neighbor not in seen:
                    new_node = Node(neighbor.val)
                    queue.append(neighbor)
                    seen[neighbor] = new_node

                # In the case that we already seen the neighbor (already created the copy)
                # We now link the copy to it's clone
                copy.neighbors.append(seen[neighbor])

        return res