import helpers

'''
2.5 Sum Lists -- You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. (You are not allowed to "cheat" and just convert the linked list to an integer. 

Example 

Input (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295. 

Output: 2 -> 1 -> 9. That is 912. 

Follow Up. Suppose the digits are in forward order. Repeat the above problem. 

Example

Input (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295. 

Output : 9 -> 1 -> 2. That is, 912. 

'''

def cheating_add_reverse_lists(ll1, ll2):
    walk_through_list = ll1.head
    first_number = "" 
    second_number = "" 
    while walk_through_list != None :
        first_number += f'{walk_through_list.data}'
        walk_through_list = walk_through_list.next 
    walk_through_list = ll2.head 
    while walk_through_list != None :
        second_number += f'{walk_through_list.data}'
        walk_through_list = walk_through_list.next 
    first_number = first_number[::-1] ; second_number = second_number[::-1]  
    sum_lists = str(int(first_number) + int(second_number))[::-1] 
    return_list = helpers.Singly_Linked_List() 
    for i in sum_lists:
        return_list.append(i) 
    return return_list 



## This one is almost correct, except that it returns the lists in the wrong order. 

def add_reverse_lists_return_in_order(ll1, ll2):
    
    return_list = helpers.Singly_Linked_List() 

    def handle_elements(node_list_1, node_list_2, carry_number): 
        if (node_list_1 == None and node_list_2 == None) : return 
        sum_two = carry_number 
        if (node_list_1 != None) : 
            sum_two += node_list_1.data
            next_node_1 = node_list_1.next 
        else : 
            next_node_1 = None 
        if (node_list_2 != None) : 
            sum_two += node_list_2.data
            next_node_2 = node_list_2.next
        else :
            next_node_2 = None 
        
        if sum_two < 10 : 
            return_list.append(sum_two) 
            return handle_elements(next_node_1, next_node_2, 0)
        else :
            return_list.append(sum_two % 10) 
            return handle_elements(next_node_1, next_node_2, 1) 
            
    handle_elements(ll1.head, ll2.head, 0) 
    print(return_list) 
    ## return new_linked_list



# Her Example 

def addLists(l1, l2) :
    
    return_list = helpers.sll_2() 

    def add_two(node1, node2, carry):
        if node1 == None and node2 == None and carry == 0 : return None
        value = carry 
        if (node1 != None) :
            value += node1.data
        if (node2 != None) :
            value += node2.data
        result = helpers.sll_Node( value % 10 ) 
        if (node1 != None or node2 != None):
            new_node1 = None if node1 == None else node1.next 
            new_node2 = None if node2 == None else node2.next
            new_carry = 1 if value >= 10 else 0 
            more = helpers.sll_Node( new_node1, new_node2, new_carry ) 
            result.next = more 
        return result 
    
    zooweemama = add_two(l1.head, l2.head, 0) 
    



# initialize lists 
first_reverse_list = helpers.Singly_Linked_List()
second_reverse_list = helpers.Singly_Linked_List() 

# set values for reverse list 1 
first_reverse_list.append(7)
first_reverse_list.append(1) 
first_reverse_list.append(6) 

# set values for reverse list 2 
second_reverse_list.append(5)
second_reverse_list.append(9) 
second_reverse_list.append(2) 

print(first_reverse_list, second_reverse_list)

#reverse_sum1 = cheating_add_reverse_lists(first_reverse_list, second_reverse_list)
#print(reverse_sum1) 
add_reverse_lists_return_in_order(first_reverse_list, second_reverse_list)
#addLists(first_reverse_list, second_reverse_list) 
