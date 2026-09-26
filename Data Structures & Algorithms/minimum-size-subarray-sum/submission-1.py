class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        @params target is a positive integer, nums is a list of positive integers
        @return the minimal length of subarray with sum greater than or qual to target.
        If this does not exist, return 0.

        Strategy 1 O(n): Sliding Window
            - Upon first look, expand window right until our total sum >= target
            - At this point, we should contract left until we reach a sum < target
            - Repeat, store the min length.
        """
        import math

        l, r = 0, 0
        min_len = math.inf
        total = 0

        while r < len(nums):
            if total < target:
                total += nums[r]
                r += 1
            else:
                min_len = min(min_len, r - l)
                total -= nums[l]
                l += 1
        
        while l < len(nums) and total >= target:
            min_len = min(min_len, r - l)
            total -= nums[l]
            l += 1

        if min_len == math.inf:
            return 0
        return min_len
        
