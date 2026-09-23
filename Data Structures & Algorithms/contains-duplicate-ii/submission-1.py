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
        from collections import Counter

        l, r = 0, min(k + 1, len(nums))
        counts = Counter(nums[:r])

        if any(count != 1 for count in counts.values()):
            return True
        
        while r <= len(nums):
            if any(x == 2 for x in counts.values()):
                return True 
            l += 1
            r += 1
            counts = Counter(nums[l:r])
        return False

        