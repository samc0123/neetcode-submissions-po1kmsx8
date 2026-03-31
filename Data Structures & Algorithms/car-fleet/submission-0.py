class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = list(zip(position,speed))
        
        fleets = 0
        prev_time_to_target = float('-inf')

        cars_sort_desc = sorted(pos_spd,reverse=True) # (pos,spd) pairs
        
        for car in cars_sort_desc:
            # Get the time for the current car
            time_to_target = (target - car[0]) / car[1]

            if time_to_target > prev_time_to_target:
                fleets+=1
                prev_time_to_target = time_to_target
        return fleets
            
        

