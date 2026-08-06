# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfsChecker(currentNode):
            if not currentNode:
                return (True, 0)
            
            leftBalance, leftHeight = dfsChecker(currentNode.left)
            rightBalance, rightHeight = dfsChecker(currentNode.right)

            currentBalance = leftBalance and rightBalance and abs(leftHeight - rightHeight) <= 1
            currentHeight = 1 + max(leftHeight, rightHeight)

            return (currentBalance, currentHeight)

        return dfsChecker(root)[0]

        
        