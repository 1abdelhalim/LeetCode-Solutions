class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        result = [float('inf')] * (n+1) 
        result[k] = 0 


        for i in range(n-1):
            for u, v, w in times:
                if result[u] != float('inf') and result[u] + w < result[v]:
                    result[v] = result[u] + w 


        max_time = max(result[1:])
        if max_time != float('inf'):
            return max_time 

        return -1 