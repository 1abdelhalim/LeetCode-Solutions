class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i, j, k = 0, 1, 2 
        n = len(arr)
        if n < 3:
            return False

        def is_odd(num):
            return num % 2 == 1

        while i < n -2  and j < n - 1 and k < n:
            if is_odd(arr[i]) and is_odd(arr[j]) and is_odd(arr[k]):
                return True 
            i += 1 
            j += 1
            k += 1

        return False 