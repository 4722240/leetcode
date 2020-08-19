from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums:List[int],start:int,end:int)->TreeNode:
            if start > end :
                return None
            mid = (start+end)//2

            node = TreeNode(nums[mid])
            node.left = helper(nums,start,mid-1)
            node.right =helper(nums,mid+1,end)
            return node
        return helper(nums,0,len(nums)-1)
