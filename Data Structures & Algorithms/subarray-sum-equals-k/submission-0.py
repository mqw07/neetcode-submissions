class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        @param nums is a list of integers, which is non-empty
        @param k an integer

        @return n s.t. there are n subarrays within nums that sum to k

        Strategies:
            - Brute force
                - Searchign everyu possible subarray and coutning when it's sum is k
                - O(n^3) Time complexity (not good)

            - Create a prefix sum array, construct possible subarrays from there
            [2, -1, 1, 2], Prefix: [0, 2, 1, 2, 4], k = 2
            - Find the current prefix sum, and count the amount of previous sums that = current - k
            O(n)
        """

        # Construct our prefix sum
        from collections import defaultdict

        res = 0
        prev_sums = defaultdict(int)
        prefix_sum = [0]

        for num in nums:
            prev_sums[prefix_sum[-1]] += 1
            prefix_sum.append(prefix_sum[-1] + num)
            res += prev_sums.get(prefix_sum[-1] - k, 0)
        
        return res