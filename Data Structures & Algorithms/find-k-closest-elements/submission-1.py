class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Find the k closest elements in arr to x
        Args:
            arr: a non-empty sorted list of integers
            k: a positive integer
            x: an integer
        
        Returns:
            lst s.t. lst is the list of elements that are k closest to x in arr.

        Strategy:
            - First, find the two indicies with elements that surround x
            - If it is smaller or larger than all elements in the array, take the first/last k elements of the array
            - otherwise, keep popping the closest element out of arr, to construct res.
        """
        index_above = 0

        def closer_index(e1, e2):
            if abs(arr[e1] - x) < abs(arr[e2] - x):
                return e1
            elif abs(arr[e1] - x) == abs(arr[e2] - x):
                return min(e1, e2)
            return e2

        while arr[index_above] < x:
            index_above += 1
            if index_above == len(arr):
                return arr[len(arr) - k:] 
        
        # index_below should give us the index just above x or x: arr[index_below - 1] < x < arr[index_below]
        if index_above == 0:
            return arr[:k]
            
        start = closer_index(index_above, index_above - 1)
        l, r = start, start + 1

        while r - l < k:
            if r == len(arr):
                l -= 1
            elif l == 0:
                r += 1
            else:
                closer = closer_index(r, l - 1)
                if closer == r:
                    r += 1
                else:
                    l -= 1
        return arr[l: r]        

