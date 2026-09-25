# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depthChecker(topNode):

            if not topNode:
                return (0, True)

            leftCheck, leftBalanced = depthChecker(topNode.left)

            if not leftBalanced:
                return (0, False)


            rightCheck, rightBalanced = depthChecker(topNode.right)
            if not rightBalanced or abs(leftCheck - rightCheck) > 1:
                return (0, False)

            return(1 + max(leftCheck, rightCheck), True)
                

        return depthChecker(root)[1]
        
        