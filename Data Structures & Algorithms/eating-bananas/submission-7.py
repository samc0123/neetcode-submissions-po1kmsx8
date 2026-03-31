class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        res = r # max possible rate
        

        while l<=r: 
            # Try to find a smaller rate 

            m = int((l+r)/2)
            rate = m
            time_eating = 0
            # Calculate the speed to eat 
            for pile in piles:
                time_eating += math.ceil(float(pile)/rate) #bananas/bananas/hour = hours
            
            if time_eating <= h:
                # This rate works, move the right pointer to see if theres a smaller one
                res = rate
                r = m - 1
            else:
                l = m + 1 
                # Ate too slow, move left pointer
        return res
    