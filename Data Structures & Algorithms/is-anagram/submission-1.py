class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Same characters
        s_dict = {}
        t_dict = {}
        if len(s) == len(t):
            for i in range(len(s)):
                s_dict[s[i]] = s.count(s[i])
                t_dict[t[i]] = t.count(t[i])
        else:
            return False
        return s_dict == t_dict

        
        