from helpers import Stack, Element
'''
Queues Via Stacks 

Implement a MyQueue class which implements a queue using two stacks 

'''

class HerQueue:
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()
    
    def size(self):
        return len(self.stack_newest) + len(self.stack_oldest)

    def add(self, value):
        self.stack_newest.push(Element(value))
    
    def shiftStacks(self):
        if self.stack_oldest.isEmpty():
            while not self.stack_newest.isEmpty():
                self.stack_oldest.push(self.stack_newest.pop())
    
    def peek(self):
        self.shiftStacks()
        return self.stack_oldest.peek()
    
    def remove(self):
        self.shiftStacks()
        return self.stack_oldest.pop()


q = HerQueue()
for i in range(10):
    q.add(i)

print(q)

for i in range(10):
    print(q.peek())
    print(q.remove().data)