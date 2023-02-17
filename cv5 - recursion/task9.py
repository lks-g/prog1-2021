def is_power(a, b):
  if a <= 0 or b <= 0:
    raise ValueError("a, b must belong to the set N")
  if a < b and a != 1:
    return False
  if a // b == 0:
    return True
  if a % b == 0:
    return is_power(a/b, b)
  return False

print(is_power(8, 2))  # True
print(is_power(9, 2))  # False