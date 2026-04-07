class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sorted in ascending order 
        # Cannot use the same index 

        """
        Intuition: 
        1. Initialize left pointer at 0 and right pointer at len - 1
        2. If the sum is too big , then decrement the right pointer 
        3. If the sum is too small, increment the left pointer 
        4. Since there is a valid solution
        """

        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum < target:
                # Too small case, increment left 
                l += 1 
            elif cur_sum > target:
                # Too big case, decrement right 
                r -= 1
            else:
                return [l+1, r+1]
        