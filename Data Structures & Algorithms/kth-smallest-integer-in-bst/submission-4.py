# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        ans = None

        def dfs(topNode):

            if not topNode:
                return

            nonlocal count
            nonlocal ans

            dfs(topNode.left)
            count = count + 1
            if count == k:
                ans = topNode.val
                return
            dfs(topNode.right)

        dfs(root)
        return ans
