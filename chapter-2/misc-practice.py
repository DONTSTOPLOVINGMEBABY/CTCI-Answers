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
    print(slow, fast, len(linked_list)) 


ll_even = helpers.Singly_Linked_List()
ll_odd = helpers.Singly_Linked_List()

for i in range(8):
    ll_even.append(i) 

for i in range(7):
    ll_odd.append(i + 8)


print(ll_even) ; fast_slow_runner(ll_even) 

print(ll_odd) ; fast_slow_runner(ll_odd) 




