class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Args;
        - nums, a nonempty list of integers that is sorted, and rotated right
        - target, an integer that may or may not be in nums

        Return;
        - i, the index of target in nums, or -1 if target does not exist in nums

        Strategy:
        - declare hi, lo pointers
        - compare nums[mid] to nums[hi], if nums[hi] > nums[mid], this 
        portion of the array is sorted. (see if target falls in this range)
        - if nums[hi] < nums[mid], we can say that all numbers in this range
        either > nums[mid] or < nums[hi]
        """

        lo, hi = 0, len(nums) - 1
        while hi >= lo:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[hi] and nums[mid] > nums[lo]:
                # We know that left and right halves are sorted, therefore list is sorted.
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            elif nums[mid] > nums[hi]:
                # right half unsorted, left sorted
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            else:
                # right sorted, left unsorted
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1