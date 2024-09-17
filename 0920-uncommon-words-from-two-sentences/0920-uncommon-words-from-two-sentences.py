class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " "+ s2 
        counter = Counter(s.split())
        ans = []

        for key, val in counter.items():
            if val == 1:
                ans.append(key)


        return ans