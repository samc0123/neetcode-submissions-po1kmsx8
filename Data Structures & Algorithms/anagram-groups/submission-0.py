class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create a dict to retain the original order 
        strs_loc = {}
        for i, w in enumerate(strs):
            strs_loc[i] = w
        
        # Sort all strs
        sorted_strs = []
        for word in strs:
            
            sorted_strs.append("".join(sorted(word)))
        # Create keys for output dict 
        anagram_lists = {key: [] for key in set(sorted_strs)}

        # Iterate through sorted_strs, add the corresponding word to the key
        for j in range(len(sorted_strs)):
            anagram_lists[sorted_strs[j]].append(strs_loc[j])
        
        # Final list
        output = []
        for v in anagram_lists.values():
            output.append(v)
        return output