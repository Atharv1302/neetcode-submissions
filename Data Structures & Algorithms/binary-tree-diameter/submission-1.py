# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, topNode):
            if not topNode:
                return 0
            
            return 1 + max(self.depth(topNode.right), self.depth(topNode.left))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        bestDiameterHere = self.depth(root.right) + self.depth(root.left)
        checkleft = self.diameterOfBinaryTree(root.left)
        checkRight = self.diameterOfBinaryTree(root.right)

        return max(bestDiameterHere, checkleft, checkRight)
        

        
        

            