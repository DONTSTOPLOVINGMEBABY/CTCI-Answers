
'''

Delete Middle Node : Implement an Algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node. 

EXAMPLE 

Input  :  the node c from the linked list: a --> b --> c --> d --> e --> f
Result :  nothing is returned, but the new linked list looks like a --> b --> d --> e --> f 

'''

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

    def append(self, node):
        self.length += 1 
        if self.head == None : 
            self.head = node 
            return 
        temp = self.head 
        while temp.next != None :
            temp = temp.next 
        temp.next = node 



    ## THIS IS THE FUNCTION FROM THE QUESTION 


    def delete_middle_node(self, node):
        if node == None or node.next == None : return False 
        copy_data = node.next.data 
        node.data = copy_data 
        node.next = node.next.next 
    
    #########################################

   

    def __str__(self):
        if self.length == 0 : return "None"
        string = "Head --> "
        temp = self.head 
        while (temp != None):
            string += f'{temp.data} --> '
            temp = temp.next 
        return string + "Tail" 



sll = Singly_Linked_List()

node1 = sll_Node(1) 
node2 = sll_Node(2) 
node3 = sll_Node(3)
node4 = sll_Node(4) 
node5 = sll_Node(5) 
node6 = sll_Node(6) 

sll.append(node1) 
sll.append(node2) 
sll.append(node3) 
sll.append(node4) 
sll.append(node5) 
sll.append(node6) 




print(sll) 
sll.delete_middle_node(node2) 
sll.delete_middle_node(node4)
print(sll) 
