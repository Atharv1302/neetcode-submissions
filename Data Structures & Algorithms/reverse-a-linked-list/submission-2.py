class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        newList = ListNode()        # dummy node
        while head:
            temp = newList.next     # save current front of reversed list
            newList.next = head     # attach current node to dummy
            head = head.next        # advance original pointer (before we modify the node's next)
            newList.next.next = temp # point the newly attached node to the old front
        return newList.next