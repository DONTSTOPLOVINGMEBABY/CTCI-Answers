from helpers import Stack, Element

'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure set of stacks that mimics this. SetOfStacks should be composed of several stacks and push pop should behave identically to a single stack (that is pop() should return the same values as it would if there were just a single stack). 
'''

class SetOfStacks:
    def __init__(self, maxsize):
        self.stacks = [Stack()]
        self.stack_number = 0 # Keeps track of which stack is the 'current' stack
        self.stack_maxsize = maxsize 
        self.priority_adds = set()
    
    def add_a_stack(self):
        self.stack_number += 1 
        self.stacks.append(Stack())
    
    def remove_a_stack(self):
        self.stack_number -= 1 
        self.stacks.pop()
    
    def push(self, data):
        element = Element(data)
        if len(self.priority_adds) > 0 :
            add_to = self.priority_adds[0]
            self.stacks[add_to].push(element)
            if len(self.stacks[add_to]) == self.stack_maxsize: 
                self.priority_adds.remove(add_to)
            return     
        if len(self.stacks[self.stack_number]) == self.stack_maxsize :
            self.add_a_stack()
        self.stacks[self.stack_number].push(element)
    
    def pop(self, index_num=False):
        if index_num != False:
            item = self.stacks[index_num].pop()
            self.priority_adds.add(index_num)
            self.priority_adds = sorted(self.priority_adds)
        else : 
            item = self.stacks[self.stack_number].pop()
        if len(self.stacks[self.stack_number]) == 0:
            self.remove_a_stack()
        return item

    def popAt(self, index):
        if self.stack_number < index - 1 : return False
        self.pop(index)

    def print_stackset(self):
        if self.stacks[0].isEmpty() : return None 
        print(self.stacks)
        for i in self.stacks:
            print(i)


stack_set = SetOfStacks(5)
for i in range(26):
    stack_set.push(i)
stack_set.print_stackset()

for i in range(10):
    print(stack_set.pop().data)

stack_set.print_stackset()
stack_set.popAt(2)
stack_set.print_stackset()

stack_set.push(-3000)
stack_set.print_stackset()