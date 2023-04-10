from helpers import Singly_Linked_List 

'''
Return Kth to Last : Implement an algorithm to find the kth to last element of a singly linked list. 
'''

## This Singly_Linked_List class does have the __len__ function overidden and can return
## the lenght of the entire linked_list 


'''
Implement this guy : 

A more optimal, but less straightforward solution is to implement this iteratively. We can use two pointers, p1 and p2. We place them k nodes apart in the linked list by putting p2 at the beginning and moving p1 k nodes into the list. Then, we move them at the same pace, p1 will hit the end of the linked list after LENGTH - k nodes into the list. At that point, p2 will be LENGTH - k nodes into the list, or k nodes from the end. 

'''


## without using len(linked_list) 
def kth_to_last_element_function1(linked_list, k_elem):
    ctr = 0 
    first_temp = linked_list.head 
    while first_temp != None : 
        ctr += 1 
        first_temp = first_temp.next 
    if (ctr < k_elem) : return False 
    hold_node = linked_list.head
    count_to_x = ctr - k_elem
    ctr2 = 0 
    while ctr2 != count_to_x :
        hold_node = hold_node.next 
        ctr2 += 1 
    return hold_node 
    


## with using len(linked_list) 
def kth_to_last_element_function2(linked_list, k_elem):
    
    if len(linked_list) < k_elem + 1 : return False 
    ctr = 0
    count_to = len(linked_list) - k_elem
    hold_head1 = linked_list.head 
    while ctr != count_to : 
        ctr += 1 
        hold_head1 = hold_head1.next 
    return hold_head1 



sll = Singly_Linked_List() 
for i in range(10):
    sll.append(i * i) 
print(sll)


print(kth_to_last_element_function1(sll, 4)) 
print(kth_to_last_element_function2(sll, 4)) 

