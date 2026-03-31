class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sort the array 
        sort_nums = sorted(nums)
        
        # Holders for sequence length 
        longest_seq = []
        longest_len = 0
        if len(sort_nums) > 0:
            longest_seq.append(sort_nums.pop())
            longest_len = len(longest_seq)
        else:
            return longest_len # length of array is 0 
        # While numbers in array, continue popping
        while len(sort_nums) > 0:
            current_term = sort_nums.pop()
            previous_term = longest_seq[len(longest_seq)-1] # Last appended term
            if abs(current_term - previous_term) <=1 and current_term not in longest_seq:
                longest_seq.append(current_term)
            elif abs(current_term - previous_term) >1:
                longest_seq = [current_term]
            if len(longest_seq) > longest_len:
                longest_len = len(longest_seq)
            print(f"Sequnece is {longest_seq}")
            print(f"Length is {longest_len}")
        
        # Return the longest sequence value 
        return longest_len



