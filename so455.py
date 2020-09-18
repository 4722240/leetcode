from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j,res = 0,0,0
        lenG,lenS= len(g), len(s)
        while i<lenG and j<lenS :
            if g[i] <= s[j] :
                i+=1
                j+=1
                res+=1
            else:
                j += 1
        return res

