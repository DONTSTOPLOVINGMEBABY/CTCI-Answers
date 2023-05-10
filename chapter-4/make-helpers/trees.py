'''
Stack : 
    - deque.append()
    - deque.pop()

Queue : 
    - deque.appendLeft()
    - deque.popLeft()
'''
from collections import deque
import random

# Display array is strictly used for visuals inside of the debugger 
def buildTree( array, display_array, start, end ):
    if start > end : return None 
    mid = (start + end) // 2 
    root = Node( array[mid] )
    root.left = buildTree( array, array[start: mid - 1], start, mid - 1 )
    root.right = buildTree( array, array[mid + 1: end], mid + 1, end )

    return root

class Node :
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

class Tree :
    def __init__(self, array):
        self.root = buildTree( array, array[0:len(array) - 1],  0, len(array) - 1)




seed = random.seed()
numbers = []
for i in range(10): 
    numbers.append(random.randint(0, 20))
numbers.sort()
tree = Tree(numbers)
