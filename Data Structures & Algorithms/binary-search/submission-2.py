class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Pre(nums, target) -> Nums is a list of integers (distinct), and target is an integer 
        # Need to find a given number in a list using binary search
        # return i st post(i) -> i is the index where target belongs witin nums, otherwise i = -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        mid = len(nums) // 2
        if target >= nums[mid]:
            index = self.search(nums[mid:], target)
            if index == -1:
                return -1
            return mid + index
        
        else:
            index = self.search(nums[:mid], target)
            if index == -1:
                return -1
            return index
        