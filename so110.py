# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root:TreeNode) :
            if root == None :
                return {"isba":True,"dep":0}
            left = helper(root.left)
            right = helper(root.right)
            dep= max(left["dep"],right["dep"])+1
            isba = left["isba"] and right["isba"] and abs(left["dep"] - right["dep"]) < 2
            return {"isba":isba,"dep":dep}
        return helper(root)["isba"]
