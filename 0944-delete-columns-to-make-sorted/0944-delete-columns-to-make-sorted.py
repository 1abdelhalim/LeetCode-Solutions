class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        sorted_strs = [''.join(chars) for chars in zip(*strs)]

        count = 0 
        for string in sorted_strs:
            if string != ''.join(sorted(string)):
                count += 1 

        return count 

