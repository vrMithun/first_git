class Node:
    def __init__(self, data=None):
        self.data = data
        self.ref = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty, cannot pop.")
            return
        self.head = self.head.ref

    def top(self):
        if self.head is None:
            print("Stack is empty.")
        else:
            print(self.head.data)

    def size(self):
        temp = 0
        n = self.head
        while n is not None:
            temp += 1
            n = n.ref
        print(temp)

    def traverse(self):
        n = self.head
        while n is not None:
            print(n.data,end=" ")
            n = n.ref
        print()
    def isEmpty(self):
        if self.head is None:
            print("Stack is empty.")
        else:
            print("Stack is not empty.") 