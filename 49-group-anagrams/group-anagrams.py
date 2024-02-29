class Solution:
    def groupAnagrams(self, strs):
        h_map = {}
        anagrams = []   
        for word in strs:
            sorted_w = "".join(sorted(word))
            if sorted_w not in h_map:
                h_map[sorted_w] = [word]
            else:
                 h_map[sorted_w].append(word)

        for val in h_map.values():
            anagrams.append(val)

        return anagrams    