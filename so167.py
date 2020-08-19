from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start  = 0
        end =len(numbers) -1
        while start < end :
            tmp = numbers[start] + numbers[end]
            if tmp < target :
                start += 1
            if tmp > target :
                end -= 1
            if tmp == target :
                return [start+1,end+1]
        return -1
