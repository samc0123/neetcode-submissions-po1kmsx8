class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## Checking if nums has a value that appears more than once
        # Hash to a set 
        nums_set = set(nums)
        # Compare length 
        if len(nums_set) == len(nums):
            return False
        else:
            return True