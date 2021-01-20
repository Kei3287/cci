from collections import defaultdict
import numpy as np

def sorted_merge(A, B, len_A, len_B):
    """
        Given two sorted arrays A, B, where A has a large enough buffer at the end to hold B.
        Merge B into A in sorted order.
        O(1) space
        O(len(A)+len(B)) time
    """
    last_A = len_A - 1
    last_B = len_B - 1
    index = last_A + last_B + 1
    while last_A != -1 or last_B != -1:
        if last_A == -1 or A[last_A] < B[last_B]:
            A[index] = B[last_B]
            last_B -= 1
        else:
            A[index] = A[last_A]
            last_A -= 1
        index -= 1
    return A


A = np.array([x for x in range(5, 10)] + [-1] * 7)
B = np.array([x for x in range(1, 8)])
print("Test 10.1")
print("A: {}".format(A))
print("B: {}".format(B))
print(sorted_merge(A, B, 5, 7))
print()

def group_anagrams(arr):
    """
        Sort an array of strings so that all the anagrams are next to each other.
        anagrams == a word, phrase, or name formed by rearranging the letters of another
                 <=> same frequencies for all characters
        O(N) space
        O(Nk) time where k = len of the longest string in arr

        soln2: Sort each character, then sort the entire array. O(NlogN + Nklogk) time
    """
    anagrams = defaultdict(list)
    for s in arr:
        key = [0] * 26
        for c in s:
            key[ord(c) - ord('a')] += 1
        anagrams[tuple(key)].append(s)
    return [item for sublist in list(anagrams.values()) for item in sublist]

print("Test 10.2")
an = ["dog", "cat", "god"]
print(group_anagrams(an))
print()


def search_in_rotated_array(arr, elem):
    """
        Given a sorted array (increasing order) of n integers that has been rotated an unknown number of times.
        Find an element in the array.
        O(1) space
        O(logN) time
    """
    if len(arr) == 1 or len(arr) == 0:
        return 0
    middle = len(arr) // 2
    if arr[middle] == elem:
        return middle
    if arr[0] < middle:
        # left half is in order
        if elem >= arr[0] and elem < middle:
            return search_in_rotated_array(arr[:middle], elem)
        else:
            return middle + search_in_rotated_array(arr[middle:], elem)
    else:
        # left half is out of order => right half is in order
        if elem >= middle and arr[-1] >= elem:
            return middle + search_in_rotated_array(arr[middle:], elem)
        else:
            return search_in_rotated_array(arr[:middle], elem)

print("Test 10.3")
arr = [15, 16, 1, 2, 5, 7]
print("Should print 4")
print(search_in_rotated_array(arr, 5))
print("Should print 1")
print(search_in_rotated_array(arr, 1))
print()

class Listy():
    def __init__(self, arr):
        self.arr = arr

    def get_element(self, i):
        if len(self.arr) <= i:
            return -1
        return self.arr[i]

def sorted_search_no_size(listy, x):
    """
        Listy is an array-like data structure (only supports positive integer) which lacks a size method.
        It has an get_element(i) method that runs in O(1) time. If i is beyond the bounds of the data structure, it returns -1.

        Given a Listy which contains sorted, positive integers, find the index at which an element x occurs.
        If x occurs multiple times, you may return any index.

        O(logN) space (recursive call stacks for binary search)
        O(logN) time
    """
    # Find the length of Listy in O(logN)
    # If we keep doubling the size, it takes k steps to find the length.
    # 2^k = N      => k = logN steps
    index = 1
    while listy.get_element(index) != 1 and x > listy.get_element(index):
        index *= 2
    return binary_search(listy, x, 0, index)

def binary_search(listy, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    val = listy.get_element(mid)
    if val == x:
        return mid
    if val > x:
        return binary_search(listy, x, low, mid-1)
    else:
        return binary_search(listy, x, mid+1, high)

print("Test 10.4")
arr = [1, 2, 5, 7, 10]
listy = Listy(arr)
print("Should print 3")
print(sorted_search_no_size(listy, 7))
print("Should print 0")
print(sorted_search_no_size(listy, 1))
