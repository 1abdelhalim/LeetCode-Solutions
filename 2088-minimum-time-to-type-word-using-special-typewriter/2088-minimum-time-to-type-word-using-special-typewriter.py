class Solution:
    def minTimeToType(self, word: str) -> int:
        start = "a"  
        result = 0  

        for ch in word:
            clockwise = abs(ord(ch) - ord(start))
            counterclockwise = 26 - clockwise
            
            result += min(clockwise, counterclockwise) + 1
            start = ch  
        
        return result
