class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Args:
        - x is a natural number

        Return
        - natural number n s.t. n = floor(sqrt(x))

        Strategy:
        - Binary search, keep halving our original until we get close to the
          desired nunber.
        - If we find that our halved number is smaller than the target, 
          add half  of that until we arrive at the correct number 
        - Roughlhy O(logn) time complecity
        """
        if x == 0:
            return 0

        left, right = 0, x # Left = 0, right = 13
        mid = (left + right) // 2 # Mid = 6
        while not(mid * mid <= x and (mid + 1) * (mid + 1) > x):
            # Iter 1: cand = 36, left = 0, right = 5, mid = 2
            # Iter 2; cand = 4, left = 3, right = 5, mid = 4
            # Iter 3: cand = 16, 
            cand = mid * mid
            # If our candidate is less than x, we need to add to mid
            if cand < x:
                left, right = mid + 1, right

            # Else, we need to have a smaller mid
            else:
                left, right = left, mid - 1

            mid = (left + right) // 2

        return mid