class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        args
            grid: a 2D grid where 1 represents land, 0 represents water
        
        return 
            n s.t. n is the number of islands on the 2D grid

        Strategy:
        - iterate through the grid, if we encounter a '1', we perform BFS 
          and add every position of a '1' into a seen set.
        - once our bfs ends, we iterate through the grid again, and
          start a bfs at any '1' not in seen.
        - keep track of # of islands as we iterate through.
        """
        from collections import deque

        num_islands = 0
        queue = deque()

        num_rows = len(grid)
        num_cols = len(grid[0])

        adj = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        seen = set()

        for rn, row in enumerate(grid):
            for cn in range(len(row)):
                if ((rn, cn) not in seen and row[cn] == '1'):
                    num_islands += 1
                    # BFS
                    queue.append((rn, cn))
                    seen.add((rn, cn))

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in adj:
                            if (0 <= r + dr < num_rows and
                                0 <= c + dc < num_cols and
                                (r + dr, c + dc) not in seen and 
                                grid[r + dr][c + dc]) == '1':
                                    seen.add((r + dr, c + dc))
                                    queue.append((r + dr, c + dc))

        return num_islands
        