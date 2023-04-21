from helpers import Singly_Linked_List, copy_linked_list

'''
Implement a function to check if a linked list is a palindrome. 
'''

def use_a_hashmap(linked_list): 
    hmap = {}
    begin = linked_list.head 
    oddctr = 0 
    while begin != None :

        if begin.data in hmap:
            hmap[begin.data] += 1 % 2  
            oddctr -= 1 
        else :
            hmap[begin.data] = 1 
            oddctr += 1 
        begin = begin.next 

    if oddctr % 2 == 0 : return False 
    
    found_odd = False 
    for i in hmap: 
        if hmap[i] == 1 and found_odd == False :
            found_odd = True 
        elif hmap[i] == 1 and found_odd : 
            return False 
    return True 

def swap(node1, node2):
    node1_cpy = node1.data
    node1.data = node2.data
    node2.data = node1_cpy 



def using_a_reverse_list(linked_list):

    def reverse_linked_list(linked_list) :
        prev = curr = nex = None 
        curr = linked_list.head 
        while curr != None :
            nex = curr.next 
            curr.next = prev
            prev = curr 
            curr = nex 
        linked_list.head = prev
        return linked_list  

    reverse_list = copy_linked_list(linked_list)
    reverse_list = reverse_linked_list(reverse_list) 
    reverse_head = reverse_list.head 
    normal_head = linked_list.head 
    while normal_head != None and reverse_head != None :
        if normal_head.data == reverse_head.data :
            normal_head = normal_head.next 
            reverse_head = reverse_head.next 
            continue 
        else :
            return False 
    return True 


def use_a_stack(linked_list):
    
    stack = []
    slow = linked_list.head 
    fast = linked_list.head 
    while fast != None and fast.next != None :
        stack.append(slow.data)
        slow = slow.next 
        fast = fast.next.next  

    if fast != None : slow = slow.next 

    while slow != None :
        if slow.data == stack.pop() :
            slow = slow.next
            continue 
        else : 
            return False 
    return True 
    


palindromes = [ "RACECAR", "DAD", "SAM", "404", "3212" ] 
linked_lists = []
for palindrome in palindromes : 
    new_ll = Singly_Linked_List() 
    for letter in palindrome :
        new_ll.append(letter)
    linked_lists.append(new_ll) 

for i in linked_lists :
    print(i, use_a_stack(i))


