class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        """
        Need to return int l s.t. after replacing up to k characters in s, 
        l is the length of the longest string containing an identical character

        The length l of the subarray at any given time must be l <= count(c) + k, for the
        most occuring char c.
        """

        max_freq = 0
        l = 0
        res = 0
        count = Counter()

        for r in range(len(s)):
            # Count needs to count ALL chars in current window
            count[s[r]] += 1

            # max_freq updates to the only possible maximum values
            max_freq = max(max_freq, count[s[r]])

            while r - l + 1 > max_freq + k:

                # Update count s.t. the shrunk window is accounted for
                count[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)
        
        return res




        

