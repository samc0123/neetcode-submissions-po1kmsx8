class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        l = 0 # left window pointer
        r = 0 # right window pointer

        res = 0 # max sequence length 

        for r in range(len(s)):
            # Remove characters from the set while they are duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1 # Keep shrinking window from the left 
            charSet.add(s[r])
            r+=1 
            print(f"Iteration {r}: {charSet})")
            res = max(res,len(charSet))
        
        return res