class Node:
    def __init__(self,val):
        self.val = val  # data, giá trị của node
        self.next = None  # con trỏ để chỉ tới node tiếp theo

class LinkedList:
    def __init__(self):
        self.head = None #  điểm bắt đầu
    def append(self,val):   #append(5)
        new_node = Node(val)   # => newnode = [val = 5, next = none]
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val, end = " ")
            cur = cur.next
    def pop(self):
        if self.head is None:
            return None
        cur = self.head
        if cur.next is None:
            val = cur.val
            self.head = None
            return val
        while cur.next.next:
            cur = cur.next
        val = cur.next.val
        cur.next = None
        return val
A = LinkedList()
A.append(1)
A.append(3)
A.append(4)
A.append(5)
A.append(8)
cur = A.head
# print(cur.val)
#A.print_list()
# reverse

    