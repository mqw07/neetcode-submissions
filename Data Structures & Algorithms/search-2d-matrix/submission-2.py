class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Args:
        - matrix, which is a m x n integer array where m and n are not 0. 
        - target, which is an integer.

        Return:
        - b s.t. b iff target is within matrix.

        Strategy:
        - 2d binary search
        - if our target is sandwiched between 2 extremes within a row, we search that row. 
        - Otherwise, we move onto the next row.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target and matrix[i][n - 1] >= target:
                hi, lo = n - 1, 0
                mid = (hi + lo) // 2
                while hi >= lo:
                    if matrix[i][mid] == target:
                        return True
                    if target > matrix[i][mid]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                    mid = (hi + lo) // 2
                return False
        return False

        