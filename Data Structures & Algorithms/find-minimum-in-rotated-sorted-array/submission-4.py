class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Args:
        - nums, a sorted array rotated n units to the right

        Return:
        - Integer n s.t. n is the minimum of the array, with time complexity
        of O(log(n)).

        Strategy:
        - Binary search on a mid value, using the last element in the array
        to pivot around
        - If the last element is larger than our mid, we know that the portion 
        of the array from mid:hi is sorted.
        - Otherwise, we search the area between mid and hi to find the starting
        point of the sorted array.
        """

        hi, lo = len(nums) - 1, 0
        min_so_far = nums[lo]
        while hi >= lo:
            mid = (hi + lo) // 2
            min_so_far = min(min_so_far, nums[mid])
            if nums[mid] > nums[hi]:
                # The portion of the array from mid to high is NOT sorted
                hi, lo = hi, mid + 1
            else:
                hi, lo = mid - 1, lo
        return min_so_far         