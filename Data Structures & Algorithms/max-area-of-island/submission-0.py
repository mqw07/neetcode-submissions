class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        args
            grid: a 2D matrix representing position of either land or water 1, 0
            respectively
                - let n, m = # rows, # columns, 1 <= n, m <= 50
            
        return
            n s.t. n is the maximum area of all islands in grid

        strategy:
        - iterate through grid, bfs on each iteration
        - keep a variable tracking the maximum island area at every iteration
        - if the current tile is a '1', check eligibility and scan for max_area
        """
        from collections import deque

        max_area = 0
        seen = set()
        queue = deque()
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        nrow, ncol = len(grid), len(grid[0])

        for rn, row in enumerate(grid):
            for cn in range(len(row)):
                
                # BFS 
                if row[cn] == 1 and (rn, cn) not in seen:
                    # New candidate for island area
                    curr_area = 1
                    queue.append((rn, cn))
                    seen.add((rn, cn))

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in neighbors:
                            nr, nc = r + dr, c + dc

                            if (0 <= nr < nrow and
                                0 <= nc < ncol and
                                (nr, nc) not in seen and
                                grid[nr][nc] == 1
                            ):
                                queue.append((nr, nc))
                                curr_area += 1
                                seen.add((nr, nc))
                    
                    max_area = max(max_area, curr_area)
        
        return max_area