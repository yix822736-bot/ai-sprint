class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
a.next = b
b.next = c

cur = a
while cur is not None:
    print(cur.val)
    cur = cur.next
