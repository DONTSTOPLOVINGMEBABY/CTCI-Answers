from helpers import sll_Node, sll_2 

'''
2.7 Intersection -- Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is if kth node of the first linked list is the exact same node (by reference) as the jth node of the second linkst list, then they are intersecting. 
'''




def test_equality(linked_list1, linked_list2) :
    head_1 = linked_list1.head 
    head_2 = linked_list2.head 
    
    while head_1 != None and head_2 != None : 
        if head_1 is head_2 : 
            print("true") 
        head_1 = head_1.next 
        head_2 = head_2.next 



ll_1 = sll_2()
ll_2 = sll_2() 


for i in range(1, 5):
    node = sll_Node(i) 
    ll_1.append(node) 

for i in range(5, 8):
    node = sll_Node(i) 
    ll_2.append(node) 

connecting_node = sll_Node(4) 
ll_1.append(connecting_node) 
ll_2.append(connecting_node) 

for i in range(8, 11):
    node = sll_Node(i) 
    ll_2.append(node) 

print(ll_1)
print(ll_2)

