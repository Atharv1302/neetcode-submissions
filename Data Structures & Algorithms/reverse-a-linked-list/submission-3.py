class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        newList = None        # dummy node
        while head:
            temp = newList     # save current front of reversed list
            newList = head     # attach current node to dummy
            head = head.next        # advance original pointer (before we modify the node's next)
            newList.next = temp # point the newly attached node to the old front
        return newList


        