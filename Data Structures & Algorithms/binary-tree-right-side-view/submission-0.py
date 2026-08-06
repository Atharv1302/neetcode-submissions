
from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        ans = []

        if root:
            queue.append(root)

        while len(queue) > 0:

            currentLength = len(queue)
            rightmost = None

            for i in range(currentLength):

                currentNode = queue.popleft()
                
                if currentNode:
                    rightmost = currentNode
                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)

            if rightmost:
                ans.append(rightmost.val)

        return ans

                




        