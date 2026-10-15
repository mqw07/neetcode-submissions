class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Args 
        - nums, list of ints
        - target, int

        Return i, j s.t. i and j are integers that represent the indices
        which has elements that add up to target

        Strategy;
        Create a hash map

        initialize needed = dict()
        for index, num in enumerate(nums):
            need = target - num
            if need in nums:
                return [needed[need], index]
            else:
                needed[need] = index
        return []
        """
        needed = dict()
        for index, num in enumerate(nums):
            need = target - num
            if need in needed:
                return [needed[need], index]
            else:
                needed[num] = index
        return []

        