class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Args:
            - piles, a non-empty array of naturals > 0
            - h, an int s.t. len(piles) <= h
        Returns:
            - k s.t. k is the minimum integer such that you can eat ALL
              bananas within h hours
        
        Strategy:
            - Define a binary search for the rate from 0 - max(piles)
            - Define a helper function to calculate the time 
            - Return the minimum value s.t. koko eats all the bananas in time.
        """
        import math
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        def valid_rate(rate, h, piles) -> bool:
            # Need to ensure that eating at rate/h bananas completes 
            # the number of bananas

            for pile in piles:
                h -= math.ceil(pile / rate)
            if h < 0:
                return False
            return True
        
        hi, lo = max(piles), 1
        min_so_far = hi

        while hi >= lo:
            mid = (hi + lo) // 2
            if valid_rate(mid, h, piles):
                min_so_far = min(min_so_far, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return min_so_far

                


        