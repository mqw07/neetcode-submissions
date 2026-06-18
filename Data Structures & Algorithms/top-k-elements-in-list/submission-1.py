class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counts = Counter(nums)
        frequently = [[] for _ in range(len(nums) + 1)]

        for num in counts:
            frequently[counts[num]].append(num)
        
        res = []
        index = 1

        print(frequently)
        while len(res) < k:
            if frequently[-index] != []:
                res.extend(frequently[-index])
            index += 1
        return res



        



        