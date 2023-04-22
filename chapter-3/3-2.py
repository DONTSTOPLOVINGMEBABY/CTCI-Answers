import random # for testing 
seed = random.seed()

'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element. Push, Pop, and min should all operate in O(1) time. 
'''

class Element:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.next_smallest = None
    
class MinStack:
    def __init__(self):
        self.head = None 

    def push(self, data): 
        elem = Element(data)
        if not self.head : 
            self.head = elem 
            return 
        if elem.data < self.head.data : 
            temp_head = self.head 
            self.head = elem
            elem.next = temp_head 
            elem.next_smallest = temp_head 
        else : 
            temp = self.head.next_smallest
            while temp.next_smallest != None :
                temp = temp.next_smallest
            temp.next = elem

    def pop(self):
        if not self.head : return None 
        item = self.head 
        self.head = item.next_smallest
        return item 

    def delete_and_return_operation(self):
        if not self.head : None 
        item = self.head 
        self.head = self.head.next 
        return item 

    def isEmpty(self):
        return not self.head 

    def __str__(self): 
        string = ""
        temp = self.head 
        while temp != None :
            string += f'{temp.data}\n'
            temp = temp.next 
        return string 
    
ms = MinStack()
for i in range(10):
    ms.push(random.randint(0, 50))

print(ms)

while not ms.isEmpty():
    print(ms.pop())


