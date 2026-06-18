class Solution:
    """
    Strategy: use a dict mapping counts of each letter in alphabet to each word in final output
    """
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def str_to_count(string) -> tuple:
            str_count = [0] * 26
            for index, c in enumerate(string):
                str_count[ord(c) - ord('a')] += 1
            return tuple(str_count)
        
        counts_to_words = defaultdict(list)
        for string in strs:
            count = str_to_count(string)
            counts_to_words[count].append(string)

        return [counts_to_words[x] for x in counts_to_words]

            
        




        