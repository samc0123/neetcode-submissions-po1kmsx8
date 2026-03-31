class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack_t_i = [] #(temp,i) tuples 

        for i,temp in enumerate(temperatures):
            while stack_t_i and temp > stack_t_i[-1][0]:
                past_temp, past_i = stack_t_i.pop()
                # (temp,i) comes out
                res[past_i] = i - past_i
            stack_t_i.append((temp,i))
        return res