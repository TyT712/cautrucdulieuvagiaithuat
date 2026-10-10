from test import Node
from test import LinkedList

B = LinkedList()

while True:
    n = int(input("Nhập số nguyên dương n: , muốn dừng nhập 0: "))
    if n == 0:
        break
    else:
        B.append(n)

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current is not None:
        next_node = current.next  # nhớ node sau đó
        current.next = prev       # đảo ngược đường dẫn
        prev = current            # chuyển prev sang node hiện tại
        current = next_node       # chuyển node hiện tại sang next_node
    linked_list.head = prev       # cập nhật lại đầu của linklist

reverse_linked_list(B)
print("Danh sách liên kết sau khi đảo ngược:" )
B.print_list()
