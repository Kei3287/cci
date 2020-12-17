# O(1) space for 256 ASCII chars (There's only 128 printable characters, but extended ASCII has 256)
# O(n) time
def is_unique(str1):
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

# O(1) space for 256 ASCII chars
# O(n) time
def check_permutation(str1, str2):
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

# O(n) space
# O(n) time
def palindrome_permutation(str1):
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

# O(1) space
# O(n) time
def one_away(str1, str2):
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

# O(n) space
# O(n) time
# string concatenation of whole string takes O(n^2) because it copies both strings every time. 1 + 2 + ... + n = n(n+1)/2
# => reduce the number of concatenation
def string_compression(str1):
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
