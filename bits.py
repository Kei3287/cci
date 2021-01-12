
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
