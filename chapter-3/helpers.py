class Element:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Singly_Linked_List:
    def __init__(self):
        self.head = None 
        self.length = 0 

    def append(self, element): 
        self.length += 1 
        if not self.head : 
            self.head = element 
            return 
        temp = self.head 
        while temp.next != None : 
            temp = temp.next 
        temp.next = element 

    def prepend(self, element): 
        self.length += 1 
        if not self.head : 
            self.head = element 
            return 
        temp = self.head 
        self.head = element 
        element.next = temp 
    
    def delete_and_return_operation(self):
        if not self.head : None 
        self.length -= 1
        item = self.head 
        self.head = self.head.next 
        return item 

    def __str__(self): 
        string = ""
        temp = self.head 
        while temp != None :
            string += f'{temp.data}\n'
            temp = temp.next 
        return string 
    
    def __len__(self):
        return self.length
    
class CANT_USE_THIS(Exception):
    pass

class Stack(Singly_Linked_List) :

    def push(self, element):
        self.prepend(element) 

    def pop(self): 
        return self.delete_and_return_operation()
    
    def peek(self):
        return self.head 

    def isEmpty(self):
        return not self.head
    
    def append(self):
        raise CANT_USE_THIS


class Queue(Singly_Linked_List):
    def queue(self, element):
        self.append(element)
    
    def dequeue(self):
        return self.delete_and_return_operation()
    
    def peek(self):
        return self.head 

    def isEmpty(self):
        return not self.head
    
    def prepend(self): 
        raise CANT_USE_THIS