# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfsMethod(root, targetSum, currentSum = 0):

            if (not root):
                return False

            if not root.right and not root.left:
                if currentSum + root.val == targetSum:
                    return True
                else:
                    return False

            if root.right and root.left:
                return dfsMethod(root.right, targetSum, root.val + currentSum) or dfsMethod(root.left, targetSum, root.val + currentSum)
            elif root.right:
                return dfsMethod(root.right, targetSum, root.val + currentSum)
            else:
                return dfsMethod(root.left, targetSum, root.val + currentSum)

        return dfsMethod(root, targetSum, 0)
