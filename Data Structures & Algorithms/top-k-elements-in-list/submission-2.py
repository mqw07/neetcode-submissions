class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Counter(nums)

        res = []
        iterate through Counter
            repeatably choose the choose the next most frequent element
            append the element that is cooresponding to max_count that to our result list
            remove the max element

        return list of most freq
        """
        
        from collections import Counter
        counts = Counter(nums)
        res = []
        for i in range(k):
            max_count = max(counts.values())
            for num in counts:
                if counts[num] == max_count:
                    res.append(num)
                    del(counts[num])
                    break            
        return res



        



        