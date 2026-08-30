class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        last_m = last_p = last_g = 0
        curr_dist = 0

        for i, house in enumerate(garbage):
            res += len(house)

            if "M" in house: 
                last_m = curr_dist
            if "P" in house: 
                last_p = curr_dist
            if "G" in house: 
                last_g = curr_dist

            if i < len(travel):
                curr_dist += travel[i]

        return res + last_m + last_p + last_g