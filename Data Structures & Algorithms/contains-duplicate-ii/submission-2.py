class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        @params nums is a list of numbers that is non-empty, k is an int s.t. 0 <= k
        @return bool b s.t. b iff there exists two distince indices i, j s.t. nums[i] == nums[j]
        AND i and j are at most k apart from one another.

        Strategy:
        Sliding window strategy 
        [1, 2, 3, 1], k = 3
        The witness above: i = 0, j = 3
        1. Initialize a window of size k + 1
        3 - 0 = 3 <= k = 3
        window = [1, 2, 3, 1]
        - Aprroach 1: Counter
        """
        l, r = 0, min(k + 1, len(nums))
        last_occurance = {}
        for i in range(r):
            if nums[i] not in last_occurance or i - last_occurance[nums[i]] > k:
                last_occurance[nums[i]] = i
            else:
                return True
        
        while r < len(nums):
            if nums[r] not in last_occurance or r - last_occurance[nums[r]] > k:
                last_occurance[nums[r]] = r
            else:
                return True
            l += 1
            r += 1
        return False

        