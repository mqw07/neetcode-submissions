class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        curr_min = prices[1]
        profit_so_far = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] <= curr_min:
                curr_min = prices[l]
                
            curr_profit = prices[r] - curr_min

            if curr_profit > profit_so_far:
                profit_so_far = curr_profit
            l += 1
            r += 1
            
        return profit_so_far

        