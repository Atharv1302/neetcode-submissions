# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        ans = []

        if root:
            queue.append(root)

        while len(queue) > 0:

            currentLevel = []

            for i in range(len(queue)):
                currNode = queue.popleft()

                currentLevel.append(currNode.val)

                if(currNode.left):
                    queue.append(currNode.left)
                
                if(currNode.right):
                    queue.append(currNode.right)

            ans.append(currentLevel)

        return ans


            

        