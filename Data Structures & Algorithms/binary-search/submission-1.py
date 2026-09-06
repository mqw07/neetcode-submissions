class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Need to find a given number in a list using binary search

        lo, hi = 0, len(nums) - 1

        while hi >= lo:
            mid = lo + (hi - lo) // 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid
        
        return -1