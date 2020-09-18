from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap,stack,res = {},[],[]
        for i in nums2 :
            while len(stack) > 0 and i > stack[-1] :
                tmp = stack.pop()
                hashmap[tmp] = i
            stack.append(i)
        for i in stack :
            hashmap[i] = -1
        for i in nums1:
            res.append(hashmap[i])
        return res
