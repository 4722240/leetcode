class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num
        while start <= end :
            mid = (start + end)//2
            tmp = mid** 2
            if tmp == num :
                return True
            if tmp > num :
                end = mid -1
                continue
            if tmp < num :
                start = mid + 1
        return False