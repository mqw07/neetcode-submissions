class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Pre(nums) -> nums is nonempty, and nums contains any integer between -1m to 1m. 

        Need to return list res s.t. Post(res) -> every element in res occurs in n more than floor(n/3) times.

        Strategy:
        Determine threshold len(nums) // 3.
        Use a counter dict to determine the occurances of each integer.
        Return the counter translated to a list.
        """
        from collections import Counter        
        threshold = len(nums) // 3

        counts = Counter(nums)

        res = []
        for integer, occurances in counts.items():
            if occurances > threshold:
                res.append(integer)
        
        return res