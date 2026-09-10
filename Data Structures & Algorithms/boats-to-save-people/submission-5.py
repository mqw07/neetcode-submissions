class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = 0

        people.sort()
        l, r = 0, len(people) - 1

        curr_weight = 0
        while l <= r:
            
            # If the right pointer individually, takes up the exact weight of one boat
            # or will exceed it with the left weight, then the right weight must
            # take up one individual boat

            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            num_boats += 1

        return num_boats


        