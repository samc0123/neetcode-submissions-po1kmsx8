class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Need to define arbitrary pivot and compare left and right pointers 

        # Two conditions 
        # Condition 1: if mid < right element, eliminate the right half
        # Condition 2: if mid > right element, eliminate the left half and the mid 

        l,r = 0, len(nums) - 1
        

        while l <= r:
            mid = int((l+r)/2)

            temp = nums[mid]

            if l == r:
                break 

            # Condition 1:
            if temp < nums[r]:
                r = mid 
            # Condition 2 
            elif temp > nums[r]:
                l = mid + 1

        return nums[l]
            
            

        