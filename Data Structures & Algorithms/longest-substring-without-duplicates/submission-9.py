class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Case of no length 
        if len(s) == 0:
            return 0 

        # Longest string has to be at least 1 char
        longest_str = 1 
        l,r = 0,1

        while r <= len(s):
            # Get set of current window 
            window_set = set(s[l:r])

            # Compare set length against window length 
            # If set is shorter, means duplicate in the window
            if len(window_set) < r-l:
                # Shrink from the left to remove the dup 
                l += 1 
            else:
                # Check if the longest_str needs to be updated
                longest_str = len(window_set) if len(window_set) > longest_str else longest_str
                # Increase window size 
                r += 1        
        return longest_str