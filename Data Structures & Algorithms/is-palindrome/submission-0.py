class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = [st.lower() for st in s if st.isalnum()]
        print(clean_text)
        for i in range(len(clean_text) // 2):
            if clean_text[i] != clean_text[-i - 1]:
                return False
        
        return True
        