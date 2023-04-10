from helpers import Singly_Linked_List 

'''
Write code to remove duplicates from an unsorted linked list. 

FOLLOW UP 

How would you solve this problem if a temporary buffer is not allowed
'''

def using_a_hashmap(linked_list):
    
    ## get all elements from linked_list_and_put_them_in_hash_map
    
    hash_map = {}
    head = linked_list.head 
    while head != None :
        if head.data in hash_map:
            linked_list.delete(head.data)
        else : 
            hash_map[head.data] = True 
        head = head.next     



def not_using_a_hashmap(linked_list): 
    current_location = 0 
    current_node = linked_list.head
    
    while current_node.next != None :
        save_data = current_node.data 
        keep_place = current_node 
        while keep_place != None : 
            if keep_place.next != None and keep_place.next.data == save_data :
                linked_list.delete(keep_place.next.data)
                keep_place.next = keep_place.next.next 
            keep_place = keep_place.next 
        current_node = current_node.next 
    


sll = Singly_Linked_List()
for i in range(5):
    for j in range(i):
        sll.append(i) 
print(sll)
using_a_hashmap(sll) 
print(sll) 

sll2 = Singly_Linked_List() 
for i in range(5):
    for j in range(i):
        sll2.append(i) 
print(sll2)
not_using_a_hashmap(sll2) 
print(sll2) 


