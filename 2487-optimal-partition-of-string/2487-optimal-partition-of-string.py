class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        
        min_substrs = 1 
        chars_set = set()
        
        for ch in s:
            if ch in chars_set:
                min_substrs += 1 
                chars_set.clear()

            
            chars_set.add(ch)

        return min_substrs 