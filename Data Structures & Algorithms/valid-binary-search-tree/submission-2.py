# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        
        def checker(lowerBound, currentNode, upperBound):

            if not currentNode:
                return True

            if not(lowerBound < currentNode.val) or not(currentNode.val < upperBound):
                return False
            
            return checker(lowerBound, currentNode.left, currentNode.val) and checker(currentNode.val, currentNode.right, upperBound)

        return checker(float("-inf"), root, float("inf"))

        