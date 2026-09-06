class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Pre(nums): nums is List of integers that can be empty.
        Need to return n s.t. Post(n): n is the length of the longest consecutive sequence of elements

        At every iteration, n must represent the length of longest consecutive in nums[:i]
        Utilize hash map to help track values 

        We have the set of starting numbers to iterate through,
        we need to search through the set for the next number within numset.
        If this value does not exist, go onto the next. Otherwise, iterate through.

        Because of our subset construction for starts, we will never run into another
        starting value.
        """
        if not nums:
            return 0
            
        numset = set(nums)
        starts = {x for x in numset if x - 1 not in numset}

        seqlen = set()
        for start in starts:
            i = start
            while i + 1 in numset:
                i += 1
            seqlen.add(i - start + 1)

        return max(seqlen)


        