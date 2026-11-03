class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        args
            grid, m x n matrix where each tile contains one of the follwoing
                -1, (water cell) cannot be traversed
                0, Treasure chest 
                INF, land cell that can be traversed

                m, n cannot be 0.
        
        return None
            Modify grid s.t. all land cells now contain their distance to the nearest
            treasure chest

        Strategy:
            - BFS, find the closest treasure from each cell, record that distance
            - Store this distance in grid.  

        """
        from collections import deque

        seen = set()
        queue = deque()

        neighbors = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        rows, cols = len(grid), len(grid[0])

        for nr in range(rows):
            for nc in range(cols):
                if grid[nr][nc] == 0:
                    seen.add((nr, nc))

                    # each queue element stores row #, col #, and # of spaces it is from
                    # the closest target
                    queue.append((nr, nc, 0))
        
        # Do BFS on the Targets
        while queue:
            r, c, dt = queue.popleft()
            grid[r][c] = dt
            # Check candidacy of neighbors
            for neighbor in neighbors:
                dr, dc = neighbor
                if (
                    0 <= r + dr < rows and
                    0 <= c + dc < cols and
                    grid[r + dr][c + dc] not in {-1, 0} and
                    (r + dr, c + dc) not in seen
                ):
                    queue.append((r + dr, c + dc, dt + 1))
                    seen.add((r + dr, c + dc))

        
        