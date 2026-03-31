class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Self Implement the Counter class

        # We know max occurrences of the sequence can only be of length k, so 
        # initialize an array of that length 
        # We also need an empty array to store the actual elements that occur
        # i number of times 

        # The index tells us the number of occurrences 
        occurrences = [[] for i in range(len(nums)+1)]
        
        # Now we need to be able to count each elements occurrences 
        # Use a hashmap 
        count_map = {}

        for val in nums:
            element = count_map.get(val,0)
            count_map[val] = element + 1
        
        # Now we have the occurrences of each, reassign to array to get the 
        # list of occurrences by index 

        for element_val,element_occ in count_map.items():
            # v is no occurrences, k is the element 
            occurrences[element_occ].append(element_val)
        print(count_map)
        # Pop from the backend of occurrences until you get an array length 
        # > 0 k times, and append the value to return array 
        final_return_array = []
        for j in range(len(occurrences)-1,-1,-1):
            print(j)
            for term_to_return in occurrences[j]:
                print(term_to_return)
                if len(final_return_array) < k:
                    final_return_array.append(term_to_return)
        return final_return_array