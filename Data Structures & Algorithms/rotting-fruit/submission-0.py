class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """"
        We need to determine the minimum # of mins before all fruits rot 

        Args
            grid, a 2x2 matrix where each tile represents a emptycell, fresh or rotting fruits, 0, 1, 2.
            grid is guarenteed to be nonempty. (more than 1 rows and more than 1 columns)
        
        Return
            N s.t. n represents the minimum # of minutes that elapse before all fruits
            rot

        Strategy:
            - for every elapsed minute, all fruits directly adjacent to rotting ones 
            will become rotten

            Find location of all rotting fruits, perform BFS, count the number of 
            minutes elapsed per BFS cycle

            To determine completeness, compare our grid with desired grid 
            (All oranges are rotted). If we traverse all without reaching this state,
            return -1
        """
        # Find grid locations of all rotted fruits
            # add these locations to the queue
        
        # Perform BFS on these locations
        # While Queue is nonempty, valid neighbors exist
            # Count the minutes elapsed 
        
            # When there are no valid neighbors, we can compare our grid
            # to the target grid, if match, return minutes, if not, return -1
        
        from collections import deque
        queue = deque()
        neighbors = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        seen = set()

        minutes = 0

        for rn, row in enumerate(grid):
            for cn, tile in enumerate(row):
                if tile == 2:
                    queue.append((rn, cn, 0))
                    seen.add((rn, cn))
        
        mins = 0

        while queue:
            r, c, depth = queue.popleft()
            mins = max(mins, depth)
            grid[r][c] = 2

            for dr, dc in neighbors:
                newr, newc = r + dr, c + dc
                if (
                    0 <= newr < len(grid) and
                    0 <= newc < len(grid[0]) and    
                    (newr, newc) not in seen and
                    grid[newr][newc] == 1
                ):
                    queue.append((newr, newc, depth + 1))
                    seen.add((newr, newc))

        for row in grid:
            for tile in row:
                if tile == 1:
                    return -1

        return mins
        