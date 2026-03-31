class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_mult = 1
        total_mult_nonzero = 1
        for i in nums:
            if i == 0:
                total_mult_nonzero = total_mult
            else:
                total_mult_nonzero *= i
            total_mult *= i
    
        result = [0 * n for n in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = total_mult_nonzero
            else:
                result[i] = int(total_mult/nums[i])
    
        return result