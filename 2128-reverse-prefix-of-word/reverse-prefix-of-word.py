class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = set(word)
        if ch not in s:
            return word
            
        i = word.index(ch)
    
        return (word[i::-1] + word[i+1: ])
        