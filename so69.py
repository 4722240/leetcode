class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        k=x
        while k**2>x or (k+1)**2 <=x :
            k = int((k+x/k)/2)
        return int(k)