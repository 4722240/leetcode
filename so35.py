from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return search(nums, 0, len(nums)-1,target)


def search(nums:List[int],start:int,end:int,target:int) ->int:
    print(start,end)
    if start == end :
        if nums[start] >= target :
            return start
        else:
            return start+1
    mid = (start + end)//2
    if nums[mid] == target :
        return mid
    if target > nums[mid] :
        return search(nums,mid+1,end,target)
    if target < nums[mid] :
        if start < mid :
            return search(nums,start,mid-1,target)
        else :
            return search(nums,start,mid,target)
