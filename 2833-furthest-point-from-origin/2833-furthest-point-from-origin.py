class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r_values = 0 
        l_values = 0 
        n = len(moves)

        for i in range(n):
            if moves[i] == '_':
                r_values += 1 
                l_values += 1 
            elif moves[i] == "R":
                r_values += 1 
                l_values -= 1 
            else:
                l_values += 1 
                r_values -= 1
                
        return max(r_values, l_values)