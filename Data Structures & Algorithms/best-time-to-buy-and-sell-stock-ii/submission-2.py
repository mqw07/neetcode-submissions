class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Pre(prices) -> prices is a non-empty list of integers (prices)
        for all price in prices, 0 <= price <= 10,000

        Need to return natural number n s.t. Post(n) -> n is the max profit
        achievable by buying and selling stock over the course of prices, 
        where you can only hold one share of a stock at a time.

        Strategy: (Greedy)
        - Initialize a min_so_far value. Use this to help calculate profit.
        - At any point where you can sell for profit, sell.
        - Make this new value the new min_so_far. Repeat.

        """
        profit_so_far = 0
        min_so_far = prices[0]

        for price in prices:
            if price < min_so_far:
                min_so_far = price
            else:
                profit_so_far += price - min_so_far
                min_so_far = price
        
        return profit_so_far