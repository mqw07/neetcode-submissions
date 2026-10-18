class Solution:
    """
    Encode:
        Given list of strings, need to return a encoded strign

    Decode:
        Given a single encoding string, need to return the original

    Strategy:
        Encode
            - Iterate through each string in strs
                - add length of each word, followed by word into encoded string 

            - Put the length of each string before the string itself, in the encoded result
        Decode
            - We know how many further characters we need to take from the encoded string per word
                - Iterate through the encoded string, parse out the initial number of characters from the string
        
        5x4ght

    """

    def encode(self, strs: list[str]) -> str:
        encoded = ''
        for word in strs:
            leng = len(word)
            encoded += (str(leng) + '#' + word)

        return encoded
    
    def decode(self, encoded: str) -> list[str]:
        # Look through the encoded string, until we find the #.
        # Store the characters have before we reach it. This becomes our length.
        decoded = []

        index = 0
        curr_leng = 0

        leng_string = ''
        while index < len(encoded):
            char = encoded[index] 
            if char != '#':
                leng_string += char
                index += 1
            else:
            
                curr_leng = int(leng_string)
                index += 1

                leng_string = ''

                word = encoded[index: index + curr_leng]
                decoded.append(word)
                index += curr_leng
                curr_leng = 0
                
        return decoded


 