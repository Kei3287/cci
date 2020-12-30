import queue
import collections

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
    def __init__(self, val, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

def min_height_bst(sorted_arr):
    """
        Given a sorted(increasing order) array with unique integer elements,
        create a binary tree with minimal height.
        O(N) space
        O(logN) time
        If we insert each element from root instead of recursion, it will be O(NlogN) time.
    """
    n = len(sorted_arr)
    if n == 0:
        return None
    if n == 1:
        return Node(sorted_arr[0])

    middle = len(sorted_arr) // 2
    val = sorted_arr[middle]
    n = Node(val)
    n.left = min_height_bst(sorted_arr[:middle])
    n.right = min_height_bst(sorted_arr[middle+1:])
    return n

print("Test 4.2")
min_bst = min_height_bst([1, 2, 3, 4, 5])
min_bst = min_height_bst([1, 2, 3, 4, 5, 6])

