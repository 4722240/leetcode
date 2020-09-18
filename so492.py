import math
from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        tmp = int(math.sqrt(area))
        while tmp >= 1 :
            print(area,tmp)
            if area % tmp == 0 :
                return [area//tmp,tmp]
            else:
                tmp-=1
        return [area,1]
