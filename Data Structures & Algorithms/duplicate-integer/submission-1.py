class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        initialize seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False