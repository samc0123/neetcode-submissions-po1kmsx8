class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = i+1

        for i in range(len(numbers)):
            for j in range(i+1,len(numbers),1):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
            