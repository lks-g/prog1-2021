def has_duplicates(lst):
  for elem in lst:
    if lst.count(elem) > 1:
      return True
  return False

print(has_duplicates([1, 2, 3, 4, 5]))  # False
print(has_duplicates([3, 5, 5, 12, 4])) # True