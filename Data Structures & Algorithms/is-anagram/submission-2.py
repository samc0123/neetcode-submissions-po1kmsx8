class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map_s, char_map_t = {}, {}

        for i in range(len(s)):
            char_map_s[s[i]] = char_map_s.get(s[i], 0) + 1 
            char_map_t[t[i]] = char_map_t.get(t[i], 0) + 1
        return char_map_s == char_map_t
