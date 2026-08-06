class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        
        nxt = cur.next
        new_node = ListNode(val)
        
        cur.next = new_node
        new_node.prev = cur
        new_node.next = nxt
        nxt.prev = new_node
        
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        # Traverse from nearest end
        if index < self.size // 2:
            cur = self.head
            for _ in range(index + 1):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - index):
                cur = cur.prev
        
        # Unlink the node
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.size -= 1