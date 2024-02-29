class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right =  None
        self.val = key
        
def insert(root, key):
    if root is None:
        return Node(key)
    elif root.val > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    elif root.val > key:
        return search(root.left, key)
    else:
        return search(root.right, key)
    
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(search(root, 7).val)