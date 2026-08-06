# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root: 
            return TreeNode(val)

        newNode = TreeNode(val)

        currentNode = root

        while True:

            if currentNode.val < val:
                if not currentNode.right:
                    currentNode.right = newNode
                    break
                currentNode = currentNode.right
            else:
                if not currentNode.left:
                    currentNode.left = newNode
                    break
                currentNode = currentNode.left

        return root

        