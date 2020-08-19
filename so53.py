from typing import List
from typing import Dict
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxtmp=nums[0]
        maxres=nums[0]
        for i in nums[1:] :
           maxtmp = max(maxtmp+ i, i)
           maxres = max(maxres,maxtmp)
        return maxres

    def maxSubArray2(self,nums : List[int])->int:
        return subArrayData(nums,0,len(nums)-1)["isum"]

def subArrayData(nums:List[int],start:int,end:int)-> Dict:
    if start == end :
        return {"sum":nums[start],"lsum":nums[start],"rsum":nums[start],"isum":nums[start]}

    mid = (start+end)//2
    lsub = subArrayData(nums,start,mid)
    rsub = subArrayData(nums,mid+1,end)

    subsum = lsub["sum"] + rsub["sum"]
    lsum = max(lsub["lsum"],lsub["sum"]+rsub["lsum"])
    rsum = max(rsub["rsum"],rsub["sum"]+lsub["rsum"])
    isum = max(lsub["isum"],rsub["isum"],lsub["rsum"]+rsub["lsum"])

    return {"sum":subsum,"lsum":lsum,"rsum":rsum,"isum":isum}


