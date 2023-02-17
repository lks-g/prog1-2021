def sum(n):
  a = int(input("Enter a number: "))
  if n == 1:
    return a
  return a + sum(n - 1)

print(sum(3))