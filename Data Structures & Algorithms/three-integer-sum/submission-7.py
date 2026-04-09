class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        nums = sorted(nums)
        res_set = set()

        while l < len(nums) - 2: 
            target = -nums[l]

            j = l + 1 
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    res_tup = (nums[l], nums[j], nums[k])
                    if res_tup not in res_set:
                        res_set.add(res_tup)
                    # Increment left pointer to continue searching 
                    j += 1
                elif nums[j] + nums[k] < target:
                    # Less than, so left val is too big 
                    j += 1 
                else: 
                    k -=1 
            l += 1
        return [list(triplet) for triplet in res_set]


        
                   