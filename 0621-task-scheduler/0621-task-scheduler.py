from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        freq_values = list(freq.values())
        freq_values.sort()
        f_max = freq_values[-1]  
        
        idleTime = (f_max - 1) * n
        
        for i in range(len(freq_values) - 2, -1, -1):
            idleTime -= min(f_max - 1, freq_values[i])
        
        idleTime = max(0, idleTime)
        
        return len(tasks) + idleTime
