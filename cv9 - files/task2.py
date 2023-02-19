def chop(lst):
  lst.remove(lst[0])
  lst.pop()

a = [1, 2, 3, 4]
print(a)  # [1, 2, 3, 4]
chop(a)
print(a)  # [2, 3]