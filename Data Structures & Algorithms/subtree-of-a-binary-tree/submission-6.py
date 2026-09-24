# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def sameTree(self, root, subRoot) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False

        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and subRoot:
            return False
        
        if root and not subRoot:
            return False

        if not root and not subRoot:
            return True

        if root.val == subRoot.val:
            return (self.sameTree(root, subRoot)) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)