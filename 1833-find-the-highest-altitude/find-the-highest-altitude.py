class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0 
        curr = 0
        for ch in gain:
            curr += ch
            ans = max(ans, curr)
    
        return ans