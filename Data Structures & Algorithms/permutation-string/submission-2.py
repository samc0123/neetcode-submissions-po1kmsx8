class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hashmap s1 for occurrence counts 
        hmap_s1 = {}
        for char in s1:
            hmap_s1[char] = hmap_s1.get(char,0) + 1
        
        l = 0 
        r = len(s1)   # start at s2 length, 0 index

        while r <= len(s2): # Iterate over entire s1 
            cur_perm = s2[l:r]

            # Form the hashmap of the cur_perm string
            hmap_cur_perm = {}
            for char_perm in cur_perm:
                hmap_cur_perm[char_perm] = hmap_cur_perm.get(char_perm,0) + 1 
            
            # Compare the hashmaps 
            if hmap_s1 == hmap_cur_perm:
                return True
            else: 
                # Continue to next window
                r += 1
                l += 1
            



        return False # No case where perm_set == s2_set, so false