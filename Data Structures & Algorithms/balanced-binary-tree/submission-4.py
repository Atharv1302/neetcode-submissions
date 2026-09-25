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

            leftCheck, check1 = depthChecker(topNode.left)

            if not check1:
                return (0, False)


            rightCheck, check2 = depthChecker(topNode.right)
            if not check2 or abs(leftCheck - rightCheck) > 1:
                return (0, False)

            else:
                return(1 + max(leftCheck, rightCheck), True)
                

        return depthChecker(root)[1]
        
        