class Solution:
    def minimumSum(self, num: int) -> int:
        arr = sorted(str(num))

        temp = arr[1]
        arr[1] = arr[2]
        arr[2] = temp 

        new1 = arr[0] + arr[1]
        new2 = arr[2] + arr[3] 

        return int(new1) + int(new2)
