from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sum = 0
        min = nums[0]
        for i in nums:
            sum += i
            if min > i:
                min = i
        return sum - min * len(nums)
