class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        newList = None

        while head != None:
            temp = newList
            newList = head
            head = head.next
            newList.next = temp

        return newList


        