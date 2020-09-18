from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        sum = 0
        for i in points :
            tmp = {}
            for j in points :
                if i == j : continue
                dis = (i[0] - j[0])**2 + (i[1] - j[1])**2
                tmp[dis] = tmp[dis] + 1 if dis in tmp else 1
            for k in tmp:
                if tmp[k] > 1:
                    sum += tmp[k] * (tmp[k] - 1)
        return sum

