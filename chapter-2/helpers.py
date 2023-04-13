
class sll_Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
    
    def __str__(self):
        return f'{self.data}' 

class Singly_Linked_List:
    def __init__(self):
        self.head = None 
        self.length = 0 

    def append(self, data):
        node = sll_Node(data) 
        self.length += 1 
        if self.head == None : 
            self.head = node 
            return 
        temp = self.head 
        while temp.next != None :
            temp = temp.next 
        temp.next = node 

    def delete(self, data): 
        node = sll_Node(data) 
        if self.head != None and self.head.data == data : 
            self.head = self.head.next 
            self.length -= 1 
        else :
            temp = self.head 
            while temp.next != None and temp.next.data != data :
                temp = temp.next 
            if temp.next != None and temp.next.data == data :
                temp.next = temp.next.next 
            else : 
                return False 
        return True 


    def __len__(self):
        return self.length 
    

    def __str__(self):
        if self.length == 0 : return "None"
        string = "Head --> "
        temp = self.head 
        while (temp != None):
            string += f'{temp.data} --> '
            temp = temp.next 
        return string + "Tail" 


class sll_2:
    def __init__(self):
        self.head = None 
        self.length = 0 

    def append(self, node):
        self.length += 1 
        if self.head == None : 
            self.head = node 
            return 
        temp = self.head 
        while temp.next != None :
            temp = temp.next 
        temp.next = node 

    def delete(self, data): 
        node = sll_Node(data) 
        if self.head != None and self.head.data == data : 
            self.head = self.head.next 
            self.length -= 1 
        else :
            temp = self.head 
            while temp.next != None and temp.next.data != data :
                temp = temp.next 
            if temp.next != None and temp.next.data == data :
                temp.next = temp.next.next 
            else : 
                return False 
        return True 


    def __len__(self):
        return self.length 
    

    def __str__(self):
        if self.length == 0 : return "None"
        string = "Head --> "
        temp = self.head 
        while (temp != None):
            string += f'{temp.data} --> '
            temp = temp.next 
        return string + "Tail" 


def copy_linked_list(linked_list):
    hold_head = linked_list.head 
    new_ll = Singly_Linked_List() 
    while hold_head != None :
        new_ll.append(hold_head.data) 
        hold_head = hold_head.next 
    return new_ll 

