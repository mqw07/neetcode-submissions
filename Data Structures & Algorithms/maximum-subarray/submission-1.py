class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        sliding window:

        maxx = 0
        curr = 0
        l, r = 0, 1
        while r < len(nums):
            
            if our current sum is smaller than zero, we can slide left
            
            otherwise, slide right
        
        return maxx
        """
        
        maxx = nums[0]
        curr = nums[0]
        l, r = 0, 1

        while r < len(nums):
            assert r >= 1
            if curr < 0:
                curr = 0
            curr += nums[r]
            maxx = max(maxx, curr)
            r += 1
            
        return maxx