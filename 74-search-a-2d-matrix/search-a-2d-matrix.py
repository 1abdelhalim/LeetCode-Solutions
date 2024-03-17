class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n, m = len(matrix), len(matrix[0])
        low = 0 
        high = n * m - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_row = mid // m
            mid_col = mid % m
            mid_val = matrix[mid_row][mid_col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
