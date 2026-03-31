class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = 0 
        for i in range(len(nums) - 1):
            j = i+1
            while j < len(nums):
                val = nums[i] + nums[j]
                if val == target:
                    return [i,j]
                j += 1
            