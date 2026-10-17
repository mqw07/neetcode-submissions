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
        """

        """
        Instead of arranging num:occurance
                             occurance:num
        
        Use list up to n to use as our counts
        with each list index, have another list to store our values occuring index times

        iterate backwards through this list till we get k elements
        """
        from collections import Counter
        counts = Counter(nums)

        # {1: 1, 2: 2, 3: 3}
        res = []

        bucket = [[] for _ in range(len(nums) + 1)]
        # [[], [], [], [], []]
        for num in counts:
            bucket[counts[num]].append(num)
        
        # [[], [1], [2], [3], []]
        index = 1
        while index <= len(bucket) and k > 0:
            if bucket[-index] != []:
                for item in bucket[-index]:
                    res.append(item)
                    k -= 1
                    if k <= 0:
                        break
            index += 1
        return res



        



        