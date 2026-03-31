class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while len(stack) > 0 and stack[-1][1] < temp:
                index = stack.pop()[0]
                output[index] = i - index
            stack.append((i,temp))
        return output
        