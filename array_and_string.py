# O(1) space for 256 ASCII chars (There's only 128 printable characters, but extended ASCII has 256)
# O(n) time
def is_unique(str):
  count = {}
  for s in str:
    if s in count:
      return False
    else:
      count[s] = 1
  return True

print(is_unique("avda"))

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

print(check_permutation("avva", "aavv"))


def URLify(str, size):
  output = ""
  for i in range(len(str)):
    if str[i] == " ":
      output += "%20"
    else:
      output += str[i]
  return output

print(URLify("aa a", 4))
