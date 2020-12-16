# O(1) space for 256 ASCII chars
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
  counts = {}
  for i in range(len(str1)):
    counts[str1[i]] = counts.get(str1[i], 0) + 1
    counts[str2[i]] = counts.get(str2[i], 0) - 1
  return all(map(lambda x: x == 0, counts.values()))

print(check_permutation("avva", "aavv"))
