from collections import deque
from helpers import Queue, Element
import random, time
seed = random.seed()
'''
Animal Shelter : An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the 'oldest' (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select whether they want an animal which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and deQueueCat. You may use the built in LinkedList data structure

deque operations 
------------------
- append (right side)
- appendleft
- pop (right)
- popleft
- remove (first value of x)
'''


# Good solution but probably not acceptable 
class AnimalShelter:
    def __init__(self):
        self.animals = deque()

    def enqueue(self, animal):
        self.animals.append(animal)

    def dequeueAny(self):
        return self.animals.popleft()

    def dequeueDog(self):
        return self.animals.remove("dog")

    def dequeueCat(self):
        return self.animals.remove("cat")
    
    def print_shelter(self):
        print(self.animals)

class Animal :
    def __init__(self, type):
        self.type = type 
        self.created = time.time()
        

class HenryShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
    
    def enqueue(self, animal):
        if animal == "dog" : 
            self.dogs.queue(animal)
        else :
            self.cats.queue(animal)    

    def dequeueAny(self):
        if self.cats.peek.data.created <= self.dogs.peek.data.created : 
            self.cats.dequeue()
        else :
            self.dogs.dequeue()

    def dequeueDog(self):
        self.dogs.dequeue()

    def dequeueCat(self):
        temp_cats = self.cats 
        temp_dogs = self.dogs 
        string = " "
        while temp_cats.peek() != None or temp_dogs.peek() != None : 

            if temp_cats.peek() != None and temp_dogs.peek() != None and (temp_cats.peek.created <= temp_dogs.peek.created):
                string += temp_cats.dequeue().data.type
            else : 
                string += temp_dogs.dequeue()
            if temp_cats.peek() == None and temp_dogs.peek() != None :
                string += temp_dogs.dequeue().data.type
            if temp_dogs.peek() == None and temp_cats != None : 
                string += temp_cats.dequeue().data.type
        print(string)
        

    
one = HenryShelter()
one.enqueue(Element(Animal("dog")))
one.enqueue(Element(Animal("dog")))
one.enqueue(Element(Animal("cat")))
one.enqueue(Element(Animal("cat")))
one.enqueue(Element(Animal("dog")))

one.print_me()