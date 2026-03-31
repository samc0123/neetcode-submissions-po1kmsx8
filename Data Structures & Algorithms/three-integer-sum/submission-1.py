class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array 
        # Hold one pointer constant
        # Perform binary search on the rest of the array to see if result exists
        # Append terms to result 
        # Continue moving the first pointer 

        nums_sort = sorted(nums)
        res_array = []
        for l in range(len(nums_sort)):
            m = l+1
            r = len(nums_sort) - 1


            while m<r: # cannot use duplicate terms
                triplet_sum = nums_sort[l] + nums_sort[m] + nums_sort[r]
                if triplet_sum == 0: # add to result
                    solution_array = [nums_sort[l],nums_sort[m],nums_sort[r]]
                    if solution_array not in res_array:
                        res_array.append(solution_array)
                    # Move m up, r back to end to see if more combos exist
                    m += 1
                    r = len(nums_sort) - 1
                elif triplet_sum > 0: # too big, move right pointer left:
                    r-=1
                elif triplet_sum < 0: # too small, move middle pointer right:
                    m+=1
            
        return res_array
                
                
        