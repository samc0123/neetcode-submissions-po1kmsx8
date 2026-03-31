class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Enumerate the list to get the index and value 
        seen_nums = {}
        for i,n in enumerate(nums):
            # Check if the val exists in the seen_nums, otherwise create and assign index
            if seen_nums.get(n) is not None:
                return True
            else:
                seen_nums[n] = i
                print(seen_nums)
        return False
    
