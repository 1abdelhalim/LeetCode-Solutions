class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_len = {}
        for root in dictionary:
            dict_len[root] = dict_len.get(root, 0) + len(root)
            
        sorted_dict_len = {k: v for k, v in sorted(dict_len.items(), key=lambda item: item[1])}

        words = sentence.split()
        for i in range(len(words)):
            for root in sorted_dict_len:
                if words[i].startswith(root):
                    words[i] = root
                    break  
        
        return ' '.join(words)
