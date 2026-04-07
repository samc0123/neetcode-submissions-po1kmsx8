class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Structure: key = value, value = index. 
        # Want to be able to search by key 
        val_dict = {}

        for i, v in enumerate(nums):
            # Check val_dict if target - value exists as key 
            if val_dict.get(target - v) is not None:
                # i will always be larger than whats in val_dict
                return [val_dict.get(target - v), i]
            val_dict[v] = i
        
        