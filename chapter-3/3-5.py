from helpers import Second_Stack
import random
seed = random.seed()
'''
Sort Stack : Write  a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, isEmpty 
'''


# def sort_stack(stack):
#     temp_stack = Stack()    
#     initial_length = len(stack)
#     sorted = 0 
#     remainder = initial_length
#     compare = stack.peek().data
#     while ((initial_length - sorted) != 0):

#         while (remainder != 0):
#             item = stack.pop()
#             if (item.data < compare.data):
#                 compare = item.data
#             temp_stack.push(item)
#             remainder -= 1 
#             print(len(stack))

#         stack.push(compare)

#         while not temp_stack.isEmpty():
#             item = temp_stack.pop()
#             if item is compare:
#                 continue 
#             stack.push(item)

#         sorted += 1 
#         remainder = initial_length - sorted
        
def sort_stack(stack):
    temp_stack = Second_Stack()
    initial_length = len(stack)
    sorted = 0 
    remainder = initial_length
    compare = stack.peek()
    time = 0 

    while ((initial_length - sorted) != 0):
        compare = stack.peek()
        while(remainder != 0):
            item = stack.pop()
            if (item > compare):
                compare = item 
            temp_stack.push(item)
            remainder -= 1 
            time += 1 
        
        stack.push(compare)
        found = False 

        while not temp_stack.isEmpty():
            item = temp_stack.pop()
            if item == compare and not found : 
                found = True 
                continue 
            stack.push(item)
            time += 1 
        
        sorted += 1 
        remainder = initial_length - sorted 
    print("n-squared time : ", time)

        






stack = Second_Stack()
for i in range(10):
    stack.push(random.randint(0, 21))

print(stack)
sort_stack(stack)
print(stack)
