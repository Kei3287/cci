import math
import sys
import traceback


class ThreeInOne():
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.num_of_stacks = 3
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
