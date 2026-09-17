class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Pre(board) -> board is a 9x9 Board

        Need to return bool b s.t. b iff board is a valid Sudoku board

        Strategy:
        - Search rows and columns first, return False if duplicate found (set)
        - Subdivide the problem onto each 3x3 board. (Large space complexity)
        """
        
        for i in range(len(board)):
            # Iterating over the rows
            colset = set()
            rowset = set()
            for j in range(len(board[i])):  
                # Iterating over elements in each row
                hori = board[i][j] 
                vert = board[j][i]
                if (hori != "." and hori in rowset) or (vert != "." and vert in colset):
                    print("part 1")
                    print(f"{i}, {j}")
                    return False
                rowset.add(hori)
                colset.add(vert)
        
        def search_grid(i1, j1):
            gridset = set()
            for i in range(3):
                for j in range(3):
                    if board[i + i1][j + j1] in gridset:
                        if board[i + i1][j + j1] != ".": 
                            print(f"part 2 {i1},{j1}")
                            return False
                    gridset.add(board[i + i1][j + j1])
            return True
        
        return all(search_grid(x, y) for (x, y) in 
                {
                    (0, 0), (0, 3), (0, 6),
                    (3, 0), (3, 3), (3, 6),
                    (6, 0), (6, 3), (6, 6)
                }
            )