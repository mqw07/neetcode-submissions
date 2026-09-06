class Solution:
    import math
    def maxProfit(self, prices: List[int]) -> int:
        """
        Pre(prices) -> Prices is a list with 1 <= len(prices) <= 100, where prices[i] represents
        the price of neetcoin on the i'th day.
        Need to return p s.t. Post(p) -> p is the max profit (difference) from selling neetcoin bought
        on a day before it. 

        Strategy: Two Pointers
        - Need to store max profit so far
        - Low Pointer: Need to store the lowest price seen so far
            
        Iterate through the list to find the max profit.
        """
        
        min_so_far = math.inf
        profit_so_far = 0

        for price in prices:
            min_so_far = min(min_so_far, price)
            profit_so_far = max(profit_so_far, price - min_so_far)
        
        return profit_so_far