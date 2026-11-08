class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Check if list is empty

        Iterate throughnums, keepign trtack of a coutner variable for the # of tuimes we encounter val

        When value is seen, we can delete value in place.

        Return the counter
        """
        index = 0
        leng = len(nums)
        while index < leng:
            if nums[index] == val:
                nums.remove(val)
                leng -= 1
            else:
                index += 1
                        
        return len(nums)