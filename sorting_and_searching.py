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
