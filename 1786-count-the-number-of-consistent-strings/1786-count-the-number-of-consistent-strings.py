class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count  = 0 
        chars = set()
        for ch in allowed:
            chars.add(ch)
       

        for word in words:
            if all(ch in chars for ch in word):
                count += 1 

        return count 

            
            