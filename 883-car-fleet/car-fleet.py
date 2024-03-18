class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        prev_time= 0
        count = 0
        
        for pos, spd in cars:
            curr_time = (target - pos) / spd
            
            if curr_time > prev_time:
                prev_time = curr_time
                count += 1
                
        return count