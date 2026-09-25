# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def depth(topNode):
            if not topNode:
                return 0
            
            return 1 + max(depth(topNode.right), depth(topNode.left))

        bestDiameterHere = depth(root.right) + depth(root.left)
        checkleft = self.diameterOfBinaryTree(root.left)
        checkRight = self.diameterOfBinaryTree(root.right)

        return max(bestDiameterHere, checkleft, checkRight)
        

        
        

            