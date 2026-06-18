class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Dictionary approach:
        - Map each character in s and t to their # of occurances, check if dictionary matches.
        """

        from collections import defaultdict

        s_char_count = defaultdict(int)
        t_char_count = defaultdict(int)

        for c1 in s:
            s_char_count[c1] += 1
        
        for c2 in t:
            t_char_count[c2] += 1
        
        return s_char_count == t_char_count

        