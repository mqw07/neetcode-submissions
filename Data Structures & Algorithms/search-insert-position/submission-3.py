class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Args:
            nums: sorted list of integers (nonempty)
            target: integer
        Returns:
            index s.t. index is where target appears, or would appear in logical order
        Strategy:
            Binary search, if not found, return mid + 1
        """
        hi, lo = len(nums) - 1, 0

        while hi >= lo:
            mid = (hi + lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                hi = mid - 1
            if nums[mid] < target:
                lo = mid + 1

        return lo



        