class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        for i in range(n):
            if target == matrix[i][-1]:
                return True
            elif target < matrix[i][-1]:
                low = 0
                high = len(matrix[i]) - 1 
                while low <= high:  
                    mid = (low + high) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
        return False
