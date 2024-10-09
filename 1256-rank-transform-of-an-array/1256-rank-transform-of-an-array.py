class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        
        rank_map = {val: i + 1 for i, val in enumerate(sorted_arr)}
        
        return [rank_map[num] for num in arr]
