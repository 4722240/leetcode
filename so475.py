from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        mid=[]
        for i in range(len(heaters)-1) :
            tmp = (heaters[i]+heaters[i+1])/2
            mid.append(tmp)
        index,minR = 0,0
        midLen = len(mid)
        for i in houses :
            while index < midLen  and i > mid[index] :
                index +=1
            if minR < abs( i - heaters[index]):
                minR = abs(i - heaters[index])
        return minR

