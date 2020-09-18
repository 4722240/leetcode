from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        tmp = {}
        for i in nums :
            tmp[i] = 1
        for i in range(1,len(nums)+1) :
            if i not in tmp:
                res.append(i)
        return res