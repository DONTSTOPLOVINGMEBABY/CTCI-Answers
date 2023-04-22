from helpers import sll_Node, sll_2 

'''
2.7 Intersection -- Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is if kth node of the first linked list is the exact same node (by reference) as the jth node of the second linkst list, then they are intersecting. 
'''

def test_equality(linked_list1, linked_list2) :
    head_1 = linked_list1.head 
    head_2 = linked_list2.head 
    while head_1 != None : 
        while head_2 != None : 
            if head_1 is head_2:
                print(head_1.next, head_2.next) 
                return head_1 
            head_2 = head_2.next
        head_1 = head_1.next 
        head_2 = linked_list2.head 

# Running time is O(m + n) worst case if we traversed both lists only to find
# all elements were distinct. Best case would be O(m + 1) given that
# we index all of M and then the intersecting node is the first element in n       
# Space complexity is O(m) or O(n) depending on which list is hashed 

def using_simple_hash(linked_list1, linked_list2):
    table = {}
    head1 = linked_list1.head 
    head2 = linked_list2.head 
    while head1 != None :
        table[head1] = True
        head1 = head1.next 
    while head2 != None : 
        if head2 in table:
            return head2 
        head2 = head2.next 
    return False 

# Space Complexity is reduced to O(1). We do O(m + n) operations to get the distances
# And if they overlap, then we have to do len(longer_list) - abs(m - n) more operations

def idk_what_to_2_call_this(linked_list1, linked_list2):
    head1 = linked_list1.head
    head2 = linked_list2.head 
    distance1 = 0 
    distance2 = 0 

    while head1.next != None :
        head1 = head1.next 
        distance1 += 1 
    while head2.next != None :
        head2 = head2.next 
        distance2 += 1 
    if head1 is not head2 : return False
    counter = 0 
    if distance1 == distance2 :
        head1 = linked_list1.head
        head2 = linked_list2.head 
        while head1 is not head2 :
            head1 = head1.next 
            head2 = head2.next 
        return head1 
    else : 
        if distance1 > distance2 : 
            distance3 = distance1 - (distance1 - distance2)
            new_head = linked_list1.head 
        else : 
            distance3 = distance2 - (distance2 - distance1)
            new_head = linked_list2.head 
        while counter != distance3 : 
            new_head = new_head.next 
            counter += 1 
        return new_head



ll_1 = sll_2()
ll_2 = sll_2() 

for i in range(-4, 1):
    node = sll_Node(i) 
    ll_1.append(node) 

for i in range(6, 11):
    node = sll_Node(i) 
    ll_2.append(node) 

connecting_node = sll_Node(4) 
ll_1.append(connecting_node) 
ll_2.append(connecting_node) 

for i in range(10, 12):
    node = sll_Node(i) 
    ll_2.append(node) 

print(ll_1)
print(ll_2)


print(test_equality(ll_1, ll_2) )
print(using_simple_hash(ll_1, ll_2))
print(idk_what_to_2_call_this(ll_1, ll_2))