class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        """
        Need to determine if a permutation of s1 occurs as a 
        substring in s2 (Freq Counter)

        Pre(s1, s2) -> s1, s2 are strings that only contain lowercase letters,
        1 <= len(s1), len(s2) <= 10000
        
        Return b in B s.t. Post(b) -> b iff s1 occurs as a permutation in s2
        """
        
        # s1 & it's permutations cannot be a ss if it is larger than s2
        if len(s1) > len(s2):
            return False
        
        count_s1 = Counter(s1)

        # We can iterate through s2 with window of fixed size of len(s1):
        l = 0
        for r in range(len(s1), len(s2) + 1):
            curr_counts = Counter(s2[l: r])
            if curr_counts == count_s1:
                return True
            l += 1

        return False


        
        
