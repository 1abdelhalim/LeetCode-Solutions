class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        arr = [first]  
        
        for i in range(n):
            arr.append(arr[i] ^ encoded[i])

        return arr