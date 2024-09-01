class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuples = []
        n = len(names)

        for i in range(n):
            tuples.append((names[i], heights[i]))

        tuples = sorted(tuples, key=lambda x:x[1], reverse=True)
    
        sorted_names = [name for name, height in tuples]
        return sorted_names