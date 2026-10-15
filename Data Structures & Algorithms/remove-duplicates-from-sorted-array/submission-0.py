class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Keep track of first instance of unique value
        # Remove future duplicates if they match the value above
        i = 1
        prev_unique = nums[0]
        while i < len(nums):
            if nums[i] != prev_unique:
                prev_unique = nums[i]
                i += 1
            else:
                # The current element = the previous unique element
                nums.remove(nums[i])
        return i
        