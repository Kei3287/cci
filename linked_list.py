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



def remove_dups(ll):
    """
        Remove the duplicate elements.
        O(N) space
        O(N) time
        (O(NlogN) time & O(1) space if we sort the list at the beginning.)
    """
    d = set()
    prev = ll.head
    n = ll.head
    while n != None:
        if n.val in d:
            prev.next = n.next
        else:
            d.add(n.val)
            prev = n
        n = n.next

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(3)
ll1.append(2)
ll1.print()

print("Test 2.1")
remove_dups(ll1)
print("Should print 1 2 3")
ll1.print()
print()


def kth_to_last(ll, k):
    """
        Return the kth to last element of a singly linked list.
        O(1) space
        O(N) time
    """
    p1 = ll.head
    p2 = ll.head
    for _ in range(k):
        if p2.next is None:
            return None
        p2 = p2.next
    while p2 != None:
        p1 = p1.next
        p2 = p2.next
    return p1.val

def kth_to_last_rec(ll, k):
    """
        Recursive solution for kth to last problem
        O(N) space
        O(N) time
    """
    kth_val = 0
    def kth_to_last_helper(head, k):
        nonlocal kth_val
        if head is None:
            return 0
        index = kth_to_last_helper(head.next, k) + 1
        if index == k:
            kth_val = head.val
        return index
    kth_to_last_helper(ll.head, k)
    return kth_val

ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
ll2.print()

print("Test 2.2")
print("Should print 5")
print(kth_to_last(ll2, 1))
print("Should print 3")
print(kth_to_last(ll2, 3))
print("Should print 5")
print(kth_to_last_rec(ll2, 1))
print("Should print 3")
print(kth_to_last_rec(ll2, 3))
print()


def delete_middle_node(middle):
    """
        Given only access to the middle node, delete the middle node.
        (first and last won't be deleted.)
        O(1) space
        O(1) time
    """
    if middle is None or middle.next is None:
        return
    middle.val = middle.next.val
    middle.next = middle.next.next

ll3 = LinkedList()
ll3.append(1)
ll3.append(2)
ll3.append(3)
ll3.append(4)
ll3.append(5)
print("Test 2.3")
delete_middle_node(ll3.head.next.next)
print("Should print 1 2 4 5")
ll3.print()
print()


def partition(ll, x):
    """
        Partition a linked list around a value x such that all nodes less than x comes before all nodes greater than or equal to x.
        ex) x = 5
            input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
            output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 OR 3 -> 1 -> 2 -> 5 -> 8 -> 5 -> 10, etc (value x can be anywhere as long as all values less than x is before x.)
        O(1) space
        O(N) time
    """
    ptr = ll.head.next
    prev = ll.head
    while ptr != None:
        if ptr.val < x:
            ll.head = Node(ptr.val, next = ll.head)
            prev.next = ptr.next
        else:
            prev = ptr
        ptr = ptr.next

ll4 = LinkedList()
ll4.append(1)
ll4.append(11)
ll4.append(8)
ll4.append(4)
ll4.append(10)
print("Test 2.4")
partition(ll4, 10)
print("Should print 4 8 1 11 10")
ll4.print()
print()

