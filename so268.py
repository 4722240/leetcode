from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tmp = 0
        for i in nums :
            tmp ^= i
        for j in range(len(nums) +1 ):
            tmp ^= j
        return tmp

    def missingNumber2(self,nums:List[int]) -> int:
        length = len(nums)
        sum = length * (length + 1)//2
        for i in nums :
            sum -= i
        return sum