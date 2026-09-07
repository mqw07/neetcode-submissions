class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        Pre(arr, k, threshold) -> k is a list s.t. 1 <= k <= len(arr) <= 100,000
        k is a natural number greater or equal to 1. 
        threshold is a natural

        Return natural number number_of_subarrays s.t. Post(number_of_subarrays) -> there are number_of_subarrays subarrays within arr s.t. 
        each subarray has an average value greater than or equal to threshold.

        Approach:
        Sliding window -> initialize a window of size k, then slide the window forward, tracking
        the overall # of subarrays with the average over threshold.
        """

        number_of_subarrays = 0
        l = 0

        for r in range(k, len(arr) + 1):
            avg = (sum(arr[l: r]) / k)
            if avg >= threshold:
                number_of_subarrays += 1
            l += 1
        
        return number_of_subarrays


        