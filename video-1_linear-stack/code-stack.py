class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.data
    
    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data


queue.py
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head is None
    
    def peek(self):
        if self.head is None:
            raise Exception("Queue is empty")
        return self.head.data
    
    def add(self, data):
        new_node = QueueNode(data)
        
        if self.tail is not None:
            self.tail.next = new_node
            
        self.tail = new_node
        
        if self.head is None:
            self.head = new_node
    
    def remove(self):
        if self.head is None:
            raise Exception("Queue is empty")
            
        data = self.head.data
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        return data

