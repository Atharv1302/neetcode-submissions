class Node:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0
        
    def get(self, index: int) -> int:

        if index >= 0 and index < self.size:
            ctr = self.head.next
            for i in range(index):
                ctr = ctr.next

            return ctr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:

        if self.size == 0:
            newNode = Node(val)
            self.head.next = newNode
            self.size = self.size + 1
        else:
            newNode = Node(val)
            newNode.next = self.head.next
            self.head.next = newNode
            self.size = self.size + 1
        

    def addAtTail(self, val: int) -> None:

        if(self.size == 0):
            self.addAtHead(val)

        else:

            ctr = self.head.next

            for i in range(self.size - 1):

                ctr = ctr.next

            ctr.next = Node(val)
            self.size = self.size + 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > 0 and index < self.size:
            ctr = self.head.next

            for i in range(index - 1):
                ctr = ctr.next

            newNode = Node(val)
            newNode.next = ctr.next
            ctr.next = newNode

            self.size = self.size + 1
        

    def deleteAtIndex(self, index: int) -> None:

        if index >= 0 and index < self.size:
            if index == 0:
                self.head.next = self.head.next.next
            else:
                ctr = self.head.next

                for i in range(index - 1):
                    ctr = ctr.next
                    
                ctr.next = ctr.next.next
            self.size = self.size - 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)