class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)

        for i in range(n):
            left, right = i, n - 1
            while left < right:
                curr = numbers[left] + numbers[right]
                if curr < target:
                    left += 1 
                elif curr > target:
                    right -= 1 

                else:
                    return [left+1 , right+1]

            