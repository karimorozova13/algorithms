class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def insert_at_end(self, data):
        new_node =Node(data)
        if  self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_after(self, prev_node: Node, data):
        if not prev_node is None:
            print('Does not exist')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def search_node(self,data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
            return None
    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
            if cur is None:
                return
            prev.next = cur.next
            cur = None
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            
llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\n Зв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\n Шукаємо елемент 15:")
element = llist.search_node(15)
if element:
  print(element.data)
        