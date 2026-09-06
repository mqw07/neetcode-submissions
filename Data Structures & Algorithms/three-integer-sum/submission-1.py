class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()

        # Initialize Pointers
        for i in range(len(nums)):
            # Search each sub array starting at nums[i] for two-sum solution to nums[i]
            hi, lo = len(nums) - 1, i + 1
            if nums[i] not in visited:
                while hi > lo:
                    summ = nums[hi] + nums[lo] + nums[i]
                    if summ == 0:
                        entry = [nums[i], nums[lo], nums[hi]]
                        if entry not in res:
                            res.append([nums[i], nums[lo], nums[hi]])
                        lo += 1
                    elif summ < 0:
                        lo += 1
                    else:
                        hi -= 1     
            visited.add(nums[i])
        
        return res