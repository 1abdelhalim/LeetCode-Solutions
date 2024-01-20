class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0 
        current = 0 
        start = 0 
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff 
            current += diff

            if current < 0:
                start = i+1
                current = 0 
        
        if tank >= 0:
            return start 
        else:
            return -1 