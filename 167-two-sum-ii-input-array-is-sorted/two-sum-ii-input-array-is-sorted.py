class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) -1
        
        while numbers[i] + numbers[j]!=target:
            s = numbers[i] + numbers[j]        
            if s > target:
                j-=1
            else:
               i+=1 
        
        return [i + 1 , j + 1]