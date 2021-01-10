class Node():
    def __init__(self, val = 0, next = None):
        self.next = next
        self.val = val

class LinkedList():
    def __init__(self, head = None):
        self.head = None

    def append(self, val):
        end = Node(val)
        if self.head is None:
            self.head = end
            return
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = end

    def print(self):
        ptr = self.head
        while ptr != None:
            print(ptr.val)
            ptr = ptr.next

    def remove_dups(self):
        """
            Remove the duplicate elements.
            O(N) space
            O(N) time
            (O(NlogN) time & O(1) space if we sort the list at the beginning.)
        """
        d = set()
        prev = self.head
        n = self.head
        while n != None:
            if n.val in d:
                prev.next = n.next
            else:
                d.add(n.val)
                prev = n
            n = n.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(2)
ll.print()

print("Test 2.1")
ll.remove_dups()
# Should print 1 2 3
ll.print()
print()


