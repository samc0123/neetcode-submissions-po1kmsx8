class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Pointers 
        l = 0
        r = len(numbers) - 1

        res = numbers[l]+numbers[r]

        while res != target:
            if res < target:
                l+=1
            elif res > target:
                r-=1
            res = numbers[l] + numbers[r]
        
        return [l+1,r+1]
            