from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC,tmp  = 0,0
        for i in nums :
            if i == 0 :
                tmp = 0
            else :
                tmp += 1
                if tmp > maxC :
                    maxC = tmp
        return maxC
