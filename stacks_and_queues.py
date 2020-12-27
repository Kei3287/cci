import math
import sys
import traceback


class ThreeInOne():
    """
        Implement three stacks using only one array
        O(1) time for all methods
    """
    num_of_stacks = 3

    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.values = [0] * self.num_of_stacks * self.stack_size
        self.sizes = [0] * self.num_of_stacks

    def push(self, stack_num, val):
        try:
            if self.sizes[stack_num - 1] == self.stack_size:
                raise Exception('stack is full')
            self.values[(stack_num - 1) * self.stack_size +
                        self.sizes[stack_num - 1]] = val
            self.sizes[stack_num - 1] += 1
        except Exception:
            print(traceback.format_exc())

    def pop(self, stack_num):
        try:
            if self.is_empty(stack_num):
                raise Exception('stack is empty')
            self.sizes[stack_num - 1] -= 1
            return self.values[(stack_num - 1) * self.stack_size + self.sizes[stack_num - 1]]
        except Exception:
            print(traceback.format_exc())

    def is_empty(self, stack_num):
        return self.sizes[stack_num - 1] == 0


print("Test 3.1")
stacks = ThreeInOne(3)
stacks.push(1, 1)
print(stacks.pop(1))
print(stacks.is_empty(1))
stacks.push(3, 1)
stacks.push(3, 2)
print(stacks.pop(3))
stacks.push(3, 3)
print(stacks.pop(3))
print(stacks.pop(3))
print()


class StackMin():
    """
        get_min method should return its min value in O(1) time
        all methods should run in O(1) time
    """

    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val):
        if self.is_empty():
            self.min_values.append(val)
        else:
            self.min_values.append(min(self.min_values[-1], val))
        self.values.append(val)

    def pop(self):
        try:
            if self.is_empty():
                raise Exception('stack is empty')
            self.min_values.pop()
            return self.values.pop()
        except Exception:
            print(traceback.format_exc())

    def is_empty(self):
        return len(self.values) == 0

    def get_min(self):
        try:
            if self.is_empty():
                raise Exception('stack is empty')
            return self.min_values[-1]
        except Exception:
            print(traceback.format_exc())


print("Test 3.2")
stack_min = StackMin()
stack_min.push(1)
stack_min.push(0)
print(stack_min.get_min())
stack_min.pop()
print(stack_min.get_min())
stack_min.pop()
print()


class SetOfStacks():
    """
        Create a new stack when the previous stack exceeds some threshold.
        pop_at(int index) should return the pop operation on a specific sub-stack

        O(n) space
        O(1) time for push & pop & is_empty
        O(n) time for pop_at
    """

    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []

    def push(self, val):
        if len(self.stacks) == 0 or len(self.stacks[-1]) >= self.threshold:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)

    def pop(self):
        try:
            if len(self.stacks) == 0:
                raise Exception('stack is empty')
            return self.stacks[-1].pop()
        except Exception:
            print(traceback.format_exc())

    def is_empty(self):
        return len(self.stacks) == 0

    def pop_at(self, i):
        try:
            if len(self.stacks[i-1]) == 0:
                raise Exception('stack is empty')
            val = self.stacks[i-1].pop()
            if len(self.stacks[i-1]) == 0:
                self.stacks.pop(i-1)
            return val

        except Exception:
            print(traceback.format_exc())


print("Test 3.3")
stack_sets = SetOfStacks(2)
stack_sets.push(1)
stack_sets.push(2)
stack_sets.push(3)
print(stack_sets.pop_at(1))
print(stack_sets.pop_at(1))
print(stack_sets.pop())
print()

class MyQueue():
    """
        Implement a Queue using two stacks
        O(n) space
        O(1) amortized time:
    """
    def __init__(self):
        self.new_items = []
        self.old_items = []
        self.size = 0

    def enqueue(self, val):
        self.new_items.append(val)
        self.size += 1

    def dequeue(self):
        try:
            if self.is_empty():
                raise Exception('stack is empty')
            if len(self.old_items) == 0:
                for _ in range(len(self.new_items)):
                    val = self.new_items.pop()
                    self.old_items.append(val)
            val = self.old_items.pop()
            self.size -= 1
            return val
        except Exception:
            print(traceback.format_exc())

    def is_empty(self):
        return self.size == 0

print("Test 3.4")
q = MyQueue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())

def sort_stack(stc):
    """
        Sort the stack such that the smallest elements are on the top.
        (You can only use only one extra stack.)
        O(N) space
        O(N^2) time
    """
    stc2 = []
    while stc:
        temp = stc.pop()
        for i in reversed(range(len(stc2))):
            if stc2[i] >= temp:
                break
            stc.append(stc2.pop())
        stc2.append(temp)
    return stc2

print("Test 3.5")
print(sort_stack([2, 3, 1, 4]))

class AnimalShelter():
    """
        People must adopt the oldest animal.
    """
    order = 0
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

    def dequeueAny(self):
        if len(self.dogs) == 0 and len(self.cats) == 0:
            return
        elif len(self.dogs) == 0:
            return self.cats.pop(0)
        elif len(self.cats) == 0:
            return self.dogs.pop(0)

        if self.dogs[0].order > self.cats[0].order:
            return self.cats.pop(0)
        else:
            return self.dogs.pop(0)

    def dequeueDog(self):
        return self.dogs.pop(0)

    def dequeueCat(self):
        return self.cats.pop(0)
class Animal():
    def __init__(self, name):
        self.order = None
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

print("Test 3.6")
animal_shelter = AnimalShelter()
c1 = Cat("meow")
c2 = Cat("meow meow")
d1 = Dog("woof")
d2 = Dog("woof woof")
animal_shelter.enqueue(c1)
animal_shelter.enqueue(d1)
animal_shelter.enqueue(c2)
animal_shelter.enqueue(d2)
print(animal_shelter.dequeueDog().name)
print(animal_shelter.dequeueAny().name)
print(animal_shelter.dequeueAny().name)
print(animal_shelter.dequeueAny().name)
