import queue
from collections import deque

directed_graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

def exist_route(g, start, end):
    """
        Given a directed graph, determines if there is a route
        from start to end.
        O(V) space
        O(V+E) time
    """
    q = queue.Queue()
    visited = {}
    for node in g.keys():
        visited[node] = False

    q.put(start)
    visited[start] = True
    while not q.empty():
        n = q.get()
        for neighbor in g[n]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.put(neighbor)
                if neighbor == end:
                    return True
    return False

print("Test 4.1")
print(exist_route(directed_graph, 'A', 'E'))
print(exist_route(directed_graph, 'E', 'A'))
print()


class Node():
    def __init__(self, val, right = None, left = None, parent = None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent

def min_height_bst(sorted_arr, parent = None):
    """
        Given a sorted(increasing order) array with unique integer elements,
        create a binary tree with minimal height.
        O(logN) space
        O(N) time
        If we insert each element from root instead of recursion, it will be O(NlogN) time.
    """
    n = len(sorted_arr)
    if n == 0:
        return None
    if n == 1:
        return Node(sorted_arr[0], parent = parent)

    middle = len(sorted_arr) // 2
    val = sorted_arr[middle]
    root = Node(val, parent = parent)
    root.left = min_height_bst(sorted_arr[:middle], root)
    root.right = min_height_bst(sorted_arr[middle+1:], root)
    return root

print("Test 4.2")
min_bst = min_height_bst([1, 2, 3, 4, 5])
min_bst = min_height_bst([1, 2, 3, 4, 5, 6])

def list_of_depths(bt):
    """
        Given a binary tree, create a liked list of all the nodes at each depth.
          1             linked list at each depth
         / \         => [1]
        2   3           [2] -> [3]
        O(N) time
        O(N) space
    """
    linked_lists = []
    current = [bt]
    while any(current):
        linked_lists.append(deque([n.val for n in current if n]))
        current = find_children(current)
    return linked_lists

def find_children(lst):
    children = []
    for node in lst:
        if node:
            children.append(node.left)
            children.append(node.right)
    return children

print("Test 4.3")
print(list_of_depths(min_bst))


def check_balanced(t):
    """
        Given a binary tree, determine if a binary tree is balanced.
        Balanced tree is defined to be a tree such that the heights of the two subtrees
        of any node never differ by more than one.
        O(N) time
        O(H) space where H is the height of the tree (H recursion call stack)
    """
    return check_height(t) != float('inf')

def check_height(t):
    if t is None:
        return 0
    height_l = check_height(t.left)
    height_r = check_height(t.right)
    if abs(height_l - height_r) > 1:
        return float('inf')
    return max(height_l, height_r) + 1

print("Test 4.4")
print(check_balanced(min_bst))

def check_bst(t):
    """
        Given a binary tree, determine if the binary tree is binary search tree.
        BST is defined to be a tree such that all nodes on left subtree <= current node < all nodes on right subtree.
        <=> max value on left subtree <= current node < min value on right subtree
        O(N) time
        O(H) space (recursion stack)
    """
    return is_bst(t, -float('inf'), float('inf'))

def is_bst(t, min_l, max_r):
    if t is None:
        return True
    if t.val > max_r or t.val <= min_l:
        return False
    # When we check left subtree, all nodes on the left subtree must be less than or equal to the current node's value
    if not (is_bst(t.left, min_l, t.val) and is_bst(t.right, t.val, max_r)):
        return False
    return True

print("Test 4.5")
print(check_bst(min_bst))


def successor(t, node):
    """
    Given a binary tree, find the in-order successor of a given node.
    Assume every node has a parent pointer.
    O(1) space
    O(H) time
    """
    if node.right is not None:
        return min_value(node.right)

    p = node.parent
    while p is not None:
        if p.right != node:
            break
        node = p
        p = p.parent
    return p

def min_value(t):
    current = t
    while current is not None:
        if current.left is None:
            return t
        current = current.left
    return current

print("Test 4.6")
print(successor(min_bst, min_bst.left.right).val)
