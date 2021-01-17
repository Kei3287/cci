# import numpy as np

def insertion(M, N, i, j):
    """
        Given two 32-bit numbers, M & N, and two positions, i & j.
        Insert M into N such that M starts at jth and ends at ith position of N.
        ex) M = 101
            N = 100001, i = 1, 3
            output: N = 101011

        mask1 = (000001 << i) - 000001 = 000001
        mask2 = (-1 << (j+1)) = 110000
        mask = mask1 | mask2 = 110001
    """
    mask1 = ((1 << i) - 1)
    mask2 = -1 << (j+1)
    N_cleared = N & (mask1 | mask2)
    return N_cleared | (M << i)

print("Test 5.1")
n = 33 # == 100001
m = 5   # == 101
i = 1
j = 3
print("Should be 43 (101011)")
print(insertion(m, n, i, j))
print()


def binary_to_string(x):
    """
        Given a real number 0 < x < 1, print the binary representation.
        If the number cannot be represented accurately in binary with at most 32 characters, print an Error.
        ex) Input :  0.625
            Output : 0.101 = 1 * (1/2)^1 + 0 * (1/2)^2 + 1 * (1/2)^3
    """
    if 1 < x or 0 > x:
        return "Error"
    binary = "0."
    while x > 0:
        if len(binary) == 32:
            return "Error"
        r = x * 2
        if r >= 1:
            binary += "1"
            x = r - 1
        else:
            binary += "0"
            x = r
    return binary

print("Test 5.2")
print("Should be 101")
print(binary_to_string(0.625))
print()


def flip_bit_to_win(x):
    """
        Given an integer and you can flip exactly one bit from a 0 to 1. Find the length of the longest sequence of 1s you could create.
        ex) x = 1775 == 11011101111
            output: 8
        O(1) space
        O(B) time where B is the number of bits of x
    """
    prev_len = 0
    cur_len = 0
    max_len = 0
    while x != 0:
        if x & 1 == 1:
            cur_len += 1
        else:
            # If the next bit is 0, 2 zeros in a row, so set prev_len to 0
            prev_len = 0 if x & 2 == 0 else cur_len + 1
            cur_len = 0
        # x = np.right_shift(x, 1)
        x >>= 1
        max_len = max(prev_len + cur_len, max_len)
    return max_len

print("Test 5.3")
print("Should print 8")
print(flip_bit_to_win(1775))
print()


def next_number(x):
    """
        Given a positive integer, print the next smallest and the next largest number
        that have the same number of 1 bits in their binary representation.
    """
    print(get_next_largest(x))
    # print(get_next_smallest(x))

def get_next_largest(x):
    """
                        p = pos of the first occurrence of "01" = #0s on the right + #1s on the right
                        ↓
        ex) input: 6 = 00110
           output: 9 = 01001

    """
    # Calculate the p
    c = x
    c0, c1 = 0, 0
    if c & 1 == 0:
        while c & 1 == 0 and c != 0:
            c0 += 1
            c >>= 1
    while c & 1 == 1 and c != 0:
        c1 += 1
        c >>= 1
    p = c0 + c1

    # If 01 doesn't appear, return -1
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    x |= (1 << p) # Flip 0 of the first occurrence of 01
    x &= (-1 << p) # Clear 0th ~ (p-1)th bits
    x |= (1 << (c1-1)) - 1 # Replace c1-1 0s to 1s to get a total of c1 1s.
    return x

def get_next_smallest(x):
    """
        Similer to get_next_largest:
        1. find the position of 1 such that "10" appears for the first time from LSB
        2. replace p with 0
        3. clear all bits to the right
        4. insert c1 + 1 1s from right after p in order to maximize the value
    """
    pass

print("Test 5.4")
print("Should print 6")
next_number(5)
print("Should print 25")
next_number(22)
print()

def debugger(n):
    """
        Explain what ((n & (n-1)) == 0) does.
        ex) n = 00100
            n-1 = 11011    =>  n & (n-1) = 00000
        ex) n = 11100
            n-1 = 11011    => n & (n-1) = 110000
        => It is true only if there is only one 1 bit in n.
        => True if n is a power of 2. False ow
    """
    return ((n & (n-1)) == 0)
