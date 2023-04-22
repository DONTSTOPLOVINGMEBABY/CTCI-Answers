from helpers import Stack, Element
'''
Queues Via Stacks 

Implement a MyQueue class which implements a queue using two stacks 

'''


class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.length = 0 

    def enqueue(self, data):
        self.length += 1 
        element = Element(data)
        self.stack1.push(element)
    
    def dequeue(self):
        self.length -= 1 
        while not self.stack1.isEmpty():
            item = self.stack1.pop()
            new_element = Element(item.data)
            self.stack2.push(new_element)
        item = self.stack2.pop()

        while not self.stack2.isEmpty():
            item = self.stack2.pop()
            new_element = Element(item.data)
            self.stack1.push(item)
        return item 

    def isEmpty(self):
        return not self.length

    def print_queue(self):
        while not self.stack1.isEmpty():
            item = self.stack1.pop()
            new_element = Element(item.data)
            self.stack2.push(new_element)
        item = self.stack2.pop()
        new_element = Element(item.data)
        self.stack1.push(new_element)
        print(new_element)
        while not self.stack2.isEmpty():
            item = self.stack2.pop()
            new_element = Element(item.data)
            self.stack1.push(new_element)
            print(new_element.data)


q = MyQueue()
for i in range(10):
    q.enqueue(i)

print(q.dequeue())
q.print_queue()