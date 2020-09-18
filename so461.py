class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        count = 0
        while res > 0 :
            res = res & (res-1)
            count +=1
        return count

    def hammingDistance1(self, x: int, y: int) -> int:
        return bin(x^y).count(1)