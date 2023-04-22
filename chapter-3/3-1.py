'''

Three In One: Describe how you could use a single array to implement three stacks

simple_arr = [ [] ,  [] , [] ] <-- Probably not...
                OR 
simple_arr2 = [ Stack(), Stack(), Stack() ] <-- Again, technically, I guess?? But then again, probably not 

                OR 

You could use three separate sets of head tail pointers and set boundaries as to where they could write and not write to in an array?? <-- Maybe! Sounds like a b*tch! 

Approach 1 : SimulateStack1 

    - Good Approach, but is limited to size at initialization 
    - Could write a resize method but it would be very slow, as you have to copy n elements from 'stack1' , x elements from 'stack2', and t elements from 'stack3' into a new stack thats initialized to the proper size. 

'''

class FULL(Exception):
    # print("This Stack is full")
    pass

class Empty(Exception):
    pass
    # print("This Stack is Empty")

class SimulateStack1 :
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.head1 = 0
        self.tail1 = (size // 3) - 1 
        self.head2 = (size // 3)
        self.tail2 = ((2 * size) // 3) - 1 
        self.head3 = ((2 * size) // 3)
        self.tail3 = size - 1 

    def push1(self, data):
        if self.head1 == self.tail1 :
            raise FULL
        self.stack[self.head1] = data 
        self.head1 += 1 

    def push2(self, data):
        if self.head2 == self.tail2 :
            raise FULL
        self.stack[self.head2] = data 
        self.head2 += 1 

    def push3(self, data):
        if self.head3 == self.tail3 :
            raise FULL
        self.stack[self.head3] = data 
        self.head3 += 1 

    def pop1(self):
        if not self.head1 : raise Empty 
        item = self.stack[self.head1]
        self.stack[self.head1] = None 
        self.head -= 1 
        return item

    def pop2(self):
        if not self.head1 : raise Empty 
        item = self.stack[self.head1]
        self.stack[self.head1] = None 
        self.head -= 1 
        return item

    def pop3(self):
        if not self.head1 : raise Empty 
        item = self.stack[self.head1]
        self.stack[self.head1] = None 
        self.head -= 1 
        return item

    def print1(self):
        count = 0 
        temp = []
        while self.stack[count] != None :
            temp.append(self.stack[count])
            count += 1 
        print(temp)

    def print2(self):
        count = (self.size // 3)
        temp = []
        while self.stack[count] != None :
            temp.append(self.stack[count])
            count += 1 
        print(temp)

    def print3(self):
        count = ((2 * self.size) // 3)
        temp = []
        while self.stack[count] != None :
            temp.append(self.stack[count])
            count += 1 
        print(temp)

s = SimulateStack1(3000)
for i in range(15):
    s.push1(i)
    s.push2(i * i)
    s.push3(i * i * i)

s.print1()
s.print2()
s.print3()