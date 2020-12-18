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
            self.values[(stack_num - 1) * self.stack_size + self.sizes[stack_num - 1]] = val
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
