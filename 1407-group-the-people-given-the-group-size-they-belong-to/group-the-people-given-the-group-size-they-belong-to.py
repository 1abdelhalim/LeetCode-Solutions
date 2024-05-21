class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        indices = {}
        n = len(groupSizes)
        
        for i in range(n):
            group_size = groupSizes[i]
            if group_size not in indices:
                indices[group_size] = []
            indices[group_size].append(i)
        
        ans = []
        
        for size, people in indices.items():
            for i in range(0, len(people), size):
                ans.append(people[i:i + size])

        return ans