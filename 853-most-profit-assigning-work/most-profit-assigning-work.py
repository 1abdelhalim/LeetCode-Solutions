class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        i = 0 
        n = len(profit)
        max_profit, total = 0, 0

        for w in worker:
            while i < n and jobs[i][0] <= w:
                max_profit = max(max_profit, jobs[i][1])
                i += 1 

            total += max_profit 

        return total