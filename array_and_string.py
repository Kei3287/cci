import math


def is_unique(str1):
    """
        Determine if each character in string appears only once
        O(1) space for 256 ASCII chars (There's only 128 printable characters, but extended ASCII has 256)
        O(n) time
    """
    count = {}
    for s in str1:
        if s in count:
            return False
        else:
            count[s] = 1
    return True


print("Test 1.1")
print(is_unique("avda"))
print()


def check_permutation(str1, str2):
    """
        Determine if str1 and str2 can be reordered to make them identical
        O(1) space for 256 ASCII chars
        O(n) time
    """
    if len(str1) != len(str2):
        return False
    counts = [0] * 256
    for i in range(len(str1)):
        counts[ord(str1[i])] = counts[ord(str1[i])] + 1
        counts[ord(str2[i])] = counts[ord(str2[i])] - 1
    return sum(counts) == 0


print("Test 1.2")
print(check_permutation("avva", "aavv"))
print()


def URLify(str1, size):
    """
        Replace a space with "%20"
        O(n) space
        O(n^2) time because of string concatenation at each step
    """
    output = ""
    for i in range(len(str1)):
        if str1[i] == " ":
            output += "%20"
        else:
            output += str1[i]
    return output


print("Test 1.3")
print(URLify("aa a", 4))
print()


def palindrome_permutation(str1):
    """
        Determine of a string can be reordered to make a palindrome string
        O(n) space
        O(n) time
    """
    counts = {}
    odd_count = 0
    for s in str1:
        if s == " ":
            continue
        counts[s] = counts.get(s, 0) + 1
        if counts[s] % 2 != 0:
            odd_count += 1
        else:
            odd_count -= 1
    if len(str1) % 2 == 0:
        return odd_count == 1
    else:
        return odd_count == 0


print("Test 1.4")
print(palindrome_permutation("tact coaa"))
print()


def one_away(str1, str2):
    """
        Determine if two strings are one away (insert/replace/remove)
        O(1) space
        O(n) time
    """
    if len(str1) == len(str2):
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff <= 1
    elif len(str1) - len(str2) == 1:
        removal = 0
        for i in range(len(str1)):
            if removal == 2:
                return False
            if str1[i] != str2[i-removal]:
                removal += 1
        return True
    elif len(str1) - len(str2) == -1:
        removal = 0
        for i in range(len(str1)):
            if removal == 2:
                return False
            if str1[i] != str2[i+removal]:
                removal += 1
        return True


print("Test 1.5")
print(one_away("avb", "ab"))
print(one_away("avb", "acb"))
print(one_away("avb", "avbx"))
print(one_away("aaa", "avv"))
print()


def string_compression(str1):
    """
        ex) aabbbbc -> a2b4c1

        O(n) space
        O(n) time
        string concatenation of whole string takes O(n^2) because it copies both strings every time. 1 + 2 + ... + n = n(n+1)/2
        => reduce the number of concatenation
    """
    output = ""
    count = 0
    for i in range(len(str1)):
        count += 1
        if i == len(str1) - 1 or str1[i] != str1[i+1]:
            output = output + str1[i] + str(count)
            count = 0
    if len(output) > len(str1):
        return str1
    return output


print("Test 1.6")
print(string_compression("aabbb"))
print(string_compression("avc"))
print(string_compression("bbbbc"))
print()


def rotate_matrix(mat):
    """
        Rotate the matrix by 90 degrees clockwise
        O(1) space
        O(n^2) time because it goes through each element and copy over to the right position
    """
    n = len(mat[0])
    for i in range(n//2):
        first = i
        last = n - i - 1
        # swap the ith layer circle
        for j in range(last - first):
            # save top
            temp = mat[first][first+j]
            # top <- left
            mat[first][first+j] = mat[last-j][first]
            # left <- bottom
            mat[last-j][first] = mat[last][last-j]
            # bottom <- right
            mat[last][last-j] = mat[first+j][last]
            # right <- top
            mat[first+j][last] = temp
    return mat


print("Test 1.7")
print(rotate_matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
print(rotate_matrix([[0, 1, 2, 3], [4, 5, 6, 7],
                     [8, 9, 10, 11], [12, 13, 14, 15]]))
print()


def zero_matrix(mat):
    """
        If there is an element of 0, zero out its row and column
        O(M + N) space
        O(MN) time
    """
    rows_of_0 = [False] * len(mat)
    cols_of_0 = [False] * len(mat[0])

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                rows_of_0[i] = True
                cols_of_0[j] = True
    for i in range(len(rows_of_0)):
        if rows_of_0[i]:
            mat = nullify_row(mat, i)
    for j in range(len(cols_of_0)):
        if cols_of_0[j]:
            mat = nullify_col(mat, j)
    return mat


def nullify_row(mat, i):
    for c in range(len(mat[0])):
        mat[i][c] = 0
    return mat


def nullify_col(mat, j):
    for r in range(len(mat)):
        mat[r][j] = 0
    return mat


print("Test 1.8")
print(zero_matrix([[1, 2, 0], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
print(zero_matrix([[1, 2, 3], [4, 0, 6], [7, 8, 9], [10, 11, 12]]))
print()


def string_rotation(str1, str2):
    """
        Check if str2 is a rotation of str1 using only one call to substring
        O(n) space
        O(n) time
    """
    if len(str1) != len(str2):
        return False
    return substring(str2 + str2, str1)


def substring(str1, target):
    """
        Check if the target is a substring of str1 in str1 in O(M+N) time using Z-algorithm:
        Z_string = target + $ + str1 (assuming $ doesn't exist in str1)
        Z[i] = length of longest substring in Z_string[i:] that match the prefix of Z_string
        return true if there is equal to the length of target

        O(n+m) space
        O(n+m) time
    """
    z_string = target + '$' + str1
    z = [0] * len(z_string)
    left, right = 0, 0
    for i in range(1, len(z_string)):
        if i > right:
            left, right = i, i
            # calculate z value for index i
            while z_string[right] == z_string[right-left] and right < len(z_string) - 1:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < len(z_string) and z[right] == z[right - left]:
                    right += 1
                z[i] = right - left
                right -= 1
    return any(map(lambda x: x == len(target), z))


print("Test 1.9")
print(substring("abccdea", "cde"))
print(string_rotation("erbottlewat", "waterbottle"))
print(string_rotation("wrbottlewat", "waterbottle"))
print()
