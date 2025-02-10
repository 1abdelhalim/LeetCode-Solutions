class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        n = len(intervals)
        count = 0


        for i in range(1, n):
            if intervals[i][0] < end:
                count += 1 
                end = min(end, intervals[i][1])

            else:
                end = intervals[i][1]

        return count 
