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

        max_area = 0
        seen = set()
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        nrow, ncol = len(grid), len(grid[0])

        def dfs(cords: tuple) -> int:
            r, c = cords
            if not (
                0 <= r < nrow and 
                0 <= c < ncol and
                (r, c) not in seen and
                grid[r][c] == 1
            ):
                return 0
            
            seen.add((r, c))
            summ = 1
            for dr, dc in neighbors:
                summ += dfs((r + dr, c + dc))
            
            return summ

        for rn, row in enumerate(grid):
            for cn in range(len(row)):
                # DFS 
                if row[cn] == 1 and (rn, cn) not in seen:
                    # New candidate for island area
                    max_area = max(max_area, dfs((rn, cn)))
        
        return max_area