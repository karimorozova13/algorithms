#  Last In, First Out
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

# peek, top. return last, but not delete
def peek(stack):
    return stack[-1]
print(peek(stack))

# is_empty
def is_empty(stack):
    return len(stack) == 0

print(is_empty(stack))

class Stack:
    def __init__(self) -> None:
        self.stack = []
    def push(self,el):
        self.stack.append(el)
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
s = Stack()
s.push('a')
s.push('b')
s.push('c')
print(s.peek()) # Output: 'c'
print(s.pop())  # Output: 'c'
print(s.peek()) # Output: 'b'
print(s.is_empty()) # Output: False
    
