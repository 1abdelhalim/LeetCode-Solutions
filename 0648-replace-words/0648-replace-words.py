class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len) # Sort to get the shortest root
        words = sentence.split() # get each word 
        n = len(words)

        for i in range(n):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root 
                    break 

        # now we have the words seprated 

        result = " ".join(words)

        return result 