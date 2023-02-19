def in_bisect(lst, target):
  left, right = 0, len(lst)-1
  while left <= right:
    mid = (left + right) // 2
    if lst[mid] < target:
      left = mid + 1
    elif lst[mid] > target:
      right = mid - 1
    else:
      return True
  return False

words = []
with open("words.txt", "r") as txt:
  for line in txt:
    word = line.strip()
    words.append(word)

print(in_bisect(words, "believes"))           # True
print(in_bisect(words, "Saitama"))            # False
print(in_bisect(words, "proxy"))              # True
print(in_bisect(words, "Puri-Puri Prisoner")) # False