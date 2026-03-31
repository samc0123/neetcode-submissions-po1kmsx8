class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array 
        nums_sorted = sorted(nums)
        l,r = 0, len(nums_sorted) - 1
        results = []


        while nums_sorted[l] <=0  and l < len(nums_sorted) - 2:
            r = len(nums) - 1
            while nums_sorted[r] >= 0 and r > l:
                i = l + 1
                while i < r:
                    print(l,i,r)
                    print(nums_sorted[l],nums_sorted[i],nums_sorted[r])
                    cur_sum = nums_sorted[l] + nums_sorted[i] + nums_sorted[r]
                    if cur_sum == 0 and [nums_sorted[l],nums_sorted[i], nums_sorted[r]] not in results:
                        results.append([nums_sorted[l],nums_sorted[i], nums_sorted[r]])
                    i += 1
                r -= 1
            print(f"l is {l}")
            l += 1
        
        return results
