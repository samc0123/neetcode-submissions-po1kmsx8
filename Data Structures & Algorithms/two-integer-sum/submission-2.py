class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # Assumption that every list can have a value that sums to target
       # Aiming for O(n), so brute force is eliminated bc it needs 2 pointers

    
        # Equation rearrangement 
        # Say target - nums[i] = nums[j]
        # Need to check the existence of the value in the array (O(1))
        # If no, then move i. If yes, return the sorted version of [i,j]

        for i in range(len(nums)):
            target_val = target - nums[i]
            try:
                j = nums.index(target_val,i+1)
                break
            except ValueError:
                continue 
        return ([i,j] if i<j else [j,i]) 