import helpers 


def recursively_print_ll(node):
    if (node == None): return 
    print(node.data, end="--> ") 
    return recursively_print_ll(node.next) 


def recursively_sum_ll(node, total):
    if (node == None) : return total
    return recursively_sum_ll(node.next, total + node.data)

def fast_slow_runner(linked_list):
    slow = linked_list.head 
    fast = linked_list.head 
    while fast != None and fast.next != None : 
        slow = slow.next
        fast = fast.next.next 
    print(slow) 


sll = helpers.Singly_Linked_List() 
for i in range(8):
    sll.append(i * i)
recursively_print_ll(sll.head) 
print()
print(recursively_sum_ll(sll.head, 0)) 
print(fast_slow_runner(sll)) 
