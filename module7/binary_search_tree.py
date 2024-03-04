class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right =  None
        self.val = key
    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret
        
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
 
def min_val_node(node):
    current = node
    while current.left:
        current = current.left
    return current   


def delete(root, key):
    if not root:
        return root
    
    if key < root.val:
        print('key < root.val', key, 'key - ', root.val)
        root.left = delete(root.left, key)
    elif key > root.val:
        print('key > root.val', key, 'key - ', root.val)
        
        root.right = delete(root.right, key)
    else:
        if not root.left:
            
            temp = root.right
            root = None
            print('not root.left', temp, 'temp - ')
            
            return temp
        elif not root.right:
            temp = root.left
            root = None
            print('not root.right', temp, 'temp - ')
            
            return temp
        root.val = min_val_node(root.right).val
        print('root.val = min_val_node(root.right).val', root.val)
        
        root.right = delete(root.right, root.val)
        print(root)
        
    return root
    
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

print(search(root, 7).val)
root = delete(root, 7)
print(root)