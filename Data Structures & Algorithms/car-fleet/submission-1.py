class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Comments here 

        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        Output: 3

        Need to ensure that every position is >= target for the problem to complete 
        Cars become a fleet when the positions are equal 
        Fleets will travel at the slower speed 


        '''
        stack = []

        for i in zip(position, speed):
            stack.append(i)
        
        # Sort by position 
        sort_stack = sorted(stack)
        
        # Get the time it takes for each car 
        time_stack = []
        while sort_stack:
            cur_car = sort_stack.pop(0)
            time_taken = (target-cur_car[0])/cur_car[1]
            print(f"Car eval {cur_car[0]}")
            print(time_taken)
        
                
            # If the current time is >= peeked time, then don't push. Else push 
            while len(time_stack) > 0 and time_taken >= time_stack[-1]:
                print(time_stack)
                time_stack.pop()
            
            time_stack.append(time_taken)
        return len(time_stack)