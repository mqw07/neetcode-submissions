class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        - Two pointer approach
        [1,2,3,4] target = 3

        l, r = 0, len(nums) - 1
        


        while l != r:
            check if target = nums[l] + nums[r]
            - if that's the case, return nums[l, r]

            - otherwise, search for target - nums[l] in the array. 
            
        """
        def bsearch(need, nums) -> int:
            hi, lo = len(nums) - 1, 0

            while hi >= lo:
                mid = (hi + lo) // 2
                if nums[mid] == need:
                    return mid
                if nums[mid] > need:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1
        
        for i in range(len(numbers)):
            compliment = bsearch(target - numbers[i], numbers)
            if compliment != -1 and compliment != i:
                return([min(compliment, i) + 1, max(compliment, i) + 1])
        return []