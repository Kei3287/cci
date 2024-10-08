import queue
from collections import deque
from collections import defaultdict
import sys
import traceback
import enum
import random

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
        O(N) time (T[N] = 2T[N/2] + C = 4T[N/4] + 2C + C = ... = 2^{logN} * T[1] + SUM_0-logN {2^i} = N + N = O(N))
        Geometric Series: for c > 1, 1+C+C^2+...+C^k = SUM_0-k {C^i} = O(C^k)

        OR SUM_0-logN {work per level} = SUM_0-logN {(work per recursive call) * (# of recursive calls per level)} = SUM_0-logN {1 * 2^i}
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
min_bst1 = min_height_bst([1, 2, 3, 4, 5])
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
print()


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
print()


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
print()


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
print()


class Status(enum.Enum):
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2

def default_status():
    return Status.NOT_VISITED

def build_order(projects, dependencies):
    """
    Given a list of projects and a list of dependencies, find a build order that will allow
    the projects to be built. All of a project's dependencies must be built before the project is.
    If there is no valid build order, return an error.
    ex)
        projects = [a, b, c]
        dependencies = [(b, a), (c, a), (c, b)] (second project is dependent on the first project.)
        => output: c -> b -> a
    O(V+E) time & space where V == len(projects) and E == len(dependencies)
    """
    dependency_graph = build_dependency_graph(projects, dependencies)
    return topological_sort(dependency_graph)

def build_dependency_graph(projects, dependencies):
    graph = defaultdict(list)
    for v in projects:
        graph[v] = []
    for dep in dependencies:
        graph[dep[0]].append(dep[1])
    return graph

def topological_sort(graph):
    visited = defaultdict(default_status)
    reverse_post_order = [] # sink of the graph will be at the beginning of the list.
    for v in graph.keys():
        if v not in visited:
                dfs(graph, v, visited, reverse_post_order)
    return reverse_post_order[::-1]

def dfs(graph, vertex, visited, reverse_post_order):
    # If the vertex is already in the recursion stack, we have a back edge
    try:
        if visited[vertex] == Status.VISITING:
            raise Exception("there is a cycle in the graph.")
    except Exception:
        print(traceback.format_exc())
        sys.exit(0)

    visited[vertex] = Status.VISITING
    for v in graph[vertex]:
        if visited[v] != Status.VISITED:
            dfs(graph, v, visited, reverse_post_order)
    reverse_post_order.append(vertex)
    visited[vertex] = Status.VISITED


print("Test 4.7")
# Should print c -> b-> a
print(build_order(['a', 'b', 'c'], [('b', 'a'), ('c', 'a'), ('c', 'b')]))
# Should throw an exception
# print(build_order(['a', 'b', 'c'], [('b', 'a'), ('c', 'a'), ('c', 'b'), ('b', 'c')]))
print()

def first_common_ancestor(root, n1, n2):
    """
        Given two nodes in a binary tree, find the first common ancestor of two nodes.
        (Avoid string additional node in a data structure.)
        O(H) space
        O(N) time
    """
    if root is None:
        return None
    if root == n1 or root == n2:
        return root

    left = first_common_ancestor(root.left, n1, n2)
    right = first_common_ancestor(root.right, n1, n2)
    # If n1 and n2 are on the different subtree, current node is the first common ancestor.
    if left and right:
        return root

    if not left and not right:
        return None
    return left if left is not None else right

print("Test 4.8")
# Should print 4
print(first_common_ancestor(min_bst, min_bst.left.right, min_bst.right).val)
# Should print 2
print(first_common_ancestor(min_bst, min_bst.left.right, min_bst.left.left).val)
print()


def bst_sequences(root):
    """
        Given a BST with distinct elements, print all possible arrays that could have led to this tree.
        Assume a BST is created by traversing through an array from left to right and inserting each element.
        ex)   2
             / \        => {2,1,3},{2,3,1}
            1   3
    """
    pass
print("Test 4.9")
print("pass")
print()

def check_subtree(t1, t2):
    """
        Given t1 and t2 with t1 being much bigger than t2. Determine if t2 is a subtree of t1.
        O(N + kM) where N: # nodes in t1, M: # nodes in t2, k: number of t2's root value in t1
    """
    if t1 is None:
        return False
    if t1.val == t2.val:
        return is_subtree(t1, t2)
    return check_subtree(t1.left, t2) or check_subtree(t1.right, t2)

def is_subtree(t1, t2):
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None or t1.val != t2.val:
        return False
    return is_subtree(t1.left, t2.left) and is_subtree(t1.right, t2.right)

print("Test 4.10")
min_bst1 = min_height_bst([1, 2, 2, 3, 4, 5, 6])
min_bst2 = min_height_bst([1, 2, 2])
# Should print True
print(check_subtree(min_bst1, min_bst2))
print()

class RandomNode():
    """
        Binary tree node class which, in addition to insert, find, and delete, has a method get_random_node() which returns a random node from the tree.
        All nodes should be equally likely to be chosen.
    """
    def __init__(self, val, right = None, left = None, parent = None):
        self.val = val
        self.right = right
        self.left = left
        self.parent = parent
        self.size = 1

    def insert_in_order(self, val):
        if val < self.val:
            if self.left is None:
                self.left = RandomNode(val)
            else:
                self.left.insert_in_order(val)
        else:
            if self.right is None:
                self.right = RandomNode(val)
            else:
                self.right.insert_in_order(val)
        self.size += 1

    def find(self, val):
        if val == self.val:
            return val
        elif val < self.val and self.left is not None:
            return self.left.find(val)
        elif val > self.val and self.right is not None:
            return self.right.find(val)
        return None

    def get_random_node(self):
        rand = random.randint(0, self.size-1)
        leftsize = 0 if self.left is None else self.left.size
        if rand < leftsize:
            return self.left.get_random_node()
        elif rand == leftsize:
            return self.val
        return self.right.get_random_node()

print("Test 4.11")
randNode = RandomNode(1)
randNode.insert_in_order(0)
randNode.insert_in_order(3)
randNode.insert_in_order(100)
print(randNode.get_random_node())
print(randNode.get_random_node())
print(randNode.get_random_node())
print(randNode.get_random_node())
print()

def paths_with_sum(root, target_sum):
    """
        Given a binary tree in which each node contains an integer,
        count the number of paths that sum to a given value. (The path doesn't need to start at root and end at leaf.)
        O(H) space
        O(N) time

        1 5 3 3
        |-| => run_sum_x = 6
        |-----| => run_sum_y = 12
        Since run_sum_y - sun_rum_x == target, we can check if run_sum_y - target exists in hashtable to see
        if target sum exists in between x and y.
    """
    path_count = defaultdict(lambda: 0)
    path_count[0] = 1
    return count_paths_with_sum(root, target_sum, 0, path_count, 0)

def count_paths_with_sum(root, target_sum, run_sum, path_count, total_count):
    """
        path_count is a mapping from the running_sum to the number of occurrences of such running_sum
    """
    if root is None:
        return total_count
    run_sum += root.val
    total_count += path_count[run_sum - target_sum]
    path_count[run_sum] += 1
    total_count = count_paths_with_sum(root.left, target_sum, run_sum, path_count, total_count)
    total_count = count_paths_with_sum(root.right, target_sum, run_sum, path_count, total_count)
    del path_count[run_sum]
    return total_count

print("Test 4.12")
bt = RandomNode(8)
bt.insert_in_order(5)
bt.insert_in_order(12)
bt.insert_in_order(3)
bt.insert_in_order(11)
bt.insert_in_order(15)
bt.insert_in_order(1)
bt.insert_in_order(3)
bt.insert_in_order(10)
bt.insert_in_order(2)
bt.insert_in_order(4)
# Should print 3
print(paths_with_sum(bt, 11))
