# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfsMethod(root, currentSum = 0):

            if (not root):
                return False

            if not root.right and not root.left:
                if currentSum + root.val == targetSum:
                    return True
                else:
                    return False

            return dfsMethod(root.right, root.val + currentSum) or dfsMethod(root.left, root.val + currentSum)

        return dfsMethod(root)
