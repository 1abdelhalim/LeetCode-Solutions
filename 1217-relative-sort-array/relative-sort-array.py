class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = {}
        n = len(arr1)
        result = [0] * n

        for num in arr1:
            counter[num] = counter.get(num, 0) + 1 

        i = 0
        for num in arr2:
            while counter[num] > 0:
                result[i] = num
                i += 1
                counter[num] -= 1 
            del counter[num]  
        remaining_elements = sorted(counter.keys())
        for num in remaining_elements:
            while counter[num] > 0:
                result[i] = num
                i += 1
                counter[num] -= 1 

        return result
