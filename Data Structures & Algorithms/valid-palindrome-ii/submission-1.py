class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Pre(s) -> s is alphanumeric string s.t. 0 < len(s) < 100,000
        We need to return bool b s.t. Post(b) -> b iff s' is a palindrome string
        after removing at most one character from s.

        Strategy;
        Two pointer approach, check if left and right pointers are the same.
        If not, have one skip. Check if left skip results in a valid palindrome, and if 
        right skip results in valid palindrome. If not, return False.
        """

        def check_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        skip = True

        while l < r:
            if s[l] != s[r]:
                if skip:
                    skip = False
                    return any((check_palindrome(l + 1, r), check_palindrome(l, r - 1)))
                return False
            l += 1
            r -= 1
        return True