class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self ):
        self.head = None
        self.tail = None
    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def push_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    def insert_after(self,prev_node, data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next= prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node
    def insert_before(self,next_node, data):
        if not next_node:
            return
        new_node = Node(data)
        new_node.prev = next_node.prev
        new_node.next = next_node
        next_node.prev = new_node
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node
    def remove_node(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                cur.prev = None
                cur.next = None
                return True
            cur = cur.next
        return False
    def search_node(self, data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                return cur_node
            cur_node = cur_node.next
        return None
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

dll = DoublyLinkedList()
dll.append_node(1)
dll.append_node(2)
dll.append_node(3)

dll.push_node(4)
dll.push_node(5)
dll.push_node(6)

node_2 = dll.search_node(2)

if node_2:
    dll.insert_after(node_2,7)
    dll.insert_before(node_2,13)
    
dll.remove_node(2)
dll.print_list()


     