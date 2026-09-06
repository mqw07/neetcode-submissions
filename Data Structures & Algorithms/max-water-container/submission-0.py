class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Need to find the largest area (height * length)
        # Initialize two pointer with length = r - l
        # Store location of current max in tuple (l, r, a) a = (r - l) * min(heights[l], heights[r])
        # Extend right if

        def area(l, r) -> int:
            return (r - l) * min(heights[r], heights[l])

        l, r = 0, len(heights) - 1
        amax = area(l, r)
        
        while l < r:
            """ Loop Invarients: 
                0 <= l < r < len(heights)
                
            """
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            amax = max(area(l, r), amax)
        return amax
