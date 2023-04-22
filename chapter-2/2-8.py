from helpers import sll_Node, sll_2

'''
Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists). 

A -> B -> C -> D -> E -> C [the same C as earlier]

'''

def using_a_hash_table(linked_list):
    table = {} 
    head1 = linked_list.head 
    while head1 != None : 
        if head1 in table: return head1 
        else : table[head1] = True    
        head1 = head1.next
    return False

def using_runners(linked_list):
    slow = linked_list.head 
    if not slow.next : return False 
    fast = linked_list.head 
    while fast != None and fast.next != None:
        slow = slow.next 
        fast = fast.next.next
        if slow is fast : 
            break

    if fast == None or fast.next == None : return False
    slow = linked_list.head
    while slow is not fast :
        slow = slow.next 
        fast = fast.next 
    return fast


sll = sll_2()
hold_nodes = []
for i in range(10):
    hold_nodes.append(sll_Node(i))
for i in hold_nodes:
    sll.append(i)
sll.append(hold_nodes[3])

print(using_a_hash_table(sll))
print(using_runners(sll))