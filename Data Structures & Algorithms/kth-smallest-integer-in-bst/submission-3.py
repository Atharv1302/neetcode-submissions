# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        bstInArray = []

        def dfs(topNode):

            if not topNode:
                return

            dfs(topNode.left)
            bstInArray.append(topNode.val)
            dfs(topNode.right)

        dfs(root)

        return bstInArray[k - 1]
