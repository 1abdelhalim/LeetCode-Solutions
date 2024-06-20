class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def canPlaceBalls(min_force: int) -> bool:
            count = 1
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if canPlaceBalls(mid):
                left = mid
            else:
                right = mid - 1
                
        return left

