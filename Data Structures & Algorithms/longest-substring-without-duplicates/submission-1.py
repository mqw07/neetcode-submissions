class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in {0, 1}:
            return len(s)
        
        l, r = 0, 1
        curr_max = 1
        while r <= len(s):
            # Loop invariant: l <= r
            substring = s[l:r]
            if len(substring) > len(set(substring)):
                l += 1
            else:
                curr_len = r - l
                curr_max = max(curr_len, curr_max)
                r += 1
        return curr_max


        