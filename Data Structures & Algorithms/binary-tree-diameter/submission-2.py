# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        bestDiameter = 0

        def depth(topNode):

            nonlocal bestDiameter

            if not topNode:
                return 0

            leftDepth = depth(topNode.left)
            rightDepth = depth(topNode.right)
            bestDiameter = max(bestDiameter, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)

        depth(root)
        return bestDiameter


        

        
        

            