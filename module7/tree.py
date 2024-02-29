# O(n)

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key
        
def preorder_traversal(root):
        if root:
            print(root.val)
            preorder_traversal(root.left)
            preorder_traversal(root.right)
            
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)
        
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)
            
root = Node(1)
root.left = Node(2)
root.right  = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Preorder Traversal:')
preorder_traversal(root)

print('\nInorder Traversal:')
inorder_traversal(root)

print('\nPostorder Traversal:')
postorder_traversal(root)
            
        
        
# preorder traversal Прямий - root, left side, right side
# inorder traversal Центровий - left side,root, right side
# postorder traversal Зворотний - left side, right side, root
