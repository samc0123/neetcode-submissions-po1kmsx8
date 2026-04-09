class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        nums = sorted(nums)
        res = []

        while l < len(nums) - 2: 
            target = -nums[l]

            j = l + 1 
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == target and [nums[l], nums[j], nums[k]] not in res:
                    res.append([nums[l], nums[j], nums[k]])
                elif nums[j] + nums[k] < target:
                    # Less than, so left val is too big 
                    j += 1 
                else: 
                    k -=1 
            l += 1
        return res


        
                   