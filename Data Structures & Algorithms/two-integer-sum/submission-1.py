class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Defaultdict approach -> store target - value as key to the value index.
        """

        from collections import defaultdict
        diff_to_index = defaultdict(int)

        for index, num in enumerate(nums): 
            diff = target - num
            
            if num in diff_to_index:
                return [diff_to_index[num], index]
            
            else:
                diff_to_index[diff] = index
        
        return [-1]
        