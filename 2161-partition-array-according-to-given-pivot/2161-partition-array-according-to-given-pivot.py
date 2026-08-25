class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []

        for num in nums:
            if num == pivot:
                result.append(num)

        for num in nums:
            if num > pivot:
                result.append(num)

        temp = []
        for num in nums:
            if pivot > num:
                temp.append(num)

        final = temp + result

        return final