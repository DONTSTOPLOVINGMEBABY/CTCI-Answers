'''
2.4 Partition -- Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. (IMPORTANT: The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and the right partitions. The additional spacing in the example below indicates the partition. Yes, the output below is one of many valud outputs!) 

EXAMPLE

Input : 3 -> 5 -> 8 -> 10 -> 2 -> 1 [partition=5] 

Output : 3 -> 1 -> 2    ->  10 -> 5 -> 5 -> 8 

'''
from helpers import Singly_Linked_List
import random 

def swap(node1, node2):
    hold_node1_data = node1.data 
    node1.data = node2.data 
    node2.data = hold_node1_data

def second_attempt(linked_list, partition):
    follower = linked_list.head 
    runner = follower.next 
    while runner : 
        if follower.data < partition :
            follower = follower.next 
            runner = follower.next 
        elif follower.data > partition: 
            while runner != None and runner.data >= partition: 
                runner = runner.next 
            if runner == None : break
            swap(follower, runner)
            follower = follower.next 
            runner = follower.next 


sll2 = Singly_Linked_List() 
seed = random.seed() 
one = [12, 2, 6, 1, 4, 17, 8, 20, 11, 18]
two = [6, 7, 18, 20, 14, 10, 20, 1, 18, 8] 

for i in range(50):
    sll2.append(random.randint(0, 100))
print(sll2)
second_attempt(sll2, 70)
print(sll2)
