class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by first item 
        intervals.sort(key= lambda x:x[0])
        result = [intervals[0]]

        for i, j in intervals[1:]:
            end = result[-1][1]
            if i > end :
                result.append([i, j])

            else:
                result[-1][1] = max(end, j)

        return result 