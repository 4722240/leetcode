class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num)) - 2
        return (2**length - 1) ^ num