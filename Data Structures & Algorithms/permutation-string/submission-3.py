class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hashmaps and sliding window best approach 
        # Window size would be equal to s1 since that is what's being checked 

        # Hash s1 as the basis hashmap 
        s1_map = {}
        for char_s1 in s1:
            char_s1_count = s1_map.get(char_s1,0)
            s1_map[char_s1] = char_s1_count + 1
        
        # Define the initial window size 
        l,r = 0,len(s1)

        # Iterate over s2 
        while r <=len(s2):
            # Get the current window string 
            s2_sub = s2[l:r]

            # Hash the current window string 
            s2_map = {}
            for char_s2 in s2_sub:
                char_s2_count = s2_map.get(char_s2,0)
                s2_map[char_s2] = char_s2_count + 1 
            
            # Compare equality of the maps 
            if s1_map == s2_map:
                return True
            
            # Move l and r over 1 unit to see if next substring matches 
            l += 1
            r += 1
        # Reach end of string and no matches found, return false
        return False