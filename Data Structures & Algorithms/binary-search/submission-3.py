class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1 
        while l<=r:
            m = int((l+r) / 2)
            mid_val = nums[m]
            
            if target < mid_val:
                # Target too small, need to search left side 
                r = m - 1
            elif target > mid_val:
                # Target too big, search right side for bigger val
                l = m+1
            else:
                return m 
        return -1 
    
    
    