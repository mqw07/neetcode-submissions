class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """ Strategy: Prefix product array and suffix product array
            where prefix measures accumulating products from either
            side of the array.
        """

        prefix_products = [nums[0]]
        suffix_products = [nums[-1]]
            # suffix product of nums[i] is recorded at suffix_products[-(i + 1)]
        for i in range(1, len(nums)):
            prefix_products.append(nums[i] * prefix_products[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            suffix_products.append(nums[i] * suffix_products[-1])
        
        res = [suffix_products[-2]]
        for i in range(1, len(nums) - 1):
            res.append(prefix_products[i - 1] * suffix_products[-(i + 2)])
        
        res.append(prefix_products[-2])
        
        return res

        
